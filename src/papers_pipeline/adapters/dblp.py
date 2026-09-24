import base64
import json
import re
from datetime import datetime, timezone
from urllib.parse import urlsplit

from papers_pipeline.adapters.base import FetchPage, FetchWindow, collect_records
from papers_pipeline.config import AdapterConfig
from papers_pipeline.errors import InfrastructureError, PaperError
from papers_pipeline.http import RequestClient
from papers_pipeline.models import InputFormat, SourceRecord


class DblpAdapter:
    name = "dblp"
    record_sources = frozenset({"dblp"})

    async def fetch(
        self,
        window: FetchWindow,
        cursor: str | None,
        client: RequestClient,
        config: AdapterConfig,
    ) -> FetchPage:
        state = _decode_cursor(cursor)
        text = await client.get_text(
            "https://dblp.org/search/publ/api",
            {
                "q": config.filters.get("query", "*"),
                "f": str(state["offset"]),
                "h": str(config.page_size),
                "format": "json",
            },
            {},
        )
        hits = _payload_hits(text)
        parsed_records, errors = collect_records(hits, self._record)
        records = tuple(
            record for record in parsed_records if _within_window(record, window)
        )
        if not hits:
            return FetchPage(
                records=records,
                next_cursor=None,
                capped=False,
                permanent_errors=errors,
            )

        next_state = {
            "consumed": state["consumed"] + len(hits),
            "offset": state["offset"] + len(hits),
            "page": state["page"] + 1,
        }
        next_cursor = _encode_cursor(next_state)
        capped = (
            next_state["page"] >= config.max_pages
            or next_state["consumed"] >= config.max_results
        )
        return FetchPage(
            records=records,
            next_cursor=next_cursor,
            capped=capped,
            permanent_errors=errors,
        )

    def _record(self, item: object) -> SourceRecord:
        if not isinstance(item, dict):
            raise PaperError("dblp record missing hit object: <unknown>")
        info = item.get("info")
        if not isinstance(info, dict):
            raise PaperError("dblp record missing info object: <unknown>")

        identifier = _required_text(
            info.get("key"), field="key", identifier="<unknown>"
        )
        title = _required_text(info.get("title"), field="title", identifier=identifier)
        published = _required_year(info.get("year"), identifier=identifier)
        input_url = _electronic_url(info.get("ee"), identifier=identifier)
        return SourceRecord(
            source=self.name,
            source_id=identifier,
            title=title,
            abstract="",
            authors=_authors(info.get("authors")),
            published=published,
            url=_scalar_text(info.get("url")) or f"https://dblp.org/rec/{identifier}",
            input_format=electronic_format(input_url),
            input_url=input_url,
            doi=_first_text(info.get("doi")),
        )


def electronic_format(url: str) -> InputFormat:
    """Electronic editions are HTML pages unless the link is a PDF itself."""
    return "pdf" if urlsplit(url).path.casefold().endswith(".pdf") else "html"


def _within_window(record: SourceRecord, window: FetchWindow) -> bool:
    return window.start.year <= record.published.year <= window.end.year


def _payload_hits(text: str) -> list[object]:
    try:
        payload = json.loads(text)
    except json.JSONDecodeError as error:
        raise InfrastructureError(f"invalid JSON from dblp: {error}") from error
    if not isinstance(payload, dict):
        raise InfrastructureError("invalid dblp payload: expected object")
    result = payload.get("result")
    if not isinstance(result, dict):
        raise InfrastructureError("invalid dblp payload: expected result object")
    hits = result.get("hits")
    if not isinstance(hits, dict):
        raise InfrastructureError("invalid dblp payload: expected result.hits object")
    items = hits.get("hit")
    if not isinstance(items, list):
        raise InfrastructureError("invalid dblp payload: expected result.hits.hit list")
    return items


def _encode_cursor(state: dict[str, int]) -> str:
    payload = json.dumps(state, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return base64.urlsafe_b64encode(payload).decode("ascii").rstrip("=")


def _decode_cursor(cursor: str | None) -> dict[str, int]:
    if cursor is None:
        return {"consumed": 0, "offset": 0, "page": 0}

    padding = "=" * (-len(cursor) % 4)
    try:
        decoded = base64.urlsafe_b64decode(f"{cursor}{padding}".encode("ascii"))
        data = json.loads(decoded.decode("utf-8"))
    except (ValueError, json.JSONDecodeError) as error:
        raise InfrastructureError(
            f"invalid dblp continuation cursor: {cursor}"
        ) from error
    if not isinstance(data, dict):
        raise InfrastructureError(f"invalid dblp continuation cursor: {cursor}")

    consumed = data.get("consumed")
    offset = data.get("offset")
    page = data.get("page")
    if (
        not isinstance(consumed, int)
        or consumed < 0
        or not isinstance(offset, int)
        or offset < 0
        or not isinstance(page, int)
        or page < 0
    ):
        raise InfrastructureError(f"invalid dblp continuation cursor: {cursor}")
    return {"consumed": consumed, "offset": offset, "page": page}


def _required_text(value: object, *, field: str, identifier: str) -> str:
    text = _scalar_text(value)
    if not text:
        raise PaperError(f"dblp record missing {field}: {identifier}")
    return text


def _required_year(value: object, *, identifier: str) -> datetime:
    if isinstance(value, int):
        year = value
    elif isinstance(value, str):
        cleaned = _clean(value)
        if not cleaned:
            raise PaperError(f"dblp record missing year: {identifier}")
        try:
            year = int(cleaned)
        except ValueError as error:
            raise PaperError(f"dblp record invalid year: {identifier}") from error
    else:
        raise PaperError(f"dblp record missing year: {identifier}")
    try:
        return datetime(year, 1, 1, tzinfo=timezone.utc)
    except ValueError as error:
        raise PaperError(f"dblp record invalid year: {identifier}") from error


def _electronic_url(ee: object, *, identifier: str) -> str:
    # Only "ee" links to the paper; "url" is dblp's own metadata page.
    electronic_url = _first_text(ee)
    if not electronic_url:
        raise PaperError(f"dblp record missing electronic URL: {identifier}")
    return electronic_url


def _authors(value: object) -> tuple[str, ...]:
    if isinstance(value, dict):
        value = value.get("author")
    if value is None:
        return ()
    if not isinstance(value, list):
        value = [value]

    authors: list[str] = []
    for item in value:
        name = _author_name(item)
        if name:
            authors.append(name)
    return tuple(authors)


def _author_name(value: object) -> str:
    if isinstance(value, dict):
        return _scalar_text(value.get("text")) or _scalar_text(value.get("@name")) or ""
    return _scalar_text(value) or ""


def _first_text(value: object) -> str | None:
    if isinstance(value, list):
        for item in value:
            text = _first_text(item)
            if text:
                return text
        return None
    text = _scalar_text(value)
    return text or None


def _scalar_text(value: object) -> str:
    if isinstance(value, str):
        return _clean(value)
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return str(value)
    return ""


def _clean(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()
