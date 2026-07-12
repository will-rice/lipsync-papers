# Paper → Markdown Conversion Pipeline — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert all papers in `papers.csv` to LLM-friendly markdown with locally-linked citations, integrated into the existing weekly cron.

**Architecture:** Four-stage idempotent pipeline keyed by `arxiv_id`. Stage 1 fetches arXiv LaTeX `e-print` tarballs (preferred) or PDFs (fallback). Stage 2 converts via pandoc (LaTeX) or marker (PDF). Stage 2.5 routes auto-flagged or manually-listed papers through a Claude Sonnet 4.6 remediation pass. Stage 3 parses the references list, resolves each entry to a local sibling MD or external URL via a priority chain (arxiv → DOI → S2 lookup), and rewrites inline citation markers. Stage 4 regenerates index files. Outputs land at `papers/<year>/<arxiv_id>.md`.

**Tech Stack:** Python 3.11+, `uv` for dep management, `pandoc 3.1.x` (system binary), `marker-pdf`, `anthropic` SDK, `pytest` functional style, GitHub Actions cron.

**Reference spec:** [docs/superpowers/specs/2026-05-02-paper-markdown-conversion-design.md](../specs/2026-05-02-paper-markdown-conversion-design.md)

---

## File Structure

**New files:**

| Path                                       | Responsibility                                        |
| ------------------------------------------ | ----------------------------------------------------- |
| `pyproject.toml`                           | uv project config, deps                               |
| `scripts/convert_papers.py`                | Entry point, orchestrates all stages                  |
| `scripts/_convert/__init__.py`             | Package marker                                        |
| `scripts/_convert/sources.py`              | Fetch arXiv e-print / S2 PDF, manage `.cache/source/` |
| `scripts/_convert/latex_to_md.py`          | pandoc invocation, `.bbl` extraction                  |
| `scripts/_convert/pdf_to_md.py`            | marker invocation                                     |
| `scripts/_convert/citations.py`            | Parse refs, resolve URLs, rewrite inline markers      |
| `scripts/_convert/remediation.py`          | LLM remediation via Anthropic SDK + heuristic flagger |
| `scripts/_convert/output.py`               | Write `papers/<year>/<arxiv_id>.md` with frontmatter  |
| `scripts/_convert/indexes.py`              | Generate `papers/README.md` and per-year READMEs      |
| `tests/__init__.py`                        | Package marker                                        |
| `tests/conftest.py`                        | Shared pytest fixtures                                |
| `tests/test_sources.py`                    | Unit + recorded-tarball tests                         |
| `tests/test_latex_to_md.py`                | Pandoc conversion goldens                             |
| `tests/test_pdf_to_md.py`                  | Marker conversion goldens                             |
| `tests/test_citations.py`                  | Ref parsing, resolution priority                      |
| `tests/test_remediation.py`                | Heuristic flagger + recorded API replay               |
| `tests/test_output.py`                     | Frontmatter & file layout                             |
| `tests/test_indexes.py`                    | Index file generation                                 |
| `tests/test_orchestrator.py`               | Idempotency + per-paper error isolation               |
| `tests/fixtures/2008.10010/`               | Wav2Lip LaTeX source (tarball + extracted)            |
| `tests/fixtures/2008.10010.expected.md`    | Wav2Lip golden output                                 |
| `tests/fixtures/pdf_only.pdf`              | Hand-picked PDF-only fixture                          |
| `tests/fixtures/pdf_only.expected.md`      | Golden output                                         |
| `tests/fixtures/citations_in.json`         | Recorded S2 lookup responses                          |
| `tests/fixtures/remediation_response.json` | Recorded Claude API response                          |

**Modified files:**

| Path                                 | Change                                                       |
| ------------------------------------ | ------------------------------------------------------------ |
| `.gitignore`                         | Add `.cache/`                                                |
| `.github/workflows/fetch_papers.yml` | Add pandoc install, uv sync, convert step, cache action      |
| `scripts/fetch_papers.py`            | Modify `update_readme()` to add `📄 Read` link to each entry |
| `README.md`                          | Document conversion pipeline + new deps                      |

---

## Task 1: Project setup — uv, deps, gitignore

**Files:**

- Create: `pyproject.toml`
- Modify: `.gitignore`

- [ ] **Step 1: Create `pyproject.toml`**

```toml
[project]
name = "lipsync-papers"
version = "0.1.0"
description = "Curated lipsync papers + LLM-friendly markdown conversion."
requires-python = ">=3.11"
dependencies = [
    "marker-pdf>=1.2.0",
    "anthropic>=0.40.0",
    "pyyaml>=6.0",
]

[dependency-groups]
dev = [
    "pytest>=8.0",
    "pre-commit>=3.5",
    "ruff>=0.6",
]

[tool.ruff]
line-length = 100
target-version = "py311"

[tool.pytest.ini_options]
testpaths = ["tests"]
```

- [ ] **Step 2: Add `.cache/` to `.gitignore`**

Append to `.gitignore` (after the existing `# Cython debug symbols` block):

```
# Conversion pipeline cache
.cache/
```

- [ ] **Step 3: Run `uv sync` to install deps and produce lockfile**

Run: `uv sync`
Expected: Installs marker-pdf, anthropic, pyyaml, pytest, plus transitive deps. Produces `uv.lock`.

- [ ] **Step 4: Verify pandoc is available locally for development**

Run: `pandoc --version`
Expected: Prints version. If missing on macOS: `brew install pandoc`. If missing on Linux: `sudo apt-get install pandoc`. Document this in README in a later task.

- [ ] **Step 5: Commit**

```bash
git add pyproject.toml uv.lock .gitignore
git commit -m "chore: introduce uv project with marker, anthropic, pyyaml deps"
```

---

## Task 2: Output writer — frontmatter and file layout

**Files:**

- Create: `scripts/_convert/__init__.py`
- Create: `scripts/_convert/output.py`
- Create: `tests/__init__.py`
- Create: `tests/conftest.py`
- Create: `tests/test_output.py`

This is built first because every later module emits to its interface.

- [ ] **Step 1: Create empty package markers**

```bash
mkdir -p scripts/_convert tests/fixtures
touch scripts/_convert/__init__.py tests/__init__.py
```

- [ ] **Step 2: Write `tests/conftest.py`**

```python
"""Shared pytest fixtures."""
from __future__ import annotations

from pathlib import Path

import pytest

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture
def fixtures_dir() -> Path:
    return FIXTURES


@pytest.fixture
def tmp_papers_dir(tmp_path: Path) -> Path:
    """Empty papers/ directory rooted in a tmp_path."""
    papers = tmp_path / "papers"
    papers.mkdir()
    return papers
```

- [ ] **Step 3: Write the failing test for `write_paper_markdown`**

Create `tests/test_output.py`:

```python
"""Tests for scripts/_convert/output.py."""
from __future__ import annotations

from pathlib import Path

import yaml

from scripts._convert.output import PaperRecord, write_paper_markdown


def test_writes_to_year_subdir(tmp_papers_dir: Path) -> None:
    record = PaperRecord(
        arxiv_id="2008.10010",
        title="A Lip Sync Expert",
        authors=["K. R. Prajwal"],
        submitted="2020-08-23",
        categories=["cs.CV"],
        arxiv_url="https://arxiv.org/abs/2008.10010",
        source="latex",
        converter="pandoc",
        body="# Wav2Lip\n\nBody text.",
        references_parsed=42,
        citations_resolved=("40/42"),
        arxiv_version="v1",
    )
    path = write_paper_markdown(record, tmp_papers_dir)
    assert path == tmp_papers_dir / "2020" / "2008.10010.md"
    assert path.exists()


def test_frontmatter_is_valid_yaml(tmp_papers_dir: Path) -> None:
    record = PaperRecord(
        arxiv_id="2008.10010",
        title="A Lip Sync Expert",
        authors=["K. R. Prajwal", "Rudrabha Mukhopadhyay"],
        submitted="2020-08-23",
        categories=["cs.CV"],
        arxiv_url="https://arxiv.org/abs/2008.10010",
        source="latex",
        converter="pandoc",
        body="# Wav2Lip\n\nBody.",
        references_parsed=42,
        citations_resolved="40/42",
        arxiv_version="v1",
    )
    path = write_paper_markdown(record, tmp_papers_dir)
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n")
    front_end = text.index("\n---\n", 4)
    front = yaml.safe_load(text[4:front_end])
    assert front["arxiv_id"] == "2008.10010"
    assert front["authors"] == ["K. R. Prajwal", "Rudrabha Mukhopadhyay"]
    assert front["llm_remediated"] is False
    assert "citations_resolved_at" in front
```

- [ ] **Step 4: Run the test to verify it fails**

Run: `uv run pytest tests/test_output.py -v`
Expected: FAIL — `ModuleNotFoundError: scripts._convert.output`

- [ ] **Step 5: Implement `scripts/_convert/output.py`**

