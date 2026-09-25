from datetime import datetime, timezone
from collections.abc import Callable
from pathlib import Path
from typing import Literal, TypedDict, cast

import httpx
import pytest

from papers_pipeline.config import TopicConfig
from papers_pipeline.config import AdapterConfig, FetchConfig
from papers_pipeline.http import Deadline, RequestClient
from papers_pipeline.models import Paper, SourceRecord

FIXTURES = Path(__file__).with_name("fixtures")


class RecordedRoute(TypedDict, total=False):
    fixture: str
    status_code: int
    headers: dict[str, str]
    mode: Literal["text", "bytes"]
    encoding: str


FixtureTransport = Callable[[dict[str, RecordedRoute]], httpx.MockTransport]


class RecordedRequestClient(RequestClient):
    def __init__(
        self,
        *,
        config: FetchConfig,
        transport: httpx.AsyncBaseTransport,
        requests: list[httpx.Request],
    ) -> None:
        super().__init__(
            config=config,
            deadline=Deadline.start(config.total_deadline_seconds),
            transport=transport,
        )
        self.requests = requests


@pytest.fixture
def source_record() -> SourceRecord:
    return SourceRecord(
        source="semantic_scholar",
        source_id="semantic-1",
        title=" Neural   Speech\nRecognition ",
        abstract=" A system for speech understanding. ",
        authors=(" Ada  Lovelace ", " Grace\nHopper "),
        published=datetime(2024, 1, 2, 12, 30, tzinfo=timezone.utc),
        url="https://example.test/papers/semantic-1",
        input_format="pdf",
        input_url="https://example.test/papers/semantic-1.pdf",
        categories=("cs.CL", "cs.AI", "cs.CL"),
        doi=None,
        arxiv_id=None,
    )


@pytest.fixture
def paper() -> Paper:
    return Paper(
        identifier="semantic_scholar:semantic-1",
        title="Neural Speech Recognition",
        abstract="A system for speech understanding.",
        authors=("Ada Lovelace", "Grace Hopper"),
        published=datetime(2024, 1, 2, 12, 30, tzinfo=timezone.utc),
        url="https://example.test/papers/semantic-1",
        source="semantic_scholar",
        input_format="pdf",
        input_url="https://example.test/papers/semantic-1.pdf",
        categories=("cs.AI", "cs.CL"),
        doi=None,
        arxiv_id=None,
    )


@pytest.fixture
def topic_config() -> TopicConfig:
    return TopicConfig(
        include_any=["speech"],
        include_all=[],
        exclude_any=[],
        categories=[],
        plugin=None,
    )


@pytest.fixture
def fixture_transport() -> FixtureTransport:
    def build(routes: dict[str, RecordedRoute]) -> httpx.MockTransport:
        recorded_routes = {
            url: _load_recorded_route(spec) for url, spec in routes.items()
        }

        def handler(request: httpx.Request) -> httpx.Response:
            url = str(request.url)
            if url not in recorded_routes:
                raise AssertionError(
                    f"unexpected recorded fixture URL: {request.method} {url}"
                )
            status_code, headers, body, mode = recorded_routes[url]
            if mode == "text":
                return httpx.Response(
                    status_code, headers=headers, text=cast(str, body)
                )
            return httpx.Response(status_code, headers=headers, content=body)

        return httpx.MockTransport(handler)

    return build


@pytest.fixture
def fetch_config() -> FetchConfig:
    return FetchConfig(
        request_timeout_seconds=5,
        retries=0,
        backoff_seconds=0,
        total_deadline_seconds=300,
    )


def _request_client(
    *,
    config: FetchConfig,
    transport: httpx.AsyncBaseTransport,
) -> RequestClient:
    return RequestClient(
        config=config,
        deadline=Deadline.start(config.total_deadline_seconds),
        transport=transport,
    )


def _recording_request_client(
    *,
    config: FetchConfig,
    routes: dict[str, RecordedRoute],
) -> RecordedRequestClient:
    recorded_routes = {url: _load_recorded_route(spec) for url, spec in routes.items()}
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        url = str(request.url)
        if url not in recorded_routes:
            raise AssertionError(
                f"unexpected recorded fixture URL: {request.method} {url}"
            )
        status_code, headers, body, mode = recorded_routes[url]
        if mode == "text":
            return httpx.Response(status_code, headers=headers, text=cast(str, body))
        return httpx.Response(status_code, headers=headers, content=body)

    return RecordedRequestClient(
        config=config,
        transport=httpx.MockTransport(handler),
        requests=requests,
    )


