import asyncio
import http.client
import ipaddress
import socket
import ssl
from dataclasses import dataclass
from typing import Protocol, cast
from urllib.parse import SplitResult, urljoin, urlsplit

from papers_pipeline.errors import InfrastructureError, PaperError

MAX_REDIRECTS = 5


@dataclass(frozen=True)
class HttpResponse:
    status_code: int
    content: bytes
    location: str | None = None


class Resolver(Protocol):
    async def resolve(self, host: str, port: int) -> tuple[str, ...]: ...


class Connector(Protocol):
    async def get(
        self,
        *,
        scheme: str,
        address: str,
        port: int,
        target: str,
        host_header: str,
        tls_server_name: str | None,
        timeout: float,
    ) -> HttpResponse: ...


class SystemResolver:
    async def resolve(self, host: str, port: int) -> tuple[str, ...]:
        def resolve_sync() -> tuple[str, ...]:
            records = socket.getaddrinfo(
                host,
                port,
                type=socket.SOCK_STREAM,
                proto=socket.IPPROTO_TCP,
            )
            return tuple(dict.fromkeys(cast(str, record[4][0]) for record in records))

        return await asyncio.to_thread(resolve_sync)


class PinnedHttpConnector:
    async def get(
        self,
        *,
        scheme: str,
        address: str,
        port: int,
        target: str,
        host_header: str,
        tls_server_name: str | None,
        timeout: float,
    ) -> HttpResponse:
        return await asyncio.to_thread(
            self._get_sync,
            scheme=scheme,
            address=address,
            port=port,
            target=target,
            host_header=host_header,
            tls_server_name=tls_server_name,
            timeout=timeout,
        )

    @staticmethod
    def _get_sync(
        *,
        scheme: str,
        address: str,
        port: int,
        target: str,
        host_header: str,
        tls_server_name: str | None,
        timeout: float,
    ) -> HttpResponse:
        connection: http.client.HTTPConnection
        if scheme == "https":
            if tls_server_name is None:
                raise ValueError("HTTPS requests require a TLS server name")
            connection = _PinnedHTTPSConnection(
                address,
                port,
                timeout,
                tls_server_name=tls_server_name,
            )
        else:
            connection = _PinnedHTTPConnection(address, port, timeout)
        try:
            connection.request(
                "GET",
                target,
                headers={
                    "Accept": "*/*",
                    "Connection": "close",
                    "Host": host_header,
                    "User-Agent": "papers-pipeline/1",
                },
            )
            response = connection.getresponse()
            return HttpResponse(
                response.status, response.read(), response.getheader("Location")
            )
        finally:
            connection.close()


class _PinnedHTTPConnection(http.client.HTTPConnection):
    def connect(self) -> None:
        self.sock = socket.create_connection((self.host, self.port), self.timeout)


class _PinnedHTTPSConnection(http.client.HTTPSConnection):
    def __init__(
        self,
        address: str,
        port: int,
        timeout: float,
        *,
        tls_server_name: str,
    ) -> None:
        context = ssl.create_default_context()
        super().__init__(address, port, timeout=timeout, context=context)
        self._tls_context = context
        self._tls_server_name = tls_server_name

    def connect(self) -> None:
        sock = socket.create_connection((self.host, self.port), self.timeout)
        self.sock = self._tls_context.wrap_socket(
            sock,
            server_hostname=self._tls_server_name,
        )