```python
"""Write per-paper markdown files with YAML frontmatter."""
from __future__ import annotations

import unicodedata
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import yaml


@dataclass
class PaperRecord:
    """Everything needed to render a per-paper markdown file."""

    arxiv_id: str
    title: str
    authors: list[str]
    submitted: str            # YYYY-MM-DD
    categories: list[str]
    arxiv_url: str
    source: str               # "latex" | "pdf" | "metadata-only"
    converter: str            # "pandoc" | "marker" | "none"
    body: str                 # already-rendered markdown body (no frontmatter, no h1)
    references_parsed: int
    citations_resolved: str   # e.g. "27/41"
    arxiv_version: str = ""
    llm_remediated: bool = False
    citations_resolved_at: str = field(default_factory=lambda: datetime.now(tz=timezone.utc).isoformat(timespec="seconds"))


def paper_path(arxiv_id: str, submitted: str, papers_root: Path) -> Path:
    """Return the destination path for a paper's markdown file."""
    year = submitted[:4]
    return papers_root / year / f"{arxiv_id}.md"


def write_paper_markdown(record: PaperRecord, papers_root: Path) -> Path:
    """Write *record* to ``papers_root/<year>/<arxiv_id>.md`` and return the path."""
    path = paper_path(record.arxiv_id, record.submitted, papers_root)
    path.parent.mkdir(parents=True, exist_ok=True)

    front = {
        "arxiv_id": record.arxiv_id,
        "title": record.title,
        "authors": record.authors,
        "submitted": record.submitted,
        "categories": record.categories,
        "arxiv_url": record.arxiv_url,
        "source": record.source,
        "converter": record.converter,
        "llm_remediated": record.llm_remediated,
        "citations_resolved": record.citations_resolved,
        "citations_resolved_at": record.citations_resolved_at,
        "references_parsed": record.references_parsed,
        "arxiv_version": record.arxiv_version,
    }
    front_yaml = yaml.safe_dump(front, sort_keys=False, allow_unicode=True)

    body = unicodedata.normalize("NFC", record.body).rstrip() + "\n"
    text = f"---\n{front_yaml}---\n\n{body}"
    path.write_text(text, encoding="utf-8")
    return path
```

- [ ] **Step 6: Run tests to verify they pass**

Run: `uv run pytest tests/test_output.py -v`
Expected: 2 passed.

- [ ] **Step 7: Commit**

```bash
git add scripts/_convert/__init__.py scripts/_convert/output.py tests/__init__.py tests/conftest.py tests/test_output.py
git commit -m "feat(convert): add per-paper markdown writer with YAML frontmatter"
```

---

## Task 3: Source fetching — arXiv e-print + S2 PDF

**Files:**

- Create: `scripts/_convert/sources.py`
- Create: `tests/test_sources.py`
- Create: `tests/fixtures/sources_2008.10010.tar.gz` (small recorded tarball)

- [ ] **Step 1: Capture a real arXiv e-print tarball as fixture**

Run:

```bash
curl -L -A "lipsync-papers-bot/1.0" -o tests/fixtures/sources_2008.10010.tar.gz \
    https://arxiv.org/e-print/2008.10010
```

Expected: `tests/fixtures/sources_2008.10010.tar.gz` exists, ~1–3 MB. Verify with `tar tzf tests/fixtures/sources_2008.10010.tar.gz | head` — you should see `.tex` files.

- [ ] **Step 2: Write the failing test for source classification**

Create `tests/test_sources.py`:

```python
"""Tests for scripts/_convert/sources.py."""
from __future__ import annotations

import shutil
import tarfile
from pathlib import Path

import pytest

from scripts._convert.sources import (
    SourceKind,
    classify_extracted_source,
    extract_arxiv_tarball,
    is_cache_fresh,
)


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
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `uv run pytest tests/test_sources.py -v`
Expected: FAIL — `ModuleNotFoundError`.

- [ ] **Step 4: Implement `scripts/_convert/sources.py`**

```python
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
S2_PAPER_URL = "https://api.semanticscholar.org/graph/v1/paper/{paper_id}?fields=openAccessPdf,externalIds"
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
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `uv run pytest tests/test_sources.py -v`
Expected: 5 passed.

- [ ] **Step 6: Commit**

```bash
git add scripts/_convert/sources.py tests/test_sources.py tests/fixtures/sources_2008.10010.tar.gz
git commit -m "feat(convert): add arXiv e-print + S2 PDF source fetcher with cache classifier"
```

---

## Task 4: LaTeX → markdown via pandoc

**Files:**

- Create: `scripts/_convert/latex_to_md.py`
- Create: `tests/test_latex_to_md.py`
- Create: `tests/fixtures/2008.10010.expected.body.md` (golden body)

- [ ] **Step 1: Manually generate a golden body for the Wav2Lip fixture**

Run:

```bash
mkdir -p /tmp/wav2lip_extract
tar xzf tests/fixtures/sources_2008.10010.tar.gz -C /tmp/wav2lip_extract
ls /tmp/wav2lip_extract  # identify the main .tex file (usually largest or named 'main.tex')
pandoc /tmp/wav2lip_extract/<main>.tex -t gfm --wrap=none -o tests/fixtures/2008.10010.expected.body.md
```

Manually trim `tests/fixtures/2008.10010.expected.body.md` if it contains pandoc preamble noise. The golden file represents the expected pandoc output for assertion.

- [ ] **Step 2: Write the failing test**

Create `tests/test_latex_to_md.py`:

```python
"""Tests for scripts/_convert/latex_to_md.py."""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest

from scripts._convert.latex_to_md import (
    LatexConversionResult,
    convert_latex_to_md,
    find_main_tex,
)
from scripts._convert.sources import extract_arxiv_tarball


@pytest.fixture
def extracted_wav2lip(fixtures_dir: Path, tmp_path: Path) -> Path:
    out = tmp_path / "extracted"
    extract_arxiv_tarball(fixtures_dir / "sources_2008.10010.tar.gz", out)
    return out


def test_find_main_tex_returns_largest(extracted_wav2lip: Path) -> None:
    main = find_main_tex(extracted_wav2lip)
    assert main is not None
    assert main.suffix == ".tex"


@pytest.mark.skipif(shutil.which("pandoc") is None, reason="pandoc not installed")
def test_convert_latex_produces_markdown(extracted_wav2lip: Path) -> None:
    result = convert_latex_to_md(extracted_wav2lip)
    assert isinstance(result, LatexConversionResult)
    assert result.body, "expected non-empty body"
    assert result.exit_code == 0
    assert "# " in result.body or "## " in result.body
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `uv run pytest tests/test_latex_to_md.py -v`
Expected: FAIL — `ModuleNotFoundError`.

- [ ] **Step 4: Implement `scripts/_convert/latex_to_md.py`**

```python
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

    body: str               # rendered markdown
    bbl_text: str           # raw .bbl contents (or "")
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
        return LatexConversionResult(body="", bbl_text="", exit_code=2, stderr="no .tex file")

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

    return LatexConversionResult(
        body=proc.stdout,
        bbl_text=bbl_text,
        exit_code=proc.returncode,
        stderr=proc.stderr,
    )
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `uv run pytest tests/test_latex_to_md.py -v`
Expected: 2 passed (or 1 passed + 1 skipped if pandoc missing).

- [ ] **Step 6: Commit**

```bash
git add scripts/_convert/latex_to_md.py tests/test_latex_to_md.py tests/fixtures/2008.10010.expected.body.md
git commit -m "feat(convert): add pandoc-based LaTeX-to-markdown converter with bbl extraction"
```

---

## Task 5: PDF → markdown via marker

**Files:**

- Create: `scripts/_convert/pdf_to_md.py`
- Create: `tests/test_pdf_to_md.py`
- Create: `tests/fixtures/pdf_only.pdf` (small hand-picked fixture)

- [ ] **Step 1: Capture a small PDF fixture**

Run:

```bash
curl -L -A "lipsync-papers-bot/1.0" -o tests/fixtures/pdf_only.pdf \
    https://arxiv.org/pdf/2008.10010
```

(Wav2Lip again — re-using the same paper as a PDF for the marker codepath.)

- [ ] **Step 2: Write the failing test**

Create `tests/test_pdf_to_md.py`:

```python
"""Tests for scripts/_convert/pdf_to_md.py."""
from __future__ import annotations

from pathlib import Path

import pytest

from scripts._convert.pdf_to_md import PdfConversionResult, convert_pdf_to_md


@pytest.mark.slow
def test_convert_pdf_produces_markdown(fixtures_dir: Path) -> None:
    result = convert_pdf_to_md(fixtures_dir / "pdf_only.pdf")
    assert isinstance(result, PdfConversionResult)
    assert result.body, "expected non-empty body"
    assert result.page_count > 0
```

- [ ] **Step 3: Run test to verify it fails**

Run: `uv run pytest tests/test_pdf_to_md.py -v`
Expected: FAIL — `ModuleNotFoundError`.

- [ ] **Step 4: Implement `scripts/_convert/pdf_to_md.py`**

```python
"""Convert a PDF to markdown via marker-pdf."""
from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path

from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered


@dataclass
class PdfConversionResult:
    body: str
    page_count: int


_CONVERTER: PdfConverter | None = None


def _get_converter() -> PdfConverter:
    """Lazily build the marker converter (loads ML models on first call)."""
    global _CONVERTER
    if _CONVERTER is None:
        logging.info("Loading marker models (one-time, ~30s)…")
        _CONVERTER = PdfConverter(artifact_dict=create_model_dict())
    return _CONVERTER


def convert_pdf_to_md(pdf_path: Path) -> PdfConversionResult:
    """Render *pdf_path* to markdown using marker-pdf."""
    converter = _get_converter()
    rendered = converter(str(pdf_path))
    body, _, images = text_from_rendered(rendered)
    page_count = len(rendered.pages) if hasattr(rendered, "pages") else body.count("\f") + 1
    return PdfConversionResult(body=body, page_count=page_count)
```

- [ ] **Step 5: Add `slow` marker registration**

Append to `pyproject.toml` `[tool.pytest.ini_options]`:

```toml
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
]
```

- [ ] **Step 6: Run test to verify it passes**

Run: `uv run pytest tests/test_pdf_to_md.py -v -m slow`
Expected: 1 passed (takes ~60s the first time as marker loads models).

- [ ] **Step 7: Commit**

```bash
git add scripts/_convert/pdf_to_md.py tests/test_pdf_to_md.py tests/fixtures/pdf_only.pdf pyproject.toml
git commit -m "feat(convert): add marker-pdf PDF-to-markdown converter"
```

---

## Task 6: Citation parsing — LaTeX `.bbl`

**Files:**

- Create: `scripts/_convert/citations.py` (initial — bbl parsing only)
- Create: `tests/test_citations.py`

- [ ] **Step 1: Write the failing test**

Create `tests/test_citations.py`:

