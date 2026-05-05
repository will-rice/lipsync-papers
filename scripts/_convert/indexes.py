"""Generate the papers/README.md and per-year README.md index files."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from datetime import date


@dataclass
class IndexEntry:
    arxiv_id: str
    title: str
    authors: list[str]
    submitted: str  # YYYY-MM-DD
    abstract: str


def _truncate_authors(authors: list[str]) -> str:
    if len(authors) > 4:
        return ", ".join(authors[:4]) + " et al."
    return ", ".join(authors)


def render_top_index(entries: list[IndexEntry]) -> str:
    """Render papers/README.md."""
    by_year: dict[str, list[IndexEntry]] = defaultdict(list)
    for e in entries:
        by_year[e.submitted[:4] or "Unknown"].append(e)

    lines = [
        "# Papers — Markdown Corpus",
        "",
        f"Total papers: {len(entries)}",
        "",
        f"_Generated: {date.today().isoformat()}_",
        "",
    ]
    for year in sorted(by_year, reverse=True):
        lines.append(f"- [{year}]({year}/README.md) — {len(by_year[year])} papers")
    return "\n".join(lines) + "\n"


def render_year_index(year: str, entries: list[IndexEntry]) -> str:
    """Render papers/<year>/README.md."""
    sorted_entries = sorted(entries, key=lambda e: e.submitted, reverse=True)
    lines = [
        f"# {year}",
        "",
        f"{len(entries)} papers in this year.",
        "",
    ]
    for e in sorted_entries:
        lines.append(f"### [{e.title}]({e.arxiv_id}.md)")
        lines.append(f"**{_truncate_authors(e.authors)}** · {e.submitted}")
        lines.append("")
        if e.abstract:
            lines.append("<details>")
            lines.append("<summary>Abstract</summary>")
            lines.append("")
            lines.append(e.abstract)
            lines.append("")
            lines.append("</details>")
            lines.append("")
    return "\n".join(lines) + "\n"
