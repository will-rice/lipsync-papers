"""Cross-source fetch orchestration with shared deadlines and continuation state."""

from collections.abc import Callable, Mapping
from dataclasses import dataclass
from datetime import UTC, datetime, time, timedelta

from papers_pipeline.adapters.base import Adapter, FetchPage, FetchWindow
from papers_pipeline.config import AdapterConfig, PipelineConfig
from papers_pipeline.errors import InfrastructureError
from papers_pipeline.http import Deadline, RequestClient
from papers_pipeline.models import (
    BackfillProgress,
    PipelineState,
    SourceContinuation,
    SourceRecord,
)


@dataclass(frozen=True)
class FetchStats:
    source: str
    fetched: int
    rejected: int
    capped: bool
    complete: bool


@dataclass(frozen=True)
class FetchResult:
    records: tuple[SourceRecord, ...]
    state: PipelineState
    stats: tuple[FetchStats, ...]
    events: tuple[str, ...]


@dataclass(frozen=True)
class _BackfillPlan:
    window: FetchWindow
    cursor: str | None
    covered_from: datetime


@dataclass(frozen=True)
class _WindowFetch:
    records: list[SourceRecord]
    cursor: str | None
    capped: bool
    complete: bool
    rejected: int
    error_events: list[str]


def _prefix_events(source: str, events: list[str]) -> tuple[str, ...]:
    return tuple(f"{source}: {event}" for event in events)


def _page_error_events(source: str, page: FetchPage) -> tuple[str, ...]:
    return tuple(
        f"{source}: permanent error: {message}" for message in page.permanent_errors
    )


def _page_config(
    config: PipelineConfig, adapter_index: int, remaining: int
) -> AdapterConfig:
    adapter_config = config.adapters[adapter_index]
    return type(adapter_config).model_validate(
        {
            **adapter_config.model_dump(),
            "page_size": min(adapter_config.page_size, remaining),
            "max_results": remaining,
        }
    )


async def fetch_all(
    config: PipelineConfig,
    state: PipelineState,
    adapters: Mapping[str, Adapter],
    client_factory: Callable[[Deadline], RequestClient],
    now: datetime,
) -> FetchResult:
    deadline = Deadline.start(config.fetch.total_deadline_seconds)
    records: list[SourceRecord] = []
    stats: list[FetchStats] = []
    events: list[str] = []
    continuations = dict(state.continuations)
    backfill = dict(state.backfill)

    for adapter_index, adapter_config in enumerate(config.adapters):
        if not adapter_config.enabled:
            continue

        adapter = adapters[adapter_config.name]
        continuation = continuations.get(adapter.name)
        window = FetchWindow(
            start=(
                continuation.window_start
                if continuation
                else now - timedelta(days=adapter_config.lookback_days)
            ),
            end=continuation.window_end if continuation else now,
        )
        starting_cursor = continuation.cursor if continuation else None
        backfill_plan = _backfill_plan(
            adapter_config, backfill.get(adapter.name), window.start
        )

        async with client_factory(deadline) as client:
            forward = await _fetch_window(
                adapter, config, adapter_index, window, starting_cursor, client
            )
            history = (
                await _fetch_window(
                    adapter,
                    config,
                    adapter_index,
                    backfill_plan.window,
                    backfill_plan.cursor,
                    client,
                )
                if backfill_plan
                else None
            )
            events.extend(_prefix_events(adapter.name, client.events))
        events.extend(forward.error_events)

        if forward.cursor is not None:
            continuations[adapter.name] = SourceContinuation(
                cursor=forward.cursor,
                window_start=window.start,
                window_end=window.end,
            )
            if forward.capped:
                events.append(f"{adapter.name}: cap reached; continuation persisted")
        elif forward.complete:
            continuations.pop(adapter.name, None)
            if starting_cursor is not None:
                events.append(f"{adapter.name}: fetch complete; cursor cleared")
            else:
                events.append(f"{adapter.name}: fetch complete")
        elif forward.capped:
            continuations.pop(adapter.name, None)
            events.append(f"{adapter.name}: cap reached")

        source_records = forward.records
        rejected = forward.rejected
        if history is not None and backfill_plan is not None:
            history_window = backfill_plan.window
            events.extend(history.error_events)
            if history.cursor is not None:
                backfill[adapter.name] = BackfillProgress(
                    covered_from=backfill_plan.covered_from,
                    continuation=SourceContinuation(
                        cursor=history.cursor,
                        window_start=history_window.start,
                        window_end=history_window.end,
                    ),
                )
                events.append(
                    f"{adapter.name}: backfill cap reached; continuation persisted"
                )
            else:
                # A complete window, or one capped without a cursor, moves the
                # history boundary back; the latter cannot be resumed.
                backfill[adapter.name] = BackfillProgress(
                    covered_from=history_window.start
                )
                events.append(
                    f"{adapter.name}: backfilled to "
                    f"{history_window.start.date().isoformat()}"
                )
            source_records = [*source_records, *history.records]
            rejected += history.rejected

        records.extend(source_records)
        stats.append(
            FetchStats(
                source=adapter.name,
                fetched=len(source_records),
                rejected=rejected,
                capped=forward.capped or bool(history and history.capped),
                complete=forward.complete,
            )
        )

    return FetchResult(
        records=tuple(records),
        state=state.model_copy(
            update={"continuations": continuations, "backfill": backfill}
        ),
        stats=tuple(stats),
        events=tuple(events),
    )


