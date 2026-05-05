"""Tests for scripts/_convert/pdf_to_md.py."""

from __future__ import annotations

from pathlib import Path

import pytest

from scripts._convert.pdf_to_md import PdfConversionResult, convert_pdf_to_md


@pytest.mark.slow
def test_convert_pdf_produces_markdown(fixtures_dir: Path) -> None:
    result = convert_pdf_to_md(fixtures_dir / "pdf_only.pdf")
    assert isinstance(result, PdfConversionResult)
    assert result.body, "expected non-empty body"
    assert result.page_count > 0
