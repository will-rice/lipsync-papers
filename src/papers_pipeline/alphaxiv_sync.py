"""Keep an alphaXiv collection in step with the repository inventory.

Every inventory paper is saved to the collection, and every paper that was
once in the inventory but has since been dropped (by a narrower topic rule,
say) is removed from it. Papers added to the collection by hand, which were
never in the inventory, are left alone.
"""

import asyncio
import csv
import itertools
import json
import logging
import os
import re
import subprocess
from pathlib import Path
from typing import Any

import httpx2
from mcp import Client
from mcp.client.streamable_http import streamable_http_client

INVENTORY = Path("papers.csv")
MCP_URL = "https://api.alphaxiv.org/mcp/v1"
# Matches the MCP SDK's own client defaults; httpx2 alone times out after 5s.
MCP_TIMEOUT = httpx2.Timeout(30.0, read=300.0)
# save_papers_to_folder and remove_papers_from_folder accept at most 50 papers
# per call.
BATCH_SIZE = 50


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
    """Save the inventory to the named folder and remove dropped papers.

    Both tools are idempotent, so the whole inventory and every dropped paper
    are sent on every run; nothing needs to remember what earlier runs did.
    """
    identifiers = read_arxiv_ids(inventory)
    dropped = dropped_arxiv_ids(inventory, identifiers)
    folder = await find_folder(client, collection)
    for tool, papers in (
        ("save_papers_to_folder", identifiers),
        ("remove_papers_from_folder", dropped),
    ):
        for batch in itertools.batched(papers, BATCH_SIZE):
            await call_tool(
                client,
                tool,
                {"folder_id": folder["folder_id"], "paper_ids_or_urls": list(batch)},
            )
    logging.info(
        "Saved %d papers to and removed %d dropped papers from alphaXiv folder %r",
        len(identifiers),
        len(dropped),
        collection,
    )


def read_arxiv_ids(path: Path) -> list[str]:
    """Return unique versionless arXiv IDs from the inventory, in order."""
    with path.open(newline="", encoding="utf-8") as inventory_file:
        identifiers = (
            re.sub(r"v\d+$", "", row["arxiv_id"])
            for row in csv.DictReader(inventory_file)
            if row["arxiv_id"]
        )
        return list(dict.fromkeys(identifiers))


def dropped_arxiv_ids(inventory: Path, current: list[str]) -> list[str]:
    """Return arXiv IDs that left the inventory, from its git history.

    Inventory rows are single lines, so every row ever removed from the file
    appears as a removed line in its history. Papers still in the inventory
    (a new version, an edited title) are not dropped.

    Args:
        inventory: The inventory file, inside a git checkout with full history.
        current: Versionless arXiv IDs in the current inventory.

    Returns:
        Versionless arXiv IDs no longer in the inventory, sorted.
    """
    history = subprocess.run(
        ["git", "log", "--format=", "--patch", "--unified=0", "--", inventory.name],
        cwd=inventory.parent,
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    with inventory.open(newline="", encoding="utf-8") as inventory_file:
        column = next(csv.reader(inventory_file)).index("arxiv_id")
    removed_rows = csv.reader(
        line[1:]
        for line in history.splitlines()
        if line.startswith("-") and not line.startswith("---")
    )
    removed = {
        re.sub(r"v\d+$", "", row[column])
        for row in removed_rows
        if len(row) > column and row[column] and row[column] != "arxiv_id"
    }
    return sorted(removed - set(current))


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
