import httpx
import pytest

from conftest import FixtureTransport


@pytest.mark.asyncio
async def test_fixture_transport_returns_recorded_response_and_rejects_unknown_urls(
    fixture_transport: FixtureTransport,
) -> None:
    transport = fixture_transport(
        {
            "https://example.test/papers": {
                "fixture": "http/recorded-paper.txt",
                "headers": {"content-type": "text/plain; charset=utf-8"},
                "mode": "text",
            },
            "https://example.test/papers.bin": {
                "fixture": "http/recorded-paper.txt",
                "mode": "bytes",
            },
        }
    )

    async with httpx.AsyncClient(transport=transport) as client:
        text_response = await client.get("https://example.test/papers")
        bytes_response = await client.get("https://example.test/papers.bin")

        with pytest.raises(
            AssertionError,
            match="unexpected recorded fixture URL: GET https://example.test/other",
        ):
            await client.get("https://example.test/other")

    assert text_response.status_code == 200
    assert text_response.text == "café\n"
    assert bytes_response.status_code == 200
    assert bytes_response.content == "café\n".encode("utf-8")
