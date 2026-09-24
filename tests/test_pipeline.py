import dataclasses
import subprocess
from collections.abc import Sequence
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pytest
import yaml

import papers_pipeline.cli as cli
from papers_pipeline.adapters.base import FetchPage
from papers_pipeline.convert import (
    CommandRunner,
    InputMaterializer,
)
from papers_pipeline.errors import ConfigError, InfrastructureError, PaperError
from papers_pipeline.git import GitRepository
from papers_pipeline.config import FetchConfig
from papers_pipeline.http import RequestClient
from papers_pipeline.models import SourceRecord
from papers_pipeline.pipeline import Dependencies, PipelinePaths, run_nightly
from papers_pipeline.state import load_state
from papers_pipeline.summary import RunSummary

NOW = datetime(2026, 9, 23, 12, tzinfo=timezone.utc)
INITIAL_README = (
    b"# Test Papers\n\n"
    b"<!-- papers-index:start -->\n"
    b"# Papers\n\n"
    b"| Published | Identifier | Title | Source |\n"
    b"| --- | --- | --- | --- |\n"
    b"<!-- papers-index:end -->\n\n"
    b"## Notes\n\nPreserve this section.\n"
)


def record(identifier: str) -> SourceRecord:
    return SourceRecord(
        source="arxiv",
        source_id=identifier,
        title=f"Neural paper {identifier}",
        abstract="A useful neural systems paper",
        authors=("Ada",),
        published=NOW,
        url=f"https://example.test/{identifier}",
        input_format="html",
        input_url=f"https://example.test/{identifier}.html",
        categories=("cs.CL",),
    )


class FakeAdapter:
    name = "arxiv"
    record_sources = frozenset({"arxiv"})

    def __init__(
        self,
        records: Sequence[SourceRecord],
        *,
        capped: bool = False,
    ) -> None:
        self.records = tuple(records)
        self.capped = capped
        self.calls = 0

    async def fetch(self, *_args: Any, **_kwargs: Any) -> FetchPage:
        self.calls += 1
        return FetchPage(
            records=self.records,
            next_cursor=None,
            capped=self.capped,
        )


class FakeMaterializer(InputMaterializer):
    async def materialize(self, paper: Any, root: Path) -> Path:
        path = root / "inputs" / f"{paper.identifier}.html"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("<p>paper</p>", encoding="utf-8")
        return path


class FakeRunner(CommandRunner):
    def __init__(
        self,
        paper_failures: set[str] | None = None,
        infrastructure_error: InfrastructureError | None = None,
        formatter_error: InfrastructureError | None = None,
    ) -> None:
        self.paper_failures = paper_failures or set()
        self.infrastructure_error = infrastructure_error
        self.formatter_error = formatter_error
        self.calls: list[list[str]] = []

    async def run(
        self, argv: Sequence[str], timeout: float
    ) -> subprocess.CompletedProcess[str]:
        self.calls.append(list(argv))
        if argv[0] == "prettier":
            if self.formatter_error is not None:
                raise self.formatter_error
            return subprocess.CompletedProcess(argv, 0, "", "")
        if self.infrastructure_error is not None:
            raise self.infrastructure_error
        identifier = Path(argv[1]).stem.split(":", 1)[-1]
        if identifier in self.paper_failures:
            raise PaperError("bad document")
        output = Path(
            next(arg.split("=", 1)[1] for arg in argv if arg.startswith("--output="))
        )
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(f"# {identifier}\n", encoding="utf-8")
        return subprocess.CompletedProcess(argv, 0, "", "")


class RecordingGit:
    def __init__(self, fail_message: str | None = None) -> None:
        self.messages: list[str] = []
        self.paths: list[tuple[Path, ...]] = []
        self.clean_checks: list[tuple[Path, ...]] = []
        self.cleared: list[tuple[Path, ...]] = []
        self.fail_message = fail_message

    def assert_clean(self, paths: Sequence[Path]) -> None:
        self.clean_checks.append(tuple(paths))

    def clear_staging(self, paths: Sequence[Path]) -> None:
        self.cleared.append(tuple(paths))

    def commit(self, paths: Sequence[Path], message: str) -> None:
        self.messages.append(message)
        self.paths.append(tuple(paths))
        if message == self.fail_message:
            raise InfrastructureError(f"git commit failed: {message}")


