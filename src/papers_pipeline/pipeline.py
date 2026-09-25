from collections.abc import Callable, Iterator, Mapping, Sequence
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import UTC, datetime, time
from pathlib import Path
import shutil

from papers_pipeline.adapters.base import Adapter
from papers_pipeline.batching import expected_markdown, infer_backlog, select_batch
from papers_pipeline.config import PipelineConfig, load_config
from papers_pipeline.convert import (
    CommandRunner,
    InputMaterializer,
    convert_batch,
)
from papers_pipeline.errors import InfrastructureError
from papers_pipeline.fetch import FetchResult, fetch_all
from papers_pipeline.formatting import format_changed
from papers_pipeline.git import GitOperations
from papers_pipeline.http import Deadline, RequestClient
from papers_pipeline.indexing import write_index
from papers_pipeline.inventory import read_inventory, write_inventory
from papers_pipeline.models import Paper, PipelineState
from papers_pipeline.preflight import ToolLookup, validate_required_tools
from papers_pipeline.normalize import deduplicate, normalize
from papers_pipeline.state import load_state, save_state
from papers_pipeline.summary import RunSummary, SourceCounts, write_actions_summary
from papers_pipeline.topics import TopicDecision, build_topic_gate


@dataclass(frozen=True)
class PipelinePaths:
    root: Path
    config: Path
    state: Path
    inventory: Path
    summary: Path | None


@dataclass(frozen=True)
class Dependencies:
    environ: Mapping[str, str]
    adapters: Mapping[str, Adapter]
    client_factory: Callable[[Deadline], RequestClient]
    runner: CommandRunner
    git: GitOperations
    now: Callable[[], datetime]
    monotonic: Callable[[], float]
    materializer: InputMaterializer | None = None
    tool_lookup: ToolLookup | None = None


@contextmanager
def report_infrastructure_failure(
    paths: PipelinePaths,
    summary: RunSummary,
) -> Iterator[None]:
    try:
        yield
    except InfrastructureError as error:
        summary.events.append(f"infrastructure failure: {error}")
        write_actions_summary(paths.summary, summary)
        raise


@contextmanager
def _timed(
    summary: RunSummary,
    stage: str,
    monotonic: Callable[[], float],
) -> Iterator[None]:
    started = monotonic()
    try:
        yield
    finally:
        elapsed = max(0.0, monotonic() - started)
        summary.timings[stage] = summary.timings.get(stage, 0.0) + elapsed


async def run_nightly(
    paths: PipelinePaths,
    dependencies: Dependencies,
) -> RunSummary:
    config = load_config(paths.config, dependencies.environ)
    validate_required_tools(config, dependencies.tool_lookup or shutil.which)
    initial_state = load_state(paths.state)
    gate = build_topic_gate(config.topic)
    summary = RunSummary()
    run_started = dependencies.monotonic()

    with report_infrastructure_failure(paths, summary):
        dependencies.git.assert_clean(_managed_paths(paths))

        with _timed(summary, "fetch", dependencies.monotonic):
            fetched = await fetch_all(
                config,
                initial_state,
                dependencies.adapters,
                dependencies.client_factory,
                dependencies.now(),
            )

        with _timed(summary, "normalize_gate_deduplicate", dependencies.monotonic):
            normalized = [normalize(record) for record in fetched.records]
            accepted = [paper for paper in normalized if gate(paper).accepted]
            previous_inventory = read_inventory(paths.inventory)
            inventory = deduplicate([*previous_inventory, *accepted])
            _record_source_results(
                summary,
                fetched=fetched,
                accepted=accepted,
                config_gate=gate,
                dependencies=dependencies,
            )
            summary.inventory = len(inventory)

        state = fetched.state
        inventory_changed = inventory != previous_inventory
        state_changed = state != initial_state
        with _timed(summary, "persist_inventory", dependencies.monotonic):
            inventory_paths = [paths.inventory, paths.state]
            inventory_before = _snapshot_files(inventory_paths)
            try:
                if inventory_changed:
                    write_inventory(paths.inventory, inventory)
                if state_changed:
                    save_state(paths.state, state)
                if inventory_changed or state_changed:
                    dependencies.git.commit(
                        inventory_paths,
                        "chore: update paper inventory",
                    )
            except BaseException:
                _rollback_files(
                    inventory_before,
                    inventory_paths,
                    dependencies.git,
                )
                raise

        attempted: set[str] = set()
        batch_number = 0
        backlog = infer_backlog(inventory, paths.root)
        summary.generated = len(backlog.generated)
        summary.pending = len(backlog.pending)
        while backlog.pending and batch_number < config.conversion.max_batches_per_run:
            if (
                dependencies.monotonic() - run_started
                >= config.conversion.deadline_seconds
            ):
                summary.events.append(
                    f"conversion deadline reached after {batch_number} batches"
                )
                break
            eligible = tuple(
                paper for paper in backlog.pending if paper.identifier not in attempted
            )
            batch = select_batch(eligible, config.conversion)
            if not batch.papers:
                break

            batch_number += 1
            attempted.update(paper.identifier for paper in batch.papers)
            summary.attempted += len(batch.papers)
            state_before_batch = state
            index_path = paths.root / "README.md"
            batch_paths = [
                index_path,
                paths.state,
                *(
                    path
                    for paper in batch.papers
                    for path in (
                        expected_markdown(paths.root, paper),
                        expected_markdown(paths.root, paper).with_suffix(".fixme.txt"),
                    )
                ),
            ]
            batch_before = _snapshot_files(batch_paths)
            try:
                with _timed(summary, "conversion", dependencies.monotonic):
                    converted = await convert_batch(
                        batch,
                        paths.root,
                        state,
                        config.concurrency,
                        dependencies.runner,
                        dependencies.materializer,
                        dependencies.now(),
                        timeout_seconds=config.conversion.timeout_seconds,
                    )
                state = converted.state
                summary.succeeded += len(converted.succeeded)
                summary.failed += len(converted.failed)
                summary.deferred += len(converted.deferred)
                summary.promoted_to_fixme += len(converted.promoted)
                summary.fixme_paths.extend(str(path) for path in converted.promoted)
                summary.events.extend(
                    (
                        f"conversion failure: {item.paper.identifier}: "
                        f"{item.error or 'unknown error'}"
                    )
                    for item in converted.failed
                )
                summary.events.extend(
                    f"conversion deferred: {item.paper.identifier}: {item.error}"
                    for item in converted.deferred
                )

                index_before = _file_content(index_path)
                with _timed(summary, "index", dependencies.monotonic):
                    index = write_index(paths.root, inventory)
                changed_paths = [
                    item.output
                    for item in converted.succeeded
                    if item.output is not None
                ]
                if _file_content(index) != index_before:
                    changed_paths.append(index)

                with _timed(summary, "format", dependencies.monotonic):
                    await format_changed(changed_paths, dependencies.runner)

                commit_paths = [*changed_paths, *converted.promoted]
                with _timed(summary, "persist_batch", dependencies.monotonic):
                    if state != state_before_batch:
                        save_state(paths.state, state)
                        commit_paths.append(paths.state)
                    if commit_paths:
                        dependencies.git.commit(
                            commit_paths,
                            f"chore: convert paper batch {batch_number}",
                        )
            except BaseException:
                _rollback_files(batch_before, batch_paths, dependencies.git)
                raise
            backlog = infer_backlog(inventory, paths.root)
            summary.generated = len(backlog.generated)
            summary.pending = len(backlog.pending)

        if summary.pending:
            summary.events.append(
                f"continuation required: {summary.pending} papers remain pending"
            )

    write_actions_summary(paths.summary, summary)
    return summary


