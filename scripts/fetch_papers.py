"""Fetch lipsync-related papers from multiple academic sources.

This script queries arXiv, Semantic Scholar, and Papers With Code for papers
related to lipsync, talking-head synthesis, and related topics.  It is designed
to be run in two modes:

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
"""

from __future__ import annotations

import argparse
import csv
import json
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

CSV_FIELDNAMES = ["arxiv_id", "title", "authors", "submitted", "categories", "url", "abstract"]

# Negative keywords – papers whose title or abstract contain any of these
# phrases (case-insensitive) are excluded from results.
NEGATIVE_KEYWORDS = [
    "speech recognition",
    # Power / electrical engineering
    "power synchronization",
    "grid-forming",
    "electric load",
    # Aerospace / mechanical
    "spacecraft",
    "tractor engine",
    # Cryptography / security (non-face)
    "audio encryption",
    "audio steganography",
    # Operations research / scheduling
    "job-shop scheduling",
    # Mechanical engineering
    "mechanical system",
    # Textiles / materials
    "warp-knitted",
    # Wireless communications & signal processing
    "integrated sensing and communication",
    "rate-splitting",
    "reconfigurable intelligent surface",
    "spread spectrum",
    "spectrum access",
    "radiation field reconstruction",
    "wireless human gesture",
    "programmable data-plane",
    # Positioning / localization (non-face)
    "indoor positioning",
    "near-field positioning",
    "human-drone",
    # Knowledge graphs
    "temporal knowledge graph",
    # Audio-visual tasks unrelated to lipsync
    "event localization",
    "audio backdoor",
    "forensic speaker",
    "intrusion detection",
    # Mathematics / physics / chemistry
    "nanostructure",
    "quantum neural",
    "pde solver",
    "printed memristor",
    "sonar",
    # Medical / clinical (matched via "lip" or "head" search terms)
    "cleft lip",
    "rhinoplasty",
    "head and neck cancer",
    "alveolar bone",
    "lip balm",
    "lip-ms",
    "transcranial",
    "alzheimer",
    "polycystic ovary",
    "diabetes mellitus",
    "perinatal",
    "dentofacial",
    "stuttering",
    "oral health",
    # Chemistry / materials science
    "face-to-face stacking",
    # Social science / humanities / business
    "talking therapies",
    "talking therapy",
    "autocratic leadership",
    "cloud cost",
    "professional wrestling",
    "respondent-driven",
    "partisan",
    "macaque",
    "ai companion chatbot",
    # Data analytics (non-face speech interfaces)
    "immersive analytics",
    # Accessibility (non-lipsync)
    "audio description text",
]

# Delay between API requests to respect arXiv's rate-limit guidance (3 s).
API_DELAY_SECONDS = 3

# Number of results to fetch per API page.
PAGE_SIZE = 100

# Maximum pages to fetch per keyword from each external source.
MAX_PAGES_PER_QUERY = 5

# Maximum length for Papers With Code paper IDs used as fallback identifiers.
MAX_PWC_ID_LENGTH = 80

# Semantic Scholar API base URL
SEMANTIC_SCHOLAR_API_BASE = "https://api.semanticscholar.org/graph/v1/paper/search"

