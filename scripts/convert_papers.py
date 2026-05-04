"""Convert all papers in papers.csv to markdown.

Usage:
    uv run python scripts/convert_papers.py
    uv run python scripts/convert_papers.py --only 2008.10010
    uv run python scripts/convert_papers.py --skip-llm
"""
from __future__ import annotations

import argparse
import csv
import logging
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PAPERS_CSV = REPO_ROOT / "papers.csv"
PAPERS_DIR = REPO_ROOT / "papers"
CACHE_DIR = REPO_ROOT / ".cache"

LLM_REMEDIATION_MAX_PAPERS = int(os.environ.get("LLM_REMEDIATION_MAX_PAPERS", "50"))
LLM_REMEDIATION_DRY_RUN = os.environ.get("LLM_REMEDIATION_DRY_RUN", "false").lower() == "true"
MAX_WORKERS = 8

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


@dataclass
class PaperRow:
    """A single row from papers.csv, normalized."""

    arxiv_id: str
    title: str
    authors: list[str]
    submitted: str
    categories: list[str]
    url: str
    abstract: str

    @property
    def year(self) -> str:
        return self.submitted[:4]


def main() -> None:
    args = parse_args()
    rows = load_papers_csv(PAPERS_CSV)
    logging.info("Loaded %d papers from %s", len(rows), PAPERS_CSV)

    if args.only:
        rows = [r for r in rows if r.arxiv_id == args.only]
        logging.info("Filtered to %d paper(s) matching --only=%s", len(rows), args.only)

    pending = [r for r in rows if needs_conversion(r, PAPERS_DIR)]
    logging.info("%d papers need conversion", len(pending))

    # Stage 1+2 (per-paper, parallel).
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(_process_paper, row): row for row in pending}
        for fut in as_completed(futures):
            row = futures[fut]
            try:
                fut.result()
            except Exception as exc:  # noqa: BLE001
                logging.exception("Failed to process %s: %s", row.arxiv_id, exc)

    # Stage 4: indexes (always regenerate; cheap).
    _regenerate_indexes(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convert papers in papers.csv to markdown.")
    parser.add_argument("--only", default=None, help="Only process this arxiv_id.")
    parser.add_argument("--skip-llm", action="store_true", help="Skip Stage 2.5 remediation.")
    return parser.parse_args()


def load_papers_csv(path: Path) -> list[PaperRow]:
    """Read papers.csv into a list of PaperRow."""
    rows: list[PaperRow] = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(PaperRow(
                arxiv_id=row["arxiv_id"],
                title=row["title"],
                authors=[a.strip() for a in row.get("authors", "").split(",") if a.strip()],
                submitted=row.get("submitted", ""),
                categories=[c for c in row.get("categories", "").split() if c],
                url=row.get("url", ""),
                abstract=row.get("abstract", ""),
            ))
    return rows


def needs_conversion(row: PaperRow, papers_dir: Path) -> bool:
    """True if this paper has no markdown file yet."""
    target = papers_dir / row.year / f"{row.arxiv_id}.md"
    return not target.exists()


def _process_paper(row: PaperRow) -> None:
    """Stub — wired up in Task 16."""
    logging.info("Would process %s", row.arxiv_id)


def _regenerate_indexes(rows: list[PaperRow]) -> None:
    """Stub — wired up in Task 17."""
    logging.info("Would regenerate indexes for %d papers", len(rows))


if __name__ == "__main__":
    main()
