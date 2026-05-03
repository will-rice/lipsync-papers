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
