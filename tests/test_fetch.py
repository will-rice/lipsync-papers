from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import date, datetime, time, timedelta, timezone

import httpx
import pytest

from papers_pipeline.adapters.base import FetchPage, FetchWindow
from papers_pipeline.config import (
    AdapterConfig,
    AdapterName,
    ConcurrencyConfig,
    ConversionConfig,
    FetchConfig,
    PipelineConfig,
    RepositoryConfig,
    TopicConfig,
)
from papers_pipeline.errors import InfrastructureError
from papers_pipeline.http import Deadline, RequestClient
from papers_pipeline.models import (
    BackfillProgress,
    PipelineState,
    SourceContinuation,
    SourceRecord,
)
from papers_pipeline.fetch import fetch_all

NOW = datetime(2026, 9, 23, 18, 29, 6, tzinfo=timezone.utc)


def source_record(
    source: str,
    source_id: str,
    *,
    published: datetime = NOW - timedelta(days=1),
) -> SourceRecord:
    return SourceRecord(
        source=source,
        source_id=source_id,
        title=f"{source_id} title",
        abstract=f"{source_id} abstract",
        authors=("A. Author",),
        published=published,
        url=f"https://example.test/{source}/{source_id}",
        input_format="pdf",
        input_url=f"https://example.test/{source}/{source_id}.pdf",
    )


def pipeline_config(*adapters: AdapterConfig) -> PipelineConfig:
    return PipelineConfig(
        repository=RepositoryConfig(
            name="Example Papers",
            slug="example-papers",
            description="Example topic",
        ),
        adapters=list(adapters),
        topic=TopicConfig(),
        fetch=FetchConfig(
            request_timeout_seconds=5,
            retries=0,
            backoff_seconds=0,
            total_deadline_seconds=300,
        ),
        conversion=ConversionConfig(
            max_batches_per_run=1,
            max_papers=5,
            max_cost=10,
            html_cost=1,
            latex_cost=1,
            pdf_cost=1,
        ),
        concurrency=ConcurrencyConfig(html=1, latex=1, pdf=1),
    )


class TrackingClient(RequestClient):
    def __init__(
        self,
        *,
        config: FetchConfig,
        deadline: Deadline,
        seed_events: tuple[str, ...] = (),
    ) -> None:
        super().__init__(
            config=config,
            deadline=deadline,
            transport=httpx.MockTransport(
                lambda request: httpx.Response(
                    599,
                    request=request,
                    text=f"unexpected network call: {request.url}",
                )
            ),
        )
        self.events.extend(seed_events)
        self.closed = False

    async def aclose(self) -> None:
        self.closed = True
        await super().aclose()


@dataclass
class RecordingAdapter:
    name: str
    pages: list[FetchPage] = field(default_factory=list)
    failure: InfrastructureError | None = None
    record_sources: frozenset[str] = field(default_factory=lambda: frozenset({"stub"}))
    windows: list[FetchWindow] = field(default_factory=list)
    cursors: list[str | None] = field(default_factory=list)
    clients: list[RequestClient] = field(default_factory=list)
    configs: list[AdapterConfig] = field(default_factory=list)

    async def fetch(
        self,
        window: FetchWindow,
        cursor: str | None,
        client: RequestClient,
        config: AdapterConfig,
    ) -> FetchPage:
        self.windows.append(window)
        self.cursors.append(cursor)
        self.clients.append(client)
        self.configs.append(config)
        if self.failure is not None:
            raise self.failure
        if not self.pages:
            raise AssertionError(f"no recorded page left for {self.name}")
        return self.pages.pop(0)


def adapter_config(
    name: AdapterName,
    *,
    lookback_days: int,
    page_size: int = 2,
    max_pages: int = 10,
    max_results: int = 10,
    enabled: bool = True,
) -> AdapterConfig:
    return AdapterConfig(
        name=name,
        enabled=enabled,
        lookback_days=lookback_days,
        page_size=page_size,
        max_pages=max_pages,
        max_results=max_results,
        filters={},
    )


def client_factory(
    config: FetchConfig,
    *,
    seed_events: tuple[str, ...] = (),
) -> tuple[Callable[[Deadline], TrackingClient], list[TrackingClient], list[Deadline]]:
    created: list[TrackingClient] = []
    deadlines: list[Deadline] = []

    def build(deadline: Deadline) -> TrackingClient:
        deadlines.append(deadline)
        client = TrackingClient(
            config=config, deadline=deadline, seed_events=seed_events
        )
        created.append(client)
        return client

    return build, created, deadlines


