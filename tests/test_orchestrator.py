"""Tests for scripts/convert_papers.py orchestration."""
from __future__ import annotations

import csv
from pathlib import Path

from scripts.convert_papers import (
    PaperRow,
    load_papers_csv,
    needs_conversion,
)


def _write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["arxiv_id", "title", "authors", "submitted",
                                          "categories", "url", "abstract"])
        w.writeheader()
        w.writerows(rows)


def test_load_papers_csv(tmp_path: Path) -> None:
    csv_path = tmp_path / "papers.csv"
    _write_csv(csv_path, [{
        "arxiv_id": "2008.10010",
        "title": "Wav2Lip",
        "authors": "K. R. Prajwal, et al.",
        "submitted": "2020-08-23",
        "categories": "cs.CV",
        "url": "https://arxiv.org/abs/2008.10010",
        "abstract": "abstract",
    }])
    rows = load_papers_csv(csv_path)
    assert len(rows) == 1
    assert isinstance(rows[0], PaperRow)
    assert rows[0].arxiv_id == "2008.10010"
    assert rows[0].year == "2020"


def test_needs_conversion_when_missing(tmp_papers_dir: Path) -> None:
    row = PaperRow(arxiv_id="2008.10010", title="Wav2Lip", authors=["A"],
                   submitted="2020-08-23", categories=[], url="…", abstract="…")
    assert needs_conversion(row, tmp_papers_dir) is True


def test_needs_conversion_when_present(tmp_papers_dir: Path) -> None:
    row = PaperRow(arxiv_id="2008.10010", title="Wav2Lip", authors=["A"],
                   submitted="2020-08-23", categories=[], url="…", abstract="…")
    target = tmp_papers_dir / "2020" / "2008.10010.md"
    target.parent.mkdir(parents=True)
    target.write_text("---\nllm_remediated: false\n---\n\nbody\n")
    assert needs_conversion(row, tmp_papers_dir) is False
