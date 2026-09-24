from dataclasses import dataclass
from datetime import datetime, timezone
from typing import cast

import pytest
from pydantic import ValidationError

from papers_pipeline.adapters.base import (
    FetchPage,
    FetchWindow,
    collect_records,
)
from papers_pipeline.adapters import build_adapters
from papers_pipeline.adapters.semantic_scholar import SemanticScholarAdapter
from papers_pipeline.config import (
    AdapterConfig,
    ConcurrencyConfig,
    ConversionConfig,
    FetchConfig,
    PipelineConfig,
    RepositoryConfig,
    TopicConfig,
)
from papers_pipeline.errors import InfrastructureError, PaperError
from papers_pipeline.models import SourceRecord


@dataclass(frozen=True)
class _ParserItem:
    value: str


def test_collect_records_keeps_paper_errors_and_records() -> None:
    source_record = SourceRecord(
        source="arxiv",
        source_id="2401.00001",
        title="Title",
        abstract="Abstract",
        authors=("Author",),
        published=datetime(2024, 1, 2, tzinfo=timezone.utc),
        url="https://example.test/paper",
        input_format="pdf",
        input_url="https://example.test/paper.pdf",
    )

    def parser(item: _ParserItem) -> SourceRecord:
        if item.value == "bad":
            raise PaperError("bad paper")
        if item.value == "boom":
            raise InfrastructureError("boom")
        return source_record

    records, errors = collect_records(
        [_ParserItem("ok"), _ParserItem("bad")],
        parser,
    )

    assert records == (source_record,)
    assert errors == ("bad paper",)


def test_collect_records_propagates_infrastructure_errors() -> None:
    def parser(_: _ParserItem) -> SourceRecord:
        raise InfrastructureError("boom")

    with pytest.raises(InfrastructureError, match="boom"):
        collect_records([_ParserItem("boom")], parser)


def test_fetch_page_is_immutable() -> None:
    page = FetchPage(
        records=(),
        next_cursor=None,
        capped=False,
        permanent_errors=(),
    )

    with pytest.raises(Exception):
        setattr(page, "records", ())


def test_fetch_window_is_immutable() -> None:
    window = FetchWindow(
        start=datetime(2024, 1, 1, tzinfo=timezone.utc),
        end=datetime(2024, 1, 8, tzinfo=timezone.utc),
    )

    with pytest.raises(Exception):
        setattr(window, "start", datetime(2024, 1, 2, tzinfo=timezone.utc))


def test_fetch_window_rejects_naive_datetimes() -> None:
    with pytest.raises(
        ValidationError,
        match="FetchWindow.start and FetchWindow.end must be timezone-aware",
    ):
        FetchWindow(
            start=datetime(2024, 1, 1),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        )


def test_fetch_window_rejects_reversed_interval() -> None:
    with pytest.raises(
        ValidationError,
        match="FetchWindow.start must be before or equal to FetchWindow.end",
    ):
        FetchWindow(
            start=datetime(2024, 1, 8, tzinfo=timezone.utc),
            end=datetime(2024, 1, 1, tzinfo=timezone.utc),
        )


def _pipeline_config(adapters: list[AdapterConfig]) -> PipelineConfig:
    return PipelineConfig(
        repository=RepositoryConfig(
            name="Example Papers",
            slug="example-papers",
            description="Example topic",
        ),
        adapters=adapters,
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


def test_build_adapters_registers_all_runtime_families() -> None:
    adapters = build_adapters(
        _pipeline_config(
            [
                AdapterConfig(
                    name="semantic_scholar",
                    enabled=True,
                    secret_env="SEMANTIC_SCHOLAR_API_KEY",
                    lookback_days=7,
                    page_size=1,
                    max_pages=1,
                    max_results=1,
                    filters={"query": "speech"},
                )
            ]
        ),
        {"SEMANTIC_SCHOLAR_API_KEY": "secret"},
    )

    assert set(adapters) == {
        "arxiv",
        "huggingface",
        "semantic_scholar",
        "dblp",
        "biorxiv_crossref",
        "papers_with_code",
    }
    semantic_adapter = cast(SemanticScholarAdapter, adapters["semantic_scholar"])

    assert semantic_adapter.api_key == "secret"


def test_build_adapters_avoids_missing_semantic_scholar_key_for_omitted_or_disabled_config() -> (
    None
):
    omitted = build_adapters(_pipeline_config([]), {})
    disabled = build_adapters(
        _pipeline_config(
            [
                AdapterConfig(
                    name="semantic_scholar",
                    enabled=False,
                    secret_env="SEMANTIC_SCHOLAR_API_KEY",
                    lookback_days=7,
                    page_size=1,
                    max_pages=1,
                    max_results=1,
                    filters={"query": "speech"},
                )
            ]
        ),
        {},
    )

    omitted_semantic = cast(SemanticScholarAdapter, omitted["semantic_scholar"])
    disabled_semantic = cast(SemanticScholarAdapter, disabled["semantic_scholar"])

    assert omitted_semantic.api_key == ""
    assert disabled_semantic.api_key == ""
