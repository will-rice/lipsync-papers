from datetime import datetime, timezone
from typing import Any, cast

import pytest

from papers_pipeline.adapters.base import FetchWindow
from papers_pipeline.adapters.papers_with_code import PapersWithCodeAdapter
from papers_pipeline.config import AdapterConfig
from papers_pipeline.errors import InfrastructureError
from papers_pipeline.http import RequestClient
from papers_pipeline.normalize import normalize

from .contract import assert_adapter_contract


@pytest.mark.asyncio
async def test_papers_with_code_contract(
    papers_with_code_client: RequestClient,
    papers_with_code_config: AdapterConfig,
) -> None:
    await assert_adapter_contract(
        PapersWithCodeAdapter(),
        papers_with_code_client,
        papers_with_code_config,
    )


@pytest.mark.asyncio
async def test_papers_with_code_uses_opaque_continuation_and_honors_api_next_url_safely(
    papers_with_code_client: RequestClient,
    papers_with_code_config: AdapterConfig,
) -> None:
    adapter = PapersWithCodeAdapter()
    recording_client = cast(Any, papers_with_code_client)
    first_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=recording_client,
        config=papers_with_code_config,
    )

    second_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=first_page.next_cursor,
        client=recording_client,
        config=papers_with_code_config,
    )

    assert tuple(record.source_id for record in first_page.records) == (
        "fixture-paper",
    )
    assert first_page.next_cursor
    assert first_page.next_cursor != "https://paperswithcode.com/api/v1/papers/?page=2"
    assert tuple(record.source_id for record in second_page.records) == (
        "fixture-paper-2",
    )
    assert str(recording_client.requests[1].url) == (
        "https://paperswithcode.com/api/v1/papers/?page=2&items_per_page=1"
    )
    assert second_page.next_cursor
    assert second_page.next_cursor != first_page.next_cursor


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "client_fixture",
    [
        "papers_with_code_last_null_next_client",
        "papers_with_code_last_blank_next_client",
    ],
)
async def test_papers_with_code_last_non_empty_page_without_api_next_stops_enumeration(
    client_fixture: str,
    request: pytest.FixtureRequest,
    papers_with_code_config: AdapterConfig,
) -> None:
    client = cast(RequestClient, request.getfixturevalue(client_fixture))

    page = await PapersWithCodeAdapter().fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=client,
        config=papers_with_code_config,
    )

    assert len(page.records) == 1
    assert page.next_cursor is None
    assert page.capped is False


@pytest.mark.asyncio
async def test_papers_with_code_local_truncation_on_final_page_resumes_without_skip_or_duplicate(
    papers_with_code_last_local_truncation_client: RequestClient,
    papers_with_code_config: AdapterConfig,
) -> None:
    adapter = PapersWithCodeAdapter()
    config = papers_with_code_config.model_copy(
        update={"page_size": 2, "max_results": 1}
    )

    first_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=papers_with_code_last_local_truncation_client,
        config=config,
    )
    second_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=first_page.next_cursor,
        client=papers_with_code_last_local_truncation_client,
        config=config,
    )

    assert tuple(record.source_id for record in first_page.records) == (
        "fixture-paper-local-1",
    )
    assert first_page.next_cursor
    assert first_page.capped is True
    assert tuple(record.source_id for record in second_page.records) == (
        "fixture-paper-local-2",
    )
    assert second_page.next_cursor is None
    assert second_page.capped is True


@pytest.mark.asyncio
async def test_papers_with_code_record_fields_normalize_correctly(
    papers_with_code_client: RequestClient,
    papers_with_code_config: AdapterConfig,
) -> None:
    page = await PapersWithCodeAdapter().fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=papers_with_code_client,
        config=papers_with_code_config,
    )

    record = page.records[0]
    paper = normalize(record)

    assert record.source == "papers_with_code"
    assert record.source_id == "fixture-paper"
    assert record.arxiv_id == "2401.00001"
    assert record.authors == ("A. Author",)
    assert record.input_url == "https://example.test/fixture.pdf"
    assert paper.identifier == "arxiv:2401.00001"


@pytest.mark.asyncio
async def test_papers_with_code_keeps_valid_records_and_requires_conversion_input(
    papers_with_code_malformed_client: RequestClient,
    papers_with_code_config: AdapterConfig,
) -> None:
    page = await PapersWithCodeAdapter().fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=papers_with_code_malformed_client,
        config=papers_with_code_config,
    )

    assert tuple(record.source_id for record in page.records) == ("fixture-paper",)
    assert page.permanent_errors == (
        "Papers With Code record lacks id, title, date, or PDF",
    )


@pytest.mark.asyncio
async def test_papers_with_code_out_of_window_page_preserves_progress_for_continuation(
    papers_with_code_out_of_window_only_client: RequestClient,
    papers_with_code_config: AdapterConfig,
) -> None:
    adapter = PapersWithCodeAdapter()
    first_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=papers_with_code_out_of_window_only_client,
        config=papers_with_code_config,
    )

    second_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=first_page.next_cursor,
        client=papers_with_code_out_of_window_only_client,
        config=papers_with_code_config,
    )

    assert first_page.records == ()
    assert first_page.next_cursor
    assert first_page.capped is False
    assert tuple(record.source_id for record in second_page.records) == (
        "fixture-paper-2",
    )


@pytest.mark.asyncio
async def test_papers_with_code_malformed_only_page_counts_toward_max_results(
    papers_with_code_malformed_only_client: RequestClient,
    papers_with_code_config: AdapterConfig,
) -> None:
    page = await PapersWithCodeAdapter().fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=papers_with_code_malformed_only_client,
        config=papers_with_code_config.model_copy(
            update={"max_pages": 10, "max_results": 1}
        ),
    )

    assert page.records == ()
    assert page.next_cursor
    assert page.capped is True
    assert page.permanent_errors == (
        "Papers With Code record lacks id, title, date, or PDF",
    )


@pytest.mark.asyncio
async def test_papers_with_code_rejects_untrusted_next_urls(
    papers_with_code_untrusted_next_client: RequestClient,
    papers_with_code_config: AdapterConfig,
) -> None:
    with pytest.raises(InfrastructureError, match="invalid papers_with_code next url"):
        await PapersWithCodeAdapter().fetch(
            window=FetchWindow(
                start=datetime(2024, 1, 1, tzinfo=timezone.utc),
                end=datetime(2024, 1, 8, tzinfo=timezone.utc),
            ),
            cursor=None,
            client=papers_with_code_untrusted_next_client,
            config=papers_with_code_config,
        )


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("client_fixture", "message"),
    [
        ("papers_with_code_auth_client", "authentication failed"),
        ("papers_with_code_invalid_json_client", "invalid JSON from papers_with_code"),
        ("papers_with_code_invalid_payload_client", "invalid papers_with_code payload"),
    ],
)
async def test_papers_with_code_failures_are_explicit(
    client_fixture: str,
    message: str,
    request: pytest.FixtureRequest,
    papers_with_code_config: AdapterConfig,
) -> None:
    client = cast(RequestClient, request.getfixturevalue(client_fixture))

    with pytest.raises(InfrastructureError, match=message):
        await PapersWithCodeAdapter().fetch(
            window=FetchWindow(
                start=datetime(2024, 1, 1, tzinfo=timezone.utc),
                end=datetime(2024, 1, 8, tzinfo=timezone.utc),
            ),
            cursor=None,
            client=client,
            config=papers_with_code_config,
        )