def _backfill_plan(
    adapter_config: AdapterConfig,
    progress: BackfillProgress | None,
    forward_start: datetime,
) -> _BackfillPlan | None:
    """Pick this run's history window: resume a capped one, or step further back."""
    if adapter_config.backfill_start is None:
        return None
    # History starts where the recurring lookback window ends.
    covered_from = progress.covered_from if progress else forward_start
    if progress and progress.continuation:
        return _BackfillPlan(
            window=FetchWindow(
                start=progress.continuation.window_start,
                end=progress.continuation.window_end,
            ),
            cursor=progress.continuation.cursor,
            covered_from=covered_from,
        )
    limit = datetime.combine(adapter_config.backfill_start, time.min, tzinfo=UTC)
    if covered_from <= limit:
        return None
    return _BackfillPlan(
        window=FetchWindow(
            start=max(
                limit, covered_from - timedelta(days=adapter_config.backfill_days)
            ),
            end=covered_from,
        ),
        cursor=None,
        covered_from=covered_from,
    )


async def _fetch_window(
    adapter: Adapter,
    config: PipelineConfig,
    adapter_index: int,
    window: FetchWindow,
    cursor: str | None,
    client: RequestClient,
) -> _WindowFetch:
    """Page through one window within the adapter's page and result caps."""
    adapter_config = config.adapters[adapter_index]
    records: list[SourceRecord] = []
    rejected = 0
    error_events: list[str] = []
    capped = False
    complete = False
    pages_fetched = 0
    while pages_fetched < adapter_config.max_pages:
        remaining = adapter_config.max_results - len(records)
        page = await adapter.fetch(
            window, cursor, client, _page_config(config, adapter_index, remaining)
        )
        pages_fetched += 1
        error_events.extend(_page_error_events(adapter.name, page))
        rejected += len(page.permanent_errors)

        if len(page.records) > remaining:
            raise InfrastructureError(
                f"{adapter.name} returned {len(page.records)} records with only "
                f"{remaining} results remaining"
            )
        records.extend(page.records)

        cursor = page.next_cursor
        if cursor is None:
            complete = not page.capped
            capped = page.capped
            break
        if (
            page.capped
            or len(records) >= adapter_config.max_results
            or pages_fetched >= adapter_config.max_pages
        ):
            capped = True
            break
    return _WindowFetch(
        records=records,
        cursor=cursor,
        capped=capped,
        complete=complete,
        rejected=rejected,
        error_events=error_events,
    )