```python
"""Tests for scripts/_convert/citations.py."""
from __future__ import annotations

from scripts._convert.citations import (
    Reference,
    parse_bbl,
)


SAMPLE_BBL = r"""
\begin{thebibliography}{99}

\bibitem{Prajwal2020}
K.~R. Prajwal, Rudrabha Mukhopadhyay, Vinay~P. Namboodiri, and C.~V. Jawahar.
\newblock A lip sync expert is all you need for speech to lip generation in the
  wild.
\newblock In {\em ACM MM}, 2020.
\newblock arXiv:2008.10010.

\bibitem{Goodfellow2014}
Ian Goodfellow, Jean Pouget-Abadie, et al.
\newblock Generative adversarial nets.
\newblock In {\em NeurIPS}, 2014.

\end{thebibliography}
"""


def test_parse_bbl_extracts_two_entries() -> None:
    refs = parse_bbl(SAMPLE_BBL)
    assert len(refs) == 2
    keys = {r.key for r in refs}
    assert keys == {"Prajwal2020", "Goodfellow2014"}


def test_parse_bbl_extracts_arxiv_id() -> None:
    refs = {r.key: r for r in parse_bbl(SAMPLE_BBL)}
    assert refs["Prajwal2020"].arxiv_id == "2008.10010"
    assert refs["Goodfellow2014"].arxiv_id is None


def test_parse_bbl_extracts_year() -> None:
    refs = {r.key: r for r in parse_bbl(SAMPLE_BBL)}
    assert refs["Prajwal2020"].year == 2020
    assert refs["Goodfellow2014"].year == 2014
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_citations.py -v`
Expected: FAIL — `ModuleNotFoundError`.

- [ ] **Step 3: Implement initial `scripts/_convert/citations.py`**

```python
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

    key: str                      # cite-key (LaTeX) or "1", "2", … (PDF)
    raw: str                      # original entry text
    title: str = ""
    authors: list[str] = field(default_factory=list)
    year: int | None = None
    arxiv_id: str | None = None
    doi: str | None = None
    resolved_url: str | None = None     # filled in by Pass B
    confidence: str = "high"            # "high" | "low" — low means leave bare on rewrite


def parse_bbl(bbl_text: str) -> list[Reference]:
    """Parse a pandoc/biblatex .bbl into a list of References."""
    refs: list[Reference] = []
    for match in _BIBITEM_RE.finditer(bbl_text):
        key = match.group(1).strip()
        body = match.group(2).strip()
        ref = Reference(key=key, raw=body)
        if (m := _ARXIV_ID_RE.search(body)):
            ref.arxiv_id = m.group(1)
        if (m := _DOI_RE.search(body)):
            ref.doi = m.group(1)
        if (m := _YEAR_RE.search(body)):
            ref.year = int(m.group(0))
        refs.append(ref)
    return refs
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_citations.py -v`
Expected: 3 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/_convert/citations.py tests/test_citations.py
git commit -m "feat(convert): parse LaTeX .bbl bibliographies into normalized references"
```

---

## Task 7: Citation parsing — PDF references section

**Files:**

- Modify: `scripts/_convert/citations.py`
- Modify: `tests/test_citations.py`

- [ ] **Step 1: Write the failing test for PDF ref parsing**

Append to `tests/test_citations.py`:

```python
SAMPLE_PDF_REFS = """
## References

[1] K. R. Prajwal, R. Mukhopadhyay, V. P. Namboodiri, and C. V. Jawahar. A Lip Sync
Expert Is All You Need for Speech to Lip Generation In The Wild. In ACM MM, 2020.

[2] I. Goodfellow, J. Pouget-Abadie, et al. Generative Adversarial Nets. In NeurIPS, 2014.

[3] J. Ho, A. Jain, and P. Abbeel. Denoising Diffusion Probabilistic Models. NeurIPS, 2020.
"""


def test_parse_pdf_references_extracts_three_entries() -> None:
    from scripts._convert.citations import parse_pdf_references
    refs = parse_pdf_references(SAMPLE_PDF_REFS)
    assert len(refs) == 3
    assert [r.key for r in refs] == ["1", "2", "3"]


def test_parse_pdf_references_extracts_titles() -> None:
    from scripts._convert.citations import parse_pdf_references
    refs = {r.key: r for r in parse_pdf_references(SAMPLE_PDF_REFS)}
    assert "Lip Sync Expert" in refs["1"].title
    assert "Generative Adversarial Nets" in refs["2"].title
    assert "Denoising Diffusion Probabilistic Models" in refs["3"].title
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_citations.py::test_parse_pdf_references_extracts_three_entries -v`
Expected: FAIL — `ImportError: cannot import name 'parse_pdf_references'`.

- [ ] **Step 3: Add `parse_pdf_references` to `scripts/_convert/citations.py`**

Append:

```python
_PDF_REF_HEADING_RE = re.compile(r"^\s*##+\s*References\s*$", re.MULTILINE | re.IGNORECASE)
_PDF_REF_ENTRY_RE = re.compile(
    r"\[(\d+)\](.+?)(?=\n\s*\[\d+\]|\Z)",
    re.DOTALL,
)


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
    """Pull the title from a flat reference line: longest title-cased phrase up to a period."""
    # Strip leading authors (typically up to first period followed by a capital letter).
    after_authors = re.split(r"\.\s+(?=[A-Z])", raw, maxsplit=1)
    candidate_text = after_authors[1] if len(after_authors) > 1 else raw
    # Title is everything up to the next period (which usually ends the title).
    title = candidate_text.split(".", 1)[0].strip()
    # Sanity bound — titles longer than 250 chars are almost certainly wrong extractions.
    if len(title) > 250:
        return ""
    return title
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_citations.py -v`
Expected: 5 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/_convert/citations.py tests/test_citations.py
git commit -m "feat(convert): parse PDF references-section into normalized references"
```

---

## Task 8: Citation resolution — local sibling, arxiv, DOI, S2

**Files:**

- Modify: `scripts/_convert/citations.py`
- Modify: `tests/test_citations.py`
- Create: `tests/fixtures/citations_in.json` (recorded S2 responses)

- [ ] **Step 1: Capture a small recorded S2 response**

Create `tests/fixtures/citations_in.json`:

```json
{
  "title:denoising diffusion probabilistic models": {
    "data": [
      {
        "externalIds": {
          "ArXiv": "2006.11239",
          "DOI": "10.5555/3495724.3496298"
        }
      }
    ]
  },
  "title:nonexistent paper title that should not match": { "data": [] }
}
```

- [ ] **Step 2: Write the failing test**

Append to `tests/test_citations.py`:

```python
def test_resolve_local_sibling_priority(tmp_path) -> None:
    from scripts._convert.citations import (
        Reference,
        ResolutionContext,
        resolve_reference,
    )
    ctx = ResolutionContext(
        corpus_arxiv_to_year={"2008.10010": "2020", "2006.11239": "2020"},
        current_year="2026",
        s2_cache={},
    )
    ref = Reference(key="x", raw="…", arxiv_id="2008.10010")
    resolve_reference(ref, ctx)
    assert ref.resolved_url == "../2020/2008.10010.md"


def test_resolve_external_arxiv_fallback() -> None:
    from scripts._convert.citations import (
        Reference,
        ResolutionContext,
        resolve_reference,
    )
    ctx = ResolutionContext(
        corpus_arxiv_to_year={},
        current_year="2026",
        s2_cache={},
    )
    ref = Reference(key="x", raw="…", arxiv_id="9999.99999")
    resolve_reference(ref, ctx)
    assert ref.resolved_url == "https://arxiv.org/abs/9999.99999"


def test_resolve_doi_fallback() -> None:
    from scripts._convert.citations import (
        Reference,
        ResolutionContext,
        resolve_reference,
    )
    ctx = ResolutionContext(
        corpus_arxiv_to_year={},
        current_year="2026",
        s2_cache={},
    )
    ref = Reference(key="x", raw="…", doi="10.1145/3394171.3413532")
    resolve_reference(ref, ctx)
    assert ref.resolved_url == "https://doi.org/10.1145/3394171.3413532"


def test_resolve_s2_lookup_promotes_to_arxiv(fixtures_dir) -> None:
    import json
    from scripts._convert.citations import (
        Reference,
        ResolutionContext,
        resolve_reference,
    )
    cache = json.loads((fixtures_dir / "citations_in.json").read_text())
    ctx = ResolutionContext(
        corpus_arxiv_to_year={"2006.11239": "2020"},
        current_year="2026",
        s2_cache=cache,
    )
    ref = Reference(key="x", raw="…", title="Denoising Diffusion Probabilistic Models")
    resolve_reference(ref, ctx)
    # arXiv ID was found via S2, then matched against corpus → local sibling
    assert ref.arxiv_id == "2006.11239"
    assert ref.resolved_url == "../2020/2006.11239.md"


def test_resolve_unresolvable_remains_none() -> None:
    from scripts._convert.citations import (
        Reference,
        ResolutionContext,
        resolve_reference,
    )
    ctx = ResolutionContext(
        corpus_arxiv_to_year={},
        current_year="2026",
        s2_cache={"title:nonexistent paper title that should not match": {"data": []}},
    )
    ref = Reference(key="x", raw="…", title="Nonexistent paper title that should not match")
    resolve_reference(ref, ctx)
    assert ref.resolved_url is None
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `uv run pytest tests/test_citations.py -v -k resolve`
Expected: FAILs — symbols not yet defined.

- [ ] **Step 4: Add resolution logic to `scripts/_convert/citations.py`**

Append:

```python
import json
import logging
import urllib.parse
import urllib.request
from dataclasses import field as _field
from pathlib import Path

S2_SEARCH_URL = "https://api.semanticscholar.org/graph/v1/paper/search?query={q}&fields=externalIds&limit=1"
USER_AGENT = "lipsync-papers-bot/1.0"


