"""Shared pytest fixtures."""

from __future__ import annotations

from pathlib import Path

import pytest

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture
def fixtures_dir() -> Path:
    return FIXTURES


@pytest.fixture
def tmp_papers_dir(tmp_path: Path) -> Path:
    """Empty papers/ directory rooted in a tmp_path."""
    papers = tmp_path / "papers"
    papers.mkdir()
    return papers
