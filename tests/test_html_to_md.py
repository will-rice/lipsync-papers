"""Tests for scripts/_convert/html_to_md.py against a real arXiv HTML page."""

from pathlib import Path

import pytest

from scripts._convert.html_to_md import convert_html_to_md, looks_like_paper

BASE_URL = "https://arxiv.org/html/2508.08468"
FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture(scope="module")
def body() -> str:
    html = (FIXTURES / "arxiv_html_2508.08468.html").read_text(encoding="utf-8")
    result = convert_html_to_md(html, base_url=BASE_URL)
    assert result.exit_code == 0, result.stderr
    return result.body


def test_strips_page_chrome(body: str) -> None:
    assert "arXiv is now an independent nonprofit" not in body
    assert "Report Issue" not in body
    assert "data:image" not in body
    assert 'class="ltx_' not in body


def test_absolutizes_image_urls(body: str) -> None:
    assert "https://arxiv.org/html/2508.08468v6/fig1.png" in body
    assert "](2508.08468v6/" not in body
    assert 'src="2508.08468v6/' not in body


def test_flattens_equation_tables(body: str) -> None:
    assert "``` math" in body, "expected display math in output"
    # Equation 1 of the fixture paper must be a fenced math block, not a layout table.
    assert "y[n]=x[n]+d[n]," in body
    display_math_in_table = [
        line for line in body.splitlines() if line.lstrip().startswith("|") and "$$" in line
    ]
    assert not display_math_in_table, f"display math inside tables: {display_math_in_table[:2]}"


def test_unwraps_internal_anchor_links(body: str) -> None:
    assert "](#" not in body


def test_preserves_paper_structure(body: str) -> None:
    headings = [line for line in body.splitlines() if line.startswith("#")]
    assert len(headings) >= 5
    assert "Abstract" in body
    assert "References" in body


def test_looks_like_paper_accepts_converted_body(body: str) -> None:
    assert looks_like_paper(body) is True


def test_looks_like_paper_rejects_short_or_flat_text() -> None:
    assert looks_like_paper("") is False
    assert looks_like_paper("just a sentence with no structure") is False
    # Long but heading-free text (e.g. an error page) must not pass.
    assert looks_like_paper("word " * 2000) is False
