from datetime import datetime, timezone
from typing import Any, cast

import httpx
import pytest
from conftest import FixtureTransport

from papers_pipeline.adapters.base import FetchWindow
from papers_pipeline.adapters.semantic_scholar import SemanticScholarAdapter
from papers_pipeline.config import AdapterConfig, FetchConfig
from papers_pipeline.errors import InfrastructureError
from papers_pipeline.http import Deadline, RequestClient
from papers_pipeline.normalize import normalize

from .contract import assert_adapter_contract


@pytest.mark.asyncio
async def test_semantic_scholar_contract(
    semantic_scholar_client: RequestClient,
    semantic_scholar_config: AdapterConfig,
) -> None:
    await assert_adapter_contract(
        SemanticScholarAdapter(api_key="secret"),
        semantic_scholar_client,
        semantic_scholar_config,
    )


@pytest.mark.asyncio
async def test_semantic_scholar_uses_declared_api_key_and_opaque_continuation(
    semantic_scholar_client: RequestClient,
    semantic_scholar_config: AdapterConfig,
) -> None:
    adapter = SemanticScholarAdapter(api_key="secret")
    recording_client = cast(Any, semantic_scholar_client)
    first_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=recording_client,
        config=semantic_scholar_config,
    )

    second_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=first_page.next_cursor,
        client=recording_client,
        config=semantic_scholar_config,
    )

    assert tuple(record.source_id for record in first_page.records) == ("abc123",)
    assert recording_client.requests[0].headers["x-api-key"] == "secret"
    assert first_page.next_cursor
    assert first_page.next_cursor != "1"
    assert tuple(record.source_id for record in second_page.records) == ("abc124",)
    assert second_page.next_cursor
    assert second_page.next_cursor != first_page.next_cursor
    assert second_page.capped is False


@pytest.mark.asyncio
async def test_semantic_scholar_max_pages_sets_capped_without_dropping_cursor(
    semantic_scholar_client: RequestClient,
    semantic_scholar_config: AdapterConfig,
) -> None:
    adapter = SemanticScholarAdapter(api_key="secret")
    first_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=semantic_scholar_client,
        config=semantic_scholar_config,
    )

    second_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=first_page.next_cursor,
        client=semantic_scholar_client,
        config=semantic_scholar_config.model_copy(
            update={"max_pages": 2, "max_results": 10}
        ),
    )

    assert second_page.next_cursor
    assert second_page.capped is True


@pytest.mark.asyncio
async def test_semantic_scholar_max_results_sets_capped_without_dropping_cursor(
    semantic_scholar_client: RequestClient,
    semantic_scholar_config: AdapterConfig,
) -> None:
    page = await SemanticScholarAdapter(api_key="secret").fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=semantic_scholar_client,
        config=semantic_scholar_config.model_copy(
            update={"max_pages": 10, "max_results": 1}
        ),
    )

    assert tuple(record.source_id for record in page.records) == ("abc123",)
    assert page.next_cursor
    assert page.capped is True


@pytest.mark.asyncio
async def test_semantic_scholar_record_fields_normalize_correctly(
    semantic_scholar_client: RequestClient,
    semantic_scholar_config: AdapterConfig,
) -> None:
    page = await SemanticScholarAdapter(api_key="secret").fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=semantic_scholar_client,
        config=semantic_scholar_config,
    )

    record = page.records[0]
    paper = normalize(record)

    assert record.source == "semantic_scholar"
    assert record.source_id == "abc123"
    assert record.doi == "10.1000/FIXTURE"
    assert record.arxiv_id == "arXiv:2401.00001"
    assert record.authors == ("A. Author",)
    assert record.url == "https://www.semanticscholar.org/paper/abc123"
    assert record.input_url == "https://example.test/fixture.pdf"
    assert paper.identifier == "arxiv:2401.00001"
    assert paper.doi == "10.1000/fixture"


@pytest.mark.asyncio
async def test_semantic_scholar_prefers_returned_next_offset_for_sparse_pages(
    semantic_scholar_sparse_next_client: RequestClient,
    semantic_scholar_config: AdapterConfig,
) -> None:
    adapter = SemanticScholarAdapter(api_key="secret")
    recording_client = cast(Any, semantic_scholar_sparse_next_client)
    first_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=recording_client,
        config=semantic_scholar_config,
    )

    second_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=first_page.next_cursor,
        client=recording_client,
        config=semantic_scholar_config,
    )

    assert tuple(record.source_id for record in first_page.records) == ("abc123",)
    assert tuple(record.source_id for record in second_page.records) == ("abc124",)
    assert recording_client.requests[1].url.params["offset"] == "100"


@pytest.mark.asyncio
async def test_semantic_scholar_keeps_valid_records_and_surfaces_malformed_entries(
    semantic_scholar_malformed_client: RequestClient,
    semantic_scholar_config: AdapterConfig,
) -> None:
    page = await SemanticScholarAdapter(api_key="secret").fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=semantic_scholar_malformed_client,
        config=semantic_scholar_config,
    )

    assert tuple(record.source_id for record in page.records) == ("abc123",)
    assert page.permanent_errors == (
        "semantic_scholar record missing openAccessPdf.url: broken-no-pdf",
    )


