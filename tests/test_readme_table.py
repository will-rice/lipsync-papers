"""Tests for the README table builder in scripts/fetch_papers.py."""

from __future__ import annotations

from datetime import date, timedelta

from scripts.fetch_papers import README_TABLE_LIMIT, _build_table


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


def test_table_shows_only_recent_papers_up_to_limit() -> None:
    base = date.today()
    # Create more papers than the limit
    papers = {
        p["arxiv_id"]: p
        for p in [_paper(i, (base - timedelta(days=i)).isoformat()) for i in range(1, README_TABLE_LIMIT + 5)]
    }
    table = _build_table(papers)
    assert table.count("#### [") == README_TABLE_LIMIT
    assert f"last {README_TABLE_LIMIT} papers ({README_TABLE_LIMIT} of {README_TABLE_LIMIT + 4} total)" in table
    assert f"<summary><h3>Last {README_TABLE_LIMIT} Papers</h3></summary>" in table
    assert "papers/README.md" in table


def test_table_shows_all_papers_when_below_limit() -> None:
    base = date.today()
    count = README_TABLE_LIMIT - 5
    papers = {
        p["arxiv_id"]: p
        for p in [_paper(i, (base - timedelta(days=i)).isoformat()) for i in range(1, count + 1)]
    }
    table = _build_table(papers)
    assert table.count("#### [") == count
    assert f"last {README_TABLE_LIMIT} papers ({count} of {count} total)" in table