def make_paths(
    tmp_path: Path,
    *,
    max_batches: int = 1,
    max_papers: int = 2,
    deadline_seconds: int = 10800,
) -> PipelinePaths:
    config = {
        "repository": {
            "name": "Test",
            "slug": "test-papers",
            "description": "Test papers",
        },
        "adapters": [
            {
                "name": "arxiv",
                "enabled": True,
                "lookback_days": 7,
                "page_size": 10,
                "max_pages": 1,
                "max_results": 10,
                "filters": {"search_query": "all"},
            }
        ],
        "topic": {
            "include_any": ["neural"],
            "include_all": [],
            "exclude_any": [],
            "categories": [],
        },
        "fetch": {
            "request_timeout_seconds": 10,
            "retries": 1,
            "backoff_seconds": 0,
            "total_deadline_seconds": 60,
        },
        "conversion": {
            "max_batches_per_run": max_batches,
            "max_papers": max_papers,
            "deadline_seconds": deadline_seconds,
            "max_cost": 100,
            "html_cost": 1,
            "latex_cost": 2,
            "pdf_cost": 10,
        },
        "concurrency": {"html": 2, "latex": 1, "pdf": 1},
    }
    config_path = tmp_path / "papers.yml"
    config_path.write_text(yaml.safe_dump(config), encoding="utf-8")
    (tmp_path / "README.md").write_bytes(INITIAL_README)
    return PipelinePaths(
        root=tmp_path,
        config=config_path,
        state=tmp_path / ".papers-state.yml",
        inventory=tmp_path / "papers.csv",
        summary=tmp_path / "step-summary.md",
    )


FETCH_CONFIG = FetchConfig(
    request_timeout_seconds=30, retries=0, backoff_seconds=0, total_deadline_seconds=900
)


def dependencies(
    adapter: FakeAdapter,
    runner: FakeRunner,
    git: RecordingGit | GitRepository,
) -> Dependencies:
    return Dependencies(
        environ={},
        adapters={"arxiv": adapter},
        # FakeAdapter never sends requests; the client only has to exist.
        client_factory=lambda deadline: RequestClient(FETCH_CONFIG, deadline),
        materializer=FakeMaterializer(),
        runner=runner,
        git=git,
        now=lambda: NOW,
        monotonic=lambda: 1.0,
        tool_lookup=lambda name: f"/tools/{name}",
    )


@pytest.mark.asyncio
async def test_preflight_fails_before_fetch_or_mutation(tmp_path: Path) -> None:
    paths = make_paths(tmp_path)
    adapter = FakeAdapter([record("never-fetched")])
    git = RecordingGit()
    deps = dependencies(adapter, FakeRunner(), git)
    deps = dataclasses.replace(
        deps, tool_lookup=lambda name: None if name == "marker_single" else name
    )

    with pytest.raises(
        InfrastructureError, match="missing required tools: marker_single"
    ):
        await run_nightly(paths, deps)

    assert adapter.calls == 0
    assert git.clean_checks == []
    assert git.messages == []


@pytest.mark.asyncio
async def test_inventory_commit_precedes_consistent_batch_commit(
    tmp_path: Path,
) -> None:
    paths = make_paths(tmp_path)
    git = RecordingGit()
    runner = FakeRunner(paper_failures={"bad"})

    summary = await run_nightly(
        paths,
        dependencies(FakeAdapter([record("good"), record("bad")]), runner, git),
    )

    assert git.messages == [
        "chore: update paper inventory",
        "chore: convert paper batch 1",
    ]
    assert summary.inventory == 2
    assert summary.attempted == 2
    assert summary.succeeded == 1
    assert summary.failed == 1
    assert paths.state in git.paths[1]
    assert git.clean_checks


@pytest.mark.asyncio
async def test_inventory_commit_failure_restores_inventory_and_state(
    tmp_path: Path,
) -> None:
    paths = make_paths(tmp_path)
    paths.inventory.write_bytes(b"")
    paths.state.write_bytes(b"cursors:\n  arxiv: prior\nfailures: {}\n")
    inventory_before = paths.inventory.read_bytes()
    state_before = paths.state.read_bytes()
    git = RecordingGit(fail_message="chore: update paper inventory")

    with pytest.raises(InfrastructureError, match="git commit failed"):
        await run_nightly(
            paths,
            dependencies(FakeAdapter([record("one")]), FakeRunner(), git),
        )

    assert paths.inventory.read_bytes() == inventory_before
    assert paths.state.read_bytes() == state_before
    assert git.cleared == [(paths.inventory, paths.state)]


