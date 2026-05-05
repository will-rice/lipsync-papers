"""Parse references and resolve them to URLs (local-sibling preferred)."""

from __future__ import annotations

import json
import logging
import re
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

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
    refs_block = markdown[heading.end() :]

    refs: list[Reference] = []
    for match in _PDF_REF_ENTRY_RE.finditer(refs_block):
        key = match.group(1).strip()
        raw = " ".join(match.group(2).split())
        ref = Reference(key=key, raw=raw)
        ref.title = _extract_title_heuristic(raw)
        if m := _ARXIV_ID_RE.search(raw):
            ref.arxiv_id = m.group(1)
        if m := _DOI_RE.search(raw):
            ref.doi = m.group(1)
        if m := _YEAR_RE.search(raw):
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


S2_SEARCH_URL = (
    "https://api.semanticscholar.org/graph/v1/paper/search?query={q}&fields=externalIds&limit=1"
)
USER_AGENT = "lipsync-papers-bot/1.0"


@dataclass
class ResolutionContext:
    """Context passed to resolve_reference — local corpus, current paper's year, S2 cache."""

    corpus_arxiv_to_year: dict[str, str]  # {"2008.10010": "2020", …}
    current_year: str  # year of the citing paper, for relative paths
    s2_cache: dict[str, dict]  # {"title:<lowercased>": <s2 response>, …}


def _local_sibling_url(arxiv_id: str, target_year: str, current_year: str) -> str:
    """Return a relative path from current_year/<id>.md to target_year/<id>.md."""
    if target_year == current_year:
        return f"./{arxiv_id}.md"
    return f"../{target_year}/{arxiv_id}.md"


def _s2_lookup_by_title(title: str, cache: dict[str, dict]) -> dict | None:
    """Look up *title* in the S2 cache, falling back to a network call on miss."""
    key = f"title:{title.lower().strip()}"
    if key in cache:
        return cache[key]
    encoded = urllib.parse.quote(title)
    url = S2_SEARCH_URL.format(q=encoded)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
        cache[key] = data
        return data
    except Exception as exc:  # noqa: BLE001
        logging.warning("S2 title lookup failed for %r: %s", title, exc)
        cache[key] = {"data": []}
        return cache[key]


def resolve_reference(ref: Reference, ctx: ResolutionContext) -> None:
    """Mutate *ref* in place: set ref.resolved_url and (sometimes) ref.arxiv_id/doi.

    Priority order:
      1. Local sibling (arxiv_id in corpus)
      2. External arXiv (arxiv_id set, not in corpus)
      3. DOI
      4. S2 title lookup → re-enter chain
      5. Leave None (citation rendered bare)
    """
    if ref.arxiv_id and ref.arxiv_id in ctx.corpus_arxiv_to_year:
        target_year = ctx.corpus_arxiv_to_year[ref.arxiv_id]
        ref.resolved_url = _local_sibling_url(ref.arxiv_id, target_year, ctx.current_year)
        return
    if ref.arxiv_id:
        ref.resolved_url = f"https://arxiv.org/abs/{ref.arxiv_id}"
        return
    if ref.doi:
        ref.resolved_url = f"https://doi.org/{ref.doi}"
        return
    if ref.title:
        s2 = _s2_lookup_by_title(ref.title, ctx.s2_cache)
        hits = (s2 or {}).get("data") or []
        if hits:
            ext = hits[0].get("externalIds") or {}
            if arxiv_id := ext.get("ArXiv"):
                ref.arxiv_id = arxiv_id
                if arxiv_id in ctx.corpus_arxiv_to_year:
                    target_year = ctx.corpus_arxiv_to_year[arxiv_id]
                    ref.resolved_url = _local_sibling_url(arxiv_id, target_year, ctx.current_year)
                else:
                    ref.resolved_url = f"https://arxiv.org/abs/{arxiv_id}"
                return
            if doi := ext.get("DOI"):
                ref.doi = doi
                ref.resolved_url = f"https://doi.org/{doi}"
                return
    # Step 5: unresolved
    ref.resolved_url = None


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