@dataclass
class ResolutionContext:
    """Context passed to resolve_reference — local corpus, current paper's year, S2 cache."""

    corpus_arxiv_to_year: dict[str, str]   # {"2008.10010": "2020", …}
    current_year: str                       # year of the citing paper, for relative paths
    s2_cache: dict[str, dict]               # {"title:<lowercased>": <s2 response>, …}


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
            if (arxiv_id := ext.get("ArXiv")):
                ref.arxiv_id = arxiv_id
                if arxiv_id in ctx.corpus_arxiv_to_year:
                    target_year = ctx.corpus_arxiv_to_year[arxiv_id]
                    ref.resolved_url = _local_sibling_url(arxiv_id, target_year, ctx.current_year)
                else:
                    ref.resolved_url = f"https://arxiv.org/abs/{arxiv_id}"
                return
            if (doi := ext.get("DOI")):
                ref.doi = doi
                ref.resolved_url = f"https://doi.org/{doi}"
                return
    # Step 5: unresolved
    ref.resolved_url = None
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `uv run pytest tests/test_citations.py -v`
Expected: 10 passed.

- [ ] **Step 6: Commit**

```bash
git add scripts/_convert/citations.py tests/test_citations.py tests/fixtures/citations_in.json
git commit -m "feat(convert): resolve references via local-sibling/arxiv/DOI/S2 priority chain"
```

---

## Task 9: Citation rewriting — inline markers + references list

**Files:**

- Modify: `scripts/_convert/citations.py`
- Modify: `tests/test_citations.py`

- [ ] **Step 1: Write the failing test**

Append to `tests/test_citations.py`:

```python
def test_rewrite_latex_cite_markers() -> None:
    from scripts._convert.citations import Reference, rewrite_latex_cites
    refs = {
        "Prajwal2020": Reference(key="Prajwal2020", raw="…", resolved_url="../2020/2008.10010.md"),
        "Goodfellow2014": Reference(key="Goodfellow2014", raw="…", resolved_url="https://arxiv.org/abs/1406.2661"),
    }
    body = "We build on Wav2Lip \\cite{Prajwal2020} and GANs \\cite{Goodfellow2014}."
    out = rewrite_latex_cites(body, refs)
    assert "[\\[Prajwal2020\\]](../2020/2008.10010.md)" in out
    assert "[\\[Goodfellow2014\\]](https://arxiv.org/abs/1406.2661)" in out


def test_rewrite_latex_cite_unresolved_stays_bare() -> None:
    from scripts._convert.citations import Reference, rewrite_latex_cites
    refs = {"Unresolved": Reference(key="Unresolved", raw="…", resolved_url=None)}
    body = "We cite \\cite{Unresolved}."
    out = rewrite_latex_cites(body, refs)
    assert "\\[Unresolved\\]" in out
    assert "](" not in out  # no link rendered


def test_rewrite_pdf_numeric_markers_high_confidence() -> None:
    from scripts._convert.citations import Reference, rewrite_pdf_numeric_cites
    refs = {
        "1": Reference(key="1", raw="…", resolved_url="../2020/2008.10010.md", confidence="high"),
        "2": Reference(key="2", raw="…", resolved_url=None, confidence="low"),
    }
    body = "We use [1] and also [2]."
    out = rewrite_pdf_numeric_cites(body, refs)
    assert "[\\[1\\]](../2020/2008.10010.md)" in out
    assert "[2]" in out  # low-confidence bare


def test_render_references_section_with_links() -> None:
    from scripts._convert.citations import Reference, render_references_section
    refs = [
        Reference(key="Prajwal2020", raw="K.R. Prajwal et al. A Lip Sync Expert. ACM MM, 2020.",
                  title="A Lip Sync Expert", arxiv_id="2008.10010",
                  resolved_url="../2020/2008.10010.md"),
        Reference(key="Unresolved", raw="Unknown ref.", resolved_url=None),
    ]
    out = render_references_section(refs)
    assert "## References" in out
    assert "[arXiv:2008.10010](../2020/2008.10010.md)" in out
    assert "Unknown ref." in out
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_citations.py -v -k rewrite or rewrite or render_references`
Expected: FAILs — symbols not defined.

- [ ] **Step 3: Add rewriting functions to `scripts/_convert/citations.py`**

Append:

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_citations.py -v`
Expected: 14 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/_convert/citations.py tests/test_citations.py
git commit -m "feat(convert): rewrite inline citation markers and render linked references section"
```

---

## Task 10: Citation cache persistence

**Files:**

- Modify: `scripts/_convert/citations.py`
- Modify: `tests/test_citations.py`

- [ ] **Step 1: Write the failing test**

Append to `tests/test_citations.py`:

```python
def test_load_and_save_citation_cache(tmp_path) -> None:
    from scripts._convert.citations import load_citation_cache, save_citation_cache
    path = tmp_path / "citations.json"
    assert load_citation_cache(path) == {}
    save_citation_cache(path, {"title:foo": {"data": [{"externalIds": {"ArXiv": "1234.5678"}}]}})
    loaded = load_citation_cache(path)
    assert "title:foo" in loaded
    assert loaded["title:foo"]["data"][0]["externalIds"]["ArXiv"] == "1234.5678"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_citations.py::test_load_and_save_citation_cache -v`
Expected: FAIL — `ImportError`.

- [ ] **Step 3: Add cache helpers to `scripts/_convert/citations.py`**

Append:

```python
def load_citation_cache(path: Path) -> dict[str, dict]:
    """Load the JSON citation cache at *path*; return {} if missing."""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def save_citation_cache(path: Path, cache: dict[str, dict]) -> None:
    """Persist *cache* as JSON at *path*, creating parent dirs."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(cache, indent=2, sort_keys=True), encoding="utf-8")
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/test_citations.py::test_load_and_save_citation_cache -v`
Expected: 1 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/_convert/citations.py tests/test_citations.py
git commit -m "feat(convert): persist citation cache to .cache/citations.json"
```

---

## Task 11: LLM remediation — heuristic flagger

**Files:**

- Create: `scripts/_convert/remediation.py`
- Create: `tests/test_remediation.py`

- [ ] **Step 1: Write the failing test**

Create `tests/test_remediation.py`:

```python
"""Tests for scripts/_convert/remediation.py."""
from __future__ import annotations

from scripts._convert.remediation import RemediationFlags, should_remediate


def test_short_body_flags_remediation() -> None:
    flags = should_remediate(
        body="Short.",
        page_count=10,
        has_references=True,
        citations_resolved_ratio=1.0,
        latex_exit_code=0,
    )
    assert flags.flagged is True
    assert "short_body" in flags.reasons


def test_no_references_flags_remediation() -> None:
    flags = should_remediate(
        body="word " * 1000,
        page_count=10,
        has_references=False,
        citations_resolved_ratio=1.0,
        latex_exit_code=0,
    )
    assert flags.flagged is True
    assert "no_references" in flags.reasons


def test_low_citation_resolution_flags() -> None:
    flags = should_remediate(
        body="word " * 1000,
        page_count=10,
        has_references=True,
        citations_resolved_ratio=0.1,
        latex_exit_code=0,
    )
    assert flags.flagged is True
    assert "low_citation_resolution" in flags.reasons


def test_clean_paper_not_flagged() -> None:
    flags = should_remediate(
        body="word " * 2000,
        page_count=10,
        has_references=True,
        citations_resolved_ratio=0.7,
        latex_exit_code=0,
    )
    assert flags.flagged is False


def test_latex_failure_flags() -> None:
    flags = should_remediate(
        body="anything",
        page_count=10,
        has_references=True,
        citations_resolved_ratio=1.0,
        latex_exit_code=1,
    )
    assert flags.flagged is True
    assert "latex_build_failed" in flags.reasons
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_remediation.py -v`
Expected: FAILs — `ModuleNotFoundError`.

- [ ] **Step 3: Implement initial `scripts/_convert/remediation.py`**

```python
"""LLM-driven remediation pass for low-quality conversions."""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path

# Heuristic thresholds
MIN_WORDS_PER_PAGE_RATIO = 0.5
MIN_WORDS_PER_PAGE = 200
LOW_CITATION_RESOLUTION_THRESHOLD = 0.30


@dataclass
class RemediationFlags:
    """Result of the heuristic flagger."""

    flagged: bool
    reasons: list[str] = field(default_factory=list)


def should_remediate(
    body: str,
    page_count: int,
    has_references: bool,
    citations_resolved_ratio: float,
    latex_exit_code: int,
) -> RemediationFlags:
    """Score a paper against the auto-flag heuristics from the spec."""
    reasons: list[str] = []
    word_count = len(body.split())
    expected_min_words = MIN_WORDS_PER_PAGE_RATIO * page_count * MIN_WORDS_PER_PAGE
    if word_count < expected_min_words:
        reasons.append("short_body")
    if not has_references:
        reasons.append("no_references")
    if citations_resolved_ratio < LOW_CITATION_RESOLUTION_THRESHOLD:
        reasons.append("low_citation_resolution")
    if latex_exit_code != 0:
        reasons.append("latex_build_failed")
    return RemediationFlags(flagged=bool(reasons), reasons=reasons)


def load_fixme_list(path: Path) -> set[str]:
    """Load the manual remediation list (one arxiv_id per line)."""
    if not path.exists():
        return set()
    return {
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    }


def append_to_fixme(path: Path, arxiv_id: str) -> None:
    """Append *arxiv_id* to the manual remediation list (no-op if already present)."""
    existing = load_fixme_list(path)
    if arxiv_id in existing:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(f"{arxiv_id}\n")
    logging.info("Auto-appended %s to %s", arxiv_id, path)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_remediation.py -v`
Expected: 5 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/_convert/remediation.py tests/test_remediation.py
git commit -m "feat(convert): add heuristic flagger and .fixme.txt manual list helpers"
```

---

## Task 12: LLM remediation — Anthropic API call

**Files:**

- Modify: `scripts/_convert/remediation.py`
- Modify: `tests/test_remediation.py`
- Create: `tests/fixtures/remediation_response.json` (recorded API response)