def _arxiv_route(*, start: int, page_size: int, search_query: str) -> str:
    return (
        "https://export.arxiv.org/api/query"
        f"?search_query=%28{search_query}%29+AND+"
        "submittedDate%3A%5B202401010000+TO+202401080000%5D"
        f"&start={start}&max_results={page_size}"
        "&sortBy=submittedDate&sortOrder=ascending"
    )


def _huggingface_route(*, page: int, page_size: int, date: str) -> str:
    return (
        "https://huggingface.co/api/daily_papers"
        f"?date={date}&p={page}&limit={page_size}"
    )


def _semantic_scholar_route(*, offset: int, page_size: int, query: str) -> str:
    return str(
        httpx.URL(
            "https://api.semanticscholar.org/graph/v1/paper/search",
            params={
                "query": query,
                "publicationDateOrYear": "2024-01-01:2024-01-08",
                "offset": str(offset),
                "limit": str(page_size),
                "fields": (
                    "paperId,title,abstract,authors,publicationDate,url,"
                    "externalIds,openAccessPdf"
                ),
            },
        )
    )


def _dblp_route(*, offset: int, page_size: int, query: str) -> str:
    return str(
        httpx.URL(
            "https://dblp.org/search/publ/api",
            params={
                "q": query,
                "f": str(offset),
                "h": str(page_size),
                "format": "json",
            },
        )
    )


@pytest.fixture
def arxiv_config() -> AdapterConfig:
    return AdapterConfig(
        name="arxiv",
        lookback_days=7,
        page_size=2,
        max_pages=10,
        max_results=10,
        filters={"search_query": "cat:cs.CL"},
    )