@pytest.mark.asyncio
async def test_fetch_uses_source_windows_continues_after_zero_output_and_clears_completed_cursor() -> (
    None
):
    config = pipeline_config(adapter_config("arxiv", lookback_days=7))
    state = PipelineState(
        continuations={
            "arxiv": SourceContinuation(
                cursor="opaque-start",
                window_start=NOW - timedelta(days=7),
                window_end=NOW,
            )
        }
    )
    adapter = RecordingAdapter(
        "arxiv",
        pages=[
            FetchPage(
                records=(), next_cursor="opaque-mid", capped=False, permanent_errors=()
            ),
            FetchPage(
                records=(source_record("arxiv", "2401.00001"),),
                next_cursor="opaque-final",
                capped=False,
                permanent_errors=(),
            ),
            FetchPage(
                records=(source_record("arxiv", "2401.00002"),),
                next_cursor=None,
                capped=False,
                permanent_errors=("malformed arxiv record",),
            ),
        ],
    )
    factory, clients, _ = client_factory(
        config.fetch,
        seed_events=("retry 1: HTTP 503 for https://example.test/arxiv",),
    )

    result = await fetch_all(config, state, {"arxiv": adapter}, factory, NOW)

    assert adapter.windows == [
        FetchWindow(start=NOW - timedelta(days=7), end=NOW),
        FetchWindow(start=NOW - timedelta(days=7), end=NOW),
        FetchWindow(start=NOW - timedelta(days=7), end=NOW),
    ]
    assert adapter.cursors == ["opaque-start", "opaque-mid", "opaque-final"]
    assert len({id(client) for client in adapter.clients}) == 1
    assert clients[0].closed is True
    assert tuple(record.source_id for record in result.records) == (
        "2401.00001",
        "2401.00002",
    )
    assert result.state.continuations == {}
    assert result.stats[0].source == "arxiv"
    assert result.stats[0].fetched == 2
    assert result.stats[0].rejected == 1
    assert result.stats[0].capped is False
    assert result.stats[0].complete is True
    assert result.events == (
        "arxiv: retry 1: HTTP 503 for https://example.test/arxiv",
        "arxiv: permanent error: malformed arxiv record",
        "arxiv: fetch complete; cursor cleared",
    )


@pytest.mark.asyncio
async def test_fetch_persists_cursor_and_marks_result_cap_without_completing() -> None:
    config = pipeline_config(adapter_config("arxiv", lookback_days=7, max_results=1))
    adapter = RecordingAdapter(
        "arxiv",
        pages=[
            FetchPage(
                records=(source_record("arxiv", "2401.00001"),),
                next_cursor="opaque-next",
                capped=False,
                permanent_errors=(),
            ),
        ],
    )
    factory, clients, _ = client_factory(config.fetch)

    result = await fetch_all(config, PipelineState(), {"arxiv": adapter}, factory, NOW)

    assert clients[0].closed is True
    assert result.state.continuations == {
        "arxiv": SourceContinuation(
            cursor="opaque-next",
            window_start=NOW - timedelta(days=7),
            window_end=NOW,
        )
    }
    assert result.stats[0].fetched == 1
    assert result.stats[0].rejected == 0
    assert result.stats[0].capped is True
    assert result.stats[0].complete is False
    assert result.events == ("arxiv: cap reached; continuation persisted",)


@pytest.mark.asyncio
async def test_fetch_raises_when_adapter_returns_more_records_than_remaining_budget() -> (
    None
):
    config = pipeline_config(
        adapter_config("arxiv", lookback_days=7, max_results=3, page_size=2)
    )
    adapter = RecordingAdapter(
        "arxiv",
        pages=[
            FetchPage(
                records=(
                    source_record("arxiv", "2401.00001"),
                    source_record("arxiv", "2401.00002"),
                ),
                next_cursor="opaque-mid",
                capped=False,
                permanent_errors=(),
            ),
            FetchPage(
                records=(
                    source_record("arxiv", "2401.00003"),
                    source_record("arxiv", "2401.00004"),
                ),
                next_cursor="opaque-skip",
                capped=False,
                permanent_errors=(),
            ),
        ],
    )
    factory, clients, _ = client_factory(config.fetch)

    with pytest.raises(
        InfrastructureError,
        match="arxiv returned 2 records with only 1 results remaining",
    ):
        await fetch_all(config, PipelineState(), {"arxiv": adapter}, factory, NOW)

    assert adapter.cursors == [None, "opaque-mid"]
    assert len(adapter.pages) == 0
    assert clients[0].closed is True