# Papers With Code API base URL
PAPERS_WITH_CODE_API_BASE = "https://paperswithcode.com/api/v1/papers/"


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

    return {
        "arxiv_id": arxiv_id,
        "title": title,
        "authors": authors,
        "submitted": submitted,
        "categories": categories,
        "url": url,
        "abstract": abstract,
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
# Semantic Scholar helpers
# ---------------------------------------------------------------------------

_S2_FIELDS = "paperId,title,authors,year,externalIds,abstract,publicationDate"


def _fetch_s2_page(keywords: str, year_filter: str, offset: int) -> dict:
    """Fetch one page of Semantic Scholar results and return the parsed JSON."""
    params = urllib.parse.urlencode(
        {
            "query": keywords,
            "fields": _S2_FIELDS,
            "year": year_filter,
            "offset": offset,
            "limit": PAGE_SIZE,
        }
    )
    url = f"{SEMANTIC_SCHOLAR_API_BASE}?{params}"
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "lipsync-papers-bot/1.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read())
        except Exception as exc:  # noqa: BLE001
            wait = min(2 ** attempt * API_DELAY_SECONDS, 30)
            print(f"  [warn] S2 request failed ({exc}); retrying in {wait}s …", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"Failed to fetch Semantic Scholar page after 5 attempts: {url}")


def _parse_s2_entry(item: dict, start_date: date, end_date: date) -> dict | None:
    """Parse a Semantic Scholar paper item into our paper dict format."""
    title = re.sub(r"\s+", " ", (item.get("title") or "")).strip()
    if not title:
        return None

    # Filter by publicationDate when available; fall back to year.
    pub_date_str = (item.get("publicationDate") or "")[:10]
    submitted = ""
    if pub_date_str:
        try:
            pub_date = date.fromisoformat(pub_date_str)
            if pub_date < start_date or pub_date > end_date:
                return None
            submitted = pub_date_str
        except ValueError:
            pass
    if not submitted:
        year = item.get("year")
        if not year:
            return None
        submitted = f"{year}-01-01"

    external_ids = item.get("externalIds") or {}
    arxiv_id = (external_ids.get("ArXiv") or "").strip()
    s2_id = (item.get("paperId") or "").strip()

    if arxiv_id:
        paper_id = arxiv_id
        url = f"https://arxiv.org/abs/{arxiv_id}"
    elif s2_id:
        paper_id = f"s2:{s2_id}"
        url = f"https://www.semanticscholar.org/paper/{s2_id}"
    else:
        return None

    authors = ", ".join(
        (a.get("name") or "").strip()
        for a in (item.get("authors") or [])
    )
    abstract = re.sub(r"\s+", " ", (item.get("abstract") or "")).strip()

    return {
        "arxiv_id": paper_id,
        "title": title,
        "authors": authors,
        "submitted": submitted,
        "categories": "",
        "url": url,
        "abstract": abstract,
    }


def fetch_semantic_scholar_papers(keywords: str, start_date: date, end_date: date) -> list[dict]:
    """Return papers from Semantic Scholar matching *keywords* in [start_date, end_date]."""
    start_year = start_date.year
    end_year = end_date.year
    year_filter = f"{start_year}-{end_year}" if start_year != end_year else str(start_year)

    papers: list[dict] = []
    offset = 0

    for _ in range(MAX_PAGES_PER_QUERY):
        try:
            data = _fetch_s2_page(keywords, year_filter, offset)
        except RuntimeError as exc:
            print(f"  [error] {exc}", file=sys.stderr)
            break

        items = data.get("data") or []
        if not items:
            break

        for item in items:
            paper = _parse_s2_entry(item, start_date, end_date)
            if paper:
                papers.append(paper)

        if len(items) < PAGE_SIZE or not data.get("next"):
            break

        offset += len(items)
        time.sleep(API_DELAY_SECONDS)

    return papers


# ---------------------------------------------------------------------------
# Papers With Code helpers
# ---------------------------------------------------------------------------


def _fetch_pwc_page(keywords: str, page: int) -> dict:
    """Fetch one page of Papers With Code results and return the parsed JSON."""
    params = urllib.parse.urlencode(
        {
            "q": keywords,
            "items_per_page": PAGE_SIZE,
            "page": page,
        }
    )
    url = f"{PAPERS_WITH_CODE_API_BASE}?{params}"
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "lipsync-papers-bot/1.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read())
        except Exception as exc:  # noqa: BLE001
            wait = min(2 ** attempt * API_DELAY_SECONDS, 30)
            print(f"  [warn] PWC request failed ({exc}); retrying in {wait}s …", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"Failed to fetch Papers With Code page after 5 attempts: {url}")


def _parse_pwc_entry(item: dict, start_date: date, end_date: date) -> dict | None:
    """Parse a Papers With Code paper item into our paper dict format."""
    title = re.sub(r"\s+", " ", (item.get("title") or "")).strip()
    if not title:
        return None

    pub_date_str = (item.get("published") or "")[:10]
    if not pub_date_str:
        return None
    try:
        pub_date = date.fromisoformat(pub_date_str)
    except ValueError:
        return None
    if pub_date < start_date or pub_date > end_date:
        return None

    arxiv_id = (item.get("arxiv_id") or "").strip()
    if arxiv_id:
        paper_id = arxiv_id
        url = item.get("url_abs") or f"https://arxiv.org/abs/{arxiv_id}"
    else:
        url = (item.get("url_abs") or "").strip()
        if not url:
            return None
        pwc_id = (item.get("id") or title)[:MAX_PWC_ID_LENGTH]
        paper_id = f"pwc:{pwc_id}"

    authors_raw = item.get("authors") or []
    authors = ", ".join(str(a).strip() for a in authors_raw if a)
    abstract = re.sub(r"\s+", " ", (item.get("abstract") or "")).strip()

    return {
        "arxiv_id": paper_id,
        "title": title,
        "authors": authors,
        "submitted": pub_date_str,
        "categories": "",
        "url": url,
        "abstract": abstract,
    }


def fetch_pwc_papers(keywords: str, start_date: date, end_date: date) -> list[dict]:
    """Return papers from Papers With Code matching *keywords* in [start_date, end_date]."""
    papers: list[dict] = []

    for page in range(1, MAX_PAGES_PER_QUERY + 1):
        try:
            data = _fetch_pwc_page(keywords, page)
        except RuntimeError as exc:
            print(f"  [error] {exc}", file=sys.stderr)
            break

        items = data.get("results") or []
        if not items:
            break

        for item in items:
            paper = _parse_pwc_entry(item, start_date, end_date)
            if paper:
                papers.append(paper)

        if not data.get("next"):
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
        return {row["arxiv_id"]: row for row in reader}


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
            title = row["title"]
            url = row["url"]

            section_lines.append(f"#### [{title}]({url})")
            section_lines.append(f"**{authors}** · {date_str}")
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


def _collect_from_source(
    source_name: str,
    fetch_fn,
    keywords_list: list[str],
    start_date: date,
    end_date: date,
    existing: dict[str, dict],
) -> int:
    """Query *fetch_fn* for each keyword and merge results into *existing*."""
    new_count = 0
    for keywords in keywords_list:
        print(f"\nQuerying {source_name} for: {keywords!r} …")
        try:
            papers = fetch_fn(keywords, start_date, end_date)
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

    return new_count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch lipsync papers from arXiv, Semantic Scholar, and Papers With Code."
    )
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
    new_count += _collect_from_source("arXiv", fetch_papers, SEARCH_QUERIES, start_date, end_date, existing)
    new_count += _collect_from_source(
        "Semantic Scholar", fetch_semantic_scholar_papers, SEARCH_QUERIES, start_date, end_date, existing
    )
    new_count += _collect_from_source(
        "Papers With Code", fetch_pwc_papers, SEARCH_QUERIES, start_date, end_date, existing
    )

    print(f"\nFound {new_count} new papers. Total: {len(existing)}.")

    if new_count > 0 or removed > 0 or not PAPERS_CSV.exists():
        save_papers(existing)
        print(f"Saved to {PAPERS_CSV}.")

    update_readme(existing)


if __name__ == "__main__":
    main()