@pytest.mark.asyncio
async def test_formatter_failure_restores_batch_outputs_state_and_index(
    tmp_path: Path,
) -> None:
    paths = make_paths(tmp_path)
    index = paths.root / "README.md"
    index_before = index.read_bytes()
    git = RecordingGit()
    runner = FakeRunner(
        paper_failures={"bad"},
        formatter_error=InfrastructureError("formatter failed"),
    )

    with pytest.raises(InfrastructureError, match="formatter failed"):
        await run_nightly(
            paths,
            dependencies(FakeAdapter([record("good"), record("bad")]), runner, git),
        )

    assert index.read_bytes() == index_before
    assert list((paths.root / "papers").glob("*")) == []
    assert load_state(paths.state).failures == {}
    assert git.messages == ["chore: update paper inventory"]


@pytest.mark.asyncio
async def test_state_save_failure_restores_batch_outputs_and_index(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = make_paths(tmp_path)
    git = RecordingGit()

    def fail_save(path: Path, _state: object) -> None:
        path.write_text("partial state", encoding="utf-8")
        raise InfrastructureError("state save failed")

    monkeypatch.setattr("papers_pipeline.pipeline.save_state", fail_save)

    with pytest.raises(InfrastructureError, match="state save failed"):
        await run_nightly(
            paths,
            dependencies(
                FakeAdapter([record("bad")]),
                FakeRunner(paper_failures={"bad"}),
                git,
            ),
        )

    assert not paths.state.exists()
    assert (paths.root / "README.md").read_bytes() == INITIAL_README
    assert list((paths.root / "papers").glob("*")) == []
    assert git.messages == ["chore: update paper inventory"]


@pytest.mark.asyncio
async def test_batch_commit_failure_rolls_back_and_later_retry_succeeds(
    tmp_path: Path,
) -> None:
    paths = make_paths(tmp_path)
    failing_git = RecordingGit(fail_message="chore: convert paper batch 1")

    with pytest.raises(InfrastructureError, match="git commit failed"):
        await run_nightly(
            paths,
            dependencies(FakeAdapter([record("one")]), FakeRunner(), failing_git),
        )

    assert (paths.root / "README.md").read_bytes() == INITIAL_README
    assert list((paths.root / "papers").glob("*")) == []
    assert failing_git.cleared[-1]

    retry_git = RecordingGit()
    summary = await run_nightly(
        paths,
        dependencies(FakeAdapter([record("one")]), FakeRunner(), retry_git),
    )

    assert summary.succeeded == 1
    assert (paths.root / "README.md").exists()
    assert len(list((paths.root / "papers").glob("*.md"))) == 1
    assert retry_git.messages == ["chore: convert paper batch 1"]


@pytest.mark.asyncio
async def test_infrastructure_failure_summarizes_without_batch_commit(
    tmp_path: Path,
) -> None:
    paths = make_paths(tmp_path)
    git = RecordingGit()
    runner = FakeRunner(infrastructure_error=InfrastructureError("disk exhausted"))

    with pytest.raises(InfrastructureError, match="disk exhausted"):
        await run_nightly(
            paths,
            dependencies(FakeAdapter([record("one")]), runner, git),
        )

    assert git.messages == ["chore: update paper inventory"]
    assert paths.summary is not None
    assert "infrastructure failure: disk exhausted" in paths.summary.read_text()


@pytest.mark.asyncio
async def test_failed_paper_is_attempted_only_once_across_batches(
    tmp_path: Path,
) -> None:
    paths = make_paths(tmp_path, max_batches=3, max_papers=1)
    git = RecordingGit()
    runner = FakeRunner(paper_failures={"a"})

    summary = await run_nightly(
        paths,
        dependencies(FakeAdapter([record("a"), record("b")]), runner, git),
    )

    conversion_inputs = [
        Path(call[1]).stem.split(":", 1)[-1]
        for call in runner.calls
        if call[0] == "pandoc"
    ]
    assert conversion_inputs == ["a", "b"]
    assert summary.attempted == 2
    assert summary.pending == 1
    assert git.messages[-2:] == [
        "chore: convert paper batch 1",
        "chore: convert paper batch 2",
    ]


@pytest.mark.asyncio
async def test_conversion_stops_starting_batches_after_its_deadline(
    tmp_path: Path,
) -> None:
    paths = make_paths(tmp_path, max_batches=3, max_papers=1, deadline_seconds=600)
    git = RecordingGit()
    runner = FakeRunner()
    # Each conversion "takes" 10,000 seconds, far past the 600-second deadline.
    deps = dataclasses.replace(
        dependencies(FakeAdapter([record("a"), record("b")]), runner, git),
        monotonic=lambda: 10_000.0 * len(runner.calls),
    )

    summary = await run_nightly(paths, deps)

    assert [message for message in git.messages if "batch" in message] == [
        "chore: convert paper batch 1"
    ]
    assert summary.pending == 1
    assert "conversion deadline reached after 1 batches" in summary.events


@pytest.mark.asyncio
async def test_formats_only_outputs_and_index_changed_by_batch(
    tmp_path: Path,
) -> None:
    paths = make_paths(tmp_path)
    git = RecordingGit()
    runner = FakeRunner()

    await run_nightly(
        paths,
        dependencies(FakeAdapter([record("one")]), runner, git),
    )

    prettier_call = next(call for call in runner.calls if call[0] == "prettier")
    assert set(prettier_call[2:]) == {
        str(tmp_path / "README.md"),
        str(next((tmp_path / "papers").glob("*.md"))),
    }
    assert str(paths.inventory) not in prettier_call
    assert str(paths.state) not in prettier_call


@pytest.mark.asyncio
async def test_no_changes_produce_no_inventory_or_batch_commit(tmp_path: Path) -> None:
    paths = make_paths(tmp_path)
    first_git = RecordingGit()
    deps = dependencies(FakeAdapter([record("one")]), FakeRunner(), first_git)
    await run_nightly(paths, deps)

    second_git = RecordingGit()
    summary = await run_nightly(
        paths,
        dependencies(FakeAdapter([record("one")]), FakeRunner(), second_git),
    )

    assert second_git.messages == []
    assert summary.generated == 1
    assert summary.pending == 0


@pytest.mark.asyncio
async def test_capped_source_records_one_continuation_event(tmp_path: Path) -> None:
    paths = make_paths(tmp_path)

    summary = await run_nightly(
        paths,
        dependencies(
            FakeAdapter([record("one")], capped=True),
            FakeRunner(),
            RecordingGit(),
        ),
    )

    assert summary.events == ["arxiv: cap reached"]


@pytest.mark.asyncio
async def test_invalid_topic_plugin_is_rejected_before_fetch(
    tmp_path: Path,
) -> None:
    paths = make_paths(tmp_path)
    raw = yaml.safe_load(paths.config.read_text(encoding="utf-8"))
    raw["topic"]["plugin"] = "papers_pipeline.topics:not_present"
    paths.config.write_text(yaml.safe_dump(raw), encoding="utf-8")
    adapter = FakeAdapter([record("one")])

    with pytest.raises(ConfigError, match="invalid topic plugin"):
        await run_nightly(
            paths,
            dependencies(adapter, FakeRunner(), RecordingGit()),
        )

    assert adapter.calls == 0
    assert not paths.inventory.exists()


def test_git_repository_commits_only_exact_changed_paths_and_deletions(
    tmp_path: Path,
) -> None:
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=tmp_path, check=True)
    subprocess.run(
        ["git", "config", "user.email", "test@example.test"],
        cwd=tmp_path,
        check=True,
    )
    kept = tmp_path / "kept.txt"
    deleted = tmp_path / "deleted.txt"
    unrelated = tmp_path / "unrelated.txt"
    for path in (kept, deleted, unrelated):
        path.write_text("initial\n", encoding="utf-8")
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-qm", "initial"], cwd=tmp_path, check=True)
    kept.write_text("changed\n", encoding="utf-8")
    deleted.unlink()
    unrelated.write_text("do not commit\n", encoding="utf-8")

    repository = GitRepository(tmp_path)
    repository.commit([kept, deleted], "update selected")
    repository.commit([kept, deleted], "nothing else")

    assert (
        subprocess.check_output(
            ["git", "rev-list", "--count", "HEAD"], cwd=tmp_path, text=True
        ).strip()
        == "2"
    )
    changed = subprocess.check_output(
        ["git", "show", "--pretty=", "--name-only", "HEAD"],
        cwd=tmp_path,
        text=True,
    ).splitlines()
    assert changed == ["deleted.txt", "kept.txt"]
    assert (
        subprocess.check_output(
            ["git", "status", "--short"],
            cwd=tmp_path,
            text=True,
        ).strip()
        == "M unrelated.txt"
    )


