"""Convert all papers in papers.csv to markdown.

Usage:
    uv run python scripts/convert_papers.py
    uv run python scripts/convert_papers.py --regenerate-all
    uv run python scripts/convert_papers.py --only 2008.10010
    uv run python scripts/convert_papers.py --skip-llm
"""

from __future__ import annotations

import argparse
import csv
import logging
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Make `scripts._convert` importable when running this file directly.
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
PAPERS_CSV = REPO_ROOT / "papers.csv"
PAPERS_DIR = REPO_ROOT / "papers"
CACHE_DIR = REPO_ROOT / ".cache"

LLM_REMEDIATION_MAX_PAPERS = int(os.environ.get("LLM_REMEDIATION_MAX_PAPERS", "50"))
LLM_REMEDIATION_DRY_RUN = os.environ.get("LLM_REMEDIATION_DRY_RUN", "false").lower() == "true"
MAX_WORKERS = int(os.environ.get("CONVERT_MAX_WORKERS", "8"))

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
    all_rows = load_papers_csv(PAPERS_CSV)
    logging.info("Loaded %d papers from %s", len(all_rows), PAPERS_CSV)

    rows = all_rows
    if args.only:
        rows = [r for r in rows if r.arxiv_id == args.only]
        logging.info("Filtered to %d paper(s) matching --only=%s", len(rows), args.only)

    pending = [r for r in rows if needs_conversion(r, PAPERS_DIR, force=args.regenerate_all)]
    logging.info("%d papers need conversion", len(pending))

    # Stage 1+2 (per-paper, parallel).
    error_log = CACHE_DIR / "conversion_errors.jsonl"
    fixme_path = PAPERS_DIR / ".fixme.txt"
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {
            pool.submit(_process_paper, row, force=args.regenerate_all): row for row in pending
        }
        for fut in as_completed(futures):
            row = futures[fut]
            try:
                fut.result()
            except Exception as exc:  # noqa: BLE001
                logging.exception("Failed to process %s", row.arxiv_id)
                record_failure_and_maybe_escalate(
                    error_log, fixme_path, row.arxiv_id, "process", str(exc)
                )

    # Stage 2.5: LLM remediation (skippable).
    if not args.skip_llm:
        _run_remediation_pass(rows)

    # Stage 4: indexes (always regenerate; cheap). Use the unfiltered corpus so a
    # --only run cannot clobber the index files down to a single entry.
    _regenerate_indexes(all_rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convert papers in papers.csv to markdown.")
    parser.add_argument("--only", default=None, help="Only process this arxiv_id.")
    parser.add_argument(
        "--regenerate-all",
        action="store_true",
        help="Rebuild markdown for every paper, even when an output file already exists.",
    )
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


# Conversion tiers, best last. A paper is only rewritten when its tier improves.
SOURCE_TIER_RANK = {"metadata-only": 0, "pdf": 1, "latex": 2, "arxiv-html": 3}

# New papers can gain an arXiv HTML rendering days after submission; retry
# non-HTML conversions until the paper lands on the top tier or ages out.
HTML_RETRY_DAYS = 30


def read_source_tier(md_path: Path) -> str:
    """Return the frontmatter ``source:`` value of an existing paper file."""
    for line in md_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("source:"):
            return line.removeprefix("source:").strip()
    return ""


def needs_conversion(row: PaperRow, papers_dir: Path, *, force: bool = False) -> bool:
    """True if this paper should be converted."""
    if force:
        return True
    target = papers_dir / row.year / f"{row.arxiv_id}.md"
    if not target.exists():
        return True
    if row.arxiv_id.startswith("s2:"):
        return False
    try:
        submitted = date.fromisoformat(row.submitted[:10])
    except ValueError:
        return False
    if (date.today() - submitted).days > HTML_RETRY_DAYS:
        return False
    return read_source_tier(target) != "arxiv-html"


def _process_paper(row: PaperRow, force: bool = False) -> None:
    """Run Stages 0-3 for a single paper. Idempotent."""
    from scripts._convert import (
        citations,
        html_to_md,
        latex_to_md,
        output,
        sources,
    )

    cache_root = CACHE_DIR / "source"
    paper_cache = sources.cache_dir_for(row.arxiv_id, cache_root)

    # Stage 0: try arXiv HTML render first (faster than source tarball/PDF paths).
    is_arxiv = not row.arxiv_id.startswith("s2:")
    body = ""
    bbl_text = ""
    bib_text = ""
    converter = "none"
    source_label = "metadata-only"

    if is_arxiv:
        page = sources.fetch_arxiv_html(row.arxiv_id)
        if page:
            html_result = html_to_md.convert_html_to_md(page.html, base_url=page.url)
            if html_result.exit_code == 0 and html_to_md.looks_like_paper(html_result.body):
                body = html_result.body
                converter = "pandoc"
                source_label = "arxiv-html"
            else:
                logging.warning(
                    "arXiv HTML conversion unusable for %s (exit=%s): %s",
                    row.arxiv_id,
                    html_result.exit_code,
                    html_result.stderr.strip(),
                )

    if not body:
        # Stage 1: ensure source is cached.
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
        if kind is sources.SourceKind.LATEX:
            result = latex_to_md.convert_latex_to_md(extracted_dir)
            body = result.body
            bbl_text = result.bbl_text
            bib_text = result.bib_text
            converter = "pandoc"
            source_label = "latex"
        elif kind is sources.SourceKind.PDF:
            from scripts._convert import pdf_to_md

            pdf_files = list(extracted_dir.rglob("*.pdf"))
            result = pdf_to_md.convert_pdf_to_md(pdf_files[0])
            body = result.body
            converter = "marker"
            source_label = "pdf"

    # Retries must not churn files: only rewrite when the conversion tier improves.
    target = output.paper_path(row.arxiv_id, row.submitted, PAPERS_DIR)
    if not force and target.exists():
        existing_tier = read_source_tier(target)
        if SOURCE_TIER_RANK[source_label] <= SOURCE_TIER_RANK.get(existing_tier, -1):
            logging.info("Keeping existing %s output for %s", existing_tier, row.arxiv_id)
            return

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
    elif bib_text:
        refs = citations.parse_bib(bib_text)
    elif body:
        refs = citations.parse_pdf_references(body)

    for ref in refs:
        citations.resolve_reference(ref, ctx)
    citations.save_citation_cache(cache_path, s2_cache)

    refs_by_key = {r.key: r for r in refs}
    if source_label == "latex":
        body = citations.rewrite_latex_cites(body, refs_by_key)
    elif source_label in ("pdf", "arxiv-html"):
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
    return {r.arxiv_id: r.year for r in rows if not r.arxiv_id.startswith("s2:")}


def _run_remediation_pass(rows: list[PaperRow]) -> None:
    """Stage 2.5 — flag low-quality papers + manually-listed ones, re-render via Claude.

    Honors LLM_REMEDIATION_DRY_RUN and LLM_REMEDIATION_MAX_PAPERS env caps.
    """
    import yaml

    from scripts._convert import remediation

    fixme_path = PAPERS_DIR / ".fixme.txt"
    fixme = remediation.load_fixme_list(fixme_path)
    candidates: list[tuple[PaperRow, Path, dict, str]] = []

    for row in rows:
        md_path = PAPERS_DIR / row.year / f"{row.arxiv_id}.md"
        if not md_path.exists():
            continue
        text = md_path.read_text(encoding="utf-8")
        front_end = text.index("\n---\n", 4)
        front = yaml.safe_load(text[4:front_end])
        body = text[front_end + 5 :]
        if front.get("llm_remediated"):
            continue

        resolved = front.get("citations_resolved", "0/0")
        try:
            num, denom = resolved.split("/")
            ratio = int(num) / max(1, int(denom))
        except (ValueError, ZeroDivisionError):
            ratio = 0.0

        flags = remediation.should_remediate(
            body=body,
            page_count=10,  # rough; we don't store this currently
            has_references=front.get("references_parsed", 0) > 0,
            citations_resolved_ratio=ratio,
            latex_exit_code=0,  # not persisted; rely on other heuristics
        )
        if flags.flagged or row.arxiv_id in fixme:
            candidates.append((row, md_path, front, body))

    candidates = candidates[:LLM_REMEDIATION_MAX_PAPERS]
    if not candidates:
        logging.info("No papers flagged for remediation.")
        return
    logging.info("Remediation candidates: %d (cap %d)", len(candidates), LLM_REMEDIATION_MAX_PAPERS)

    if LLM_REMEDIATION_DRY_RUN:
        for row, _, _, _ in candidates:
            logging.info("Would remediate %s", row.arxiv_id)
        return

    from scripts._convert.output import PaperRecord, write_paper_markdown

    client = remediation.build_anthropic_client()
    for row, md_path, front, body in candidates:
        pdf_path = CACHE_DIR / "source" / row.arxiv_id / "paper.pdf"
        if not pdf_path.exists():
            logging.warning("No PDF cached for %s; skipping remediation.", row.arxiv_id)
            continue
        try:
            corrected = remediation.remediate_with_pdf(pdf_path, body, client)
        except Exception as exc:  # noqa: BLE001
            logging.exception("Remediation API call failed for %s: %s", row.arxiv_id, exc)
            continue
        front["llm_remediated"] = True
        record = PaperRecord(
            arxiv_id=front["arxiv_id"],
            title=front["title"],
            authors=front.get("authors", []),
            submitted=front["submitted"],
            categories=front.get("categories", []),
            arxiv_url=front.get("arxiv_url", ""),
            source=front.get("source", "pdf"),
            converter=front.get("converter", "marker"),
            body=corrected,
            references_parsed=front.get("references_parsed", 0),
            citations_resolved=front.get("citations_resolved", "0/0"),
            arxiv_version=front.get("arxiv_version", ""),
            llm_remediated=True,
        )
        write_paper_markdown(record, PAPERS_DIR)


def _regenerate_indexes(rows: list[PaperRow]) -> None:
    """Write papers/README.md and papers/<year>/README.md from rows that have an MD file."""
    from collections import defaultdict

    from scripts._convert import indexes

    entries_by_year: dict[str, list[indexes.IndexEntry]] = defaultdict(list)
    all_entries: list[indexes.IndexEntry] = []
    for r in rows:
        target = PAPERS_DIR / r.year / f"{r.arxiv_id}.md"
        if not target.exists():
            continue
        entry = indexes.IndexEntry(
            arxiv_id=r.arxiv_id,
            title=r.title,
            authors=r.authors,
            submitted=r.submitted,
            abstract=r.abstract,
        )
        entries_by_year[r.year].append(entry)
        all_entries.append(entry)

    PAPERS_DIR.mkdir(parents=True, exist_ok=True)
    (PAPERS_DIR / "README.md").write_text(indexes.render_top_index(all_entries), encoding="utf-8")
    for year, entries in entries_by_year.items():
        year_dir = PAPERS_DIR / year
        year_dir.mkdir(parents=True, exist_ok=True)
        (year_dir / "README.md").write_text(
            indexes.render_year_index(year, entries), encoding="utf-8"
        )


def log_conversion_error(log_path: Path, arxiv_id: str, stage: str, error: str) -> None:
    """Append a JSON line to .cache/conversion_errors.jsonl."""
    import json
    from datetime import datetime, timezone

    log_path.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "arxiv_id": arxiv_id,
        "stage": stage,
        "error": error,
        "ts": datetime.now(tz=timezone.utc).isoformat(timespec="seconds"),
    }
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")


def _count_recent_failures(log_path: Path, arxiv_id: str) -> int:
    """Count how many times *arxiv_id* appears in the error log."""
    if not log_path.exists():
        return 0
    import json

    count = 0
    for line in log_path.read_text(encoding="utf-8").splitlines():
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        if rec.get("arxiv_id") == arxiv_id:
            count += 1
    return count


def record_failure_and_maybe_escalate(
    log_path: Path,
    fixme_path: Path,
    arxiv_id: str,
    stage: str,
    error: str,
    threshold: int = 3,
) -> None:
    """Log the failure; if cumulative count >= threshold, append to fixme.txt."""
    log_conversion_error(log_path, arxiv_id, stage, error)
    if _count_recent_failures(log_path, arxiv_id) >= threshold:
        from scripts._convert.remediation import append_to_fixme

        append_to_fixme(fixme_path, arxiv_id)


if __name__ == "__main__":
    main()
