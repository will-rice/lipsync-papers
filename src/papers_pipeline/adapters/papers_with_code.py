import base64
import json
import re
from datetime import datetime
from typing import TypedDict

import httpx

from papers_pipeline.adapters.base import FetchPage, FetchWindow, collect_records
from papers_pipeline.config import AdapterConfig
from papers_pipeline.errors import InfrastructureError, PaperError
from papers_pipeline.http import RequestClient
from papers_pipeline.models import SourceRecord

_BASE_URL = "https://paperswithcode.com/api/v1/papers/"


class PapersWithCodeAdapter:
    name = "papers_with_code"
    record_sources = frozenset({"papers_with_code"})

    async def fetch(
        self,
        window: FetchWindow,
        cursor: str | None,
        client: RequestClient,
        config: AdapterConfig,
    ) -> FetchPage:
        state = _decode_cursor(cursor)
        request_url, request_params = _request_target(
            state["url"], page_size=config.page_size
        )
        text = await client.get_text(
            request_url,
            request_params,
            {},
        )
        items, next_url = _payload_page(text)
        records, errors = collect_records(items, parse_papers_with_code)
        filtered_records = tuple(
            record
            for record in records
            if window.start <= record.published <= window.end
        )
        if not items:
            return FetchPage(
                records=filtered_records,
                next_cursor=None,
                capped=False,
                permanent_errors=errors,
            )

        consumed = state["consumed"] + (0 if state["local_index"] else len(items))
        page = state["page"] + (0 if state["local_index"] else 1)
        remaining_records = _remaining_records(
            filtered_records,
            local_index=state["local_index"],
            cursor=cursor,
        )
        page_records = remaining_records[: config.max_results]
        next_cursor: str | None
        if len(remaining_records) > len(page_records):
            next_cursor = _encode_cursor(
                {
                    "consumed": consumed,
                    "local_index": state["local_index"] + len(page_records),
                    "page": page,
                    "url": state["url"],
                }
            )
        elif next_url is not None:
            next_cursor = _encode_cursor(
                {
                    "consumed": consumed,
                    "local_index": 0,
                    "page": page,
                    "url": next_url,
                }
            )
        else:
            next_cursor = None
        capped = page >= config.max_pages or consumed >= config.max_results
        return FetchPage(
            records=page_records,
            next_cursor=next_cursor,
            capped=capped,
            permanent_errors=errors,
        )


class _CursorState(TypedDict):
    consumed: int
    local_index: int
    page: int
    url: str


def _payload_page(text: str) -> tuple[list[object], str | None]:
    try:
        payload = json.loads(text)
    except json.JSONDecodeError as error:
        raise InfrastructureError(
            f"invalid JSON from papers_with_code: {error}"
        ) from error
    if not isinstance(payload, dict):
        raise InfrastructureError("invalid papers_with_code payload: expected object")
    items = payload.get("results")
    if not isinstance(items, list):
        raise InfrastructureError(
            "invalid papers_with_code payload: expected results list"
        )
    next_value = payload.get("next")
    if next_value is None:
        return items, None
    if isinstance(next_value, str) and not _clean(next_value):
        return items, None
    next_url = _validate_next_url(next_value)
    return items, next_url


def _encode_cursor(state: _CursorState) -> str:
    payload = json.dumps(state, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return base64.urlsafe_b64encode(payload).decode("ascii").rstrip("=")


def _decode_cursor(cursor: str | None) -> _CursorState:
    if cursor is None:
        return {"consumed": 0, "local_index": 0, "page": 0, "url": _BASE_URL}

    padding = "=" * (-len(cursor) % 4)
    try:
        decoded = base64.urlsafe_b64decode(f"{cursor}{padding}".encode("ascii"))
        data = json.loads(decoded.decode("utf-8"))
    except (ValueError, json.JSONDecodeError) as error:
        raise InfrastructureError(
            f"invalid papers_with_code continuation cursor: {cursor}"
        ) from error
    if not isinstance(data, dict):
        raise InfrastructureError(
            f"invalid papers_with_code continuation cursor: {cursor}"
        )

    consumed = data.get("consumed")
    local_index = data.get("local_index", 0)
    page = data.get("page")
    url = data.get("url")
    if (
        not isinstance(consumed, int)
        or consumed < 0
        or not isinstance(local_index, int)
        or local_index < 0
        or not isinstance(page, int)
        or page < 0
    ):
        raise InfrastructureError(
            f"invalid papers_with_code continuation cursor: {cursor}"
        )
    validated_url = _validate_next_url(url)
    return {
        "consumed": consumed,
        "local_index": local_index,
        "page": page,
        "url": validated_url,
    }


def _request_target(url: str, *, page_size: int) -> tuple[str, dict[str, str]]:
    parsed = httpx.URL(url)
    params = dict(parsed.params.multi_items())
    params["items_per_page"] = str(page_size)
    base_url = f"{parsed.scheme}://{parsed.host}{parsed.path}"
    return base_url, params


def _validate_next_url(value: object) -> str:
    if not isinstance(value, str):
        raise InfrastructureError("invalid papers_with_code next url")
    url = httpx.URL(value)
    if (
        url.scheme != "https"
        or url.host != "paperswithcode.com"
        or not url.path.startswith("/api/v1/papers/")
    ):
        raise InfrastructureError("invalid papers_with_code next url")
    return str(url)


def _remaining_records(
    records: tuple[SourceRecord, ...], *, local_index: int, cursor: str | None
) -> tuple[SourceRecord, ...]:
    if local_index > len(records):
        raise InfrastructureError(
            f"invalid papers_with_code continuation cursor: {cursor or '<initial>'}"
        )
    return records[local_index:]


def parse_papers_with_code(item: object) -> SourceRecord:
    if not isinstance(item, dict):
        raise PaperError("Papers With Code record lacks id, title, date, or PDF")
    paper_id = _clean(str(item.get("id") or ""))
    title = _clean(str(item.get("title") or ""))
    published_text = _clean(str(item.get("published") or ""))
    pdf_url = _clean(str(item.get("url_pdf") or ""))
    if not paper_id or not title or not published_text or not pdf_url:
        raise PaperError("Papers With Code record lacks id, title, date, or PDF")
    try:
        published = datetime.fromisoformat(published_text.replace("Z", "+00:00"))
    except ValueError as error:
        raise PaperError(
            "Papers With Code record lacks id, title, date, or PDF"
        ) from error
    authors = item.get("authors")
    author_rows = authors if isinstance(authors, list) else []
    arxiv_id = _clean(str(item.get("arxiv_id") or "")) or None
    return SourceRecord(
        source="papers_with_code",
        source_id=paper_id,
        title=title,
        abstract=_clean(str(item.get("abstract") or "")),
        authors=tuple(
            _clean(str(author)) for author in author_rows if _clean(str(author))
        ),
        published=published,
        url=_clean(str(item.get("url_abs") or ""))
        or f"https://paperswithcode.com/paper/{paper_id}",
        input_format="pdf",
        input_url=pdf_url,
        arxiv_id=arxiv_id,
    )


def _clean(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()
