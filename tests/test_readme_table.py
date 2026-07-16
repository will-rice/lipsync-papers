"""Tests for the README table builder in scripts/fetch_papers.py."""

from __future__ import annotations

from datetime import date, timedelta

from scripts.fetch_papers import README_TABLE_WINDOW_DAYS, _build_table


def _paper(i: int, submitted: str) -> dict:
    return {
        "arxiv_id": f"2401.{i:05d}",
        "title": f"Paper {i}",
        "authors": "A. Author",
        "submitted": submitted,
        "categories": "cs.CV",
        "url": f"https://arxiv.org/abs/2401.{i:05d}",
        "abstract": "An abstract.",
    }


def test_table_shows_only_papers_inside_window() -> None:
    recent = (date.today() - timedelta(days=3)).isoformat()
    old = (date.today() - timedelta(days=README_TABLE_WINDOW_DAYS + 5)).isoformat()
    papers = {p["arxiv_id"]: p for p in [_paper(1, recent), _paper(2, old)]}
    table = _build_table(papers)
    assert table.count("#### [") == 1
    assert "Paper 1" in table
    assert "Paper 2" not in table
    assert f"last {README_TABLE_WINDOW_DAYS} days (1 of 2 papers)" in table
    assert f"<summary><h3>Last {README_TABLE_WINDOW_DAYS} Days</h3></summary>" in table
    assert "papers/README.md" in table