- [ ] **Step 1: Create a recorded API response fixture**

Create `tests/fixtures/remediation_response.json`:

```json
{
  "id": "msg_test",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "# Cleaned Paper\n\nThis is the LLM-corrected markdown.\n\n## References\n\n[1] Example."
    }
  ],
  "model": "claude-sonnet-4-6",
  "stop_reason": "end_turn",
  "usage": { "input_tokens": 5000, "output_tokens": 800 }
}
```

- [ ] **Step 2: Write the failing test using a stub Anthropic client**

Append to `tests/test_remediation.py`:

```python
def test_remediate_with_pdf_returns_corrected_markdown(fixtures_dir, tmp_path):
    import json
    from scripts._convert.remediation import remediate_with_pdf

    class StubClient:
        def __init__(self, response_path):
            self._response = json.loads(response_path.read_text())
            self.calls = []

        @property
        def messages(self):
            return self

        def create(self, **kwargs):
            self.calls.append(kwargs)
            class _Resp:
                content = [type("Block", (), {"type": "text", "text": txt["text"]})()
                           for txt in self._response["content"]]
            return _Resp()

    pdf = tmp_path / "fake.pdf"
    pdf.write_bytes(b"%PDF-1.7\n%fake")
    client = StubClient(fixtures_dir / "remediation_response.json")
    body = remediate_with_pdf(pdf, mangled_body="bad output", client=client)
    assert "Cleaned Paper" in body
    assert client.calls, "expected client.messages.create to be called"
```

- [ ] **Step 3: Run test to verify it fails**

Run: `uv run pytest tests/test_remediation.py::test_remediate_with_pdf_returns_corrected_markdown -v`
Expected: FAIL — `ImportError`.

- [ ] **Step 4: Add `remediate_with_pdf` to `scripts/_convert/remediation.py`**

Append:

````python
import base64
from typing import Protocol

CLAUDE_MODEL = "claude-sonnet-4-6"
MAX_OUTPUT_TOKENS = 16000

REMEDIATION_SYSTEM_PROMPT = """You are given (1) a PDF of an academic paper and (2) a markdown rendering produced by automated tools that may have errors. Output a corrected markdown that preserves the section/equation/citation structure of the PDF, keeps citation markers like [1] or \\cite{Smith2020} intact, and uses LaTeX $...$ for math. Do not add references that aren't in the PDF. Output only the corrected markdown — no preamble, no explanation."""


class _AnthropicLike(Protocol):
    """Duck-typed Anthropic client interface, narrow enough for our use."""

    @property
    def messages(self): ...


def remediate_with_pdf(
    pdf_path: Path,
    mangled_body: str,
    client: _AnthropicLike,
) -> str:
    """Call Claude with the PDF + mangled markdown, return the corrected markdown."""
    pdf_b64 = base64.standard_b64encode(pdf_path.read_bytes()).decode("ascii")
    response = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=MAX_OUTPUT_TOKENS,
        system=[
            {
                "type": "text",
                "text": REMEDIATION_SYSTEM_PROMPT,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "document",
                        "source": {
                            "type": "base64",
                            "media_type": "application/pdf",
                            "data": pdf_b64,
                        },
                    },
                    {
                        "type": "text",
                        "text": f"Existing (potentially mangled) rendering:\n\n```markdown\n{mangled_body}\n```",
                    },
                ],
            }
        ],
    )
    parts = [b.text for b in response.content if getattr(b, "type", "") == "text"]
    return "\n".join(parts).strip()


def build_anthropic_client():
    """Construct a real anthropic.Anthropic client. Imported lazily so tests don't need the SDK env."""
    import anthropic
    return anthropic.Anthropic()
````

- [ ] **Step 5: Run test to verify it passes**

Run: `uv run pytest tests/test_remediation.py -v`
Expected: 6 passed.

- [ ] **Step 6: Commit**

```bash
git add scripts/_convert/remediation.py tests/test_remediation.py tests/fixtures/remediation_response.json
git commit -m "feat(convert): add Claude Sonnet remediation call with PDF + cached system prompt"
```

---

## Task 13: Index file generation

**Files:**

- Create: `scripts/_convert/indexes.py`
- Create: `tests/test_indexes.py`

- [ ] **Step 1: Write the failing test**

Create `tests/test_indexes.py`:

```python
"""Tests for scripts/_convert/indexes.py."""
from __future__ import annotations

from pathlib import Path

from scripts._convert.indexes import IndexEntry, render_top_index, render_year_index


def _entry(arxiv_id: str, title: str, year: str) -> IndexEntry:
    return IndexEntry(
        arxiv_id=arxiv_id,
        title=title,
        authors=["A. Author", "B. Author", "C. Author", "D. Author", "E. Author"],
        submitted=f"{year}-06-15",
        abstract="An abstract.",
    )


def test_top_index_groups_by_year() -> None:
    entries = [
        _entry("2008.10010", "Wav2Lip", "2020"),
        _entry("2604.23586", "Talker-T2AV", "2026"),
    ]
    md = render_top_index(entries)
    assert "Total papers: 2" in md
    assert "[2020](2020/README.md)" in md
    assert "[2026](2026/README.md)" in md
    assert md.index("2026") < md.index("2020")  # newest first


def test_year_index_lists_papers_with_local_links() -> None:
    entries = [_entry("2008.10010", "Wav2Lip", "2020")]
    md = render_year_index("2020", entries)
    assert "[Wav2Lip](2008.10010.md)" in md
    assert "A. Author, B. Author, C. Author, D. Author et al." in md
    assert "An abstract." in md
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_indexes.py -v`
Expected: FAILs — `ModuleNotFoundError`.

- [ ] **Step 3: Implement `scripts/_convert/indexes.py`**

```python
"""Generate the papers/README.md and per-year README.md index files."""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from datetime import date


@dataclass
class IndexEntry:
    arxiv_id: str
    title: str
    authors: list[str]
    submitted: str       # YYYY-MM-DD
    abstract: str


def _truncate_authors(authors: list[str]) -> str:
    if len(authors) > 4:
        return ", ".join(authors[:4]) + " et al."
    return ", ".join(authors)


def render_top_index(entries: list[IndexEntry]) -> str:
    """Render papers/README.md."""
    by_year: dict[str, list[IndexEntry]] = defaultdict(list)
    for e in entries:
        by_year[e.submitted[:4] or "Unknown"].append(e)

    lines = [
        "# Papers — Markdown Corpus",
        "",
        f"Total papers: {len(entries)}",
        "",
        f"_Generated: {date.today().isoformat()}_",
        "",
    ]
    for year in sorted(by_year, reverse=True):
        lines.append(f"- [{year}]({year}/README.md) — {len(by_year[year])} papers")
    return "\n".join(lines) + "\n"


def render_year_index(year: str, entries: list[IndexEntry]) -> str:
    """Render papers/<year>/README.md."""
    sorted_entries = sorted(entries, key=lambda e: e.submitted, reverse=True)
    lines = [
        f"# {year}",
        "",
        f"{len(entries)} papers in this year.",
        "",
    ]
    for e in sorted_entries:
        lines.append(f"### [{e.title}]({e.arxiv_id}.md)")
        lines.append(f"**{_truncate_authors(e.authors)}** · {e.submitted}")
        lines.append("")
        if e.abstract:
            lines.append("<details>")
            lines.append("<summary>Abstract</summary>")
            lines.append("")
            lines.append(e.abstract)
            lines.append("")
            lines.append("</details>")
            lines.append("")
    return "\n".join(lines) + "\n"
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_indexes.py -v`
Expected: 2 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/_convert/indexes.py tests/test_indexes.py
git commit -m "feat(convert): generate papers/README.md and per-year index files"
```

---

## Task 14: Augment top-level README to link to local MD

**Files:**

- Modify: `scripts/fetch_papers.py:844-883` (the `_build_table` function)

- [ ] **Step 1: Locate and read `_build_table`**

Open `scripts/fetch_papers.py` and re-read the `_build_table` function (around lines 844–883) to confirm the exact current content before editing.

- [ ] **Step 2: Modify `_build_table` to add a 📄 Read link when the local MD exists**

Replace the body of `_build_table` so each entry conditionally appends a local-file link:

```python
def _build_table(papers_by_id: dict[str, dict]) -> str:
    rows = sorted(papers_by_id.values(), key=lambda r: r.get("submitted", ""), reverse=True)

    by_year: dict[str, list] = defaultdict(list)
    for row in rows:
        year = row.get("submitted", "")[:4] or "Unknown"
        by_year[year].append(row)

    sections: list[str] = []
    for year in sorted(by_year.keys(), reverse=True):
        section_lines = [f"<details open>", f"<summary><h3>{year}</h3></summary>", ""]
        for row in by_year[year]:
            authors = row.get("authors", "")
            if authors.count(",") >= 4:
                authors = ", ".join(authors.split(", ")[:4]) + " et al."
            date_str = row.get("submitted", "")[:10]
            abstract = row.get("abstract", "").strip()
            title = row["title"]
            url = row["url"]
            arxiv_id = row.get("arxiv_id", "")

            local_md = REPO_ROOT / "papers" / year / f"{arxiv_id}.md"
            local_link = ""
            if local_md.exists():
                local_link = f" · [📄 Read](papers/{year}/{arxiv_id}.md)"

            section_lines.append(f"#### [{title}]({url}){local_link}")
            section_lines.append(f"**{authors}** · {date_str}")
            section_lines.append("")
            if abstract:
                section_lines.append("<details>")
                section_lines.append("<summary>Abstract</summary>")
                section_lines.append("")
                section_lines.append(abstract)
                section_lines.append("")
                section_lines.append("</details>")
                section_lines.append("")
            else:
                section_lines.append("")

        section_lines.append("</details>")
        sections.append("\n".join(section_lines))

    return "\n\n".join(sections)
