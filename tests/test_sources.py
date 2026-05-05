"""Tests for scripts/_convert/sources.py."""

from __future__ import annotations

from pathlib import Path

from scripts._convert.sources import (
    SourceKind,
    classify_extracted_source,
    extract_arxiv_tarball,
    is_cache_fresh,
)


def test_extract_arxiv_tarball_produces_tex(fixtures_dir: Path, tmp_path: Path) -> None:
    src = fixtures_dir / "sources_2008.10010.tar.gz"
    out = tmp_path / "extracted"
    extract_arxiv_tarball(src, out)
    tex_files = list(out.rglob("*.tex"))
    assert tex_files, "expected at least one .tex file"


def test_classify_extracted_source_latex(fixtures_dir: Path, tmp_path: Path) -> None:
    src = fixtures_dir / "sources_2008.10010.tar.gz"
    out = tmp_path / "extracted"
    extract_arxiv_tarball(src, out)
    assert classify_extracted_source(out) == SourceKind.LATEX


def test_classify_extracted_source_pdf_only(tmp_path: Path) -> None:
    out = tmp_path / "extracted"
    out.mkdir()
    (out / "paper.pdf").write_bytes(b"%PDF-1.7\n%fake")
    assert classify_extracted_source(out) == SourceKind.PDF


def test_is_cache_fresh_recent(tmp_path: Path) -> None:
    p = tmp_path / "x"
    p.mkdir()
    assert is_cache_fresh(p, max_age_days=30) is True


def test_is_cache_fresh_missing(tmp_path: Path) -> None:
    assert is_cache_fresh(tmp_path / "nonexistent", max_age_days=30) is False
