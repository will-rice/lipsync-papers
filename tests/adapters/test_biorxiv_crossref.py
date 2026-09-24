from datetime import datetime, timezone
from pathlib import Path
from typing import Any, cast

import httpx
import pytest

from papers_pipeline.adapters.base import FetchWindow
from papers_pipeline.adapters.biorxiv_crossref import BiorxivCrossrefAdapter
from papers_pipeline.config import AdapterConfig, FetchConfig
from papers_pipeline.errors import ConfigError, InfrastructureError
from papers_pipeline.http import Deadline, RequestClient
from papers_pipeline.normalize import normalize

from .contract import assert_adapter_contract


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("provider", "client_fixture", "config_fixture"),
    [
        ("biorxiv", "biorxiv_client", "biorxiv_config"),
        ("crossref", "crossref_client", "crossref_config"),
    ],
)
async def test_combined_adapter_contract(
    provider: str,
    client_fixture: str,
    config_fixture: str,
    request: pytest.FixtureRequest,
) -> None:
    client = cast(RequestClient, request.getfixturevalue(client_fixture))
    config = cast(AdapterConfig, request.getfixturevalue(config_fixture)).model_copy(
        update={"filters": {"provider": provider}}
    )

    await assert_adapter_contract(BiorxivCrossrefAdapter(), client, config)


@pytest.mark.asyncio
async def test_biorxiv_uses_opaque_offset_continuation(
    biorxiv_client: RequestClient,
    biorxiv_config: AdapterConfig,
) -> None:
    adapter = BiorxivCrossrefAdapter()
    recording_client = cast(Any, biorxiv_client)
    first_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=recording_client,
        config=biorxiv_config,
    )

    second_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=first_page.next_cursor,
        client=recording_client,
        config=biorxiv_config,
    )

    assert tuple(record.source_id for record in first_page.records) == (
        "10.1101/2024.01.02.123456",
    )
    assert first_page.next_cursor
    assert first_page.next_cursor != "1"
    assert tuple(record.source_id for record in second_page.records) == (
        "10.1101/2024.01.03.123457",
    )
    assert recording_client.requests[1].url.path.endswith("/1")
    assert second_page.next_cursor
    assert second_page.next_cursor != first_page.next_cursor
    assert second_page.capped is False


@pytest.mark.asyncio
async def test_biorxiv_local_truncation_resumes_raw_page_without_duplicates(
    fetch_config: FetchConfig,
    biorxiv_config: AdapterConfig,
) -> None:
    requests: list[httpx.Request] = []
    fixture = (
        Path(__file__).parents[1]
        / "fixtures"
        / "adapters"
        / "biorxiv_crossref"
        / "biorxiv-over-budget.json"
    )

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        body = (
            fixture.read_text()
            if request.url.path.endswith("/0")
            else '{"collection":[]}'
        )
        return httpx.Response(200, text=body)

    client = RequestClient(
        fetch_config,
        Deadline.start(fetch_config.total_deadline_seconds),
        transport=httpx.MockTransport(handler),
    )
    adapter = BiorxivCrossrefAdapter()
    config = biorxiv_config.model_copy(update={"page_size": 4, "max_results": 2})
    window = FetchWindow(
        start=datetime(2024, 1, 1, tzinfo=timezone.utc),
        end=datetime(2024, 1, 8, tzinfo=timezone.utc),
    )

    first = await adapter.fetch(window, None, client, config)
    second = await adapter.fetch(window, first.next_cursor, client, config)
    final = await adapter.fetch(window, second.next_cursor, client, config)

    assert tuple(record.source_id for record in first.records) == (
        "10.1101/2024.01.02.000001",
    )
    assert first.permanent_errors == ("bioRxiv record lacks DOI, title, or date",)
    assert first.capped is True
    assert tuple(record.source_id for record in second.records) == (
        "10.1101/2024.01.03.000002",
    )
    assert second.permanent_errors == ()
    assert second.capped is True
    assert final.records == ()
    assert final.next_cursor is None
    assert [request.url.path.rsplit("/", 1)[-1] for request in requests] == [
        "0",
        "0",
        "4",
    ]


