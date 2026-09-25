import base64
import json
import re
from collections.abc import Mapping
from datetime import date, datetime, timedelta
from typing import TypedDict

from papers_pipeline.adapters.base import FetchPage, FetchWindow, collect_records
from papers_pipeline.config import AdapterConfig
from papers_pipeline.errors import InfrastructureError, PaperError
from papers_pipeline.http import RequestClient
from papers_pipeline.models import SourceRecord


class _CursorState(TypedDict):
    date: str | None
    page: int
    source_consumed: int


class HuggingFaceAdapter:
    name = "huggingface"
    record_sources = frozenset({"huggingface"})

    async def fetch(
        self,
        window: FetchWindow,
        cursor: str | None,
        client: RequestClient,
        config: AdapterConfig,
    ) -> FetchPage:
        state = _decode_cursor(cursor)
        # The API rejects dates after its latest published day (HTTP 400), which
        # lags "today" in UTC. Start the day before the window ends: the lookback
        # windows overlap, so today's list is fetched by the next run, and a
        # backfill chunk's end day is covered by the chunk after it.
        current_date = (
            date.fromisoformat(state["date"])
            if state["date"] is not None
            else (window.end - timedelta(days=1)).date()
        )
        text = await client.get_text(
            "https://huggingface.co/api/daily_papers",
            {
                "date": current_date.isoformat(),
                "p": str(state["page"]),
                "limit": str(config.page_size),
            },
            {},
        )
        try:
            payload = json.loads(text)
        except json.JSONDecodeError as error:
            raise InfrastructureError(
                f"invalid JSON from huggingface: {error}"
            ) from error
        if not isinstance(payload, list):
            raise InfrastructureError(
                "invalid JSON from huggingface: expected list payload"
            )

        parsed_records, errors = collect_records(payload, self._record)
        records = tuple(
            record
            for record in parsed_records
            if window.start <= record.published <= window.end
        )
        if not payload:
            previous_date = current_date - timedelta(days=1)
            next_cursor = (
                _encode_cursor(
                    {
                        "date": previous_date.isoformat(),
                        "page": 0,
                        "source_consumed": state["source_consumed"],
                    }
                )
                if previous_date >= window.start.date()
                else None
            )
            return FetchPage(
                records=records,
                next_cursor=next_cursor,
                capped=False,
                permanent_errors=errors,
            )

        next_state: _CursorState = {
            "date": current_date.isoformat(),
            "page": state["page"] + 1,
            "source_consumed": state["source_consumed"] + len(payload),
        }
        next_cursor = _encode_cursor(next_state)
        capped = len(payload) >= config.max_results
        return FetchPage(
            records=records,
            next_cursor=next_cursor,
            capped=capped,
            permanent_errors=errors,
        )

    def _record(self, item: object) -> SourceRecord:
        if not isinstance(item, dict):
            raise PaperError("huggingface record missing paper object: <unknown>")
        paper = item.get("paper")
        if not isinstance(paper, dict):
            raise PaperError("huggingface record missing paper object: <unknown>")

        identifier = _required_identifier(paper)
        published = _required_datetime(paper.get("publishedAt"), identifier=identifier)
        title = _required_text(paper.get("title"), field="title", identifier=identifier)
        abstract = _clean(_optional_text(paper.get("summary")))
        authors = _authors(paper.get("authors"), identifier=identifier)
        categories = _categories(paper.get("categories") or paper.get("tags"))
        return SourceRecord(
            source=self.name,
            source_id=identifier,
            arxiv_id=identifier,
            title=title,
            abstract=abstract,
            authors=authors,
            published=published,
            url=f"https://huggingface.co/papers/{identifier}",
            input_format="pdf",
            input_url=f"https://arxiv.org/pdf/{identifier}",
            categories=categories,
        )


def _encode_cursor(state: Mapping[str, object]) -> str:
    payload = json.dumps(state, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return base64.urlsafe_b64encode(payload).decode("ascii").rstrip("=")


def _decode_cursor(cursor: str | None) -> _CursorState:
    if cursor is None:
        return {"date": None, "page": 0, "source_consumed": 0}
    padding = "=" * (-len(cursor) % 4)
    try:
        decoded = base64.urlsafe_b64decode(f"{cursor}{padding}".encode("ascii"))
        data = json.loads(decoded.decode("utf-8"))
    except (ValueError, json.JSONDecodeError) as error:
        raise InfrastructureError(
            f"invalid huggingface continuation cursor: {cursor}"
        ) from error
    if not isinstance(data, dict):
        raise InfrastructureError(f"invalid huggingface continuation cursor: {cursor}")
    consumed = data.get("source_consumed", data.get("consumed", data.get("emitted")))
    page = data.get("page")
    raw_date = data.get("date")
    if (
        not isinstance(consumed, int)
        or consumed < 0
        or not isinstance(page, int)
        or page < 0
    ):
        raise InfrastructureError(f"invalid huggingface continuation cursor: {cursor}")
    if raw_date is not None:
        if not isinstance(raw_date, str):
            raise InfrastructureError(
                f"invalid huggingface continuation cursor: {cursor}"
            )
        try:
            date.fromisoformat(raw_date)
        except ValueError as error:
            raise InfrastructureError(
                f"invalid huggingface continuation cursor: {cursor}"
            ) from error
    return {"date": raw_date, "page": page, "source_consumed": consumed}


def _required_identifier(paper: dict[str, object]) -> str:
    raw_identifier = _required_text(paper.get("id"), field="id", identifier="<unknown>")
    identifier = re.sub(r"(?i)^arxiv:", "", raw_identifier)
    cleaned = _clean(identifier)
    if not cleaned:
        raise PaperError("huggingface record missing id: <unknown>")
    return cleaned


def _required_datetime(value: object, *, identifier: str) -> datetime:
    if value is None:
        raise PaperError(f"huggingface record missing publishedAt: {identifier}")
    if not isinstance(value, str):
        raise PaperError(f"huggingface record invalid publishedAt: {identifier}")
    try:
        published = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise PaperError(
            f"huggingface record invalid publishedAt: {identifier}"
        ) from error
    if published.tzinfo is None or published.utcoffset() is None:
        raise PaperError(f"huggingface record invalid publishedAt: {identifier}")
    return published


def _required_text(value: object, *, field: str, identifier: str) -> str:
    if not isinstance(value, str):
        raise PaperError(f"huggingface record missing {field}: {identifier}")
    cleaned = _clean(value)
    if not cleaned:
        raise PaperError(f"huggingface record missing {field}: {identifier}")
    return cleaned


def _optional_text(value: object) -> str:
    return value if isinstance(value, str) else ""


def _authors(value: object, *, identifier: str) -> tuple[str, ...]:
    if value is None:
        return ()
    if not isinstance(value, list):
        raise PaperError(f"huggingface record invalid authors: {identifier}")
    authors: list[str] = []
    for item in value:
        if not isinstance(item, dict):
            raise PaperError(f"huggingface record invalid authors: {identifier}")
        name = _clean(str(item.get("name", "")))
        if name:
            authors.append(name)
    return tuple(authors)


def _categories(value: object) -> tuple[str, ...]:
    if value is None:
        return ()
    if not isinstance(value, list):
        return ()
    categories: list[str] = []
    for item in value:
        category = _clean(str(item))
        if category:
            categories.append(category)
    return tuple(categories)


def _clean(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()
