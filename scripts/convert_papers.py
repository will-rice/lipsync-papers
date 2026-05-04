"""Convert all papers in papers.csv to markdown.

Usage:
    uv run python scripts/convert_papers.py
    uv run python scripts/convert_papers.py --only 2008.10010
    uv run python scripts/convert_papers.py --skip-llm
"""

from __future__ import annotations

import argparse
import csv
import logging
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PAPERS_CSV = REPO_ROOT / "papers.csv"
PAPERS_DIR = REPO_ROOT / "papers"
CACHE_DIR = REPO_ROOT / ".cache"

LLM_REMEDIATION_MAX_PAPERS = int(os.environ.get("LLM_REMEDIATION_MAX_PAPERS", "50"))
LLM_REMEDIATION_DRY_RUN = os.environ.get("LLM_REMEDIATION_DRY_RUN", "false").lower() == "true"
MAX_WORKERS = 8

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


@dataclass
class PaperRow:
    """A single row from papers.csv, normalized."""

    arxiv_id: str
    title: str
    authors: list[str]
    submitted: str
    categories: list[str]
    url: str
    abstract: str

    @property
    def year(self) -> str:
        return self.submitted[:4]


def main() -> None:
    args = parse_args()
    rows = load_papers_csv(PAPERS_CSV)
    logging.info("Loaded %d papers from %s", len(rows), PAPERS_CSV)

    if args.only:
        rows = [r for r in rows if r.arxiv_id == args.only]
        logging.info("Filtered to %d paper(s) matching --only=%s", len(rows), args.only)

    pending = [r for r in rows if needs_conversion(r, PAPERS_DIR)]
    logging.info("%d papers need conversion", len(pending))

    # Stage 1+2 (per-paper, parallel).
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(_process_paper, row): row for row in pending}
        for fut in as_completed(futures):
            row = futures[fut]
            try:
                fut.result()
            except Exception as exc:  # noqa: BLE001
                logging.exception("Failed to process %s: %s", row.arxiv_id, exc)

    # Stage 4: indexes (always regenerate; cheap).
    _regenerate_indexes(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convert papers in papers.csv to markdown.")
    parser.add_argument("--only", default=None, help="Only process this arxiv_id.")
    parser.add_argument("--skip-llm", action="store_true", help="Skip Stage 2.5 remediation.")
    return parser.parse_args()


def load_papers_csv(path: Path) -> list[PaperRow]:
    """Read papers.csv into a list of PaperRow."""
    rows: list[PaperRow] = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(
                PaperRow(
                    arxiv_id=row["arxiv_id"],
                    title=row["title"],
                    authors=[a.strip() for a in row.get("authors", "").split(",") if a.strip()],
                    submitted=row.get("submitted", ""),
                    categories=[c for c in row.get("categories", "").split() if c],
                    url=row.get("url", ""),
                    abstract=row.get("abstract", ""),
                )
            )
    return rows


def needs_conversion(row: PaperRow, papers_dir: Path) -> bool:
    """True if this paper has no markdown file yet."""
    target = papers_dir / row.year / f"{row.arxiv_id}.md"
    return not target.exists()


def _process_paper(row: PaperRow) -> None:
    """Run Stages 1, 2, and 3 for a single paper. Idempotent."""
    from scripts._convert import (
        citations,
        latex_to_md,
        output,
        pdf_to_md,
        sources,
    )

    cache_root = CACHE_DIR / "source"
    paper_cache = sources.cache_dir_for(row.arxiv_id, cache_root)

    # Stage 1: ensure source is cached.
    is_arxiv = not row.arxiv_id.startswith(("s2:", "pwc:"))
    extracted_dir = paper_cache / "extracted"
    if not sources.is_cache_fresh(extracted_dir):
        if is_arxiv:
            tarball = paper_cache / "source.tar.gz"
            if not tarball.exists():
                sources.fetch_arxiv_eprint(row.arxiv_id, tarball)
            sources.extract_arxiv_tarball(tarball, extracted_dir)
        else:
            # S2 path: try openAccessPdf
            s2_paper_id = row.arxiv_id.removeprefix("s2:")
            pdf_url = sources.fetch_s2_pdf_url(s2_paper_id)
            if pdf_url:
                pdf_dest = paper_cache / "paper.pdf"
                sources.fetch_pdf(pdf_url, pdf_dest)
                extracted_dir.mkdir(parents=True, exist_ok=True)
                (extracted_dir / "paper.pdf").write_bytes(pdf_dest.read_bytes())
            else:
                extracted_dir.mkdir(parents=True, exist_ok=True)  # empty → metadata-only

    kind = sources.classify_extracted_source(extracted_dir)

    # Stage 2: convert.
    body = ""
    bbl_text = ""
    converter = "none"
    source_label = "metadata-only"

    if kind is sources.SourceKind.LATEX:
        result = latex_to_md.convert_latex_to_md(extracted_dir)
        body = result.body
        bbl_text = result.bbl_text
        converter = "pandoc"
        source_label = "latex"
    elif kind is sources.SourceKind.PDF:
        pdf_files = list(extracted_dir.rglob("*.pdf"))
        result = pdf_to_md.convert_pdf_to_md(pdf_files[0])
        body = result.body
        converter = "marker"
        source_label = "pdf"

    # Stage 3: parse + resolve + rewrite citations.
    cache_path = CACHE_DIR / "citations.json"
    s2_cache = citations.load_citation_cache(cache_path)
    corpus = _build_corpus_index()
    ctx = citations.ResolutionContext(
        corpus_arxiv_to_year=corpus,
        current_year=row.year,
        s2_cache=s2_cache,
    )

    refs: list[citations.Reference] = []
    if bbl_text:
        refs = citations.parse_bbl(bbl_text)
    elif body:
        refs = citations.parse_pdf_references(body)

    for ref in refs:
        citations.resolve_reference(ref, ctx)
    citations.save_citation_cache(cache_path, s2_cache)

    refs_by_key = {r.key: r for r in refs}
    if source_label == "latex":
        body = citations.rewrite_latex_cites(body, refs_by_key)
    elif source_label == "pdf":
        body = citations.rewrite_pdf_numeric_cites(body, refs_by_key)

    if refs:
        # Strip any existing References section, then append our linked one.
        from scripts._convert.citations import _PDF_REF_HEADING_RE  # internal use OK

        head = _PDF_REF_HEADING_RE.split(body, maxsplit=1)[0].rstrip()
        body = head + "\n\n" + citations.render_references_section(refs)

    record = output.PaperRecord(
        arxiv_id=row.arxiv_id,
        title=row.title,
        authors=row.authors,
        submitted=row.submitted,
        categories=row.categories,
        arxiv_url=row.url,
        source=source_label,
        converter=converter,
        body=body if body else f"## Abstract\n\n{row.abstract}\n",
        references_parsed=len(refs),
        citations_resolved=citations.resolved_count(refs) if refs else "0/0",
    )
    output.write_paper_markdown(record, PAPERS_DIR)


def _build_corpus_index() -> dict[str, str]:
    """Map arxiv_id → year for every paper in papers.csv (for local-sibling links)."""
    rows = load_papers_csv(PAPERS_CSV)
    return {r.arxiv_id: r.year for r in rows if not r.arxiv_id.startswith(("s2:", "pwc:"))}


def _regenerate_indexes(rows: list[PaperRow]) -> None:
    """Stub — wired up in Task 17."""
    logging.info("Would regenerate indexes for %d papers", len(rows))


if __name__ == "__main__":
    main()