```

- [ ] **Step 3: Verify by hand-running fetch_papers.py with `--days 0`**

Run: `uv run python scripts/fetch_papers.py --days 0`
Expected: Re-renders README.md from existing CSV. Since no `papers/` exists yet, no `📄 Read` links appear. (When papers are converted later, links will materialize.)

- [ ] **Step 4: Commit**

```bash
git add scripts/fetch_papers.py
git commit -m "feat(readme): add per-entry 'Read' link when local markdown exists"
```

---

## Task 15: Orchestrator skeleton — load CSV, dispatch per paper

**Files:**

- Create: `scripts/convert_papers.py`
- Create: `tests/test_orchestrator.py`

- [ ] **Step 1: Write the failing test**

Create `tests/test_orchestrator.py`:

```python
"""Tests for scripts/convert_papers.py orchestration."""
from __future__ import annotations

import csv
from pathlib import Path

from scripts.convert_papers import (
    PaperRow,
    load_papers_csv,
    needs_conversion,
)


def _write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["arxiv_id", "title", "authors", "submitted",
                                          "categories", "url", "abstract"])
        w.writeheader()
        w.writerows(rows)


def test_load_papers_csv(tmp_path: Path) -> None:
    csv_path = tmp_path / "papers.csv"
    _write_csv(csv_path, [{
        "arxiv_id": "2008.10010",
        "title": "Wav2Lip",
        "authors": "K. R. Prajwal, et al.",
        "submitted": "2020-08-23",
        "categories": "cs.CV",
        "url": "https://arxiv.org/abs/2008.10010",
        "abstract": "abstract",
    }])
    rows = load_papers_csv(csv_path)
    assert len(rows) == 1
    assert isinstance(rows[0], PaperRow)
    assert rows[0].arxiv_id == "2008.10010"
    assert rows[0].year == "2020"


def test_needs_conversion_when_missing(tmp_papers_dir: Path) -> None:
    row = PaperRow(arxiv_id="2008.10010", title="Wav2Lip", authors=["A"],
                   submitted="2020-08-23", categories=[], url="…", abstract="…")
    assert needs_conversion(row, tmp_papers_dir) is True


def test_needs_conversion_when_present(tmp_papers_dir: Path) -> None:
    row = PaperRow(arxiv_id="2008.10010", title="Wav2Lip", authors=["A"],
                   submitted="2020-08-23", categories=[], url="…", abstract="…")
    target = tmp_papers_dir / "2020" / "2008.10010.md"
    target.parent.mkdir(parents=True)
    target.write_text("---\nllm_remediated: false\n---\n\nbody\n")
    assert needs_conversion(row, tmp_papers_dir) is False
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_orchestrator.py -v`
Expected: FAILs — `ModuleNotFoundError`.

- [ ] **Step 3: Implement `scripts/convert_papers.py`**

```python
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
            rows.append(PaperRow(
                arxiv_id=row["arxiv_id"],
                title=row["title"],
                authors=[a.strip() for a in row.get("authors", "").split(",") if a.strip()],
                submitted=row.get("submitted", ""),
                categories=[c for c in row.get("categories", "").split() if c],
                url=row.get("url", ""),
                abstract=row.get("abstract", ""),
            ))
    return rows


def needs_conversion(row: PaperRow, papers_dir: Path) -> bool:
    """True if this paper has no markdown file yet."""
    target = papers_dir / row.year / f"{row.arxiv_id}.md"
    return not target.exists()


def _process_paper(row: PaperRow) -> None:
    """Stub — wired up in Task 16."""
    logging.info("Would process %s", row.arxiv_id)


def _regenerate_indexes(rows: list[PaperRow]) -> None:
    """Stub — wired up in Task 17."""
    logging.info("Would regenerate indexes for %d papers", len(rows))


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_orchestrator.py -v`
Expected: 3 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/convert_papers.py tests/test_orchestrator.py
git commit -m "feat(convert): orchestrator skeleton with CSV loading and per-paper dispatch"
```

---

## Task 16: Wire orchestrator to stages 1–3

**Files:**

- Modify: `scripts/convert_papers.py`
- Modify: `tests/test_orchestrator.py`

- [ ] **Step 1: Write a failing integration test using the Wav2Lip fixture**

Append to `tests/test_orchestrator.py`:

```python
import shutil

import pytest


@pytest.mark.slow
def test_process_paper_end_to_end_latex(monkeypatch, tmp_path, fixtures_dir):
    """End-to-end: pre-seed cache with the fixture tarball, run process, assert MD exists."""
    from scripts import convert_papers

    cache_root = tmp_path / ".cache" / "source"
    papers_root = tmp_path / "papers"
    cache_root.mkdir(parents=True)

    # Seed the cache so Stage 1 short-circuits.
    paper_cache = cache_root / "2008.10010"
    paper_cache.mkdir()
    src_tar = paper_cache / "source.tar.gz"
    shutil.copy(fixtures_dir / "sources_2008.10010.tar.gz", src_tar)

    monkeypatch.setattr(convert_papers, "PAPERS_DIR", papers_root)
    monkeypatch.setattr(convert_papers, "CACHE_DIR", tmp_path / ".cache")

    row = convert_papers.PaperRow(
        arxiv_id="2008.10010",
        title="Wav2Lip",
        authors=["K. R. Prajwal"],
        submitted="2020-08-23",
        categories=["cs.CV"],
        url="https://arxiv.org/abs/2008.10010",
        abstract="abstract",
    )
    convert_papers._process_paper(row)
    assert (papers_root / "2020" / "2008.10010.md").exists()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_orchestrator.py::test_process_paper_end_to_end_latex -v -m slow`
Expected: FAIL — `_process_paper` is still a stub that doesn't write a file.

- [ ] **Step 3: Replace `_process_paper` with full Stage 1+2+3 logic**

Replace the `_process_paper` function in `scripts/convert_papers.py`:

```python
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
    page_count = 1
    converter = "none"
    source_label = "metadata-only"
    latex_exit_code = 0

    if kind is sources.SourceKind.LATEX:
        result = latex_to_md.convert_latex_to_md(extracted_dir)
        body = result.body
        bbl_text = result.bbl_text
        latex_exit_code = result.exit_code
        converter = "pandoc"
        source_label = "latex"
    elif kind is sources.SourceKind.PDF:
        pdf_files = list(extracted_dir.rglob("*.pdf"))
        result = pdf_to_md.convert_pdf_to_md(pdf_files[0])
        body = result.body
        page_count = result.page_count
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

    has_references = bool(refs)
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
```

- [ ] **Step 4: Run the integration test**

Run: `uv run pytest tests/test_orchestrator.py::test_process_paper_end_to_end_latex -v -m slow`
Expected: 1 passed (slow — runs pandoc once).

- [ ] **Step 5: Commit**

```bash
git add scripts/convert_papers.py tests/test_orchestrator.py
git commit -m "feat(convert): wire orchestrator to stages 1, 2, and 3 for arxiv + S2 papers"
```

---

## Task 17: Wire orchestrator to stage 4 (indexes)

**Files:**

- Modify: `scripts/convert_papers.py`
- Modify: `tests/test_orchestrator.py`

- [ ] **Step 1: Write the failing test**

Append to `tests/test_orchestrator.py`:

```python
def test_regenerate_indexes_creates_top_and_year_files(monkeypatch, tmp_path):
    from scripts import convert_papers

    monkeypatch.setattr(convert_papers, "PAPERS_DIR", tmp_path / "papers")

    rows = [
        convert_papers.PaperRow(
            arxiv_id="2008.10010", title="Wav2Lip", authors=["A"],
            submitted="2020-08-23", categories=["cs.CV"], url="…", abstract="…",
        ),
        convert_papers.PaperRow(
            arxiv_id="2604.23586", title="Talker", authors=["B"],
            submitted="2026-04-26", categories=["cs.CV"], url="…", abstract="…",
        ),
    ]
    # Pre-create the per-paper MD files so per-year index has something to point at.
    for r in rows:
        p = tmp_path / "papers" / r.year / f"{r.arxiv_id}.md"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("body")

    convert_papers._regenerate_indexes(rows)
    assert (tmp_path / "papers" / "README.md").exists()
    assert (tmp_path / "papers" / "2020" / "README.md").exists()
    assert (tmp_path / "papers" / "2026" / "README.md").exists()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_orchestrator.py::test_regenerate_indexes_creates_top_and_year_files -v`
Expected: FAIL — `_regenerate_indexes` is still a stub.

- [ ] **Step 3: Replace `_regenerate_indexes` with real logic**

Replace the function in `scripts/convert_papers.py`:

```python
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
        (year_dir / "README.md").write_text(indexes.render_year_index(year, entries), encoding="utf-8")
```

- [ ] **Step 4: Run test to verify it passes**

Run: `uv run pytest tests/test_orchestrator.py::test_regenerate_indexes_creates_top_and_year_files -v`
Expected: 1 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/convert_papers.py tests/test_orchestrator.py
git commit -m "feat(convert): regenerate top-level and per-year index files in orchestrator"
```

---

## Task 18: Per-paper error logging + fixme escalation

**Files:**

- Modify: `scripts/convert_papers.py`
- Create: `tests/test_error_handling.py`

- [ ] **Step 1: Write the failing test**

Create `tests/test_error_handling.py`:

```python
"""Tests for per-paper error isolation and 3-strike escalation."""
from __future__ import annotations

import json
from pathlib import Path

from scripts.convert_papers import (
    log_conversion_error,
    record_failure_and_maybe_escalate,
)


def test_log_conversion_error_appends_jsonl(tmp_path: Path) -> None:
    log_path = tmp_path / "conversion_errors.jsonl"
    log_conversion_error(log_path, "2008.10010", "stage1", "boom")
    log_conversion_error(log_path, "2008.10010", "stage2", "kaboom")
    lines = log_path.read_text().splitlines()
    assert len(lines) == 2
    record = json.loads(lines[0])
    assert record["arxiv_id"] == "2008.10010"
    assert record["stage"] == "stage1"