# BibTeX entry: @type{key, ... }  with balanced braces in the body.
_BIB_ENTRY_HEAD_RE = re.compile(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", re.MULTILINE)
_BIB_FIELD_RE = re.compile(
    r"(\w+)\s*=\s*(?:\{((?:[^{}]|\{[^{}]*\})*)\}|\"([^\"]*)\"|([^,\n]+?))\s*(?:,|\Z|(?=\n\s*\}))",
    re.DOTALL,
)
_BIB_ARXIV_RE = re.compile(r"arXiv[:\s]+(\d{4}\.\d{4,5})", re.IGNORECASE)
_BIB_ARXIV_BARE_RE = re.compile(r"\b(\d{4}\.\d{4,5})\b")


def _split_bib_entries(bib_text: str) -> list[tuple[str, str]]:
    """Yield (cite-key, body) pairs by tracking balanced braces from each ``@type{key,`` head."""
    entries: list[tuple[str, str]] = []
    for match in _BIB_ENTRY_HEAD_RE.finditer(bib_text):
        key = match.group(2).strip()
        depth = 1
        start = match.end()
        i = start
        while i < len(bib_text) and depth > 0:
            ch = bib_text[i]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
            i += 1
        if depth == 0:
            entries.append((key, bib_text[start : i - 1]))
    return entries


def parse_bib(bib_text: str) -> list[Reference]:
    """Parse a BibTeX .bib file into a list of References."""
    refs: list[Reference] = []
    for key, body in _split_bib_entries(bib_text):
        fields: dict[str, str] = {}
        for fm in _BIB_FIELD_RE.finditer(body):
            name = fm.group(1).lower()
            value = fm.group(2) or fm.group(3) or fm.group(4) or ""
            fields[name] = re.sub(r"[{}]", "", value).strip()

        ref = Reference(
            key=key,
            raw=fields.get("title", "") or body.strip(),
            title=fields.get("title", ""),
        )
        if year := fields.get("year"):
            try:
                ref.year = int(re.findall(r"\d{4}", year)[0])
            except (ValueError, IndexError):
                pass
        if arxiv := (fields.get("eprint") or fields.get("arxivid")):
            ref.arxiv_id = arxiv.strip()
        elif (journal := fields.get("journal", "")) and (m := _BIB_ARXIV_RE.search(journal)):
            ref.arxiv_id = m.group(1)
        elif (note := fields.get("note", "")) and (m := _BIB_ARXIV_BARE_RE.search(note)):
            ref.arxiv_id = m.group(1)
        if doi := fields.get("doi"):
            ref.doi = doi.strip()
        refs.append(ref)
    return refs


_CITE_RE = re.compile(r"\\cite\{([^}]+)\}")
_PDF_NUM_CITE_RE = re.compile(r"\[(\d+)\]")


def rewrite_latex_cites(body: str, refs: dict[str, Reference]) -> str:
    """Rewrite each ``\\cite{key}`` in *body* using *refs* mapping (resolved_url required)."""

    def _replace(m: re.Match[str]) -> str:
        keys_raw = m.group(1)
        rendered_keys = []
        for key in (k.strip() for k in keys_raw.split(",")):
            ref = refs.get(key)
            if ref and ref.resolved_url:
                rendered_keys.append(f"[\\[{key}\\]]({ref.resolved_url})")
            else:
                rendered_keys.append(f"\\[{key}\\]")
        return ", ".join(rendered_keys)

    return _CITE_RE.sub(_replace, body)


def rewrite_pdf_numeric_cites(body: str, refs: dict[str, Reference]) -> str:
    """Rewrite ``[N]`` markers in *body* using *refs* — only high-confidence refs become links."""
    # Avoid touching the ## References section — split and rejoin.
    parts = _PDF_REF_HEADING_RE.split(body, maxsplit=1)
    head = parts[0]
    tail = parts[1] if len(parts) > 1 else ""

    def _replace(m: re.Match[str]) -> str:
        key = m.group(1)
        ref = refs.get(key)
        if ref and ref.resolved_url and ref.confidence == "high":
            return f"[\\[{key}\\]]({ref.resolved_url})"
        return m.group(0)

    rewritten_head = _PDF_NUM_CITE_RE.sub(_replace, head)
    if tail:
        return rewritten_head + "## References" + tail
    return rewritten_head


def render_references_section(refs: list[Reference]) -> str:
    """Render a ``## References`` section with each entry getting its resolved link."""
    lines = ["## References", ""]
    for i, ref in enumerate(refs, start=1):
        link_suffix = ""
        if ref.arxiv_id and ref.resolved_url:
            link_suffix = f" [arXiv:{ref.arxiv_id}]({ref.resolved_url})"
        elif ref.doi and ref.resolved_url:
            link_suffix = f" [doi:{ref.doi}]({ref.resolved_url})"
        elif ref.resolved_url:
            link_suffix = f" [link]({ref.resolved_url})"
        lines.append(f"{i}. {ref.raw.strip()}{link_suffix}")
    return "\n".join(lines) + "\n"


def resolved_count(refs: list[Reference]) -> str:
    """Return a diagnostic string like ``27/41``."""
    resolved = sum(1 for r in refs if r.resolved_url)
    return f"{resolved}/{len(refs)}"


def load_citation_cache(path: Path) -> dict[str, dict]:
    """Load the JSON citation cache at *path*; return {} if missing."""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def save_citation_cache(path: Path, cache: dict[str, dict]) -> None:
    """Persist *cache* as JSON at *path*, creating parent dirs."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(cache, indent=2, sort_keys=True), encoding="utf-8")
