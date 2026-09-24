import base64
import json
import re
from datetime import datetime, timezone
from typing import TypedDict

from papers_pipeline.adapters.base import FetchPage, FetchWindow, collect_records
from papers_pipeline.config import AdapterConfig
from papers_pipeline.errors import InfrastructureError, PaperError
from papers_pipeline.http import RequestClient
from papers_pipeline.models import SourceRecord


# Relevance search pages by offset/limit and filters by publication date, but
# only its first 1,000 results per query are reachable.
_SEARCH_URL = "https://api.semanticscholar.org/graph/v1/paper/search"
_REACHABLE_RESULTS = 1000


class SemanticScholarAdapter:
    name = "semantic_scholar"
    record_sources = frozenset({"semantic_scholar"})

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    async def fetch(
        self,
        window: FetchWindow,
        cursor: str | None,
        client: RequestClient,
        config: AdapterConfig,
    ) -> FetchPage:
        state = _decode_cursor(cursor)
        text = await client.get_text(
            _SEARCH_URL,
            {
                "query": config.filters.get("query", "*"),
                "publicationDateOrYear": (
                    f"{window.start.date().isoformat()}:{window.end.date().isoformat()}"
                ),
                "offset": state["offset"],
                "limit": str(config.page_size),
                "fields": (
                    "paperId,title,abstract,authors,publicationDate,url,"
                    "externalIds,openAccessPdf"
                ),
            },
            {"x-api-key": self.api_key},
        )
        items, next_offset, total = _payload_page(text)
        parsed_records, errors = collect_records(items, self._record)
        if state["page"] == 0 and total > _REACHABLE_RESULTS:
            errors = (
                *errors,
                f"semantic_scholar window {window.start.date()}..{window.end.date()} "
                f"matches {total} papers; only the first {_REACHABLE_RESULTS} are "
                "reachable, so shorten the window",
            )
        records = tuple(
            record
            for record in parsed_records
            if window.start <= record.published <= window.end
        )
        if not items:
            return FetchPage(
                records=records,
                next_cursor=None,
                capped=False,
                permanent_errors=errors,
            )

        next_state: _CursorState = {
            "consumed": state["consumed"] + len(items),
            "offset": _next_offset(
                current_offset=state["offset"],
                payload_next=next_offset,
                item_count=len(items),
            ),
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
            raise PaperError("semantic_scholar record missing object: <unknown>")

        identifier = _required_text(
            item.get("paperId"), field="paperId", identifier="<unknown>"
        )
        title = _required_text(item.get("title"), field="title", identifier=identifier)
        published = _required_datetime(
            item.get("publicationDate"),
            field="publicationDate",
            identifier=identifier,
        )
        input_url = _required_pdf_url(item.get("openAccessPdf"), identifier=identifier)
        external_ids = item.get("externalIds")
        identifiers = external_ids if isinstance(external_ids, dict) else {}
        return SourceRecord(
            source=self.name,
            source_id=identifier,
            title=title,
            abstract=_clean(_optional_text(item.get("abstract"))),
            authors=_authors(item.get("authors")),
            published=published,
            url=_optional_text(item.get("url"))
            or f"https://www.semanticscholar.org/paper/{identifier}",
            input_format="pdf",
            input_url=input_url,
            doi=_scalar_text(identifiers.get("DOI")),
            arxiv_id=_scalar_text(identifiers.get("ArXiv")),
        )


class _CursorState(TypedDict):
    consumed: int
    offset: str
    page: int


def _payload_page(text: str) -> tuple[list[object], object, int]:
    try:
        payload = json.loads(text)
    except json.JSONDecodeError as error:
        raise InfrastructureError(
            f"invalid JSON from semantic_scholar: {error}"
        ) from error
    if not isinstance(payload, dict):
        raise InfrastructureError("invalid semantic_scholar payload: expected object")
    items = payload.get("data")
    if not isinstance(items, list):
        raise InfrastructureError(
            "invalid semantic_scholar payload: expected data list"
        )
    # The API documents total as a string but returns an integer.
    try:
        total = int(payload.get("total", 0))
    except (TypeError, ValueError) as error:
        raise InfrastructureError(
            "invalid semantic_scholar payload: expected total"
        ) from error
    return items, payload.get("next"), total


def _encode_cursor(state: _CursorState) -> str:
    payload = json.dumps(state, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return base64.urlsafe_b64encode(payload).decode("ascii").rstrip("=")


def _decode_cursor(cursor: str | None) -> _CursorState:
    if cursor is None:
        return {"consumed": 0, "offset": "0", "page": 0}

    padding = "=" * (-len(cursor) % 4)
    try:
        decoded = base64.urlsafe_b64decode(f"{cursor}{padding}".encode("ascii"))
        data = json.loads(decoded.decode("utf-8"))
    except (ValueError, json.JSONDecodeError) as error:
        raise InfrastructureError(
            f"invalid semantic_scholar continuation cursor: {cursor}"
        ) from error
    if not isinstance(data, dict):
        raise InfrastructureError(
            f"invalid semantic_scholar continuation cursor: {cursor}"
        )

    consumed = data.get("consumed")
    offset = data.get("offset")
    page = data.get("page")
    normalized_offset: str
    if isinstance(offset, int) and offset >= 0:
        normalized_offset = str(offset)
    elif isinstance(offset, str) and offset:
        normalized_offset = _clean(offset)
    else:
        normalized_offset = ""
    if (
        not isinstance(consumed, int)
        or consumed < 0
        or not normalized_offset
        or not isinstance(page, int)
        or page < 0
    ):
        raise InfrastructureError(
            f"invalid semantic_scholar continuation cursor: {cursor}"
        )
    return {"consumed": consumed, "offset": normalized_offset, "page": page}


def _next_offset(*, current_offset: str, payload_next: object, item_count: int) -> str:
    if isinstance(payload_next, int) and payload_next >= 0:
        return str(payload_next)

    if isinstance(payload_next, str):
        next_offset = _clean(payload_next)
        if next_offset:
            return next_offset

    try:
        return str(int(current_offset) + item_count)
    except ValueError as error:
        raise InfrastructureError(
            "invalid semantic_scholar payload: expected next continuation token"
        ) from error


def _required_pdf_url(value: object, *, identifier: str) -> str:
    if not isinstance(value, dict):
        raise PaperError(
            f"semantic_scholar record missing openAccessPdf.url: {identifier}"
        )
    url = _optional_text(value.get("url"))
    if not url:
        raise PaperError(
            f"semantic_scholar record missing openAccessPdf.url: {identifier}"
        )
    return url


def _required_datetime(value: object, *, field: str, identifier: str) -> datetime:
    if not isinstance(value, str):
        raise PaperError(f"semantic_scholar record missing {field}: {identifier}")
    cleaned = _clean(value)
    if not cleaned:
        raise PaperError(f"semantic_scholar record missing {field}: {identifier}")
    try:
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", cleaned):
            published = datetime.fromisoformat(f"{cleaned}T00:00:00+00:00")
        else:
            published = datetime.fromisoformat(cleaned.replace("Z", "+00:00"))
    except ValueError as error:
        raise PaperError(
            f"semantic_scholar record invalid {field}: {identifier}"
        ) from error
    if published.tzinfo is None or published.utcoffset() is None:
        published = published.replace(tzinfo=timezone.utc)
    return published


def _required_text(value: object, *, field: str, identifier: str) -> str:
    text = _optional_text(value)
    if not text:
        raise PaperError(f"semantic_scholar record missing {field}: {identifier}")
    return text


def _authors(value: object) -> tuple[str, ...]:
    if not isinstance(value, list):
        return ()
    authors: list[str] = []
    for item in value:
        if isinstance(item, dict):
            name = _optional_text(item.get("name"))
        else:
            name = _optional_text(item)
        if name:
            authors.append(name)
    return tuple(authors)


def _scalar_text(value: object) -> str | None:
    text = _optional_text(value)
    return text or None


def _optional_text(value: object) -> str:
    if not isinstance(value, str):
        return ""
    return _clean(value)


def _clean(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()