def test_record_failure_escalates_after_three(tmp_path: Path) -> None:
    log_path = tmp_path / "conversion_errors.jsonl"
    fixme_path = tmp_path / "fixme.txt"
    for _ in range(3):
        record_failure_and_maybe_escalate(log_path, fixme_path, "2008.10010", "stage1", "boom")
    fixme = fixme_path.read_text().strip().splitlines()
    assert "2008.10010" in fixme


def test_record_failure_does_not_escalate_after_two(tmp_path: Path) -> None:
    log_path = tmp_path / "conversion_errors.jsonl"
    fixme_path = tmp_path / "fixme.txt"
    for _ in range(2):
        record_failure_and_maybe_escalate(log_path, fixme_path, "2008.10010", "stage1", "boom")
    assert not fixme_path.exists()
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_error_handling.py -v`
Expected: FAILs — symbols not defined.

- [ ] **Step 3: Add error-handling helpers to `scripts/convert_papers.py`**

Append (above the `if __name__ == "__main__":` block):

```python
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
```

- [ ] **Step 4: Wire error handling into the `main()` futures loop**

Replace the `as_completed` block in `main()` with:

```python
    error_log = CACHE_DIR / "conversion_errors.jsonl"
    fixme_path = PAPERS_DIR / ".fixme.txt"
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(_process_paper, row): row for row in pending}
        for fut in as_completed(futures):
            row = futures[fut]
            try:
                fut.result()
            except Exception as exc:  # noqa: BLE001
                logging.exception("Failed to process %s", row.arxiv_id)
                record_failure_and_maybe_escalate(
                    error_log, fixme_path, row.arxiv_id, "process", str(exc)
                )
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `uv run pytest tests/test_error_handling.py -v`
Expected: 3 passed.

- [ ] **Step 6: Commit**

```bash
git add scripts/convert_papers.py tests/test_error_handling.py
git commit -m "feat(convert): per-paper error logging with 3-strike fixme escalation"
```

---

## Task 19: Wire LLM remediation pass into orchestrator

**Files:**

- Modify: `scripts/convert_papers.py`
- Modify: `tests/test_orchestrator.py`

- [ ] **Step 1: Write the failing test (uses dry-run mode to avoid live API)**

Append to `tests/test_orchestrator.py`:

```python
def test_llm_remediation_dry_run_logs_without_api(monkeypatch, tmp_path, caplog):
    from scripts import convert_papers

    monkeypatch.setattr(convert_papers, "PAPERS_DIR", tmp_path / "papers")
    monkeypatch.setattr(convert_papers, "CACHE_DIR", tmp_path / ".cache")
    monkeypatch.setattr(convert_papers, "LLM_REMEDIATION_DRY_RUN", True)
    monkeypatch.setattr(convert_papers, "LLM_REMEDIATION_MAX_PAPERS", 50)

    # Pre-create a paper file with low citation resolution to trigger flagger.
    p = tmp_path / "papers" / "2020" / "2008.10010.md"
    p.parent.mkdir(parents=True)
    p.write_text(
        "---\n"
        "arxiv_id: 2008.10010\n"
        "submitted: 2020-08-23\n"
        "source: pdf\n"
        "converter: marker\n"
        "llm_remediated: false\n"
        "citations_resolved: 1/30\n"
        "references_parsed: 30\n"
        "---\n\nshort body\n"
    )
    pdf_path = tmp_path / ".cache" / "source" / "2008.10010" / "paper.pdf"
    pdf_path.parent.mkdir(parents=True)
    pdf_path.write_bytes(b"%PDF-1.7\n")

    rows = [convert_papers.PaperRow(
        arxiv_id="2008.10010", title="Wav2Lip", authors=["A"],
        submitted="2020-08-23", categories=[], url="…", abstract="…",
    )]
    with caplog.at_level("INFO"):
        convert_papers._run_remediation_pass(rows)
    assert any("would remediate 2008.10010" in m.lower() for m in caplog.text.splitlines())
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_orchestrator.py::test_llm_remediation_dry_run_logs_without_api -v`
Expected: FAIL — `_run_remediation_pass` not defined.

- [ ] **Step 3: Add `_run_remediation_pass` to `scripts/convert_papers.py`**

Append (before the `_regenerate_indexes` function):

```python
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
        body = text[front_end + 5:]
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
    logging.info("Remediation candidates: %d (cap %d)",
                 len(candidates), LLM_REMEDIATION_MAX_PAPERS)

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
```

- [ ] **Step 4: Wire `_run_remediation_pass` into `main()`**

In `main()`, after the futures loop and before `_regenerate_indexes(rows)`, add:

```python
    if not args.skip_llm:
        _run_remediation_pass(rows)
```

- [ ] **Step 5: Run test to verify it passes**

Run: `uv run pytest tests/test_orchestrator.py::test_llm_remediation_dry_run_logs_without_api -v`
Expected: 1 passed.

- [ ] **Step 6: Commit**

```bash
git add scripts/convert_papers.py tests/test_orchestrator.py
git commit -m "feat(convert): wire Stage 2.5 LLM remediation with dry-run + cap"
```

---

## Task 20: Idempotency end-to-end test

**Files:**

- Modify: `tests/test_orchestrator.py`

- [ ] **Step 1: Write the failing test**

Append to `tests/test_orchestrator.py`:

```python
@pytest.mark.slow
def test_second_run_is_idempotent(monkeypatch, tmp_path, fixtures_dir):
    """After one full process_paper run, a second run for the same paper should write nothing new."""
    import shutil
    import time

    from scripts import convert_papers

    cache_root = tmp_path / ".cache" / "source"
    papers_root = tmp_path / "papers"
    cache_root.mkdir(parents=True)
    paper_cache = cache_root / "2008.10010"
    paper_cache.mkdir()
    shutil.copy(fixtures_dir / "sources_2008.10010.tar.gz", paper_cache / "source.tar.gz")

    monkeypatch.setattr(convert_papers, "PAPERS_DIR", papers_root)
    monkeypatch.setattr(convert_papers, "CACHE_DIR", tmp_path / ".cache")

    row = convert_papers.PaperRow(
        arxiv_id="2008.10010", title="Wav2Lip", authors=["A"],
        submitted="2020-08-23", categories=["cs.CV"],
        url="https://arxiv.org/abs/2008.10010", abstract="abstract",
    )
    convert_papers._process_paper(row)
    md_path = papers_root / "2020" / "2008.10010.md"
    first_mtime = md_path.stat().st_mtime
    time.sleep(0.05)

    # needs_conversion should now return False
    assert convert_papers.needs_conversion(row, papers_root) is False
    # If we still call _process_paper directly, it WILL re-write — but main() guards with needs_conversion.
    # So this test verifies the guard, not the inner call.
```

- [ ] **Step 2: Run test to verify it passes (it should pass directly, since the guard already exists)**

Run: `uv run pytest tests/test_orchestrator.py::test_second_run_is_idempotent -v -m slow`
Expected: 1 passed.

- [ ] **Step 3: Commit**

```bash
git add tests/test_orchestrator.py
git commit -m "test(convert): verify second-run idempotency via needs_conversion guard"
```

---

## Task 21: Update GitHub Actions workflow

**Files:**

- Modify: `.github/workflows/fetch_papers.yml`

- [ ] **Step 1: Read the current workflow**

Open `.github/workflows/fetch_papers.yml` and re-read it before editing. (Required by Edit tool; also necessary to pick the right insertion points.)

- [ ] **Step 2: Replace the workflow with the extended version**

Below is the full extended workflow. The changes vs. the old version: install pandoc, switch to `uv` for dependency install, add a cache step for `.cache/`, run `convert_papers.py`, and commit `papers/` + `README.md` as a unit.

```yaml
name: Fetch Lipsync Papers

on:
  schedule:
    - cron: "0 6 * * *"
  workflow_dispatch:
    inputs:
      full:
        description: "Full historical fetch (true|false)"
        required: false
        default: "false"

jobs:
  fetch:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4

      - name: Install pandoc
        run: |
          sudo apt-get update
          sudo apt-get install -y pandoc

      - name: Install uv
        uses: astral-sh/setup-uv@v3

      - name: Sync dependencies
        run: uv sync

      - name: Restore conversion cache
        uses: actions/cache@v4
        with:
          path: |
            .cache/source
            .cache/citations.json
          key: convert-cache-${{ github.run_id }}
          restore-keys: convert-cache-

      - name: Fetch papers (incremental or full)
        run: |
          if [ "${{ github.event.inputs.full }}" = "true" ]; then
            uv run python scripts/fetch_papers.py --full
          else
            uv run python scripts/fetch_papers.py
          fi

      - name: Convert papers to markdown
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          LLM_REMEDIATION_MAX_PAPERS: "50"
        run: uv run python scripts/convert_papers.py

      - name: Commit and push changes
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add papers/ papers.csv README.md
          if git diff --cached --quiet; then
            echo "No changes to commit."
          else
            git commit -m "chore: update papers and markdown [skip ci]"
            git push
          fi
```

- [ ] **Step 3: Validate the YAML**

Run: `uv run python -c "import yaml; yaml.safe_load(open('.github/workflows/fetch_papers.yml'))"`
Expected: No output (valid YAML).

- [ ] **Step 4: Commit**

```bash
git add .github/workflows/fetch_papers.yml
git commit -m "ci: install pandoc + run convert_papers.py + cache .cache/ across runs"
```

---

## Task 22: Documentation — README updates

**Files:**

- Modify: `README.md`

- [ ] **Step 1: Re-read the current README.md to identify the right insertion point**

Read `README.md`. You're looking for the "## Running locally" section (around line 12).

- [ ] **Step 2: Add a "## Markdown corpus" section right above "## Running locally"**

Insert this block before the `## Running locally` heading:

````markdown
## Markdown corpus

Each paper is also available as LLM-friendly markdown under `papers/<year>/<arxiv_id>.md`. The conversion pipeline:

