"""Generate the papers/README.md corpus index.

Per-year pages are intentionally not generated: the front README carries a
rolling 30-day window, and full-year browsing is served by GitHub's own file
listing for each ``papers/<year>/`` directory, which the top index links to.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from datetime import date


@dataclass
class IndexEntry:
    arxiv_id: str
    submitted: str  # YYYY-MM-DD


def render_top_index(entries: list[IndexEntry]) -> str:
    """Render papers/README.md: total count plus a link to each year's directory."""
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
        lines.append(f"- [{year}]({year}/) — {len(by_year[year])} papers")
    return "\n".join(lines) + "\n"