@pytest.mark.asyncio
async def test_fetch_passes_remaining_budget_to_adapter_and_preserves_page_two_continuation() -> (
    None
):
    config = pipeline_config(
        adapter_config("arxiv", lookback_days=7, max_results=3, page_size=2)
    )
    adapter = RecordingAdapter(
        "arxiv",
        pages=[
            FetchPage(
                records=(
                    source_record("arxiv", "2401.00001"),
                    source_record("arxiv", "2401.00002"),
                ),
                next_cursor="opaque-mid",
                capped=False,
                permanent_errors=(),
            ),
            FetchPage(
                records=(source_record("arxiv", "2401.00003"),),
                next_cursor="opaque-tail",
                capped=True,
                permanent_errors=(),
            ),
        ],
    )
    factory, clients, _ = client_factory(config.fetch)

    result = await fetch_all(config, PipelineState(), {"arxiv": adapter}, factory, NOW)

    assert [(cfg.page_size, cfg.max_results) for cfg in adapter.configs] == [
        (2, 3),
        (1, 1),
    ]
    assert tuple(record.source_id for record in result.records) == (
        "2401.00001",
        "2401.00002",
        "2401.00003",
    )
    assert len({record.source_id for record in result.records}) == 3
    assert result.state.continuations["arxiv"].cursor == "opaque-tail"
    assert result.stats[0].fetched == 3
    assert result.stats[0].capped is True
    assert result.stats[0].complete is False
    assert result.events == ("arxiv: cap reached; continuation persisted",)
    assert clients[0].closed is True


@pytest.mark.asyncio
async def test_fetch_enforces_page_cap_and_uses_configured_adapter_order_under_one_deadline() -> (
    None
):
    config = pipeline_config(
        adapter_config("dblp", lookback_days=3, max_pages=1),
        adapter_config("arxiv", lookback_days=7),
    )
    dblp = RecordingAdapter(
        "dblp",
        pages=[
            FetchPage(
                records=(source_record("dblp", "dblp-1"),),
                next_cursor="dblp-cursor",
                capped=False,
                permanent_errors=(),
            ),
        ],
    )
    arxiv = RecordingAdapter(
        "arxiv",
        pages=[
            FetchPage(
                records=(source_record("arxiv", "2401.00003"),),
                next_cursor=None,
                capped=False,
                permanent_errors=(),
            ),
        ],
    )
    factory, clients, deadlines = client_factory(config.fetch)

    result = await fetch_all(
        config,
        PipelineState(),
        {"arxiv": arxiv, "dblp": dblp},
        factory,
        NOW,
    )

    assert dblp.windows == [FetchWindow(start=NOW - timedelta(days=3), end=NOW)]
    assert arxiv.windows == [FetchWindow(start=NOW - timedelta(days=7), end=NOW)]
    assert tuple(record.source for record in result.records) == ("dblp", "arxiv")
    assert tuple(stat.source for stat in result.stats) == ("dblp", "arxiv")
    assert result.state.continuations["dblp"].cursor == "dblp-cursor"
    assert result.stats[0].capped is True
    assert result.stats[0].complete is False
    assert result.stats[1].capped is False
    assert result.stats[1].complete is True
    assert len(clients) == 2
    assert clients[0].closed is True
    assert clients[1].closed is True
    assert deadlines[0] is deadlines[1]
    assert result.events == (
        "dblp: cap reached; continuation persisted",
        "arxiv: fetch complete",
    )


@pytest.mark.asyncio
async def test_infrastructure_failure_aborts_fetching_and_closes_current_client() -> (
    None
):
    config = pipeline_config(
        adapter_config("arxiv", lookback_days=7),
        adapter_config("dblp", lookback_days=3),
    )
    failing = RecordingAdapter(
        "arxiv",
        failure=InfrastructureError(
            "request retries exhausted: https://example.test/arxiv"
        ),
    )
    skipped = RecordingAdapter(
        "dblp",
        pages=[
            FetchPage(
                records=(source_record("dblp", "dblp-1"),),
                next_cursor=None,
                capped=False,
                permanent_errors=(),
            )
        ],
    )
    factory, clients, _ = client_factory(config.fetch)

    with pytest.raises(InfrastructureError, match="request retries exhausted"):
        await fetch_all(
            config, PipelineState(), {"arxiv": failing, "dblp": skipped}, factory, NOW
        )

    assert len(clients) == 1
    assert clients[0].closed is True
    assert skipped.windows == []


@pytest.mark.asyncio
async def test_later_run_reuses_persisted_window_until_source_completes() -> None:
    config = pipeline_config(adapter_config("arxiv", lookback_days=7, max_pages=1))
    first_adapter = RecordingAdapter(
        "arxiv",
        pages=[
            FetchPage(
                records=(source_record("arxiv", "first"),),
                next_cursor="resume",
                capped=False,
                permanent_errors=(),
            )
        ],
    )
    factory, _, _ = client_factory(config.fetch)
    first = await fetch_all(
        config, PipelineState(), {"arxiv": first_adapter}, factory, NOW
    )

    later = NOW + timedelta(days=2)
    second_adapter = RecordingAdapter(
        "arxiv",
        pages=[
            FetchPage(
                records=(source_record("arxiv", "second"),),
                next_cursor=None,
                capped=False,
                permanent_errors=(),
            )
        ],
    )
    resumed = await fetch_all(
        config, first.state, {"arxiv": second_adapter}, factory, later
    )

    assert second_adapter.windows == [
        FetchWindow(start=NOW - timedelta(days=7), end=NOW)
    ]
    assert second_adapter.cursors == ["resume"]
    assert resumed.state.continuations == {}


