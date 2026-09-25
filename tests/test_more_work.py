from datetime import date, datetime, timezone

import pytest

from papers_pipeline.config import PipelineConfig
from papers_pipeline.models import BackfillProgress, PipelineState, SourceContinuation
from papers_pipeline.pipeline import has_more_work
from papers_pipeline.summary import RunSummary
from test_fetch import adapter_config, pipeline_config

LIMIT = datetime(1991, 8, 1, tzinfo=timezone.utc)
LATER = datetime(2020, 1, 1, tzinfo=timezone.utc)
EARLIER = datetime(2019, 1, 1, tzinfo=timezone.utc)


def config(backfill_start: date | None = date(1991, 8, 1)) -> PipelineConfig:
    return pipeline_config(
        adapter_config("arxiv", lookback_days=7).model_copy(
            update={"backfill_start": backfill_start}
        )
    )


def covered(at: datetime, *, in_flight: bool = False) -> PipelineState:
    continuation = (
        SourceContinuation(cursor="c", window_start=at, window_end=LATER)
        if in_flight
        else None
    )
    return PipelineState(
        backfill={"arxiv": BackfillProgress(covered_from=at, continuation=continuation)}
    )


@pytest.mark.parametrize(
    ("before", "after", "summary", "expected"),
    [
        # Backfill advanced and has further to go.
        (PipelineState(), covered(LATER), RunSummary(), True),
        (covered(LATER), covered(EARLIER), RunSummary(), True),
        (covered(LATER), covered(LATER, in_flight=True), RunSummary(), True),
        # Backfill finished; continue only while conversion progresses.
        (covered(EARLIER), covered(LIMIT), RunSummary(pending=5, succeeded=3), True),
        (covered(LIMIT), covered(LIMIT), RunSummary(pending=5, succeeded=3), True),
        (covered(LIMIT), covered(LIMIT), RunSummary(pending=5, succeeded=0), False),
        (covered(EARLIER), covered(LIMIT), RunSummary(pending=0), False),
        # No progress (e.g. the source was unavailable): stop the chain.
        (covered(LATER), covered(LATER), RunSummary(), False),
    ],
)
def test_more_work_requires_progress_and_something_left(
    before: PipelineState, after: PipelineState, summary: RunSummary, expected: bool
) -> None:
    assert has_more_work(config(), before, after, summary) is expected


def test_sources_without_backfill_need_no_more_runs() -> None:
    assert (
        has_more_work(config(None), PipelineState(), PipelineState(), RunSummary())
        is False
    )
