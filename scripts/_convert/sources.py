"""Fetch and cache paper source from arXiv (LaTeX preferred) or Semantic Scholar (PDF)."""

from __future__ import annotations

import enum
import json
import logging
import tarfile
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ARXIV_EPRINT_URL = "https://arxiv.org/e-print/{arxiv_id}"
S2_PAPER_URL = (
    "https://api.semanticscholar.org/graph/v1/paper/{paper_id}?fields=openAccessPdf,externalIds"
)
USER_AGENT = "lipsync-papers-bot/1.0"
ARXIV_RATE_LIMIT_SECONDS = 3
DEFAULT_CACHE_AGE_DAYS = 30


class SourceKind(enum.Enum):
    LATEX = "latex"
    PDF = "pdf"
    EMPTY = "empty"


def cache_dir_for(arxiv_id: str, cache_root: Path) -> Path:
    """Return the on-disk cache directory for a paper's source files."""
    return cache_root / arxiv_id


def is_cache_fresh(cache_dir: Path, max_age_days: int = DEFAULT_CACHE_AGE_DAYS) -> bool:
    """Return True if *cache_dir* exists and was modified within max_age_days."""
    if not cache_dir.exists():
        return False
    mtime = datetime.fromtimestamp(cache_dir.stat().st_mtime, tz=timezone.utc)
    age = datetime.now(tz=timezone.utc) - mtime
    return age.days < max_age_days


def fetch_arxiv_eprint(arxiv_id: str, dest: Path) -> Path:
    """Download the arXiv e-print tarball for *arxiv_id* to *dest*. Returns *dest*."""
    url = ARXIV_EPRINT_URL.format(arxiv_id=arxiv_id)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    logging.info("Fetching arXiv e-print: %s", url)
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    time.sleep(ARXIV_RATE_LIMIT_SECONDS)
    return dest


def extract_arxiv_tarball(tarball: Path, out_dir: Path) -> None:
    """Extract a gzipped arXiv source tarball to *out_dir*. Tolerant of single-file submissions."""
    out_dir.mkdir(parents=True, exist_ok=True)
    try:
        with tarfile.open(tarball, "r:gz") as tf:
            tf.extractall(out_dir, filter="data")
    except tarfile.ReadError:
        # Single-file submission (often a raw .tex or .pdf gzipped without tar)
        # Fallback: copy as-is, classifier will sort it out.
        (out_dir / tarball.name).write_bytes(tarball.read_bytes())


def classify_extracted_source(extracted: Path) -> SourceKind:
    """Determine whether *extracted* contains LaTeX, a PDF only, or nothing useful."""
    if any(extracted.rglob("*.tex")):
        return SourceKind.LATEX
    if any(extracted.rglob("*.pdf")):
        return SourceKind.PDF
    return SourceKind.EMPTY


def fetch_s2_pdf_url(s2_paper_id: str) -> str | None:
    """Query Semantic Scholar for an open-access PDF URL. Return None if unavailable."""
    url = S2_PAPER_URL.format(paper_id=s2_paper_id)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as exc:
        logging.warning("S2 lookup failed for %s: %s", s2_paper_id, exc)
        return None
    open_access = data.get("openAccessPdf") or {}
    return open_access.get("url")


def fetch_pdf(url: str, dest: Path) -> Path:
    """Download a PDF from *url* to *dest*. Returns *dest*."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    logging.info("Fetching PDF: %s", url)
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    return dest
