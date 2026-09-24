"""Add papers from the repository inventory to an alphaXiv collection."""

import asyncio
import csv
import itertools
import json
import logging
import os
import re
from pathlib import Path
from typing import Any

import httpx2
from mcp import Client
from mcp.client.streamable_http import streamable_http_client

INVENTORY = Path("papers.csv")
MCP_URL = "https://api.alphaxiv.org/mcp/v1"
# Matches the MCP SDK's own client defaults; httpx2 alone times out after 5s.
MCP_TIMEOUT = httpx2.Timeout(30.0, read=300.0)
# save_papers_to_folder accepts at most 50 papers per call.
SAVE_BATCH_SIZE = 50


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    api_key = os.environ["ALPHAXIV_API_KEY"]
    collection = os.environ["ALPHAXIV_COLLECTION"]
    # Actions passes unset secrets and variables as empty strings.
    if not api_key or not collection:
        raise ValueError("ALPHAXIV_API_KEY and ALPHAXIV_COLLECTION must be set")
    asyncio.run(sync(INVENTORY, collection, api_key))


async def sync(inventory: Path, collection: str, api_key: str) -> None:
    headers = {"Authorization": f"Bearer {api_key}"}
    async with httpx2.AsyncClient(headers=headers, timeout=MCP_TIMEOUT) as http_client:
        transport = streamable_http_client(MCP_URL, http_client=http_client)
        async with Client(transport) as client:
            await sync_collection(inventory, collection, client)


async def sync_collection(inventory: Path, collection: str, client: Client) -> None:
    """Save every inventory paper to the named folder.

    save_papers_to_folder is idempotent and never removes papers, so the
    whole inventory is sent on every run.
    """
    identifiers = read_arxiv_ids(inventory)
    folder = await find_folder(client, collection)
    for batch in itertools.batched(identifiers, SAVE_BATCH_SIZE):
        await call_tool(
            client,
            "save_papers_to_folder",
            {"folder_id": folder["folder_id"], "paper_ids_or_urls": list(batch)},
        )
    logging.info("Saved %d papers to alphaXiv folder %r", len(identifiers), collection)


def read_arxiv_ids(path: Path) -> list[str]:
    """Return unique versionless arXiv IDs from the inventory, in order."""
    with path.open(newline="", encoding="utf-8") as inventory_file:
        identifiers = (
            re.sub(r"v\d+$", "", row["arxiv_id"])
            for row in csv.DictReader(inventory_file)
            if row["arxiv_id"]
        )
        return list(dict.fromkeys(identifiers))


async def find_folder(client: Client, name: str) -> dict[str, Any]:
    library = await call_tool(client, "list_library", {})
    matches: list[dict[str, Any]] = [
        folder for folder in library["folders"] if folder["name"] == name
    ]
    if len(matches) != 1:
        raise ValueError(
            f"expected one alphaXiv folder named {name!r}, found {len(matches)}"
        )
    return matches[0]


async def call_tool(client: Client, name: str, arguments: dict[str, Any]) -> Any:
    result = await client.call_tool(name, arguments)
    text = "".join(block.text for block in result.content if block.type == "text")
    if result.is_error:
        raise ValueError(f"alphaXiv {name} failed: {text}")
    return json.loads(text)


if __name__ == "__main__":
    main()
