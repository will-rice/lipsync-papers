"""Tests for scripts/_convert/indexes.py."""

from __future__ import annotations


from scripts._convert.indexes import IndexEntry, render_top_index, render_year_index


def _entry(arxiv_id: str, title: str, year: str) -> IndexEntry:
    return IndexEntry(
        arxiv_id=arxiv_id,
        title=title,
        authors=["A. Author", "B. Author", "C. Author", "D. Author", "E. Author"],
        submitted=f"{year}-06-15",
        abstract="An abstract.",
    )


def test_top_index_groups_by_year() -> None:
    entries = [
        _entry("2008.10010", "Wav2Lip", "2020"),
        _entry("2604.23586", "Talker-T2AV", "2026"),
    ]
    md = render_top_index(entries)
    assert "Total papers: 2" in md
    assert "[2020](2020/README.md)" in md
    assert "[2026](2026/README.md)" in md
    assert md.index("2026") < md.index("2020")  # newest first


def test_year_index_lists_papers_with_local_links() -> None:
    entries = [_entry("2008.10010", "Wav2Lip", "2020")]
    md = render_year_index("2020", entries)
    assert "[Wav2Lip](2008.10010.md)" in md
    assert "A. Author, B. Author, C. Author, D. Author et al." in md
    assert "An abstract." in md