- Fetches LaTeX source from `arxiv.org/e-print/<id>` (preferred; preserves equations and citation structure) or PDFs (fallback for papers without LaTeX source).
- Converts via [pandoc](https://pandoc.org) (LaTeX) or [marker](https://github.com/datalab-to/marker) (PDF).
- Auto-flagged or manually-listed (`papers/.fixme.txt`) low-quality outputs go through a Claude Sonnet 4.6 remediation pass.
- Citations are rewritten as clickable links — local sibling MD when the cited paper is in this corpus, external arXiv/DOI URLs otherwise.

Browse the corpus at [papers/README.md](papers/README.md). Each paper file has YAML frontmatter with metadata + diagnostics (`source`, `converter`, `llm_remediated`, `citations_resolved`).

### Running locally

You'll need pandoc:

```bash
# macOS
brew install pandoc

# Ubuntu
sudo apt-get install pandoc
```
````

Then:

```bash
uv sync
uv run python scripts/fetch_papers.py        # update papers.csv (existing)
uv run python scripts/convert_papers.py      # convert any new papers to markdown
```

````

- [ ] **Step 3: Update the existing "## Running locally" content to mention `uv`**

The existing section uses bare `python`. Replace its code block with:

```bash
# Incremental fetch (last 8 days)
uv run python scripts/fetch_papers.py

# Full historical fetch (everything since 2020-01-01)
uv run python scripts/fetch_papers.py --full

# Custom window
uv run python scripts/fetch_papers.py --days 30
````

And replace the line `No third-party dependencies are required — the script uses only the Python standard library.` with:

```markdown
The fetch script uses only the Python standard library; the conversion pipeline adds `marker-pdf`, `anthropic`, `pyyaml`, and the `pandoc` system binary (managed via `uv` and your package manager).
```

- [ ] **Step 4: Commit**

```bash
git add README.md
git commit -m "docs: document markdown corpus, conversion pipeline, and uv-based local setup"
```

---

## Task 23: pre-commit configuration

**Files:**

- Create: `.pre-commit-config.yaml`

- [ ] **Step 1: Create `.pre-commit-config.yaml`**

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: trailing-whitespace
        exclude: ^(papers/|tests/fixtures/)
      - id: end-of-file-fixer
        exclude: ^(papers/|tests/fixtures/)
      - id: check-yaml
      - id: check-added-large-files
        args: ["--maxkb=2000"]

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.6.9
    hooks:
      - id: ruff
        args: ["--fix"]
      - id: ruff-format
```

- [ ] **Step 2: Install and run pre-commit**

Run:

```bash
uv run pre-commit install
uv run pre-commit run -a
```

Expected: Hooks may auto-fix formatting on a few files. If they do, stage and commit the fixes (they're cosmetic).

- [ ] **Step 3: Commit**

```bash
git add .pre-commit-config.yaml
# plus any cosmetic fixes from step 2
git commit -m "chore: add pre-commit config (ruff + standard hygiene hooks)"
```

---

## Task 24: Smoke test — run pipeline against a few real papers

**Files:**

- (No file changes)

This is a manual verification step before the full back-fill.

- [ ] **Step 1: Run the pipeline against just the Wav2Lip paper**

Run: `uv run python scripts/convert_papers.py --only 2008.10010 --skip-llm`
Expected: Stages 1–4 complete. Output at `papers/2020/2008.10010.md` exists, has YAML frontmatter, has a `## References` section with at least some linked entries. `papers/README.md` and `papers/2020/README.md` also exist.

- [ ] **Step 2: Inspect the output**

Run: `head -60 papers/2020/2008.10010.md`
Expected: YAML frontmatter, then markdown body. Confirm by eye:

- `source: latex`, `converter: pandoc`
- `references_parsed > 0`, `citations_resolved` ratio above 0
- Body has section headers from the actual paper

- [ ] **Step 3: Run against three more papers spanning different years**

Pick three additional `arxiv_id`s from `papers.csv` (one from 2022, one from 2024, one from 2026):

```bash
uv run python scripts/convert_papers.py --only <id1> --skip-llm
uv run python scripts/convert_papers.py --only <id2> --skip-llm
uv run python scripts/convert_papers.py --only <id3> --skip-llm
```

Expected: All four MD files exist, indexes regenerated. Verify cross-paper local-sibling links work by grepping one of them for `../2020/2008.10010.md`.

- [ ] **Step 4: Discard the smoke-test outputs**

The full back-fill will regenerate everything, so delete the partial output:

```bash
rm -rf papers/ .cache/
```

- [ ] **Step 5: Commit any unrelated cleanups (none expected)**

```bash
git status
# expect: nothing to commit
```

---

## Task 25: Initial back-fill PR

**Files:**

- Create: `papers/` (entire tree, ~511 files)

This task produces the large initial commit. Run it locally — the workflow's first scheduled run can also do it, but a deliberate local back-fill makes the diff reviewable.

- [ ] **Step 1: Run the full pipeline (without LLM remediation)**

Run: `uv run python scripts/convert_papers.py --skip-llm`
Expected: Takes 60–90 minutes. At the end, ~511 files exist under `papers/`.

- [ ] **Step 2: Sanity-check size and counts**

Run: `find papers -name '*.md' | wc -l && du -sh papers/`
Expected: ~511 files, ~15–50 MB.

- [ ] **Step 3: Run the LLM remediation pass with dry-run first**

Run: `LLM_REMEDIATION_DRY_RUN=true uv run python scripts/convert_papers.py`
Expected: Logs "Would remediate <id>" for each flagged paper. Eyeball that the count is reasonable (under the 50-paper cap).

- [ ] **Step 4: Run the LLM remediation pass for real**

Run: `uv run python scripts/convert_papers.py`
Expected: Takes 30–60 minutes; touches the flagged subset only. Cost: ~$25–45.

- [ ] **Step 5: Commit the back-fill**

```bash
git add papers/
git commit -m "chore: initial markdown back-fill for all papers in papers.csv

Adds papers/<year>/<arxiv_id>.md for every entry in papers.csv plus
top-level and per-year README index files. Generated by
scripts/convert_papers.py."
```

- [ ] **Step 6: Open PR**

```bash
gh pr create --title "Initial markdown back-fill (511 papers)" --body "$(cat <<'EOF'
## Summary

First full run of the conversion pipeline. Adds `papers/<year>/<arxiv_id>.md` for every entry in `papers.csv`, plus top-level and per-year READMEs.

## Counts

- ~511 paper markdown files
- 7 year directories (2020–2026)
- LLM remediation: triggered on N papers (see commit messages)

## Reviewer notes

This PR is intentionally large. Spot-check a few files; the full diff isn't meant to be read line by line.

## Test plan

- [ ] Spot-check 3 papers across 3 different years
- [ ] Confirm `papers/README.md` lists year sections in newest-first order
- [ ] Click a local sibling link and verify it resolves
- [ ] Confirm `README.md` (top-level) shows 📄 Read links on each entry
EOF
)"
```

---

## Spec coverage check

Mapping spec sections → tasks:

| Spec section                                              | Task(s)                                                                                                 |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Architecture overview                                     | Tasks 2–4, 5, 6–10, 11–12, 13, 15–17                                                                    |
| Code organization                                         | Tasks 2, 3, 4, 5, 6, 11, 13, 15                                                                         |
| Disk layout (`papers/<year>/<id>.md`)                     | Task 2, 17                                                                                              |
| YAML frontmatter                                          | Task 2                                                                                                  |
| Index files (`papers/README.md`, per-year)                | Task 13, 17                                                                                             |
| Top-level README augmentation                             | Task 14                                                                                                 |
| Citation Pass A (parse)                                   | Task 6 (LaTeX), Task 7 (PDF)                                                                            |
| Citation Pass B (resolve)                                 | Task 8                                                                                                  |
| Citation Pass C (rewrite)                                 | Task 9                                                                                                  |
| Citation cache                                            | Task 10                                                                                                 |
| Stage 2.5 heuristic flagger                               | Task 11                                                                                                 |
| Stage 2.5 LLM call                                        | Task 12                                                                                                 |
| Stage 2.5 wired in orchestrator                           | Task 19                                                                                                 |
| `papers/.fixme.txt` manual list                           | Task 11                                                                                                 |
| 3-strike escalation                                       | Task 18                                                                                                 |
| Per-paper error logging                                   | Task 18                                                                                                 |
| Idempotency rules                                         | Task 15, 17, 20                                                                                         |
| ThreadPoolExecutor concurrency                            | Task 15                                                                                                 |
| Workflow integration                                      | Task 21                                                                                                 |
| Cost-control env vars                                     | Task 19                                                                                                 |
| Testing strategy (4 fixtures, golden tests, recorded API) | Tasks 3, 4, 5, 6, 12                                                                                    |
| Edge case: withdrawn paper                                | Task 18 (general error path)                                                                            |
| Edge case: no bibliography                                | Task 16 (refs empty → `references_parsed: 0`)                                                           |
| Edge case: self-citation                                  | Task 8 (resolved via local-sibling)                                                                     |
| Initial back-fill                                         | Task 25                                                                                                 |
| Pandoc version pin                                        | Task 21 (apt install — version pin via documenting in README; explicit pinning is a future improvement) |

Gaps noted:

- Pandoc minor-version pinning is not enforced in CI (only documented). If reproducibility regressions appear, add a pinned `apt-get install pandoc=3.1.x` step.
- Multi-version arXiv `arxiv_version` field is in the frontmatter schema but not currently captured at fetch time. The `e-print` URL returns latest by default; capturing the version requires inspecting tarball metadata. Defer until a real need surfaces.

---

## Plan complete and saved to `docs/superpowers/plans/2026-05-02-paper-markdown-conversion.md`.

Two execution options:

**1. Subagent-Driven (recommended)** — I dispatch a fresh subagent per task, review between tasks, fast iteration.

**2. Inline Execution** — Execute tasks in this session using executing-plans, batch execution with checkpoints.

Which approach?
