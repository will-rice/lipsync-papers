from datetime import datetime, timezone

from papers_pipeline.adapters.base import Adapter, FetchWindow
from papers_pipeline.config import AdapterConfig
from papers_pipeline.http import RequestClient

WINDOW_START = datetime(2024, 1, 1, tzinfo=timezone.utc)
WINDOW_END = datetime(2024, 1, 8, tzinfo=timezone.utc)


async def assert_adapter_contract(
    adapter: Adapter, client: RequestClient, config: AdapterConfig
) -> None:
    page = await adapter.fetch(
        window=FetchWindow(start=WINDOW_START, end=WINDOW_END),
        cursor=None,
        client=client,
        config=config,
    )
    assert page.records
    assert all(record.source in adapter.record_sources for record in page.records)
    assert all(
        WINDOW_START <= record.published <= WINDOW_END for record in page.records
    )
    assert page.next_cursor is None or page.next_cursor