@pytest.mark.asyncio
async def test_crossref_uses_opaque_cursor_and_prefers_html_conversion_input(
    crossref_client: RequestClient,
    crossref_config: AdapterConfig,
) -> None:
    adapter = BiorxivCrossrefAdapter()
    recording_client = cast(Any, crossref_client)
    first_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=recording_client,
        config=crossref_config,
    )

    second_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=first_page.next_cursor,
        client=recording_client,
        config=crossref_config,
    )

    record = first_page.records[0]
    paper = normalize(record)

    assert record.source == "crossref"
    assert record.input_format == "html"
    assert record.input_url == "https://example.test/fixture.html"
    assert record.authors == ("A. Author", "OnlyFamily")
    assert paper.identifier == "doi:10.1000/fixture"
    assert first_page.next_cursor
    assert first_page.next_cursor != "cursor-2"
    assert tuple(record.source_id for record in second_page.records) == (
        "10.1000/fixture-2",
    )
    assert recording_client.requests[1].url.params["cursor"] == "cursor-2"


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "client_fixture",
    [
        "crossref_last_missing_next_cursor_client",
        "crossref_last_blank_next_cursor_client",
    ],
)
async def test_crossref_last_non_empty_page_without_next_cursor_stops_enumeration(
    client_fixture: str,
    request: pytest.FixtureRequest,
    crossref_config: AdapterConfig,
) -> None:
    client = cast(RequestClient, request.getfixturevalue(client_fixture))

    page = await BiorxivCrossrefAdapter().fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=client,
        config=crossref_config,
    )

    assert len(page.records) == 1
    assert page.next_cursor is None
    assert page.capped is False


@pytest.mark.asyncio
async def test_crossref_local_truncation_on_final_page_resumes_without_skip_or_duplicate(
    crossref_last_local_truncation_client: RequestClient,
    crossref_config: AdapterConfig,
) -> None:
    adapter = BiorxivCrossrefAdapter()
    config = crossref_config.model_copy(update={"page_size": 2, "max_results": 1})

    first_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=crossref_last_local_truncation_client,
        config=config,
    )
    second_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=first_page.next_cursor,
        client=crossref_last_local_truncation_client,
        config=config,
    )

    assert tuple(record.source_id for record in first_page.records) == (
        "10.1000/fixture-local-1",
    )
    assert first_page.next_cursor
    assert first_page.capped is True
    assert tuple(record.source_id for record in second_page.records) == (
        "10.1000/fixture-local-2",
    )
    assert second_page.next_cursor is None
    assert second_page.capped is True


@pytest.mark.asyncio
async def test_crossref_partial_dates_default_missing_month_and_day(
    crossref_client: RequestClient,
    crossref_config: AdapterConfig,
) -> None:
    first_page = await BiorxivCrossrefAdapter().fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=crossref_client,
        config=crossref_config,
    )

    second_page = await BiorxivCrossrefAdapter().fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=first_page.next_cursor,
        client=crossref_client,
        config=crossref_config,
    )

    assert first_page.records[0].published == datetime(2024, 1, 1, tzinfo=timezone.utc)
    assert second_page.records[0].published == datetime(2024, 1, 1, tzinfo=timezone.utc)


@pytest.mark.asyncio
async def test_biorxiv_keeps_valid_records_and_surfaces_malformed_neighbors(
    biorxiv_malformed_client: RequestClient,
    biorxiv_config: AdapterConfig,
) -> None:
    page = await BiorxivCrossrefAdapter().fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=biorxiv_malformed_client,
        config=biorxiv_config,
    )

    assert tuple(record.source_id for record in page.records) == (
        "10.1101/2024.01.02.123456",
    )
    assert page.permanent_errors == ("bioRxiv record lacks DOI, title, or date",)


