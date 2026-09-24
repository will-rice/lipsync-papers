from collections.abc import Awaitable, Callable

import httpx
import pytest

from papers_pipeline.config import FetchConfig
from papers_pipeline.errors import InfrastructureError
from papers_pipeline.http import Deadline, RequestClient


class FakeClock:
    def __init__(self, now: float = 0.0) -> None:
        self.now = now
        self.sleeps: list[float] = []

    def __call__(self) -> float:
        return self.now

    async def sleep(self, seconds: float) -> None:
        self.sleeps.append(seconds)
        self.now += seconds


@pytest.fixture
def fake_clock() -> FakeClock:
    return FakeClock()


@pytest.fixture
def fetch_config() -> FetchConfig:
    return FetchConfig(
        request_timeout_seconds=5,
        retries=3,
        backoff_seconds=1,
        total_deadline_seconds=900,
    )


def test_deadline_remaining_raises_once_expired(fake_clock: FakeClock) -> None:
    deadline = Deadline.start(2, fake_clock)
    fake_clock.now = 2

    with pytest.raises(InfrastructureError, match="fetch deadline exceeded"):
        deadline.remaining()


@pytest.mark.asyncio
async def test_request_timeout_is_bounded_by_remaining_deadline(
    fetch_config: FetchConfig, fake_clock: FakeClock
) -> None:
    observed_timeouts: list[dict[str, float]] = []

    def handler(request: httpx.Request) -> httpx.Response:
        timeout = request.extensions["timeout"]
        assert isinstance(timeout, dict)
        observed_timeouts.append(timeout)
        return httpx.Response(200, text="ok")

    client = RequestClient(
        fetch_config.model_copy(update={"request_timeout_seconds": 30}),
        Deadline.start(2.5, fake_clock),
        transport=httpx.MockTransport(handler),
        sleep=fake_clock.sleep,
    )

    assert await client.get_text("https://example.test", {}, {}) == "ok"
    assert observed_timeouts == [
        {"connect": 2.5, "read": 2.5, "write": 2.5, "pool": 2.5}
    ]