def has_more_work(
    config: PipelineConfig,
    before: PipelineState,
    after: PipelineState,
    summary: RunSummary,
) -> bool:
    """Whether another run right away would make progress.

    Work remains while any backfill has not reached its start date or papers
    are pending. Another run is only worth it if this one moved: its backfill
    advanced or it converted papers. A run stalled by an unavailable source or
    a stuck backlog ends the chain; the schedule retries later.
    """
    progressed = after.backfill != before.backfill or summary.succeeded > 0
    return progressed and (summary.pending > 0 or _backfill_incomplete(config, after))


def _backfill_incomplete(config: PipelineConfig, state: PipelineState) -> bool:
    for adapter in config.adapters:
        if not adapter.enabled or adapter.backfill_start is None:
            continue
        progress = state.backfill.get(adapter.name)
        limit = datetime.combine(adapter.backfill_start, time.min, tzinfo=UTC)
        if (
            progress is None
            or progress.continuation is not None
            or progress.covered_from > limit
        ):
            return True
    return False


def _record_source_results(
    summary: RunSummary,
    *,
    fetched: FetchResult,
    accepted: list[Paper],
    config_gate: Callable[[Paper], TopicDecision],
    dependencies: Dependencies,
) -> None:
    source_counts: list[SourceCounts] = []
    selected_new = deduplicate(accepted)
    retained_keys = {(paper.identifier, paper.source) for paper in selected_new}
    for item in fetched.stats:
        adapter = dependencies.adapters[item.source]
        source_records = [
            record
            for record in fetched.records
            if record.source in adapter.record_sources
        ]
        source_normalized = [normalize(record) for record in source_records]
        source_accepted = [
            paper for paper in source_normalized if config_gate(paper).accepted
        ]
        retained = sum(
            (paper.identifier, paper.source) in retained_keys
            for paper in source_accepted
        )
        source_counts.append(
            SourceCounts(
                source=item.source,
                fetched=item.fetched,
                accepted=len(source_accepted),
                deduplicated=len(source_accepted) - retained,
                rejected=item.rejected + len(source_normalized) - len(source_accepted),
                capped=item.capped,
                complete=item.complete,
            )
        )
        if item.rejected:
            summary.events.append(
                f"{item.source}: {item.rejected} permanent record failures"
            )
    summary.sources = tuple(source_counts)
    summary.events.extend(fetched.events)


def _file_content(path: Path) -> bytes | None:
    try:
        return path.read_bytes()
    except FileNotFoundError:
        return None


def _managed_paths(paths: PipelinePaths) -> list[Path]:
    return [
        paths.inventory,
        paths.state,
        paths.root / "README.md",
        paths.root / "papers",
    ]


def _snapshot_files(paths: Sequence[Path]) -> dict[Path, bytes | None]:
    return {path: _file_content(path) for path in paths}


def _rollback_files(
    before: Mapping[Path, bytes | None],
    transaction_paths: Sequence[Path],
    git: GitOperations,
) -> None:
    rollback_error: OSError | None = None
    for path, content in before.items():
        try:
            if content is None:
                path.unlink(missing_ok=True)
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                temporary = path.with_name(f"{path.name}.rollback")
                temporary.write_bytes(content)
                temporary.replace(path)
        except OSError as error:
            rollback_error = rollback_error or error
    git.clear_staging(transaction_paths)
    if rollback_error is not None:
        raise InfrastructureError("pipeline file rollback failed") from rollback_error
