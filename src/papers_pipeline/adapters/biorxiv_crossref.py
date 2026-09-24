import base64
import json
import re
from datetime import datetime, timezone
from typing import TypedDict

from papers_pipeline.adapters.base import FetchPage, FetchWindow, collect_records
from papers_pipeline.config import AdapterConfig
from papers_pipeline.errors import ConfigError, InfrastructureError, PaperError
from papers_pipeline.http import RequestClient
from papers_pipeline.models import SourceRecord

_BIORXIV = "biorxiv"
_CROSSREF = "crossref"


class BiorxivCrossrefAdapter:
    name = "biorxiv_crossref"
    record_sources = frozenset({_BIORXIV, _CROSSREF})

    async def fetch(
        self,
        window: FetchWindow,
        cursor: str | None,
        client: RequestClient,
        config: AdapterConfig,
    ) -> FetchPage:
        provider = _provider(config)
        state = _decode_cursor(cursor, provider=provider)
        next_token: str | None

        if provider == _BIORXIV:
            items = await _fetch_biorxiv(
                window=window, client=client, offset=state["token"]
            )
        else:
            items, next_token = await _fetch_crossref(
                window=window,
                client=client,
                page_size=config.page_size,
                cursor_value=state["token"],
            )
            records, errors = collect_records(items, parse_crossref)

        if not items:
            return FetchPage(
                records=(),
                next_cursor=None,
                capped=False,
                permanent_errors=(),
            )

        if provider == _CROSSREF:
            filtered_records = tuple(
                record
                for record in records
                if window.start <= record.published <= window.end
            )
            consumed = state["consumed"] + (0 if state["local_index"] else len(items))
            page = state["page"] + (0 if state["local_index"] else 1)
            remaining_records = _remaining_records(
                filtered_records,
                local_index=state["local_index"],
                provider=provider,
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
                        "provider": provider,
                        "token": state["token"],
                    }
                )
            elif next_token is not None:
                next_cursor = _encode_cursor(
                    {
                        "consumed": consumed,
                        "local_index": 0,
                        "page": page,
                        "provider": provider,
                        "token": next_token,
                    }
                )
            else:
                next_cursor = None
            capped = page >= config.max_pages or consumed >= config.max_results
        else:
            if state["local_index"] > len(items):
                raise InfrastructureError(
                    f"invalid {provider} continuation cursor: {cursor or '<initial>'}"
                )
            raw_records = items[
                state["local_index"] : state["local_index"] + config.max_results
            ]
            records, errors = collect_records(raw_records, parse_biorxiv)
            page_records = tuple(
                record
                for record in records
                if window.start <= record.published <= window.end
            )
            raw_end = state["local_index"] + len(raw_records)
            consumed = state["consumed"] + len(raw_records)
            page_complete = raw_end == len(items)
            page = state["page"] + int(page_complete)
            next_token = (
                str(int(state["token"]) + len(items))
                if page_complete
                else state["token"]
            )
            next_cursor = _encode_cursor(
                {
                    "consumed": consumed,
                    "local_index": 0 if page_complete else raw_end,
                    "page": page,
                    "provider": provider,
                    "token": next_token,
                }
            )
            capped = page >= config.max_pages or len(raw_records) >= config.max_results
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
    provider: str
    token: str


async def _fetch_biorxiv(
    *,
    window: FetchWindow,
    client: RequestClient,
    offset: str,
) -> list[object]:
    text = await client.get_text(
        (
            "https://api.biorxiv.org/details/biorxiv/"
            f"{window.start.date().isoformat()}/{window.end.date().isoformat()}/{offset}"
        ),
        {},
        {},
    )
    try:
        payload = json.loads(text)
    except json.JSONDecodeError as error:
        raise InfrastructureError(f"invalid JSON from biorxiv: {error}") from error
    if not isinstance(payload, dict):
        raise InfrastructureError("invalid biorxiv payload: expected object")
    items = payload.get("collection")
    if not isinstance(items, list):
        raise InfrastructureError("invalid biorxiv payload: expected collection list")
    return items


