from datetime import datetime, timezone

import pytest

from papers_pipeline.adapters.base import FetchWindow
from papers_pipeline.adapters.dblp import DblpAdapter, electronic_format
from papers_pipeline.config import AdapterConfig
from papers_pipeline.errors import InfrastructureError
from papers_pipeline.http import RequestClient
from papers_pipeline.normalize import normalize

from .contract import assert_adapter_contract


@pytest.mark.asyncio
async def test_dblp_contract(
    dblp_client: RequestClient,
    dblp_config: AdapterConfig,
) -> None:
    await assert_adapter_contract(DblpAdapter(), dblp_client, dblp_config)


@pytest.mark.asyncio
async def test_dblp_continuation_cursor_is_deterministic_and_opaque(
    dblp_client: RequestClient,
    dblp_config: AdapterConfig,
) -> None:
    adapter = DblpAdapter()
    first_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=dblp_client,
        config=dblp_config,
    )

    second_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=first_page.next_cursor,
        client=dblp_client,
        config=dblp_config,
    )

    assert tuple(record.source_id for record in first_page.records) == (
        "conf/test/Fixture24",
    )
    assert first_page.next_cursor
    assert first_page.next_cursor != "1"
    assert tuple(record.source_id for record in second_page.records) == (
        "journals/test/Fixture25",
    )
    assert second_page.next_cursor
    assert second_page.next_cursor != first_page.next_cursor
    assert second_page.capped is False


@pytest.mark.asyncio
async def test_dblp_max_pages_sets_capped_without_dropping_cursor(
    dblp_client: RequestClient,
    dblp_config: AdapterConfig,
) -> None:
    adapter = DblpAdapter()
    first_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=dblp_client,
        config=dblp_config,
    )

    second_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=first_page.next_cursor,
        client=dblp_client,
        config=dblp_config.model_copy(update={"max_pages": 2, "max_results": 10}),
    )

    assert second_page.next_cursor
    assert second_page.capped is True


@pytest.mark.asyncio
async def test_dblp_max_results_sets_capped_without_dropping_cursor(
    dblp_client: RequestClient,
    dblp_config: AdapterConfig,
) -> None:
    page = await DblpAdapter().fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=dblp_client,
        config=dblp_config.model_copy(update={"max_pages": 10, "max_results": 1}),
    )

    assert tuple(record.source_id for record in page.records) == (
        "conf/test/Fixture24",
    )
    assert page.next_cursor
    assert page.capped is True


@pytest.mark.asyncio
async def test_dblp_record_fields_normalize_correctly(
    dblp_client: RequestClient,
    dblp_config: AdapterConfig,
) -> None:
    first_page = await DblpAdapter().fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=dblp_client,
        config=dblp_config,
    )

    second_page = await DblpAdapter().fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=first_page.next_cursor,
        client=dblp_client,
        config=dblp_config,
    )

    record = first_page.records[0]
    second_record = second_page.records[0]
    paper = normalize(record)

    assert record.source == "dblp"
    assert record.source_id == "conf/test/Fixture24"
    assert record.authors == ("A. Author",)
    assert record.doi == "10.1000/FIXTURE"
    assert record.url == "https://dblp.org/rec/conf/test/Fixture24"
    assert record.input_url == "https://example.test/fixture.html"
    assert paper.identifier == "doi:10.1000/fixture"
    assert second_record.authors == ("B. Author",)
    assert second_record.input_url == "https://example.test/fixture-2.html"