@pytest.mark.asyncio
async def test_retry_stops_at_total_deadline(
    fetch_config: FetchConfig, fake_clock: FakeClock
) -> None:
    attempts = 0

    def handler(_: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        return httpx.Response(503)

    deadline = Deadline.start(2, fake_clock)
    client = RequestClient(
        fetch_config,
        deadline,
        transport=httpx.MockTransport(handler),
        sleep=fake_clock.sleep,
    )

    with pytest.raises(InfrastructureError, match="fetch deadline exceeded"):
        await client.get_text("https://example.test", {}, {})

    assert attempts == 2
    assert fake_clock.sleeps == [1.0]
    assert client.events == [
        "retry 1: HTTP 503 for https://example.test",
        "retry 2: HTTP 503 for https://example.test",
    ]


@pytest.mark.asyncio
async def test_retryable_network_failures_back_off_until_exhausted(
    fetch_config: FetchConfig, fake_clock: FakeClock
) -> None:
    attempts = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        raise httpx.ReadTimeout("timed out", request=request)

    client = RequestClient(
        fetch_config,
        Deadline.start(30, fake_clock),
        transport=httpx.MockTransport(handler),
        sleep=fake_clock.sleep,
    )

    with pytest.raises(
        InfrastructureError, match="request retries exhausted: https://example.test"
    ):
        await client.get_text("https://example.test", {}, {})

    assert attempts == 4
    assert fake_clock.sleeps == [1.0, 2.0, 4.0]
    assert client.events == [
        "retry 1: network failure for https://example.test",
        "retry 2: network failure for https://example.test",
        "retry 3: network failure for https://example.test",
    ]


@pytest.mark.asyncio
async def test_retryable_protocol_failures_back_off_until_exhausted(
    fetch_config: FetchConfig, fake_clock: FakeClock
) -> None:
    attempts = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        raise httpx.RemoteProtocolError("bad framing", request=request)

    client = RequestClient(
        fetch_config,
        Deadline.start(30, fake_clock),
        transport=httpx.MockTransport(handler),
        sleep=fake_clock.sleep,
    )

    with pytest.raises(
        InfrastructureError, match="request retries exhausted: https://example.test"
    ):
        await client.get_text("https://example.test", {}, {})

    assert attempts == 4
    assert fake_clock.sleeps == [1.0, 2.0, 4.0]
    assert client.events == [
        "retry 1: network failure for https://example.test",
        "retry 2: network failure for https://example.test",
        "retry 3: network failure for https://example.test",
    ]


@pytest.mark.asyncio
async def test_permanent_401_is_not_retried(
    fetch_config: FetchConfig, fake_clock: FakeClock
) -> None:
    attempts = 0

    def handler(_: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        return httpx.Response(401)

    client = RequestClient(
        fetch_config,
        Deadline.start(30, fake_clock),
        transport=httpx.MockTransport(handler),
        sleep=fake_clock.sleep,
    )

    with pytest.raises(InfrastructureError, match="authentication failed"):
        await client.get_text("https://example.test", {}, {})

    assert attempts == 1
    assert fake_clock.sleeps == []
    assert client.events == []


@pytest.mark.asyncio
async def test_redirect_302_is_not_treated_as_success(
    fetch_config: FetchConfig, fake_clock: FakeClock
) -> None:
    attempts = 0

    def handler(_: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        return httpx.Response(302, text="moved")

    client = RequestClient(
        fetch_config,
        Deadline.start(30, fake_clock),
        transport=httpx.MockTransport(handler),
        sleep=fake_clock.sleep,
    )

    with pytest.raises(
        InfrastructureError, match="redirect HTTP 302: https://example.test"
    ):
        await client.get_text("https://example.test", {}, {})

    assert attempts == 1
    assert fake_clock.sleeps == []
    assert client.events == []


@pytest.mark.asyncio
async def test_too_many_redirects_fails_immediately(
    fetch_config: FetchConfig, fake_clock: FakeClock
) -> None:
    attempts = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        raise httpx.TooManyRedirects("redirect loop", request=request)

    client = RequestClient(
        fetch_config,
        Deadline.start(30, fake_clock),
        transport=httpx.MockTransport(handler),
        sleep=fake_clock.sleep,
    )

    with pytest.raises(
        InfrastructureError, match="too many redirects: https://example.test"
    ):
        await client.get_text("https://example.test", {}, {})

    assert attempts == 1
    assert fake_clock.sleeps == []
    assert client.events == []


@pytest.mark.asyncio
async def test_non_retryable_404_fails_immediately(
    fetch_config: FetchConfig, fake_clock: FakeClock
) -> None:
    attempts = 0

    def handler(_: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        return httpx.Response(404)

    client = RequestClient(
        fetch_config,
        Deadline.start(30, fake_clock),
        transport=httpx.MockTransport(handler),
        sleep=fake_clock.sleep,
    )

    with pytest.raises(
        InfrastructureError, match="permanent HTTP 404: https://example.test"
    ):
        await client.get_text("https://example.test", {}, {})

    assert attempts == 1
    assert fake_clock.sleeps == []
    assert client.events == []


@pytest.mark.asyncio
async def test_request_client_supports_clean_shutdown(
    fetch_config: FetchConfig,
    fake_clock: FakeClock,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    transport = httpx.MockTransport(lambda _: httpx.Response(200, text="ok"))
    closed = False
    original_aclose: Callable[[], Awaitable[None]] = transport.aclose

    async def tracking_aclose() -> None:
        nonlocal closed
        closed = True
        await original_aclose()

    monkeypatch.setattr(transport, "aclose", tracking_aclose)
    client = RequestClient(
        fetch_config,
        Deadline.start(30, fake_clock),
        transport=transport,
        sleep=fake_clock.sleep,
    )

    async with client:
        assert await client.get_text("https://example.test", {}, {}) == "ok"

    assert closed is True
