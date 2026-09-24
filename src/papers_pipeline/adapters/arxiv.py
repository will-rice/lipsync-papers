import base64
import json
import re
from datetime import datetime, timezone
from xml.etree import ElementTree

from papers_pipeline.adapters.base import FetchPage, FetchWindow, collect_records
from papers_pipeline.config import AdapterConfig
from papers_pipeline.errors import InfrastructureError, PaperError
from papers_pipeline.http import RequestClient
from papers_pipeline.models import SourceRecord

ATOM = {"a": "http://www.w3.org/2005/Atom"}


class ArxivAdapter:
    name = "arxiv"
    record_sources = frozenset({"arxiv"})

    async def fetch(
        self,
        window: FetchWindow,
        cursor: str | None,
        client: RequestClient,
        config: AdapterConfig,
    ) -> FetchPage:
        state = _decode_cursor(cursor)
        text = await client.get_text(
            "https://export.arxiv.org/api/query",
            {
                "search_query": _windowed_query(
                    config.filters.get("search_query", "all:*"), window
                ),
                "start": str(state["start"]),
                "max_results": str(config.page_size),
                "sortBy": "submittedDate",
                "sortOrder": "ascending",
            },
            {},
        )
        try:
            root = ElementTree.fromstring(text)
        except ElementTree.ParseError as error:
            raise InfrastructureError(f"invalid XML from arxiv: {error}") from error

        entries = tuple(root.findall("a:entry", ATOM))
        parsed_records, errors = collect_records(entries, self._record)
        records = tuple(
            record
            for record in parsed_records
            if window.start <= record.published <= window.end
        )
        if not entries:
            return FetchPage(
                records=records,
                next_cursor=None,
                capped=False,
                permanent_errors=errors,
            )

        next_state = {
            "consumed": state["consumed"] + len(entries),
            "page": state["page"] + 1,
            "start": state["start"] + len(entries),
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

    def _record(self, entry: ElementTree.Element) -> SourceRecord:
        identifier = _required_identifier(entry)
        published = _required_datetime(
            _find_text(entry, "a:published"), field="published", identifier=identifier
        )
        title = _required_text(
            _find_text(entry, "a:title"), field="title", identifier=identifier
        )
        abstract = _required_text(
            _find_text(entry, "a:summary"), field="summary", identifier=identifier
        )
        authors = tuple(
            author
            for author in (
                _clean(node.findtext("a:name", namespaces=ATOM, default=""))
                for node in entry.findall("a:author", ATOM)
            )
            if author
        )
        if not authors:
            raise PaperError(f"arxiv record missing authors: {identifier}")

        categories = tuple(
            category
            for category in (
                _clean(node.attrib.get("term", ""))
                for node in entry.findall("a:category", ATOM)
            )
            if category
        )
        return SourceRecord(
            source=self.name,
            source_id=identifier,
            arxiv_id=identifier,
            title=title,
            abstract=abstract,
            authors=authors,
            published=published,
            url=f"https://arxiv.org/abs/{identifier}",
            input_format="pdf",
            input_url=f"https://arxiv.org/pdf/{identifier}",
            categories=categories,
        )


def _encode_cursor(state: dict[str, int]) -> str:
    payload = json.dumps(state, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return base64.urlsafe_b64encode(payload).decode("ascii").rstrip("=")


def _decode_cursor(cursor: str | None) -> dict[str, int]:
    if cursor is None:
        return {"consumed": 0, "page": 0, "start": 0}
    padding = "=" * (-len(cursor) % 4)
    try:
        decoded = base64.urlsafe_b64decode(f"{cursor}{padding}".encode("ascii"))
        data = json.loads(decoded.decode("utf-8"))
    except (ValueError, json.JSONDecodeError) as error:
        raise InfrastructureError(
            f"invalid arxiv continuation cursor: {cursor}"
        ) from error
    if not isinstance(data, dict):
        raise InfrastructureError(f"invalid arxiv continuation cursor: {cursor}")
    consumed = data.get("consumed")
    page = data.get("page")
    start = data.get("start")
    if consumed is None and isinstance(start, int):
        consumed = start
    if (
        not isinstance(consumed, int)
        or consumed < 0
        or not isinstance(page, int)
        or page < 0
        or not isinstance(start, int)
        or start < 0
    ):
        raise InfrastructureError(f"invalid arxiv continuation cursor: {cursor}")
    return {"consumed": consumed, "page": page, "start": start}


def _required_identifier(entry: ElementTree.Element) -> str:
    raw_identifier = _required_text(
        _find_text(entry, "a:id"), field="id", identifier="<unknown>"
    )
    normalized = re.sub(
        r"(?i)^arxiv:", "", raw_identifier.rstrip("/").rsplit("/", 1)[-1]
    )
    identifier = _clean(normalized)
    if not identifier:
        raise PaperError("arxiv record missing id: <unknown>")
    return identifier


def _find_text(entry: ElementTree.Element, path: str) -> str:
    return entry.findtext(path, namespaces=ATOM, default="")


def _required_datetime(value: str, *, field: str, identifier: str) -> datetime:
    if not value:
        raise PaperError(f"arxiv record missing {field} timestamp: {identifier}")
    try:
        published = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise PaperError(
            f"arxiv record invalid {field} timestamp: {identifier}"
        ) from error
    if published.tzinfo is None or published.utcoffset() is None:
        raise PaperError(f"arxiv record invalid {field} timestamp: {identifier}")
    return published


def _required_text(value: str, *, field: str, identifier: str) -> str:
    cleaned = _clean(value)
    if not cleaned:
        raise PaperError(f"arxiv record missing {field}: {identifier}")
    return cleaned


def _clean(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def _windowed_query(query: str, window: FetchWindow) -> str:
    start = window.start.astimezone(timezone.utc).strftime("%Y%m%d%H%M")
    end = window.end.astimezone(timezone.utc).strftime("%Y%m%d%H%M")
    return f"({query}) AND submittedDate:[{start} TO {end}]"
