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
    def __init__(self, payload: bytes, url: str = "") -> None:
        self._payload = payload
        self._url = url

    def read(self) -> bytes:
        return self._payload

    def geturl(self) -> str:
        return self._url

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


_GOOD_HTML = b"<html><body>" + (b"x" * 600) + b"</body></html>"


def _http_404(url: str) -> urllib.error.HTTPError:
    return urllib.error.HTTPError(url=url, code=404, msg="Not Found", hdrs=None, fp=None)


def test_fetch_arxiv_html_success(monkeypatch) -> None:
    def fake_urlopen(req, timeout=0):  # noqa: ARG001
        return _FakeResponse(_GOOD_HTML, url="https://arxiv.org/html/2401.01207v2")

    monkeypatch.setattr("scripts._convert.sources.time.sleep", lambda *_: None)
    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)

    page = fetch_arxiv_html("2401.01207")
    assert page is not None
    assert "<body>" in page.html
    assert page.url == "https://arxiv.org/html/2401.01207v2"


def test_fetch_arxiv_html_falls_back_to_ar5iv(monkeypatch) -> None:
    def fake_urlopen(req, timeout=0):  # noqa: ARG001
        if "ar5iv" in req.full_url:
            return _FakeResponse(_GOOD_HTML, url=req.full_url)
        raise _http_404(req.full_url)

    monkeypatch.setattr("scripts._convert.sources.time.sleep", lambda *_: None)
    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)

    page = fetch_arxiv_html("2008.10010")
    assert page is not None
    assert page.url == "https://ar5iv.labs.arxiv.org/html/2008.10010"


def test_fetch_arxiv_html_ar5iv_abs_redirect_returns_none(monkeypatch) -> None:
    # ar5iv redirects to the arxiv.org abstract page when it has no conversion.
    def fake_urlopen(req, timeout=0):  # noqa: ARG001
        if "ar5iv" in req.full_url:
            return _FakeResponse(_GOOD_HTML, url="https://arxiv.org/abs/2401.01207")
        raise _http_404(req.full_url)

    monkeypatch.setattr("scripts._convert.sources.time.sleep", lambda *_: None)
    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)

    assert fetch_arxiv_html("2401.01207") is None


def test_fetch_arxiv_html_too_short_returns_none(monkeypatch) -> None:
    def fake_urlopen(req, timeout=0):  # noqa: ARG001
        return _FakeResponse(b"<html><body>short</body></html>", url=req.full_url)

    monkeypatch.setattr("scripts._convert.sources.time.sleep", lambda *_: None)
    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)

    assert fetch_arxiv_html("2401.01207") is None


def test_fetch_arxiv_html_skips_non_arxiv(monkeypatch) -> None:
    def fake_urlopen(req, timeout=0):  # noqa: ARG001
        raise AssertionError("network should not be called for non-arxiv IDs")

    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)
    assert fetch_arxiv_html("s2:abc") is None
