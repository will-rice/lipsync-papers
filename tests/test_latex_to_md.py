"""Tests for scripts/_convert/latex_to_md.py."""
from __future__ import annotations

import shutil
from pathlib import Path

import pytest

from scripts._convert.latex_to_md import (
    LatexConversionResult,
    convert_latex_to_md,
    find_main_tex,
)
from scripts._convert.sources import extract_arxiv_tarball


@pytest.fixture
def extracted_wav2lip(fixtures_dir: Path, tmp_path: Path) -> Path:
    out = tmp_path / "extracted"
    extract_arxiv_tarball(fixtures_dir / "sources_2008.10010.tar.gz", out)
    return out


def test_find_main_tex_returns_largest(extracted_wav2lip: Path) -> None:
    main = find_main_tex(extracted_wav2lip)
    assert main is not None
    assert main.suffix == ".tex"


@pytest.mark.skipif(shutil.which("pandoc") is None, reason="pandoc not installed")
def test_convert_latex_produces_markdown(extracted_wav2lip: Path) -> None:
    result = convert_latex_to_md(extracted_wav2lip)
    assert isinstance(result, LatexConversionResult)
    assert result.body, "expected non-empty body"
    assert result.exit_code == 0
    assert "# " in result.body or "## " in result.body
