"""Tests for scripts/_convert/output.py."""

from __future__ import annotations

from pathlib import Path

import yaml

from scripts._convert.output import PaperRecord, write_paper_markdown


def test_writes_to_year_subdir(tmp_papers_dir: Path) -> None:
    record = PaperRecord(
        arxiv_id="2008.10010",
        title="A Lip Sync Expert",
        authors=["K. R. Prajwal"],
        submitted="2020-08-23",
        categories=["cs.CV"],
        arxiv_url="https://arxiv.org/abs/2008.10010",
        source="latex",
        converter="pandoc",
        body="# Wav2Lip\n\nBody text.",
        references_parsed=42,
        citations_resolved=("40/42"),
        arxiv_version="v1",
    )
    path = write_paper_markdown(record, tmp_papers_dir)
    assert path == tmp_papers_dir / "2020" / "2008.10010.md"
    assert path.exists()


def test_frontmatter_is_valid_yaml(tmp_papers_dir: Path) -> None:
    record = PaperRecord(
        arxiv_id="2008.10010",
        title="A Lip Sync Expert",
        authors=["K. R. Prajwal", "Rudrabha Mukhopadhyay"],
        submitted="2020-08-23",
        categories=["cs.CV"],
        arxiv_url="https://arxiv.org/abs/2008.10010",
        source="latex",
        converter="pandoc",
        body="# Wav2Lip\n\nBody.",
        references_parsed=42,
        citations_resolved="40/42",
        arxiv_version="v1",
    )
    path = write_paper_markdown(record, tmp_papers_dir)
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n")
    front_end = text.index("\n---\n", 4)
    front = yaml.safe_load(text[4:front_end])
    assert front["arxiv_id"] == "2008.10010"
    assert front["authors"] == ["K. R. Prajwal", "Rudrabha Mukhopadhyay"]
    assert front["llm_remediated"] is False
    assert "citations_resolved_at" in front
