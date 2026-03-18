"""Fetch lipsync-related papers from the arXiv API.

This script queries the arXiv API for papers related to lipsync, talking-head
synthesis, and related topics.  It is designed to be run in two modes:

* **Historical (first run)**: pulls everything submitted since wav2lip
  (2020-01-01 onwards).
* **Incremental (scheduled)**: pulls only papers submitted in the last N days
  (default 8, so a weekly cron with a one-day overlap never misses anything).

Results are written to ``papers.csv`` in the repository root and the
``README.md`` table is regenerated from that file.

Usage::

    # Full historical fetch (first-run / back-fill):
    python scripts/fetch_papers.py --full

    # Incremental fetch (last 8 days, for weekly cron):
    python scripts/fetch_papers.py

    # Incremental fetch for the last N days:
    python scripts/fetch_papers.py --days 30

    # Back-fill author keywords for all existing papers that are missing them:
    python scripts/fetch_papers.py --backfill-keywords
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
PAPERS_CSV = REPO_ROOT / "papers.csv"
README_MD = REPO_ROOT / "README.md"

# arXiv API base URL
ARXIV_API_BASE = "http://export.arxiv.org/api/query"

# Search queries – cast a wide net over lipsync and related topics.
SEARCH_QUERIES = [
    "lip sync",
    "lip synchronization",
    "wav2lip",
    "talking head",
    "talking face",
    "audio-driven face",
    "speech-driven face",
    "audio visual speech",
    "face reenactment",
    "neural dubbing",
]

# Earliest date to consider (wav2lip: ACM MM 2020, submitted April 2020).
HISTORY_START = date(2020, 1, 1)

# arXiv namespaces
NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}

CSV_FIELDNAMES = ["arxiv_id", "title", "authors", "submitted", "categories", "url", "abstract", "keywords"]

# Negative keywords – papers whose title or abstract contain any of these
# phrases (case-insensitive) are excluded from results.
NEGATIVE_KEYWORDS = [
    "speech recognition",
]

# Delay between API requests to respect arXiv's rate-limit guidance (3 s).
API_DELAY_SECONDS = 3

# Number of results to fetch per API page.
PAGE_SIZE = 100


# ---------------------------------------------------------------------------
# arXiv helpers
# ---------------------------------------------------------------------------


def _build_query(keywords: str, start_date: date, end_date: date) -> str:
    """Return a URL-encoded arXiv API query string."""
    # Date range filter: submittedDate:[YYYYMMDD TO YYYYMMDD]
    date_filter = (
        f"submittedDate:[{start_date.strftime('%Y%m%d')}0000"
        f" TO {end_date.strftime('%Y%m%d')}2359]"
    )
    # Title + abstract search
    term = f'(ti:"{keywords}" OR abs:"{keywords}") AND {date_filter}'
    return term


def _fetch_page(query: str, start: int, max_results: int) -> ET.Element:
    """Fetch one page of arXiv results and return the parsed XML root."""
    params = urllib.parse.urlencode(
        {
            "search_query": query,
            "start": start,
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
    )
    url = f"{ARXIV_API_BASE}?{params}"
    for attempt in range(5):
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                data = resp.read()
            return ET.fromstring(data)
        except Exception as exc:  # noqa: BLE001
            wait = min(2 ** attempt * API_DELAY_SECONDS, 30)
            print(f"  [warn] request failed ({exc}); retrying in {wait}s …", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"Failed to fetch arXiv page after 5 attempts: {url}")


_KEYWORDS_PATTERN = re.compile(
    # Match "Keywords:" / "Key Words:" / "keyword:" at a word boundary,
    # capture everything up to either a sentence boundary (". " followed by
    # an uppercase letter, signalling the next sentence) or end-of-string.
    r"(?:^|\b)[Kk]ey\s*[Ww]ords?\s*[:\-–]\s*(.+?)(?:\.\s*(?=[A-Z])|$)",
    re.DOTALL,
)


def _extract_keywords(text: str) -> str:
    """Extract a 'Keywords: ...' block from *text*, returning a normalised,
    semicolon-separated string, or an empty string if nothing is found."""
    if not text:
        return ""
    m = _KEYWORDS_PATTERN.search(text)
    if not m:
        return ""
    raw = re.sub(r"\s+", " ", m.group(1)).strip().rstrip(".")
    # Normalise separators to "; " for consistent display
    raw = re.sub(r"\s*[,;]\s*", "; ", raw)
    return raw


def _parse_entry(entry: ET.Element) -> dict | None:
    """Parse a single <entry> element into a paper dict."""
    arxiv_id_raw = entry.findtext("atom:id", namespaces=NS) or ""
    # e.g. http://arxiv.org/abs/2008.10010v1 → 2008.10010
    arxiv_id = re.sub(r"v\d+$", "", arxiv_id_raw.split("/abs/")[-1]).strip()
    if not arxiv_id:
        return None

    title = re.sub(r"\s+", " ", entry.findtext("atom:title", namespaces=NS) or "").strip()

    authors = ", ".join(
        (a.findtext("atom:name", namespaces=NS) or "").strip()
        for a in entry.findall("atom:author", namespaces=NS)
    )

    published_raw = entry.findtext("atom:published", namespaces=NS) or ""
    submitted = published_raw[:10]  # YYYY-MM-DD

    categories = " ".join(
        cat.get("term", "")
        for cat in entry.findall("atom:category", namespaces=NS)
    )

    url = f"https://arxiv.org/abs/{arxiv_id}"

    abstract = re.sub(
        r"\s+",
        " ",
        entry.findtext("atom:summary", namespaces=NS) or "",
    ).strip()

    # Extract author-provided keywords from the arXiv comment field first,
    # then fall back to scanning the abstract for a "Keywords: ..." line.
    comment = re.sub(
        r"\s+",
        " ",
        entry.findtext("arxiv:comment", namespaces=NS) or "",
    ).strip()
    keywords = _extract_keywords(comment) or _extract_keywords(abstract)

    return {
        "arxiv_id": arxiv_id,
        "title": title,
        "authors": authors,
        "submitted": submitted,
        "categories": categories,
        "url": url,
        "abstract": abstract,
        "keywords": keywords,
    }


_NEGATIVE_KEYWORDS_LOWER = [kw.lower() for kw in NEGATIVE_KEYWORDS]


def _is_excluded(paper: dict) -> bool:
    """Return True if the paper matches any negative keyword."""
    haystack = f"{paper.get('title', '')} {paper.get('abstract', '')}".lower()
    return any(kw in haystack for kw in _NEGATIVE_KEYWORDS_LOWER)


def fetch_papers(keywords: str, start_date: date, end_date: date) -> list[dict]:
    """Return all papers matching *keywords* within [start_date, end_date]."""
    query = _build_query(keywords, start_date, end_date)
    papers: list[dict] = []
    start = 0

    while True:
        root = _fetch_page(query, start=start, max_results=PAGE_SIZE)

        total_el = root.find("opensearch:totalResults", {"opensearch": "http://a9.com/-/spec/opensearch/1.1/"})
        total = int(total_el.text) if total_el is not None and total_el.text else 0

        entries = root.findall("atom:entry", namespaces=NS)
        if not entries:
            break

        for entry in entries:
            paper = _parse_entry(entry)
            if paper:
                papers.append(paper)

        start += len(entries)
        if start >= total or len(entries) < PAGE_SIZE:
            break

        time.sleep(API_DELAY_SECONDS)

    return papers


# ---------------------------------------------------------------------------
# CSV helpers
# ---------------------------------------------------------------------------


def load_existing_papers() -> dict[str, dict]:
    """Load papers from CSV, keyed by arxiv_id."""
    if not PAPERS_CSV.exists():
        return {}
    with PAPERS_CSV.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = {}
        for row in reader:
            # Ensure the keywords field is present even in older CSV files
            row.setdefault("keywords", "")
            rows[row["arxiv_id"]] = row
        return rows


def fetch_keywords_for_paper(arxiv_id: str) -> str:
    """Fetch the arXiv API entry for a single paper and extract keywords.

    Returns the extracted keyword string (may be empty).
    """
    url = f"{ARXIV_API_BASE}?id_list={urllib.parse.quote(arxiv_id)}&max_results=1"
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                data = resp.read()
            root = ET.fromstring(data)
            entry = root.find("atom:entry", namespaces=NS)
            if entry is None:
                return ""
            comment = re.sub(
                r"\s+",
                " ",
                entry.findtext("arxiv:comment", namespaces=NS) or "",
            ).strip()
            abstract = re.sub(
                r"\s+",
                " ",
                entry.findtext("atom:summary", namespaces=NS) or "",
            ).strip()
            return _extract_keywords(comment) or _extract_keywords(abstract)
        except Exception as exc:  # noqa: BLE001
            wait = min(2 ** attempt * API_DELAY_SECONDS, 30)
            print(f"  [warn] keyword fetch failed ({exc}); retrying in {wait}s …", file=sys.stderr)
            time.sleep(wait)
    return ""


def save_papers(papers_by_id: dict[str, dict]) -> None:
    """Write all papers to CSV sorted by submitted date (newest first)."""
    rows = sorted(papers_by_id.values(), key=lambda r: r.get("submitted", ""), reverse=True)
    with PAPERS_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDNAMES, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


# ---------------------------------------------------------------------------
# README helpers
# ---------------------------------------------------------------------------

_TABLE_START = "<!-- PAPERS_TABLE_START -->"
_TABLE_END = "<!-- PAPERS_TABLE_END -->"


def _build_table(papers_by_id: dict[str, dict]) -> str:
    rows = sorted(papers_by_id.values(), key=lambda r: r.get("submitted", ""), reverse=True)

    # Group by year (newest first).
    by_year: dict[str, list] = defaultdict(list)
    for row in rows:
        year = row.get("submitted", "")[:4] or "Unknown"
        by_year[year].append(row)

    sections: list[str] = []
    for year in sorted(by_year.keys(), reverse=True):
        section_lines = [f"### {year}", ""]
        for row in by_year[year]:
            # Truncate long author lists for readability
            authors = row.get("authors", "")
            if authors.count(",") >= 4:
                authors = ", ".join(authors.split(", ")[:4]) + " et al."
            date_str = row.get("submitted", "")[:10]
            abstract = row.get("abstract", "").strip()
            keywords = row.get("keywords", "").strip()
            title = row["title"]
            url = row["url"]

            section_lines.append(f"#### [{title}]({url})")
            section_lines.append(f"**{authors}** · {date_str}")
            section_lines.append("")
            if keywords:
                section_lines.append(f"**Keywords:** {keywords}")
                section_lines.append("")
            if abstract:
                section_lines.append("<details>")
                section_lines.append("<summary>Abstract</summary>")
                section_lines.append("")
                section_lines.append(abstract)
                section_lines.append("")
                section_lines.append("</details>")
                section_lines.append("")
            else:
                section_lines.append("")

        sections.append("\n".join(section_lines))

    return "\n\n".join(sections)


def update_readme(papers_by_id: dict[str, dict]) -> None:
    """Regenerate the paper table in README.md."""
    if not README_MD.exists():
        return

    content = README_MD.read_text(encoding="utf-8")
    table = _build_table(papers_by_id)
    new_section = f"{_TABLE_START}\n{table}\n{_TABLE_END}"

    if _TABLE_START in content:
        # Replace existing table
        pattern = re.compile(
            re.escape(_TABLE_START) + r".*?" + re.escape(_TABLE_END),
            re.DOTALL,
        )
        content = pattern.sub(lambda _: new_section, content)
    else:
        # Append after the first paragraph
        content = content.rstrip() + "\n\n" + new_section + "\n"

    README_MD.write_text(content, encoding="utf-8")
    print(f"README updated with {len(papers_by_id)} papers.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch lipsync papers from arXiv.")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--full",
        action="store_true",
        help=f"Fetch all papers since {HISTORY_START} (historical back-fill).",
    )
    mode.add_argument(
        "--days",
        type=int,
        default=8,
        metavar="N",
        help="Fetch papers from the last N days (default: 8, for weekly cron).",
    )
    parser.add_argument(
        "--backfill-keywords",
        action="store_true",
        help="Fetch missing keywords for all existing papers that lack them.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    today = datetime.now(tz=timezone.utc).date()

    if args.full:
        start_date = HISTORY_START
        end_date = today
        print(f"Full historical fetch: {start_date} → {end_date}")
    else:
        start_date = today - timedelta(days=args.days)
        end_date = today
        print(f"Incremental fetch (last {args.days} days): {start_date} → {end_date}")

    existing = load_existing_papers()
    print(f"Loaded {len(existing)} existing papers from {PAPERS_CSV.name}.")

    # Remove any previously saved papers that match negative keywords.
    before = len(existing)
    existing = {pid: p for pid, p in existing.items() if not _is_excluded(p)}
    removed = before - len(existing)
    if removed:
        print(f"Removed {removed} existing paper(s) matching negative keywords.")

    new_count = 0
    for keywords in SEARCH_QUERIES:
        print(f"\nQuerying arXiv for: {keywords!r} …")
        try:
            papers = fetch_papers(keywords, start_date, end_date)
        except RuntimeError as exc:
            print(f"  [error] {exc}", file=sys.stderr)
            continue

        for paper in papers:
            pid = paper["arxiv_id"]
            if pid not in existing and not _is_excluded(paper):
                existing[pid] = paper
                new_count += 1
                print(f"  + {pid}: {paper['title'][:70]}")

        time.sleep(API_DELAY_SECONDS)

    print(f"\nFound {new_count} new papers. Total: {len(existing)}.")

    # Backfill keywords for papers that are missing them.  This runs only when
    # --backfill-keywords is explicitly requested to avoid unexpected API calls
    # during normal incremental/full fetches.
    kw_filled = 0
    if args.backfill_keywords:
        missing_kw = [pid for pid, p in existing.items() if not p.get("keywords", "").strip()]
        if missing_kw:
            print(f"\nBackfilling keywords for {len(missing_kw)} paper(s) …")
            for pid in missing_kw:
                kw = fetch_keywords_for_paper(pid)
                if kw:
                    existing[pid]["keywords"] = kw
                    kw_filled += 1
                    print(f"  keywords for {pid}: {kw[:80]}")
                time.sleep(API_DELAY_SECONDS)
            if kw_filled:
                print(f"Filled keywords for {kw_filled} paper(s).")

    if new_count > 0 or removed > 0 or kw_filled > 0 or not PAPERS_CSV.exists():
        save_papers(existing)
        print(f"Saved to {PAPERS_CSV}.")

    update_readme(existing)


if __name__ == "__main__":
    main()