@pytest.mark.asyncio
async def test_crossref_keeps_valid_records_and_surfaces_missing_full_text(
    crossref_malformed_client: RequestClient,
    crossref_config: AdapterConfig,
) -> None:
    page = await BiorxivCrossrefAdapter().fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=crossref_malformed_client,
        config=crossref_config,
    )

    assert tuple(record.source_id for record in page.records) == ("10.1000/fixture",)
    assert page.permanent_errors == (
        "Crossref record lacks DOI, title, date, or full text",
    )


@pytest.mark.asyncio
async def test_biorxiv_out_of_window_page_preserves_progress_for_continuation(
    biorxiv_out_of_window_only_client: RequestClient,
    biorxiv_config: AdapterConfig,
) -> None:
    adapter = BiorxivCrossrefAdapter()
    first_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=biorxiv_out_of_window_only_client,
        config=biorxiv_config,
    )

    second_page = await adapter.fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=first_page.next_cursor,
        client=biorxiv_out_of_window_only_client,
        config=biorxiv_config,
    )

    assert first_page.records == ()
    assert first_page.next_cursor
    assert first_page.capped is False
    assert tuple(record.source_id for record in second_page.records) == (
        "10.1101/2024.01.03.123457",
    )


@pytest.mark.asyncio
async def test_crossref_malformed_only_page_counts_toward_max_results(
    crossref_malformed_only_client: RequestClient,
    crossref_config: AdapterConfig,
) -> None:
    page = await BiorxivCrossrefAdapter().fetch(
        window=FetchWindow(
            start=datetime(2024, 1, 1, tzinfo=timezone.utc),
            end=datetime(2024, 1, 8, tzinfo=timezone.utc),
        ),
        cursor=None,
        client=crossref_malformed_only_client,
        config=crossref_config.model_copy(update={"max_pages": 10, "max_results": 1}),
    )

    assert page.records == ()
    assert page.next_cursor
    assert page.capped is True
    assert page.permanent_errors == (
        "Crossref record lacks DOI, title, date, or full text",
    )


@pytest.mark.asyncio
async def test_invalid_provider_is_rejected_before_fetch(
    crossref_client: RequestClient,
    crossref_config: AdapterConfig,
) -> None:
    with pytest.raises(ConfigError, match="provider must be biorxiv or crossref"):
        await BiorxivCrossrefAdapter().fetch(
            window=FetchWindow(
                start=datetime(2024, 1, 1, tzinfo=timezone.utc),
                end=datetime(2024, 1, 8, tzinfo=timezone.utc),
            ),
            cursor=None,
            client=crossref_client,
            config=crossref_config.model_copy(
                update={"filters": {"provider": "medrxiv"}}
            ),
        )


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("client_fixture", "message"),
    [
        ("biorxiv_invalid_json_client", "invalid JSON from biorxiv"),
        ("crossref_invalid_json_client", "invalid JSON from crossref"),
        ("crossref_invalid_payload_client", "invalid crossref payload"),
    ],
)
async def test_combined_adapter_invalid_pages_are_infrastructure_failures(
    client_fixture: str,
    message: str,
    request: pytest.FixtureRequest,
    biorxiv_config: AdapterConfig,
    crossref_config: AdapterConfig,
) -> None:
    client = cast(RequestClient, request.getfixturevalue(client_fixture))
    config = biorxiv_config if client_fixture.startswith("biorxiv") else crossref_config

    with pytest.raises(InfrastructureError, match=message):
        await BiorxivCrossrefAdapter().fetch(
            window=FetchWindow(
                start=datetime(2024, 1, 1, tzinfo=timezone.utc),
                end=datetime(2024, 1, 8, tzinfo=timezone.utc),
            ),
            cursor=None,
            client=client,
            config=config,
        )