def test_git_repository_rejects_dirty_relevant_paths_but_allows_unrelated_changes(
    tmp_path: Path,
) -> None:
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    relevant = tmp_path / "papers.csv"
    unrelated = tmp_path / "notes.txt"
    relevant.write_text("initial\n", encoding="utf-8")
    unrelated.write_text("initial\n", encoding="utf-8")
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    subprocess.run(
        [
            "git",
            "-c",
            "user.name=Test",
            "-c",
            "user.email=test@example.test",
            "commit",
            "-qm",
            "initial",
        ],
        cwd=tmp_path,
        check=True,
    )
    unrelated.write_text("user change\n", encoding="utf-8")
    repository = GitRepository(tmp_path)

    repository.assert_clean([relevant])
    relevant.write_text("pipeline collision\n", encoding="utf-8")

    with pytest.raises(
        InfrastructureError,
        match=r"uncommitted changes.*commit or stash[\s\S]*papers\.csv",
    ):
        repository.assert_clean([relevant])


def test_git_repository_staging_cleanup_ignores_paths_not_staged(
    tmp_path: Path,
) -> None:
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    tracked = tmp_path / "tracked.txt"
    tracked.write_text("initial\n", encoding="utf-8")
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    subprocess.run(
        [
            "git",
            "-c",
            "user.name=Test",
            "-c",
            "user.email=test@example.test",
            "commit",
            "-qm",
            "initial",
        ],
        cwd=tmp_path,
        check=True,
    )

    GitRepository(tmp_path).clear_staging([tmp_path / "missing.txt"])