@pytest.mark.asyncio
async def test_semantic_scholar_all_out_of_window_page_preserves_progress_for_continuation(
    semantic_scholar_out_of_window_only_client: RequestClient,
    semantic_scholar_config: AdapterConfig,
) -> None:
    adapter = SemanticScholarAdapter(api_key="secret")
    first_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=semantic_scholar_out_of_window_only_client,
        config=semantic_scholar_config,
    )

    second_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=first_page.next_cursor,
        client=semantic_scholar_out_of_window_only_client,
        config=semantic_scholar_config,
    )

    assert first_page.records == ()
    assert first_page.next_cursor
    assert first_page.capped is False
    assert tuple(record.source_id for record in second_page.records) == ("abc124",)


@pytest.mark.asyncio
async def test_semantic_scholar_malformed_only_page_counts_toward_max_results(
    semantic_scholar_malformed_only_client: RequestClient,
    semantic_scholar_config: AdapterConfig,
) -> None:
    page = await SemanticScholarAdapter(api_key="secret").fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=semantic_scholar_malformed_only_client,
        config=semantic_scholar_config.model_copy(
            update={"max_pages": 10, "max_results": 1}
        ),
    )

    assert page.records == ()
    assert page.next_cursor
    assert page.capped is True
    assert page.permanent_errors == (
        "semantic_scholar record missing openAccessPdf.url: broken-only",
    )


@pytest.mark.asyncio
async def test_semantic_scholar_authentication_failure_is_explicit(
    semantic_scholar_auth_client: RequestClient,
    semantic_scholar_config: AdapterConfig,
) -> None:
    with pytest.raises(InfrastructureError, match="authentication failed"):
        await SemanticScholarAdapter(api_key="secret").fetch(
            window=FetchWindow(
                start=datetime(2024, 1, 1, tzinfo=timezone.utc),
                end=datetime(2024, 1, 8, tzinfo=timezone.utc),
            ),
            cursor=None,
            client=semantic_scholar_auth_client,
            config=semantic_scholar_config,
        )


@pytest.mark.asyncio
async def test_semantic_scholar_invalid_json_page_is_infrastructure_failure(
    semantic_scholar_invalid_json_client: RequestClient,
    semantic_scholar_config: AdapterConfig,
) -> None:
    with pytest.raises(InfrastructureError, match="invalid JSON from semantic_scholar"):
        await SemanticScholarAdapter(api_key="secret").fetch(
            window=FetchWindow(
                start=datetime(2024, 1, 1, tzinfo=timezone.utc),
                end=datetime(2024, 1, 8, tzinfo=timezone.utc),
            ),
            cursor=None,
            client=semantic_scholar_invalid_json_client,
            config=semantic_scholar_config,
        )


@pytest.mark.asyncio
async def test_semantic_scholar_invalid_payload_is_infrastructure_failure(
    semantic_scholar_invalid_payload_client: RequestClient,
    semantic_scholar_config: AdapterConfig,
) -> None:
    with pytest.raises(InfrastructureError, match="invalid semantic_scholar payload"):
        await SemanticScholarAdapter(api_key="secret").fetch(
            window=FetchWindow(
                start=datetime(2024, 1, 1, tzinfo=timezone.utc),
                end=datetime(2024, 1, 8, tzinfo=timezone.utc),
            ),
            cursor=None,
            client=semantic_scholar_invalid_payload_client,
            config=semantic_scholar_config,
        )


@pytest.mark.asyncio
async def test_semantic_scholar_reports_windows_beyond_reachable_results(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    semantic_scholar_config: AdapterConfig,
) -> None:
    route = str(
        httpx.URL(
            "https://api.semanticscholar.org/graph/v1/paper/search",
            params={
                "query": "speech recognition",
                "publicationDateOrYear": "2024-01-01:2024-01-08",
                "offset": "0",
                "limit": "1",
                "fields": (
                    "paperId,title,abstract,authors,publicationDate,url,"
                    "externalIds,openAccessPdf"
                ),
            },
        )
    )
    client = RequestClient(
        fetch_config,
        Deadline.start(fetch_config.total_deadline_seconds),
        transport=fixture_transport(
            {route: {"fixture": "adapters/semantic_scholar/page-over-reachable.json"}}
        ),
    )

    async with client:
        page = await SemanticScholarAdapter(api_key="secret").fetch(
            window=FetchWindow(
                start=datetime(2024, 1, 1, tzinfo=timezone.utc),
                end=datetime(2024, 1, 8, tzinfo=timezone.utc),
            ),
            cursor=None,
            client=client,
            config=semantic_scholar_config,
        )

    assert page.permanent_errors[-1] == (
        "semantic_scholar window 2024-01-01..2024-01-08 matches 5000 papers; "
        "only the first 1000 are reachable, so shorten the window"
    )
