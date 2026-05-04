"""Parse references and resolve them to URLs (local-sibling preferred)."""

from __future__ import annotations

import re
from dataclasses import dataclass, field

# Pattern for individual \bibitem blocks (greedy until next \bibitem or thebibliography end)
_BIBITEM_RE = re.compile(
    r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}(.+?)(?=\\bibitem|\\end\{thebibliography\}|\Z)",
    re.DOTALL,
)
_ARXIV_ID_RE = re.compile(r"arXiv[:\s]+(\d{4}\.\d{4,5})", re.IGNORECASE)
_DOI_RE = re.compile(r"doi[:\s]+(10\.\d+/[\w./-]+)", re.IGNORECASE)
_YEAR_RE = re.compile(r"\b(19|20)\d{2}\b")
_PDF_REF_HEADING_RE = re.compile(r"^\s*##+\s*References\s*$", re.MULTILINE | re.IGNORECASE)
_PDF_REF_ENTRY_RE = re.compile(
    r"\[(\d+)\](.+?)(?=\n\s*\[\d+\]|\Z)",
    re.DOTALL,
)
_PERIOD_BEFORE_CAPITAL_RE = re.compile(r"\.\s+(?=[A-Z])")


@dataclass
class Reference:
    """A single bibliography entry, normalized for resolution."""

    key: str  # cite-key (LaTeX) or "1", "2", … (PDF)
    raw: str  # original entry text
    title: str = ""
    authors: list[str] = field(default_factory=list)
    year: int | None = None
    arxiv_id: str | None = None
    doi: str | None = None
    resolved_url: str | None = None  # filled in by Pass B
    confidence: str = "high"  # "high" | "low" — low means leave bare on rewrite


def parse_pdf_references(markdown: str) -> list[Reference]:
    """Parse a marker-rendered ## References section into References.

    Title extraction heuristic: take the longest title-cased span up to the first period
    after the author list. Works on ~85% of ML papers.
    """
    heading = _PDF_REF_HEADING_RE.search(markdown)
    if not heading:
        return []
    refs_block = markdown[heading.end():]

    refs: list[Reference] = []
    for match in _PDF_REF_ENTRY_RE.finditer(refs_block):
        key = match.group(1).strip()
        raw = " ".join(match.group(2).split())
        ref = Reference(key=key, raw=raw)
        ref.title = _extract_title_heuristic(raw)
        if (m := _ARXIV_ID_RE.search(raw)):
            ref.arxiv_id = m.group(1)
        if (m := _DOI_RE.search(raw)):
            ref.doi = m.group(1)
        if (m := _YEAR_RE.search(raw)):
            ref.year = int(m.group(0))
        if not ref.title:
            ref.confidence = "low"
        refs.append(ref)
    return refs


def _extract_title_heuristic(raw: str) -> str:
    """Pull the title from a flat reference line: first multi-char word-bounded period split.

    Skips single-letter initials (e.g. "K.", "R.") and accepts two-char abbreviations
    like "al." so "et al. Title" parses correctly.
    """
    # Walk period+capital splits; stop at the first one where the preceding token is 2+ chars.
    # Single-letter initials ("K.", "J.") are skipped so the boundary falls after a surname or "al".
    candidate_text = raw
    for match in _PERIOD_BEFORE_CAPITAL_RE.finditer(raw):
        before = raw[: match.start()]
        last_token = re.split(r"[\s,]+", before)[-1] if before else ""
        if len(last_token) >= 2:
            candidate_text = raw[match.end() :]
            break
    # Title is everything up to the next period (venue / "In …" follows).
    title = candidate_text.split(".", 1)[0].strip()
    # Sanity bound — titles longer than 250 chars are almost certainly wrong extractions.
    if len(title) > 250:
        return ""
    return title


def parse_bbl(bbl_text: str) -> list[Reference]:
    """Parse a pandoc/biblatex .bbl into a list of References."""
    refs: list[Reference] = []
    for match in _BIBITEM_RE.finditer(bbl_text):
        key = match.group(1).strip()
        body = match.group(2).strip()
        ref = Reference(key=key, raw=body)
        if m := _ARXIV_ID_RE.search(body):
            ref.arxiv_id = m.group(1)
        if m := _DOI_RE.search(body):
            ref.doi = m.group(1)
        if m := _YEAR_RE.search(body):
            ref.year = int(m.group(0))
        refs.append(ref)
    return refs