@pytest.mark.asyncio
async def test_dblp_same_year_record_is_included_for_exact_day_window(
    dblp_client: RequestClient,
    dblp_config: AdapterConfig,
) -> None:
    page = await DblpAdapter().fetch(
        window=FetchWindow(
            start=datetime(2024, 9, 1, tzinfo=timezone.utc),
            end=datetime(2024, 9, 7, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=dblp_client,
        config=dblp_config,
    )

    assert tuple(record.source_id for record in page.records) == (
        "conf/test/Fixture24",
    )


@pytest.mark.asyncio
async def test_dblp_outside_year_record_is_excluded(
    dblp_client: RequestClient,
    dblp_config: AdapterConfig,
) -> None:
    page = await DblpAdapter().fetch(
        window=FetchWindow(
            start=datetime(2025, 1, 1, tzinfo=timezone.utc),
            end=datetime(2025, 1, 7, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=dblp_client,
        config=dblp_config,
    )

    assert page.records == ()


@pytest.mark.asyncio
async def test_dblp_keeps_valid_records_and_surfaces_missing_conversion_input(
    dblp_malformed_client: RequestClient,
    dblp_config: AdapterConfig,
) -> None:
    page = await DblpAdapter().fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=dblp_malformed_client,
        config=dblp_config,
    )

    assert tuple(record.source_id for record in page.records) == (
        "conf/test/Fixture24",
    )
    assert page.permanent_errors == (
        "dblp record missing electronic URL: conf/test/Broken24",
    )


@pytest.mark.asyncio
async def test_dblp_all_out_of_window_page_preserves_progress_for_continuation(
    dblp_out_of_window_only_client: RequestClient,
    dblp_config: AdapterConfig,
) -> None:
    adapter = DblpAdapter()
    first_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=dblp_out_of_window_only_client,
        config=dblp_config,
    )

    second_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=first_page.next_cursor,
        client=dblp_out_of_window_only_client,
        config=dblp_config,
    )

    assert first_page.records == ()
    assert first_page.next_cursor
    assert first_page.capped is False
    assert tuple(record.source_id for record in second_page.records) == (
        "journals/test/Fixture25",
    )


@pytest.mark.asyncio
async def test_dblp_malformed_only_page_counts_toward_max_results(
    dblp_malformed_only_client: RequestClient,
    dblp_config: AdapterConfig,
) -> None:
    page = await DblpAdapter().fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=dblp_malformed_only_client,
        config=dblp_config.model_copy(update={"max_pages": 10, "max_results": 1}),
    )

    assert page.records == ()
    assert page.next_cursor
    assert page.capped is True
    assert page.permanent_errors == (
        "dblp record missing electronic URL: conf/test/BrokenOnly24",
    )


@pytest.mark.asyncio
async def test_dblp_invalid_json_page_is_infrastructure_failure(
    dblp_invalid_json_client: RequestClient,
    dblp_config: AdapterConfig,
) -> None:
    with pytest.raises(InfrastructureError, match="invalid JSON from dblp"):
        await DblpAdapter().fetch(
            window=FetchWindow(
                start=datetime(2024, 1, 1, tzinfo=timezone.utc),
                end=datetime(2024, 1, 8, tzinfo=timezone.utc),
            ),
            cursor=None,
            client=dblp_invalid_json_client,
            config=dblp_config,
        )


@pytest.mark.asyncio
async def test_dblp_invalid_payload_is_infrastructure_failure(
    dblp_invalid_payload_client: RequestClient,
    dblp_config: AdapterConfig,
) -> None:
    with pytest.raises(InfrastructureError, match="invalid dblp payload"):
        await DblpAdapter().fetch(
            window=FetchWindow(
                start=datetime(2024, 1, 1, tzinfo=timezone.utc),
                end=datetime(2024, 1, 8, tzinfo=timezone.utc),
            ),
            cursor=None,
            client=dblp_invalid_payload_client,
            config=dblp_config,
        )


@pytest.mark.parametrize(
    ("url", "expected"),
    [
        ("https://ceur-ws.org/Vol-4038/paper_249.pdf", "pdf"),
        ("https://example.test/PAPER.PDF?download=1", "pdf"),
        ("https://doi.org/10.1000/fixture", "html"),
        ("https://example.test/fixture.html", "html"),
    ],
)
def test_dblp_electronic_editions_that_are_pdfs_convert_as_pdf(
    url: str, expected: str
) -> None:
    assert electronic_format(url) == expected