async def _fetch_crossref(
    *,
    window: FetchWindow,
    client: RequestClient,
    page_size: int,
    cursor_value: str,
) -> tuple[list[object], str | None]:
    text = await client.get_text(
        "https://api.crossref.org/works",
        {
            "filter": (
                f"from-pub-date:{window.start.date().isoformat()},"
                f"until-pub-date:{window.end.date().isoformat()}"
            ),
            "rows": str(page_size),
            "cursor": cursor_value,
        },
        {"User-Agent": "papers-pipeline/0.1"},
    )
    try:
        payload = json.loads(text)
    except json.JSONDecodeError as error:
        raise InfrastructureError(f"invalid JSON from crossref: {error}") from error
    if not isinstance(payload, dict):
        raise InfrastructureError("invalid crossref payload: expected object")
    message = payload.get("message")
    if not isinstance(message, dict):
        raise InfrastructureError("invalid crossref payload: expected message object")
    items = message.get("items")
    if not isinstance(items, list):
        raise InfrastructureError(
            "invalid crossref payload: expected message.items list"
        )
    next_cursor_value = message.get("next-cursor")
    next_cursor = (
        _clean(next_cursor_value) or None
        if isinstance(next_cursor_value, str)
        else None
    )
    return items, next_cursor


def _encode_cursor(state: _CursorState) -> str:
    payload = json.dumps(state, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return base64.urlsafe_b64encode(payload).decode("ascii").rstrip("=")


def _decode_cursor(cursor: str | None, *, provider: str) -> _CursorState:
    if cursor is None:
        return {
            "consumed": 0,
            "local_index": 0,
            "page": 0,
            "provider": provider,
            "token": "0" if provider == _BIORXIV else "*",
        }

    padding = "=" * (-len(cursor) % 4)
    try:
        decoded = base64.urlsafe_b64decode(f"{cursor}{padding}".encode("ascii"))
        data = json.loads(decoded.decode("utf-8"))
    except (ValueError, json.JSONDecodeError) as error:
        raise InfrastructureError(
            f"invalid {provider} continuation cursor: {cursor}"
        ) from error
    if not isinstance(data, dict):
        raise InfrastructureError(f"invalid {provider} continuation cursor: {cursor}")

    consumed = data.get("consumed")
    local_index = data.get("local_index", 0)
    page = data.get("page")
    encoded_provider = data.get("provider")
    token = _clean(str(data.get("token") or ""))
    if (
        not isinstance(consumed, int)
        or consumed < 0
        or not isinstance(local_index, int)
        or local_index < 0
        or not isinstance(page, int)
        or page < 0
        or encoded_provider != provider
        or not token
        or (provider == _BIORXIV and not token.isdigit())
    ):
        raise InfrastructureError(f"invalid {provider} continuation cursor: {cursor}")
    return {
        "consumed": consumed,
        "local_index": local_index,
        "page": page,
        "provider": provider,
        "token": token,
    }


def _provider(config: AdapterConfig) -> str:
    provider = _clean(config.filters.get("provider", _BIORXIV))
    if provider not in {_BIORXIV, _CROSSREF}:
        raise ConfigError(
            "biorxiv_crossref.filters.provider must be biorxiv or crossref"
        )
    return provider


def biorxiv_pdf_url(doi: str) -> str:
    """Return the full-text PDF URL bioRxiv serves for a preprint DOI."""
    return f"https://www.biorxiv.org/content/{doi}.full.pdf"


def parse_biorxiv(item: object) -> SourceRecord:
    if not isinstance(item, dict):
        raise PaperError("bioRxiv record lacks DOI, title, or date")
    doi = _clean(str(item.get("doi") or ""))
    title = _clean(str(item.get("title") or ""))
    published = _clean(str(item.get("date") or ""))
    if not doi or not title or not published:
        raise PaperError("bioRxiv record lacks DOI, title, or date")
    try:
        published_at = datetime.fromisoformat(f"{published}T00:00:00+00:00")
    except ValueError as error:
        raise PaperError("bioRxiv record lacks DOI, title, or date") from error
    category = _clean(str(item.get("category") or ""))
    return SourceRecord(
        source=_BIORXIV,
        source_id=doi,
        doi=doi,
        title=title,
        abstract=_clean(str(item.get("abstract") or "")),
        authors=tuple(
            author.strip()
            for author in str(item.get("authors") or "").split(";")
            if author.strip()
        ),
        published=published_at,
        url=f"https://doi.org/{doi}",
        input_format="pdf",
        input_url=biorxiv_pdf_url(doi),
        categories=(category,) if category else (),
    )


def parse_crossref(item: object) -> SourceRecord:
    if not isinstance(item, dict):
        raise PaperError("Crossref record lacks DOI, title, date, or full text")
    doi = _clean(str(item.get("DOI") or ""))
    title = _first_title(item.get("title"))
    published = _date_from_parts(_published_date_parts(item))
    html_url, pdf_url = _links(item.get("link"))
    input_url = html_url or pdf_url
    if not doi or not title or published is None or not input_url:
        raise PaperError("Crossref record lacks DOI, title, date, or full text")
    return SourceRecord(
        source=_CROSSREF,
        source_id=doi,
        doi=doi,
        title=title,
        abstract=_clean(str(item.get("abstract") or "")),
        authors=_crossref_authors(item.get("author")),
        published=published,
        url=_clean(str(item.get("URL") or "")) or f"https://doi.org/{doi}",
        input_format="html" if html_url else "pdf",
        input_url=input_url,
    )


def _published_date_parts(item: dict[str, object]) -> list[object] | None:
    for key in ("published", "published-print", "published-online", "issued"):
        container = item.get(key)
        if not isinstance(container, dict):
            continue
        date_parts = container.get("date-parts")
        if not isinstance(date_parts, list) or not date_parts:
            continue
        first = date_parts[0]
        if isinstance(first, list):
            return first
    return None


def _date_from_parts(parts: list[object] | None) -> datetime | None:
    if not parts:
        return None
    year = _int_date_part(parts[0])
    month = _int_date_part(parts[1]) if len(parts) >= 2 else 1
    day = _int_date_part(parts[2]) if len(parts) >= 3 else 1
    if year is None or month is None or day is None:
        return None
    try:
        return datetime(year, month, day, tzinfo=timezone.utc)
    except ValueError:
        return None


def _int_date_part(value: object) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        cleaned = _clean(value)
        if cleaned:
            try:
                return int(cleaned)
            except ValueError:
                return None
    return None


def _first_title(value: object) -> str:
    if not isinstance(value, list):
        return ""
    for item in value:
        if isinstance(item, str):
            title = _clean(item)
            if title:
                return title
    return ""


def _crossref_authors(value: object) -> tuple[str, ...]:
    if not isinstance(value, list):
        return ()
    authors: list[str] = []
    for item in value:
        if not isinstance(item, dict):
            continue
        author = " ".join(
            part
            for part in (
                _clean(str(item.get("given") or "")),
                _clean(str(item.get("family") or "")),
            )
            if part
        )
        if author:
            authors.append(author)
    return tuple(authors)


def _remaining_records(
    records: tuple[SourceRecord, ...],
    *,
    local_index: int,
    provider: str,
    cursor: str | None,
) -> tuple[SourceRecord, ...]:
    if local_index > len(records):
        raise InfrastructureError(
            f"invalid {provider} continuation cursor: {cursor or '<initial>'}"
        )
    return records[local_index:]


def _links(value: object) -> tuple[str, str]:
    if not isinstance(value, list):
        return "", ""
    html_url = ""
    pdf_url = ""
    for item in value:
        if not isinstance(item, dict):
            continue
        url = _clean(str(item.get("URL") or ""))
        content_type = _clean(str(item.get("content-type") or "")).casefold()
        if not url:
            continue
        if not html_url and content_type == "text/html":
            html_url = url
        if not pdf_url and content_type == "application/pdf":
            pdf_url = url
    return html_url, pdf_url


def _clean(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()
