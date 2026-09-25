from datetime import datetime, timezone

import pytest

from papers_pipeline.adapters.base import FetchWindow
from papers_pipeline.adapters.huggingface import HuggingFaceAdapter
from papers_pipeline.config import AdapterConfig
from papers_pipeline.errors import InfrastructureError
from papers_pipeline.http import Deadline, RequestClient
from papers_pipeline.config import FetchConfig
from conftest import FixtureTransport
from papers_pipeline.normalize import normalize

from .contract import assert_adapter_contract


@pytest.mark.asyncio
async def test_huggingface_contract(
    huggingface_client: RequestClient, huggingface_config: AdapterConfig
) -> None:
    await assert_adapter_contract(
        HuggingFaceAdapter(), huggingface_client, huggingface_config
    )


@pytest.mark.asyncio
async def test_huggingface_continuation_cursor_is_deterministic_and_opaque(
    huggingface_client: RequestClient, huggingface_config: AdapterConfig
) -> None:
    adapter = HuggingFaceAdapter()
    first_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=huggingface_client,
        config=huggingface_config,
    )

    page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=first_page.next_cursor,
        client=huggingface_client,
        config=huggingface_config,
    )

    assert first_page.next_cursor
    assert first_page.next_cursor != "1"
    assert tuple(record.source_id for record in page.records) == ("2401.00002",)
    assert page.next_cursor
    assert page.next_cursor != first_page.next_cursor
    assert page.capped is False
    assert page.permanent_errors == ()


@pytest.mark.asyncio
async def test_huggingface_max_pages_sets_capped_without_dropping_cursor(
    huggingface_client: RequestClient, huggingface_config: AdapterConfig
) -> None:
    adapter = HuggingFaceAdapter()
    first_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=huggingface_client,
        config=huggingface_config,
    )

    page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=first_page.next_cursor,
        client=huggingface_client,
        config=huggingface_config.model_copy(
            update={"max_pages": 2, "max_results": 10}
        ),
    )

    assert page.next_cursor
    assert page.capped is False


@pytest.mark.asyncio
async def test_huggingface_max_results_sets_capped_without_dropping_cursor(
    huggingface_client: RequestClient, huggingface_config: AdapterConfig
) -> None:
    page = await HuggingFaceAdapter().fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=huggingface_client,
        config=huggingface_config.model_copy(
            update={"max_pages": 10, "max_results": 1}
        ),
    )

    assert tuple(record.source_id for record in page.records) == ("2401.00001",)
    assert page.next_cursor
    assert page.capped is True


@pytest.mark.asyncio
async def test_huggingface_record_fields_normalize_correctly(
    huggingface_client: RequestClient, huggingface_config: AdapterConfig
) -> None:
    page = await HuggingFaceAdapter().fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=huggingface_client,
        config=huggingface_config,
    )

    record = page.records[0]
    paper = normalize(record)

    assert record.source == "huggingface"
    assert record.source_id == "2401.00001"
    assert record.arxiv_id == "2401.00001"
    assert record.authors == ("A. Author",)
    assert record.categories == ()
    assert record.url == "https://huggingface.co/papers/2401.00001"
    assert record.input_url == "https://arxiv.org/pdf/2401.00001"
    assert paper.identifier == "arxiv:2401.00001"


@pytest.mark.asyncio
async def test_huggingface_keeps_valid_records_and_surfaces_malformed_entries(
    huggingface_malformed_client: RequestClient, huggingface_config: AdapterConfig
) -> None:
    page = await HuggingFaceAdapter().fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=huggingface_malformed_client,
        config=huggingface_config,
    )

    assert tuple(record.source_id for record in page.records) == ("2401.00001",)
    assert page.permanent_errors == (
        "huggingface record missing publishedAt: 2401.99999",
    )


@pytest.mark.asyncio
async def test_huggingface_all_out_of_window_page_preserves_progress_for_continuation(
    huggingface_out_of_window_only_client: RequestClient,
    huggingface_config: AdapterConfig,
) -> None:
    adapter = HuggingFaceAdapter()
    first_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=huggingface_out_of_window_only_client,
        config=huggingface_config,
    )

    second_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=first_page.next_cursor,
        client=huggingface_out_of_window_only_client,
        config=huggingface_config,
    )

    assert first_page.records == ()
    assert first_page.next_cursor
    assert first_page.capped is False
    assert first_page.permanent_errors == ()
    assert tuple(record.source_id for record in second_page.records) == ("2401.00002",)


@pytest.mark.asyncio
async def test_huggingface_malformed_only_page_counts_toward_max_results(
    huggingface_malformed_only_client: RequestClient, huggingface_config: AdapterConfig
) -> None:
    page = await HuggingFaceAdapter().fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=huggingface_malformed_only_client,
        config=huggingface_config.model_copy(
            update={"max_pages": 10, "max_results": 1}
        ),
    )

    assert page.records == ()
    assert page.next_cursor
    assert page.capped is True
    assert page.permanent_errors == (
        "huggingface record missing publishedAt: 2401.99998",
    )


@pytest.mark.asyncio
async def test_huggingface_invalid_json_page_is_infrastructure_failure(
    huggingface_invalid_json_client: RequestClient, huggingface_config: AdapterConfig
) -> None:
    with pytest.raises(InfrastructureError, match="invalid JSON"):
        await HuggingFaceAdapter().fetch(
            window=FetchWindow(
                start=datetime(2024, 1, 1, tzinfo=timezone.utc),
                end=datetime(2024, 1, 8, tzinfo=timezone.utc),
            ),
            cursor=None,
            client=huggingface_invalid_json_client,
            config=huggingface_config,
        )


@pytest.mark.asyncio
async def test_huggingface_enumerates_each_utc_date_and_resumes_mid_range(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    huggingface_config: AdapterConfig,
) -> None:
    transport = fixture_transport(
        {
            "https://huggingface.co/api/daily_papers?date=2024-01-07&p=0&limit=2": {
                "fixture": "adapters/huggingface/day-7.json"
            },
            "https://huggingface.co/api/daily_papers?date=2024-01-07&p=1&limit=2": {
                "fixture": "adapters/huggingface/empty.json"
            },
            "https://huggingface.co/api/daily_papers?date=2024-01-06&p=0&limit=2": {
                "fixture": "adapters/huggingface/day-6.json"
            },
            "https://huggingface.co/api/daily_papers?date=2024-01-06&p=1&limit=2": {
                "fixture": "adapters/huggingface/empty.json"
            },
        }
    )
    client = RequestClient(
        fetch_config,
        Deadline.start(fetch_config.total_deadline_seconds),
        transport=transport,
    )
    adapter = HuggingFaceAdapter()
    window = FetchWindow(
        start=datetime(2024, 1, 6, tzinfo=timezone.utc),
        end=datetime(2024, 1, 8, tzinfo=timezone.utc),
    )

    # The first day requested is the one before the window ends; the API
    # rejects days it has not published yet.
    page = await adapter.fetch(window, None, client, huggingface_config)
    assert tuple(record.source_id for record in page.records) == ("2401.00007",)
    resume_cursor = page.next_cursor

    page = await adapter.fetch(window, resume_cursor, client, huggingface_config)
    assert page.records == ()
    page = await adapter.fetch(window, page.next_cursor, client, huggingface_config)
    assert tuple(record.source_id for record in page.records) == ("2401.00006",)
    page = await adapter.fetch(window, page.next_cursor, client, huggingface_config)
    assert page.records == ()
    assert page.next_cursor is None
