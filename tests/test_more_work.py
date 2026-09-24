from datetime import date, datetime, timezone

import pytest

from papers_pipeline.config import PipelineConfig
from papers_pipeline.models import BackfillProgress, PipelineState, SourceContinuation
from papers_pipeline.pipeline import has_more_work
from papers_pipeline.summary import RunSummary
from test_fetch import adapter_config, pipeline_config

START = date(1991, 8, 1)
LIMIT = datetime(1991, 8, 1, tzinfo=timezone.utc)
LATER = datetime(2020, 1, 1, tzinfo=timezone.utc)


def config(backfill_start: date | None = START) -> PipelineConfig:
    return pipeline_config(
        adapter_config("arxiv", lookback_days=7).model_copy(
            update={"backfill_start": backfill_start}
        )
    )


@pytest.mark.parametrize(
    ("state", "summary", "expected"),
    [
        # Backfill has not reached its start date.
        (PipelineState(), RunSummary(), True),
        (
            PipelineState(backfill={"arxiv": BackfillProgress(covered_from=LATER)}),
            RunSummary(),
            True,
        ),
        # A capped chunk is still in flight, even at the start date.
        (
            PipelineState(
                backfill={
                    "arxiv": BackfillProgress(
                        covered_from=LIMIT,
                        continuation=SourceContinuation(
                            cursor="c", window_start=LIMIT, window_end=LATER
                        ),
                    )
                }
            ),
            RunSummary(),
            True,
        ),
        # History fetched: continue only while conversion is making progress.
        (
            PipelineState(backfill={"arxiv": BackfillProgress(covered_from=LIMIT)}),
            RunSummary(pending=5, succeeded=3),
            True,
        ),
        (
            PipelineState(backfill={"arxiv": BackfillProgress(covered_from=LIMIT)}),
            RunSummary(pending=5, succeeded=0),
            False,
        ),
        (
            PipelineState(backfill={"arxiv": BackfillProgress(covered_from=LIMIT)}),
            RunSummary(pending=0, succeeded=3),
            False,
        ),
    ],
)
def test_more_work_tracks_backfill_and_conversion_progress(
    state: PipelineState, summary: RunSummary, expected: bool
) -> None:
    assert has_more_work(config(), state, summary) is expected


def test_sources_without_backfill_need_no_more_runs() -> None:
    assert has_more_work(config(None), PipelineState(), RunSummary()) is False
