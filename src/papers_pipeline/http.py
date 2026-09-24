"""Deadline-aware HTTP client with bounded retry behavior."""

import asyncio
import time
from collections.abc import Awaitable, Callable, Mapping
from dataclasses import dataclass
from typing import Self

import httpx

from .config import FetchConfig
from .errors import InfrastructureError

_RETRYABLE_STATUS_CODES = frozenset({408, 429, 500, 502, 503, 504})
_NON_RETRYABLE_REQUEST_ERROR_MESSAGE = "request failed"


@dataclass(frozen=True)
class Deadline:
    """Shared fetch deadline carried across multiple requests."""

    expires_at: float
    clock: Callable[[], float]

    @classmethod
    def start(cls, seconds: float, clock: Callable[[], float] = time.monotonic) -> Self:
        return cls(clock() + seconds, clock)

    def remaining(self) -> float:
        remaining = self.expires_at - self.clock()
        if remaining <= 0:
            raise InfrastructureError("fetch deadline exceeded")
        return remaining


class RequestClient:
    """Thin retrying HTTP client that respects a shared total deadline."""

    def __init__(
        self,
        config: FetchConfig,
        deadline: Deadline,
        transport: httpx.AsyncBaseTransport | None = None,
        sleep: Callable[[float], Awaitable[None]] = asyncio.sleep,
    ) -> None:
        self.config = config
        self.deadline = deadline
        self._client = httpx.AsyncClient(transport=transport)
        self._sleep = sleep
        self.events: list[str] = []

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: object | None,
    ) -> None:
        await self.aclose()

    async def aclose(self) -> None:
        await self._client.aclose()

    async def get_text(
        self, url: str, params: Mapping[str, str], headers: Mapping[str, str]
    ) -> str:
        for attempt in range(self.config.retries + 1):
            timeout = min(
                self.config.request_timeout_seconds,
                self.deadline.remaining(),
            )
            try:
                response = await self._client.get(
                    url,
                    params=params,
                    headers=headers,
                    timeout=timeout,
                )
            except httpx.RequestError as error:
                if self._is_retryable_request_error(error):
                    if attempt == self.config.retries:
                        raise InfrastructureError(
                            f"request retries exhausted: {url}"
                        ) from error
                    self.events.append(
                        f"retry {attempt + 1}: network failure for {url}"
                    )
                else:
                    raise self._request_error_to_infrastructure_error(
                        url, error
                    ) from error
            else:
                if response.status_code in {401, 403}:
                    raise InfrastructureError(f"authentication failed: {url}")
                if 300 <= response.status_code < 400:
                    raise InfrastructureError(
                        f"redirect HTTP {response.status_code}: {url}"
                    )
                if response.status_code in _RETRYABLE_STATUS_CODES:
                    if attempt == self.config.retries:
                        raise InfrastructureError(f"request retries exhausted: {url}")
                    self.events.append(
                        f"retry {attempt + 1}: HTTP {response.status_code} for {url}"
                    )
                elif response.is_error:
                    raise InfrastructureError(
                        f"permanent HTTP {response.status_code}: {url}"
                    )
                else:
                    return str(response.text)

            await self._sleep_with_deadline(url, attempt)

        raise AssertionError("retry loop exhausted without result")

    def _is_retryable_request_error(self, error: httpx.RequestError) -> bool:
        return isinstance(
            error,
            (httpx.TimeoutException, httpx.NetworkError, httpx.ProtocolError),
        )

    def _request_error_to_infrastructure_error(
        self, url: str, error: httpx.RequestError
    ) -> InfrastructureError:
        if isinstance(error, httpx.TooManyRedirects):
            return InfrastructureError(f"too many redirects: {url}")
        return InfrastructureError(f"{_NON_RETRYABLE_REQUEST_ERROR_MESSAGE}: {url}")

    async def _sleep_with_deadline(self, url: str, attempt: int) -> None:
        delay = self.config.backoff_seconds * (2**attempt)
        if delay <= 0:
            return

        remaining = self.deadline.remaining()
        if delay >= remaining:
            raise InfrastructureError("fetch deadline exceeded")

        await self._sleep(delay)
