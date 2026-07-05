"""Tests for scripts/_convert/sources.py."""

import urllib.error
from pathlib import Path

from scripts._convert.sources import (
    SourceKind,
    classify_extracted_source,
    extract_arxiv_tarball,
    fetch_arxiv_html,
    is_cache_fresh,
)


class _FakeResponse:
    def __init__(self, payload: bytes) -> None:
        self._payload = payload

    def read(self) -> bytes:
        return self._payload

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        return None


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


def test_fetch_arxiv_html_success(monkeypatch) -> None:
    payload = b"<html><body>" + (b"x" * 600) + b"</body></html>"

    def fake_urlopen(req, timeout=0):  # noqa: ARG001
        return _FakeResponse(payload)

    monkeypatch.setattr("scripts._convert.sources.time.sleep", lambda *_: None)
    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)

    html = fetch_arxiv_html("2401.01207")
    assert html is not None
    assert "<body>" in html


def test_fetch_arxiv_html_404_returns_none(monkeypatch) -> None:
    def fake_urlopen(req, timeout=0):  # noqa: ARG001
        raise urllib.error.HTTPError(
            url="https://arxiv.org/html/2401.01207",
            code=404,
            msg="Not Found",
            hdrs=None,
            fp=None,
        )

    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)

    assert fetch_arxiv_html("2401.01207") is None


def test_fetch_arxiv_html_too_short_returns_none(monkeypatch) -> None:
    def fake_urlopen(req, timeout=0):  # noqa: ARG001
        return _FakeResponse(b"<html><body>short</body></html>")

    monkeypatch.setattr("scripts._convert.sources.time.sleep", lambda *_: None)
    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)

    assert fetch_arxiv_html("2401.01207") is None


def test_fetch_arxiv_html_skips_non_arxiv(monkeypatch) -> None:
    def fake_urlopen(req, timeout=0):  # noqa: ARG001
        raise AssertionError("network should not be called for non-arxiv IDs")

    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)
    assert fetch_arxiv_html("s2:abc") is None
    assert fetch_arxiv_html("pwc:abc") is None