class RemoteDownloader:
    def __init__(
        self,
        *,
        resolver: Resolver | None = None,
        connector: Connector | None = None,
    ) -> None:
        self._resolver = resolver or SystemResolver()
        self._connector = connector or PinnedHttpConnector()

    async def download(self, url: str, timeout: float) -> bytes:
        for _ in range(MAX_REDIRECTS + 1):
            response = await self._get(url, timeout)
            if not 300 <= response.status_code < 400:
                return _classify_response(response, url)
            if response.location is None:
                raise PaperError(f"conversion input redirect without location: {url}")
            # Every hop goes through _get, so redirects are held to the same
            # origin and public-address checks as the original URL.
            url = urljoin(url, response.location)
        raise PaperError(f"conversion input exceeded {MAX_REDIRECTS} redirects: {url}")

    async def _get(self, url: str, timeout: float) -> HttpResponse:
        parts = urlsplit(url)
        host, port = _validate_origin(parts, url)
        try:
            addresses = _literal_or_resolved(host)
            if addresses is None:
                addresses = await self._resolver.resolve(host, port)
        except (OSError, ValueError) as error:
            raise InfrastructureError(
                f"conversion input resolution failed: {url}"
            ) from error

        validated = _validate_addresses(addresses, url)
        # Stable preference avoids DNS-order-dependent behavior.
        address = sorted(validated, key=lambda item: (item.version, item.packed))[0]
        host_header = _host_header(host, port, parts.scheme)
        target = parts.path or "/"
        if parts.query:
            target = f"{target}?{parts.query}"
        try:
            return await self._connector.get(
                scheme=parts.scheme,
                address=str(address),
                port=port,
                target=target,
                host_header=host_header,
                tls_server_name=host if parts.scheme == "https" else None,
                timeout=timeout,
            )
        except (OSError, http.client.HTTPException) as error:
            raise InfrastructureError(
                f"conversion input network failure: {url}"
            ) from error


def _validate_origin(parts: SplitResult, url: str) -> tuple[str, int]:
    if parts.scheme not in {"http", "https"}:
        raise PaperError(f"unsupported conversion input URL: {url}")
    if parts.username is not None or parts.password is not None:
        raise PaperError(f"conversion input URL credentials are forbidden: {url}")
    host = parts.hostname
    if not host:
        raise PaperError(f"invalid conversion input URL: {url}")
    normalized_host = host.rstrip(".").casefold()
    if normalized_host == "localhost" or normalized_host.endswith(".localhost"):
        raise PaperError(f"localhost conversion input URL is forbidden: {url}")
    try:
        port = parts.port or (443 if parts.scheme == "https" else 80)
    except ValueError as error:
        raise PaperError(f"invalid conversion input URL: {url}") from error
    return normalized_host, port


def _literal_or_resolved(
    host: str,
) -> tuple[str, ...] | None:
    try:
        return (str(ipaddress.ip_address(host)),)
    except ValueError:
        return None


def _validate_addresses(
    addresses: tuple[str, ...], url: str
) -> tuple[ipaddress.IPv4Address | ipaddress.IPv6Address, ...]:
    if not addresses:
        raise InfrastructureError(
            f"conversion input resolution returned no addresses: {url}"
        )
    try:
        parsed = tuple(ipaddress.ip_address(address) for address in addresses)
    except ValueError as error:
        raise InfrastructureError(
            f"conversion input resolution returned an invalid address: {url}"
        ) from error
    if any(
        not address.is_global
        or address.is_loopback
        or address.is_private
        or address.is_link_local
        or address.is_multicast
        or address.is_reserved
        or address.is_unspecified
        for address in parsed
    ):
        raise PaperError(f"conversion input resolved to non-public address: {url}")
    return parsed


def _host_header(host: str, port: int, scheme: str) -> str:
    display_host = f"[{host}]" if ":" in host else host
    default_port = 443 if scheme == "https" else 80
    return display_host if port == default_port else f"{display_host}:{port}"


def _classify_response(response: HttpResponse, url: str) -> bytes:
    status = response.status_code
    # A host refusing or rate-limiting one paper (paywall, bot check, 429) fails
    # that paper; failures are counted per paper and reset on success, so a
    # transient block costs one attempt instead of stalling every run.
    if status == 408:
        raise InfrastructureError(f"conversion input HTTP 408: {url}")
    if 400 <= status < 500:
        raise PaperError(f"conversion input HTTP {status}: {url}")
    if status >= 400:
        raise InfrastructureError(f"conversion input HTTP {status}: {url}")
    return response.content