def page(*records: SourceRecord, next_cursor: str | None = None) -> FetchPage:
    return FetchPage(
        records=records, next_cursor=next_cursor, capped=False, permanent_errors=()
    )


def backfill_config(start: date, *, backfill_days: int = 30) -> PipelineConfig:
    return pipeline_config(
        adapter_config("arxiv", lookback_days=7).model_copy(
            update={"backfill_start": start, "backfill_days": backfill_days}
        )
    )


@pytest.mark.asyncio
async def test_backfill_steps_back_one_chunk_behind_the_lookback_window() -> None:
    config = backfill_config(date(2020, 1, 1))
    old = source_record("arxiv", "old", published=NOW - timedelta(days=20))
    adapter = RecordingAdapter("arxiv", pages=[page(), page(old)])
    factory, _, _ = client_factory(config.fetch)

    result = await fetch_all(config, PipelineState(), {"arxiv": adapter}, factory, NOW)

    lookback_start = NOW - timedelta(days=7)
    assert adapter.windows == [
        FetchWindow(start=lookback_start, end=NOW),
        FetchWindow(start=lookback_start - timedelta(days=30), end=lookback_start),
    ]
    assert result.records == (old,)
    assert result.stats[0].fetched == 1
    assert result.state.backfill == {
        "arxiv": BackfillProgress(covered_from=lookback_start - timedelta(days=30))
    }
    assert result.events[-1] == (
        f"arxiv: backfilled to {(lookback_start - timedelta(days=30)).date()}"
    )


@pytest.mark.asyncio
async def test_capped_backfill_window_resumes_before_stepping_further_back() -> None:
    config = backfill_config(date(2020, 1, 1))
    covered_from = NOW - timedelta(days=100)
    history_window = FetchWindow(
        start=covered_from - timedelta(days=30), end=covered_from
    )
    state = PipelineState(
        backfill={
            "arxiv": BackfillProgress(
                covered_from=covered_from,
                continuation=SourceContinuation(
                    cursor="history-2",
                    window_start=history_window.start,
                    window_end=history_window.end,
                ),
            )
        }
    )
    adapter = RecordingAdapter(
        "arxiv", pages=[page(), page(next_cursor="history-3"), page(), page()]
    )
    factory, _, _ = client_factory(config.fetch)
    capped = config.model_copy(
        update={"adapters": [config.adapters[0].model_copy(update={"max_pages": 1})]}
    )

    first = await fetch_all(capped, state, {"arxiv": adapter}, factory, NOW)
    second = await fetch_all(config, first.state, {"arxiv": adapter}, factory, NOW)

    # Each run fetches its lookback window, then resumes the capped history window.
    assert adapter.windows[1::2] == [history_window, history_window]
    assert adapter.cursors[1::2] == ["history-2", "history-3"]
    assert first.state.backfill["arxiv"].covered_from == covered_from
    assert second.state.backfill == {
        "arxiv": BackfillProgress(covered_from=history_window.start)
    }


@pytest.mark.asyncio
async def test_backfill_stops_at_its_start_date() -> None:
    start = (NOW - timedelta(days=20)).date()
    config = backfill_config(start)
    adapter = RecordingAdapter("arxiv", pages=[page(), page(), page()])
    factory, _, _ = client_factory(config.fetch)

    first = await fetch_all(config, PipelineState(), {"arxiv": adapter}, factory, NOW)
    second = await fetch_all(config, first.state, {"arxiv": adapter}, factory, NOW)

    limit = datetime.combine(start, time.min, tzinfo=timezone.utc)
    assert adapter.windows[1] == FetchWindow(start=limit, end=NOW - timedelta(days=7))
    assert len(adapter.windows) == 3  # second run fetches only the lookback window
    assert second.state.backfill == {"arxiv": BackfillProgress(covered_from=limit)}


@pytest.mark.parametrize("name", ["dblp", "papers_with_code"])
def test_backfill_requires_a_source_that_queries_date_ranges(
    name: AdapterName,
) -> None:
    with pytest.raises(ValueError, match=f"{name} cannot backfill"):
        adapter_config(name, lookback_days=7).model_validate(
            {
                **adapter_config(name, lookback_days=7).model_dump(),
                "backfill_start": date(2020, 1, 1),
            }
        )