def test_format_corpus_cli_selects_only_requested_shard(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    papers = tmp_path / "papers"
    papers.mkdir()
    for name in ("a.md", "b.md", "c.md"):
        (papers / name).write_text(name, encoding="utf-8")
    selected: list[Path] = []

    async def capture(paths: Sequence[Path], _runner: CommandRunner) -> None:
        selected.extend(paths)

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(cli, "format_changed", capture)

    assert cli.app(["format-corpus", "--shard-index", "1", "--shard-count", "2"]) == 0
    assert selected == [papers / "b.md"]


def test_nightly_cli_builds_real_dependency_graph(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = make_paths(tmp_path)
    captured: list[Dependencies] = []

    async def capture(_paths: PipelinePaths, deps: Dependencies) -> RunSummary:
        captured.append(deps)
        return RunSummary()

    monkeypatch.setattr(cli, "run_nightly", capture)
    monkeypatch.setattr(cli, "build_adapters", lambda *_args: {})
    monkeypatch.delenv("GITHUB_OUTPUT", raising=False)

    assert cli.app(["nightly", "--config", str(paths.config)]) == 0
    assert isinstance(captured[0].git, GitRepository)
    assert isinstance(captured[0].runner, CommandRunner)
    assert captured[0].materializer.__class__.__name__ == "DownloadingMaterializer"


@pytest.mark.parametrize(("succeeded", "expected"), [(1, "true"), (0, "false")])
def test_nightly_cli_reports_whether_more_work_remains(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    succeeded: int,
    expected: str,
) -> None:
    paths = make_paths(tmp_path)
    output = tmp_path / "github-output"

    async def run(_paths: PipelinePaths, _deps: Dependencies) -> RunSummary:
        return RunSummary(pending=3, succeeded=succeeded)

    monkeypatch.setattr(cli, "run_nightly", run)
    monkeypatch.setattr(cli, "build_adapters", lambda *_args: {})
    monkeypatch.setenv("GITHUB_OUTPUT", str(output))

    assert cli.app(["nightly", "--config", str(paths.config)]) == 0
    assert output.read_text(encoding="utf-8") == f"more_work={expected}\n"