@pytest.fixture
def arxiv_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    arxiv_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _arxiv_route(
                start=0,
                page_size=arxiv_config.page_size,
                search_query="cat%3Acs.CL",
            ): {
                "fixture": "adapters/arxiv/page.xml",
            },
            _arxiv_route(
                start=2,
                page_size=arxiv_config.page_size,
                search_query="cat%3Acs.CL",
            ): {
                "fixture": "adapters/arxiv/page-2.xml",
            },
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def arxiv_malformed_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    arxiv_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _arxiv_route(
                start=0,
                page_size=arxiv_config.page_size,
                search_query="cat%3Acs.CL",
            ): {
                "fixture": "adapters/arxiv/page-malformed-record.xml",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def arxiv_invalid_xml_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    arxiv_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _arxiv_route(
                start=0,
                page_size=arxiv_config.page_size,
                search_query="cat%3Acs.CL",
            ): {
                "fixture": "adapters/arxiv/page-invalid.xml",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def arxiv_out_of_window_only_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    arxiv_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _arxiv_route(
                start=0,
                page_size=arxiv_config.page_size,
                search_query="cat%3Acs.CL",
            ): {
                "fixture": "adapters/arxiv/page-out-of-window-only.xml",
            },
            _arxiv_route(
                start=1,
                page_size=arxiv_config.page_size,
                search_query="cat%3Acs.CL",
            ): {
                "fixture": "adapters/arxiv/page-2.xml",
            },
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def arxiv_malformed_only_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    arxiv_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _arxiv_route(
                start=0,
                page_size=arxiv_config.page_size,
                search_query="cat%3Acs.CL",
            ): {
                "fixture": "adapters/arxiv/page-malformed-only.xml",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def huggingface_config() -> AdapterConfig:
    return AdapterConfig(
        name="huggingface",
        lookback_days=7,
        page_size=2,
        max_pages=10,
        max_results=10,
        filters={},
    )


@pytest.fixture
def huggingface_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    huggingface_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _huggingface_route(
                page=0,
                page_size=huggingface_config.page_size,
                date="2024-01-07",
            ): {
                "fixture": "adapters/huggingface/page.json",
            },
            _huggingface_route(
                page=1,
                page_size=huggingface_config.page_size,
                date="2024-01-07",
            ): {
                "fixture": "adapters/huggingface/page-2.json",
            },
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def huggingface_malformed_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    huggingface_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _huggingface_route(
                page=0,
                page_size=huggingface_config.page_size,
                date="2024-01-07",
            ): {
                "fixture": "adapters/huggingface/page-malformed-record.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def huggingface_invalid_json_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    huggingface_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _huggingface_route(
                page=0,
                page_size=huggingface_config.page_size,
                date="2024-01-07",
            ): {
                "fixture": "adapters/huggingface/page-invalid.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def huggingface_out_of_window_only_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    huggingface_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _huggingface_route(
                page=0,
                page_size=huggingface_config.page_size,
                date="2024-01-07",
            ): {
                "fixture": "adapters/huggingface/page-out-of-window-only.json",
            },
            _huggingface_route(
                page=1,
                page_size=huggingface_config.page_size,
                date="2024-01-07",
            ): {
                "fixture": "adapters/huggingface/page-2.json",
            },
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def huggingface_malformed_only_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    huggingface_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _huggingface_route(
                page=0,
                page_size=huggingface_config.page_size,
                date="2024-01-07",
            ): {
                "fixture": "adapters/huggingface/page-malformed-only.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def semantic_scholar_config() -> AdapterConfig:
    return AdapterConfig(
        name="semantic_scholar",
        secret_env="SEMANTIC_SCHOLAR_API_KEY",
        lookback_days=7,
        page_size=1,
        max_pages=10,
        max_results=10,
        filters={"query": "speech recognition"},
    )


@pytest.fixture
def semantic_scholar_client(
    fetch_config: FetchConfig,
    semantic_scholar_config: AdapterConfig,
) -> RecordedRequestClient:
    return _recording_request_client(
        config=fetch_config,
        routes={
            _semantic_scholar_route(
                offset=0,
                page_size=semantic_scholar_config.page_size,
                query="speech recognition",
            ): {
                "fixture": "adapters/semantic_scholar/page.json",
            },
            _semantic_scholar_route(
                offset=1,
                page_size=semantic_scholar_config.page_size,
                query="speech recognition",
            ): {
                "fixture": "adapters/semantic_scholar/page-2.json",
            },
        },
    )


@pytest.fixture
def semantic_scholar_malformed_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    semantic_scholar_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _semantic_scholar_route(
                offset=0,
                page_size=semantic_scholar_config.page_size,
                query="speech recognition",
            ): {
                "fixture": "adapters/semantic_scholar/page-malformed-record.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def semantic_scholar_invalid_json_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    semantic_scholar_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _semantic_scholar_route(
                offset=0,
                page_size=semantic_scholar_config.page_size,
                query="speech recognition",
            ): {
                "fixture": "adapters/semantic_scholar/page-invalid.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def semantic_scholar_invalid_payload_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    semantic_scholar_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _semantic_scholar_route(
                offset=0,
                page_size=semantic_scholar_config.page_size,
                query="speech recognition",
            ): {
                "fixture": "adapters/semantic_scholar/page-invalid-payload.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def semantic_scholar_auth_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    semantic_scholar_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _semantic_scholar_route(
                offset=0,
                page_size=semantic_scholar_config.page_size,
                query="speech recognition",
            ): {
                "fixture": "adapters/semantic_scholar/page.json",
                "status_code": 401,
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def semantic_scholar_out_of_window_only_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    semantic_scholar_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _semantic_scholar_route(
                offset=0,
                page_size=semantic_scholar_config.page_size,
                query="speech recognition",
            ): {
                "fixture": "adapters/semantic_scholar/page-out-of-window-only.json",
            },
            _semantic_scholar_route(
                offset=1,
                page_size=semantic_scholar_config.page_size,
                query="speech recognition",
            ): {
                "fixture": "adapters/semantic_scholar/page-2.json",
            },
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def semantic_scholar_malformed_only_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    semantic_scholar_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _semantic_scholar_route(
                offset=0,
                page_size=semantic_scholar_config.page_size,
                query="speech recognition",
            ): {
                "fixture": "adapters/semantic_scholar/page-malformed-only.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def semantic_scholar_sparse_next_client(
    fetch_config: FetchConfig,
    semantic_scholar_config: AdapterConfig,
) -> RecordedRequestClient:
    return _recording_request_client(
        config=fetch_config,
        routes={
            _semantic_scholar_route(
                offset=0,
                page_size=semantic_scholar_config.page_size,
                query="speech recognition",
            ): {
                "fixture": "adapters/semantic_scholar/page-sparse-next.json",
            },
            _semantic_scholar_route(
                offset=100,
                page_size=semantic_scholar_config.page_size,
                query="speech recognition",
            ): {
                "fixture": "adapters/semantic_scholar/page-2.json",
            },
        },
    )


@pytest.fixture
def dblp_config() -> AdapterConfig:
    return AdapterConfig(
        name="dblp",
        lookback_days=7,
        page_size=1,
        max_pages=10,
        max_results=10,
        filters={"query": "speech recognition"},
    )


@pytest.fixture
def dblp_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    dblp_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _dblp_route(
                offset=0, page_size=dblp_config.page_size, query="speech recognition"
            ): {
                "fixture": "adapters/dblp/page.json",
            },
            _dblp_route(
                offset=1, page_size=dblp_config.page_size, query="speech recognition"
            ): {
                "fixture": "adapters/dblp/page-2.json",
            },
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def dblp_malformed_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    dblp_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _dblp_route(
                offset=0, page_size=dblp_config.page_size, query="speech recognition"
            ): {
                "fixture": "adapters/dblp/page-malformed-record.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def dblp_invalid_json_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    dblp_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _dblp_route(
                offset=0, page_size=dblp_config.page_size, query="speech recognition"
            ): {
                "fixture": "adapters/dblp/page-invalid.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def dblp_invalid_payload_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    dblp_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _dblp_route(
                offset=0, page_size=dblp_config.page_size, query="speech recognition"
            ): {
                "fixture": "adapters/dblp/page-invalid-payload.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def dblp_out_of_window_only_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    dblp_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _dblp_route(
                offset=0, page_size=dblp_config.page_size, query="speech recognition"
            ): {
                "fixture": "adapters/dblp/page-out-of-window-only.json",
            },
            _dblp_route(
                offset=1, page_size=dblp_config.page_size, query="speech recognition"
            ): {
                "fixture": "adapters/dblp/page-2.json",
            },
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def dblp_malformed_only_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    dblp_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _dblp_route(
                offset=0, page_size=dblp_config.page_size, query="speech recognition"
            ): {
                "fixture": "adapters/dblp/page-malformed-only.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


def _load_recorded_route(
    spec: RecordedRoute,
) -> tuple[int, dict[str, str], str | bytes, Literal["text", "bytes"]]:
    fixture_path = (FIXTURES / spec["fixture"]).resolve()
    fixtures_root = FIXTURES.resolve()
    try:
        fixture_path.relative_to(fixtures_root)
    except ValueError as error:
        raise ValueError(
            f"fixture path escapes test fixtures: {spec['fixture']}"
        ) from error
    if not fixture_path.is_file():
        raise FileNotFoundError(f"missing recorded fixture: {spec['fixture']}")

    status_code = spec.get("status_code", 200)
    headers = dict(spec.get("headers", {}))
    mode = spec.get("mode", "text")
    if mode == "text":
        return (
            status_code,
            headers,
            fixture_path.read_text(encoding=spec.get("encoding", "utf-8")),
            mode,
        )
    return status_code, headers, fixture_path.read_bytes(), mode


def _biorxiv_route(*, start_date: str, end_date: str, offset: int) -> str:
    return f"https://api.biorxiv.org/details/biorxiv/{start_date}/{end_date}/{offset}"


def _crossref_route(
    *, start_date: str, end_date: str, page_size: int, cursor: str
) -> str:
    return str(
        httpx.URL(
            "https://api.crossref.org/works",
            params={
                "filter": f"from-pub-date:{start_date},until-pub-date:{end_date}",
                "rows": str(page_size),
                "cursor": cursor,
            },
        )
    )


def _papers_with_code_route(*, page_size: int, page: int | None = None) -> str:
    base_url = httpx.URL(
        "https://paperswithcode.com/api/v1/papers/"
        if page is None
        else f"https://paperswithcode.com/api/v1/papers/?page={page}"
    )
    return str(
        base_url.copy_with(
            query=str(
                httpx.QueryParams(
                    {
                        **({"page": str(page)} if page is not None else {}),
                        "items_per_page": str(page_size),
                    }
                )
            ).encode()
        )
    )


@pytest.fixture
def biorxiv_config() -> AdapterConfig:
    return AdapterConfig(
        name="biorxiv_crossref",
        lookback_days=7,
        page_size=1,
        max_pages=10,
        max_results=10,
        filters={"provider": "biorxiv"},
    )


@pytest.fixture
def biorxiv_client(
    fetch_config: FetchConfig,
    biorxiv_config: AdapterConfig,
) -> RecordedRequestClient:
    return _recording_request_client(
        config=fetch_config,
        routes={
            _biorxiv_route(start_date="2024-01-01", end_date="2024-01-08", offset=0): {
                "fixture": "adapters/biorxiv_crossref/biorxiv.json",
            },
            _biorxiv_route(start_date="2024-01-01", end_date="2024-01-08", offset=1): {
                "fixture": "adapters/biorxiv_crossref/biorxiv-page-2.json",
            },
        },
    )


@pytest.fixture
def biorxiv_malformed_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    biorxiv_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _biorxiv_route(start_date="2024-01-01", end_date="2024-01-08", offset=0): {
                "fixture": "adapters/biorxiv_crossref/biorxiv-malformed-record.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def biorxiv_invalid_json_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    biorxiv_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _biorxiv_route(start_date="2024-01-01", end_date="2024-01-08", offset=0): {
                "fixture": "adapters/biorxiv_crossref/biorxiv-invalid.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def biorxiv_out_of_window_only_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    biorxiv_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _biorxiv_route(start_date="2024-01-01", end_date="2024-01-08", offset=0): {
                "fixture": "adapters/biorxiv_crossref/biorxiv-out-of-window-only.json",
            },
            _biorxiv_route(start_date="2024-01-01", end_date="2024-01-08", offset=1): {
                "fixture": "adapters/biorxiv_crossref/biorxiv-page-2.json",
            },
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def crossref_config() -> AdapterConfig:
    return AdapterConfig(
        name="biorxiv_crossref",
        lookback_days=7,
        page_size=1,
        max_pages=10,
        max_results=10,
        filters={"provider": "crossref"},
    )


@pytest.fixture
def crossref_client(
    fetch_config: FetchConfig,
    crossref_config: AdapterConfig,
) -> RecordedRequestClient:
    return _recording_request_client(
        config=fetch_config,
        routes={
            _crossref_route(
                start_date="2024-01-01",
                end_date="2024-01-08",
                page_size=crossref_config.page_size,
                cursor="*",
            ): {
                "fixture": "adapters/biorxiv_crossref/crossref.json",
            },
            _crossref_route(
                start_date="2024-01-01",
                end_date="2024-01-08",
                page_size=crossref_config.page_size,
                cursor="cursor-2",
            ): {
                "fixture": "adapters/biorxiv_crossref/crossref-page-2.json",
            },
        },
    )


@pytest.fixture
def crossref_malformed_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    crossref_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _crossref_route(
                start_date="2024-01-01",
                end_date="2024-01-08",
                page_size=crossref_config.page_size,
                cursor="*",
            ): {
                "fixture": "adapters/biorxiv_crossref/crossref-malformed-record.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def crossref_invalid_json_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    crossref_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _crossref_route(
                start_date="2024-01-01",
                end_date="2024-01-08",
                page_size=crossref_config.page_size,
                cursor="*",
            ): {
                "fixture": "adapters/biorxiv_crossref/crossref-invalid.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def crossref_invalid_payload_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    crossref_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _crossref_route(
                start_date="2024-01-01",
                end_date="2024-01-08",
                page_size=crossref_config.page_size,
                cursor="*",
            ): {
                "fixture": "adapters/biorxiv_crossref/crossref-invalid-payload.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def crossref_malformed_only_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    crossref_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _crossref_route(
                start_date="2024-01-01",
                end_date="2024-01-08",
                page_size=crossref_config.page_size,
                cursor="*",
            ): {
                "fixture": "adapters/biorxiv_crossref/crossref-malformed-only.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def crossref_last_missing_next_cursor_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    crossref_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _crossref_route(
                start_date="2024-01-01",
                end_date="2024-01-08",
                page_size=crossref_config.page_size,
                cursor="*",
            ): {
                "fixture": "adapters/biorxiv_crossref/crossref-last-missing-next-cursor.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def crossref_last_blank_next_cursor_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    crossref_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _crossref_route(
                start_date="2024-01-01",
                end_date="2024-01-08",
                page_size=crossref_config.page_size,
                cursor="*",
            ): {
                "fixture": "adapters/biorxiv_crossref/crossref-last-blank-next-cursor.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def crossref_last_local_truncation_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _crossref_route(
                start_date="2024-01-01",
                end_date="2024-01-08",
                page_size=2,
                cursor="*",
            ): {
                "fixture": "adapters/biorxiv_crossref/crossref-last-local-truncation.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def papers_with_code_config() -> AdapterConfig:
    return AdapterConfig(
        name="papers_with_code",
        lookback_days=7,
        page_size=1,
        max_pages=10,
        max_results=10,
        filters={},
    )


@pytest.fixture
def papers_with_code_client(
    fetch_config: FetchConfig,
    papers_with_code_config: AdapterConfig,
) -> RecordedRequestClient:
    return _recording_request_client(
        config=fetch_config,
        routes={
            _papers_with_code_route(page_size=papers_with_code_config.page_size): {
                "fixture": "adapters/papers_with_code/page.json",
            },
            _papers_with_code_route(
                page_size=papers_with_code_config.page_size, page=2
            ): {
                "fixture": "adapters/papers_with_code/page-2.json",
            },
        },
    )


@pytest.fixture
def papers_with_code_malformed_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    papers_with_code_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _papers_with_code_route(page_size=papers_with_code_config.page_size): {
                "fixture": "adapters/papers_with_code/page-malformed-record.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def papers_with_code_invalid_json_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    papers_with_code_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _papers_with_code_route(page_size=papers_with_code_config.page_size): {
                "fixture": "adapters/papers_with_code/page-invalid.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def papers_with_code_invalid_payload_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    papers_with_code_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _papers_with_code_route(page_size=papers_with_code_config.page_size): {
                "fixture": "adapters/papers_with_code/page-invalid-payload.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def papers_with_code_auth_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    papers_with_code_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _papers_with_code_route(page_size=papers_with_code_config.page_size): {
                "fixture": "adapters/papers_with_code/page.json",
                "status_code": 403,
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def papers_with_code_out_of_window_only_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    papers_with_code_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _papers_with_code_route(page_size=papers_with_code_config.page_size): {
                "fixture": "adapters/papers_with_code/page-out-of-window-only.json",
            },
            _papers_with_code_route(
                page_size=papers_with_code_config.page_size, page=2
            ): {
                "fixture": "adapters/papers_with_code/page-2.json",
            },
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def papers_with_code_malformed_only_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    papers_with_code_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _papers_with_code_route(page_size=papers_with_code_config.page_size): {
                "fixture": "adapters/papers_with_code/page-malformed-only.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def papers_with_code_untrusted_next_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    papers_with_code_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _papers_with_code_route(page_size=papers_with_code_config.page_size): {
                "fixture": "adapters/papers_with_code/page-untrusted-next.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def papers_with_code_last_null_next_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    papers_with_code_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _papers_with_code_route(page_size=papers_with_code_config.page_size): {
                "fixture": "adapters/papers_with_code/page-last-null-next.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def papers_with_code_last_blank_next_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
    papers_with_code_config: AdapterConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _papers_with_code_route(page_size=papers_with_code_config.page_size): {
                "fixture": "adapters/papers_with_code/page-last-blank-next.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)


@pytest.fixture
def papers_with_code_last_local_truncation_client(
    fixture_transport: FixtureTransport,
    fetch_config: FetchConfig,
) -> RequestClient:
    transport = fixture_transport(
        {
            _papers_with_code_route(page_size=2): {
                "fixture": "adapters/papers_with_code/page-last-local-truncation.json",
            }
        }
    )
    return _request_client(config=fetch_config, transport=transport)
