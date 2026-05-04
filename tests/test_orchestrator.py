"""Tests for scripts/convert_papers.py orchestration."""

from __future__ import annotations

import csv
import shutil
from pathlib import Path

import pytest

from scripts.convert_papers import (
    PaperRow,
    load_papers_csv,
    needs_conversion,
)


def _write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "arxiv_id",
                "title",
                "authors",
                "submitted",
                "categories",
                "url",
                "abstract",
            ],
        )
        w.writeheader()
        w.writerows(rows)


def test_load_papers_csv(tmp_path: Path) -> None:
    csv_path = tmp_path / "papers.csv"
    _write_csv(
        csv_path,
        [
            {
                "arxiv_id": "2008.10010",
                "title": "Wav2Lip",
                "authors": "K. R. Prajwal, et al.",
                "submitted": "2020-08-23",
                "categories": "cs.CV",
                "url": "https://arxiv.org/abs/2008.10010",
                "abstract": "abstract",
            }
        ],
    )
    rows = load_papers_csv(csv_path)
    assert len(rows) == 1
    assert isinstance(rows[0], PaperRow)
    assert rows[0].arxiv_id == "2008.10010"
    assert rows[0].year == "2020"


def test_needs_conversion_when_missing(tmp_papers_dir: Path) -> None:
    row = PaperRow(
        arxiv_id="2008.10010",
        title="Wav2Lip",
        authors=["A"],
        submitted="2020-08-23",
        categories=[],
        url="…",
        abstract="…",
    )
    assert needs_conversion(row, tmp_papers_dir) is True


def test_needs_conversion_when_present(tmp_papers_dir: Path) -> None:
    row = PaperRow(
        arxiv_id="2008.10010",
        title="Wav2Lip",
        authors=["A"],
        submitted="2020-08-23",
        categories=[],
        url="…",
        abstract="…",
    )
    target = tmp_papers_dir / "2020" / "2008.10010.md"
    target.parent.mkdir(parents=True)
    target.write_text("---\nllm_remediated: false\n---\n\nbody\n")
    assert needs_conversion(row, tmp_papers_dir) is False


@pytest.mark.slow
@pytest.mark.skipif(shutil.which("pandoc") is None, reason="pandoc not installed")
def test_process_paper_end_to_end_latex(monkeypatch, tmp_path, fixtures_dir):
    """End-to-end: pre-seed cache with the fixture tarball, run process, assert MD exists."""
    from scripts import convert_papers

    cache_root = tmp_path / ".cache" / "source"
    papers_root = tmp_path / "papers"
    cache_root.mkdir(parents=True)

    # Seed the cache so Stage 1 short-circuits.
    paper_cache = cache_root / "2008.10010"
    paper_cache.mkdir()
    src_tar = paper_cache / "source.tar.gz"
    shutil.copy(fixtures_dir / "sources_2008.10010.tar.gz", src_tar)

    monkeypatch.setattr(convert_papers, "PAPERS_DIR", papers_root)
    monkeypatch.setattr(convert_papers, "CACHE_DIR", tmp_path / ".cache")

    row = convert_papers.PaperRow(
        arxiv_id="2008.10010",
        title="Wav2Lip",
        authors=["K. R. Prajwal"],
        submitted="2020-08-23",
        categories=["cs.CV"],
        url="https://arxiv.org/abs/2008.10010",
        abstract="abstract",
    )
    convert_papers._process_paper(row)
    assert (papers_root / "2020" / "2008.10010.md").exists()


def test_regenerate_indexes_creates_top_and_year_files(monkeypatch, tmp_path):
    from scripts import convert_papers

    monkeypatch.setattr(convert_papers, "PAPERS_DIR", tmp_path / "papers")

    rows = [
        convert_papers.PaperRow(
            arxiv_id="2008.10010",
            title="Wav2Lip",
            authors=["A"],
            submitted="2020-08-23",
            categories=["cs.CV"],
            url="…",
            abstract="…",
        ),
        convert_papers.PaperRow(
            arxiv_id="2604.23586",
            title="Talker",
            authors=["B"],
            submitted="2026-04-26",
            categories=["cs.CV"],
            url="…",
            abstract="…",
        ),
    ]
    # Pre-create the per-paper MD files so per-year index has something to point at.
    for r in rows:
        p = tmp_path / "papers" / r.year / f"{r.arxiv_id}.md"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("body")

    convert_papers._regenerate_indexes(rows)
    assert (tmp_path / "papers" / "README.md").exists()
    assert (tmp_path / "papers" / "2020" / "README.md").exists()
    assert (tmp_path / "papers" / "2026" / "README.md").exists()


def test_llm_remediation_dry_run_logs_without_api(monkeypatch, tmp_path, caplog):
    from scripts import convert_papers

    monkeypatch.setattr(convert_papers, "PAPERS_DIR", tmp_path / "papers")
    monkeypatch.setattr(convert_papers, "CACHE_DIR", tmp_path / ".cache")
    monkeypatch.setattr(convert_papers, "LLM_REMEDIATION_DRY_RUN", True)
    monkeypatch.setattr(convert_papers, "LLM_REMEDIATION_MAX_PAPERS", 50)

    # Pre-create a paper file with low citation resolution to trigger flagger.
    p = tmp_path / "papers" / "2020" / "2008.10010.md"
    p.parent.mkdir(parents=True)
    p.write_text(
        "---\n"
        "arxiv_id: 2008.10010\n"
        "submitted: 2020-08-23\n"
        "source: pdf\n"
        "converter: marker\n"
        "llm_remediated: false\n"
        "citations_resolved: 1/30\n"
        "references_parsed: 30\n"
        "---\n\nshort body\n"
    )
    pdf_path = tmp_path / ".cache" / "source" / "2008.10010" / "paper.pdf"
    pdf_path.parent.mkdir(parents=True)
    pdf_path.write_bytes(b"%PDF-1.7\n")

    rows = [
        convert_papers.PaperRow(
            arxiv_id="2008.10010",
            title="Wav2Lip",
            authors=["A"],
            submitted="2020-08-23",
            categories=[],
            url="…",
            abstract="…",
        )
    ]
    with caplog.at_level("INFO"):
        convert_papers._run_remediation_pass(rows)
    assert any("would remediate 2008.10010" in m.lower() for m in caplog.text.splitlines())


@pytest.mark.slow
@pytest.mark.skipif(shutil.which("pandoc") is None, reason="pandoc not installed")
def test_second_run_is_idempotent(monkeypatch, tmp_path, fixtures_dir):
    """After one full process_paper run, a second run for the same paper should write nothing new."""
    import time

    from scripts import convert_papers

    cache_root = tmp_path / ".cache" / "source"
    papers_root = tmp_path / "papers"
    cache_root.mkdir(parents=True)
    paper_cache = cache_root / "2008.10010"
    paper_cache.mkdir()
    shutil.copy(fixtures_dir / "sources_2008.10010.tar.gz", paper_cache / "source.tar.gz")

    monkeypatch.setattr(convert_papers, "PAPERS_DIR", papers_root)
    monkeypatch.setattr(convert_papers, "CACHE_DIR", tmp_path / ".cache")

    row = convert_papers.PaperRow(
        arxiv_id="2008.10010",
        title="Wav2Lip",
        authors=["A"],
        submitted="2020-08-23",
        categories=["cs.CV"],
        url="https://arxiv.org/abs/2008.10010",
        abstract="abstract",
    )
    convert_papers._process_paper(row)
    time.sleep(0.05)

    # needs_conversion should now return False
    assert convert_papers.needs_conversion(row, papers_root) is False
