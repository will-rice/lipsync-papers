"""Convert extracted LaTeX source to markdown via pandoc."""

from __future__ import annotations

import logging
import subprocess
from dataclasses import dataclass
from pathlib import Path

PANDOC_TIMEOUT_SECONDS = 120


@dataclass
class LatexConversionResult:
    """Outcome of a single pandoc invocation."""

    body: str  # rendered markdown
    bbl_text: str  # raw .bbl contents (or "")
    bib_text: str  # raw .bib contents when no .bbl was generated (or "")
    exit_code: int
    stderr: str


def find_main_tex(extracted: Path) -> Path | None:
    """Identify the main .tex file in an extracted arXiv source tree.

    Heuristic: pick the largest .tex file (arXiv submissions almost always have one
    dominant document); ties broken by name preference (main.tex > paper.tex > ...).
    """
    tex_files = list(extracted.rglob("*.tex"))
    if not tex_files:
        return None
    preferred_names = {"main.tex", "paper.tex", "ms.tex"}
    preferred = [t for t in tex_files if t.name in preferred_names]
    if preferred:
        return max(preferred, key=lambda p: p.stat().st_size)
    return max(tex_files, key=lambda p: p.stat().st_size)


def find_bbl(extracted: Path) -> Path | None:
    """Return the .bbl file (rendered bibliography) if present."""
    bbls = list(extracted.rglob("*.bbl"))
    if not bbls:
        return None
    return max(bbls, key=lambda p: p.stat().st_size)


def find_bib(extracted: Path) -> Path | None:
    """Return the largest .bib file (BibTeX source) if present."""
    bibs = list(extracted.rglob("*.bib"))
    if not bibs:
        return None
    return max(bibs, key=lambda p: p.stat().st_size)


def convert_latex_to_md(extracted: Path) -> LatexConversionResult:
    """Run pandoc on the main .tex file, return the markdown body and .bbl text.

    Pandoc args:
      --from latex
      --to gfm                  # GitHub-flavored markdown
      --wrap=none               # don't reflow; keep line structure
      --citeproc=false          # leave \\cite{...} as raw text for our citation pass
      --resource-path=<extracted>  # so \\input{} resolves
    """
    main = find_main_tex(extracted)
    if main is None:
        return LatexConversionResult(
            body="", bbl_text="", bib_text="", exit_code=2, stderr="no .tex file"
        )

    cmd = [
        "pandoc",
        "--from=latex",
        "--to=gfm",
        "--wrap=none",
        f"--resource-path={extracted}",
        str(main),
    ]
    logging.info("Running: %s", " ".join(cmd))
    proc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=PANDOC_TIMEOUT_SECONDS,
        cwd=extracted,
    )

    bbl = find_bbl(extracted)
    bbl_text = bbl.read_text(encoding="utf-8", errors="replace") if bbl else ""
    bib_text = ""
    if not bbl_text:
        bib = find_bib(extracted)
        bib_text = bib.read_text(encoding="utf-8", errors="replace") if bib else ""

    return LatexConversionResult(
        body=proc.stdout,
        bbl_text=bbl_text,
        bib_text=bib_text,
        exit_code=proc.returncode,
        stderr=proc.stderr,
    )
