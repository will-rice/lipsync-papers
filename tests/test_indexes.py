"""Tests for scripts/_convert/indexes.py."""

from __future__ import annotations


from scripts._convert.indexes import IndexEntry, render_top_index


def _entry(arxiv_id: str, year: str) -> IndexEntry:
    return IndexEntry(arxiv_id=arxiv_id, submitted=f"{year}-06-15")


def test_top_index_groups_by_year() -> None:
    entries = [
        _entry("2008.10010", "2020"),
        _entry("2604.23586", "2026"),
    ]
    md = render_top_index(entries)
    assert "Total papers: 2" in md
    # Links point at the year directory, not a per-year README.
    assert "[2020](2020/)" in md
    assert "[2026](2026/)" in md
    assert md.index("2026") < md.index("2020")  # newest first
