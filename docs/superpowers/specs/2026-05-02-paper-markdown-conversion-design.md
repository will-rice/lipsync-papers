# Paper → Markdown Conversion Pipeline

**Status:** Design approved, ready for planning
**Date:** 2026-05-02
**Author:** brainstormed with Claude

## Goal

Download every paper listed in `papers.csv` and convert it to LLM-friendly markdown, with all in-paper citations rewritten as clickable links — preferring local sibling files when the cited paper is also in the corpus, falling back to external arXiv/DOI URLs otherwise.

The intended consumer is an LLM (or a research agent driven by one) reading whole papers and following citation links across the corpus. Quality bar: faithful section/equation/table structure, accurate citation graph.

## Non-goals

- Not building a search/RAG layer over the markdown.
- Not training or fine-tuning anything on the corpus.
- Not extracting figures/images (text + equations only; figure captions are kept, the bitmaps are not).
- Not building a UI. The artifact is markdown files in git.

## Architecture

A four-stage idempotent pipeline driven by `papers.csv` as the single source of truth. Every stage is a no-op when its outputs exist and are newer than its inputs, so the cron can re-run safely on any state.

```
papers.csv ──► Stage 1: fetch source ──► .cache/source/<id>/    (gitignored)
                  │
                  ├─ arXiv tier:  https://arxiv.org/e-print/<id>  (LaTeX tarball)
                  ├─ S2 tier:     openAccessPdf URL via S2 API     (PDF)
                  └─ no source:   skip to metadata-only stub
                  │
                  ▼
              Stage 2: convert to markdown (parallel, ThreadPoolExecutor)
                  ├─ has LaTeX source? → pandoc tex→md
                  ├─ PDF only?         → marker pdf→md
                  └─ no source at all? → metadata-only stub
                  │
                  ▼
              Stage 2.5: LLM remediation (auto-flagged + manual list)
                  └─ heuristics flag mangled outputs → Claude Sonnet re-renders from PDF
                  │
                  ▼
              Stage 3: resolve citations (per-paper, two-pass)
                  ├─ Pass A: parse refs into structured map
                  └─ Pass B: rewrite inline markers + references list
                  │
                  ▼
              papers/<year>/<arxiv_id>.md  (committed)
                  │
                  ▼
              Stage 4: render index files
                  ├─ papers/README.md           (top-level lobby)
                  ├─ papers/<year>/README.md    (per-year listing)
                  └─ top-level README.md        (existing, augmented with local links)
```

### Code organization

Mirrors the existing `scripts/fetch_papers.py` style — single entry script, top-level `main()`, cascading helpers, `uv`-managed deps:

- `scripts/convert_papers.py` — entry point, orchestrates all stages.
- `scripts/_convert/` package:
  - `sources.py` — fetch arXiv e-print / S2 PDF, cache to `.cache/source/`.
  - `latex_to_md.py` — pandoc invocation, `.bbl` extraction.
  - `pdf_to_md.py` — marker invocation.
  - `citations.py` — parse refs, build resolution map, rewrite inline markers.
  - `remediation.py` — LLM remediation pass via Anthropic SDK.
  - `output.py` — write `papers/<year>/<arxiv_id>.md` with frontmatter.
  - `indexes.py` — generate `papers/README.md` and per-year READMEs.

External deps:

- **System:** `pandoc` (apt-get in workflow, pinned to `3.1.x`).
- **Python:** `marker-pdf`, `anthropic`. Network calls keep using `urllib` like the existing fetcher (no `requests`).

## Output structure

### Disk layout

```
papers/
├── README.md              ← top-level index: paper count + year-section links
├── 2020/
│   ├── README.md          ← per-year listing, mirrors existing top-level format
│   ├── 2008.10010.md      ← Wav2Lip
│   └── …
├── 2021/
│   ├── README.md
│   └── …
…
└── 2026/
    ├── README.md
    └── 2604.23586.md
```

### Per-paper file format

YAML frontmatter (parseable by an LLM/loader without re-reading CSV) followed by the rendered body:

```markdown
---
arxiv_id: 2604.23586
title: "Talker-T2AV: Joint Talking Audio-Video Generation with…"
authors: [Zhen Ye, Xu Tan, Aoxiong Yin, …]
submitted: 2026-04-26
categories: [cs.CV, cs.CL, cs.MM, cs.SD, eess.AS]
arxiv_url: https://arxiv.org/abs/2604.23586
source: latex                  # latex | pdf | metadata-only
converter: pandoc              # pandoc | marker
llm_remediated: false
citations_resolved: 27/41      # diagnostic — fraction of refs with a resolved URL
citations_resolved_at: 2026-05-02T14:23:00Z   # for idempotency vs. papers.csv mtime
references_parsed: 41
arxiv_version: v2
---

# Talker-T2AV: Joint Talking Audio-Video Generation…

**Authors:** Zhen Ye, Xu Tan, …
**Submitted:** 2026-04-26 · [arXiv:2604.23586](https://arxiv.org/abs/2604.23586)

## Abstract
…

## 1. Introduction
…cross-modal coherence, building on Wav2Lip [[1]](../2020/2008.10010.md) and …

## References
1. K. R. Prajwal, et al. **A Lip Sync Expert Is All You Need for Speech to Lip Generation In The Wild.** [arXiv:2008.10010](../2020/2008.10010.md)
2. …
```

### Index files

- **`papers/README.md`** — short. Generation date, total paper count, one collapsible `<details>` block per year linking to `papers/<year>/README.md`.
- **`papers/<year>/README.md`** — for each paper that year: title link to local `.md`, truncated authors (first 4 + "et al."), date, collapsible abstract — same visual style as the existing top-level `README.md` table.
- **Top-level `README.md`** — keep `update_readme()` logic; augment each entry with a `📄 [Read](papers/<year>/<arxiv_id>.md)` link next to the existing arXiv link, *only* when the markdown file exists.

## Citation resolution

### Pass A — extract refs into a normalized map

Same shape regardless of source tier:

```python
{
    "Prajwal2020": {           # cite-key (LaTeX) or "1", "2", … (PDF)
        "raw": "K. R. Prajwal, et al. A Lip Sync Expert Is All You…",
        "title": "A Lip Sync Expert Is All You Need for Speech to Lip Generation…",
        "authors": ["K. R. Prajwal", …],
        "year": 2020,
        "arxiv_id": "2008.10010",   # may be None
        "doi": None,                 # may be None
    },
    …
}
```

- **LaTeX (Tier 1):** parse the `.bbl` file (always present after pandoc's `--biblatex` build). Extract `eprint`/`arxivid`/`doi` fields when set; otherwise pull title from the entry's body.
- **PDF (Tier 2/3):** regex-split the `## References` section by leading `[N]` or `N.`, then run a tolerant title extractor (longest title-cased span up to first period — works on ~85% of ML papers).

### Pass B — resolve to URL, in priority order

1. **Local sibling** — if `ref.arxiv_id` matches any `arxiv_id` in `papers.csv` → `../<year>/<arxiv_id>.md`.
2. **External arXiv** — `ref.arxiv_id` set but not in corpus → `https://arxiv.org/abs/<id>`.
3. **DOI** — `ref.doi` set → `https://doi.org/<doi>`.
4. **Semantic Scholar lookup by title** — single API call per unresolved ref. Returns `arxiv_id`/`doi` if known. Cached in `.cache/citations.json` so we don't re-query across runs.
5. **Fallback** — render the citation marker as plain text (no link).

### Pass C — rewrite inline markers in body markdown

- LaTeX: `\cite{Prajwal2020}` → `[\[Prajwal2020\]](resolved-url)` (post-process pandoc's raw `\cite` output).
- PDF: `[1]` → `[\[1\]](resolved-url)` only when the position-to-ref mapping is high-confidence (positional match unambiguous AND the ref's title was extracted cleanly). Low-confidence markers stay bare.

The references-section list at the bottom of each paper also gets resolved links inline so an LLM can navigate from the references list directly, not just from inline markers.

### Cache schema

`.cache/citations.json` (gitignored):

```json
{
  "title:a lip sync expert is all you need for speech…": {
    "arxiv_id": "2008.10010",
    "doi": null,
    "resolved_at": "2026-05-02"
  }
}
```

## Stage 2.5 — LLM remediation

When rule-based conversion produces low-quality output, re-render the paper from the PDF using Claude Sonnet 4.6.

### Gating: B + A layered

**Auto-flag (B)** — after Stage 2, score each paper on cheap heuristics:

- Body length < `0.5 * pdf_page_count * 200 words` → suspiciously short.
- No `## References` section parsed.
- High ratio of unicode artifacts (`α₂β`-style clumps) outside math-context blocks.
- `citations_resolved` ratio below 30%.
- LaTeX build returned non-zero exit code.

Any flag → route through remediation.

**Manual list (A)** — `papers/.fixme.txt`, one arxiv_id per line. Always included regardless of auto-flag state.

After 3 consecutive Stage 1/2 failures, a paper is auto-appended to `papers/.fixme.txt`. Self-healing without losing audit trail.

### Mechanics

- Use the Anthropic Python SDK with `claude-sonnet-4-6` (current latest).
- PDF passed as a `document` content block (Claude API accepts PDFs natively, no separate vision pipeline).
- System prompt cached for the run (5-minute TTL covers the typical batch).
- Sequential — no parallel API calls; TPM limits make ad-hoc parallelism more trouble than it's worth at our scale.

### Prompt sketch

> You are given (1) a PDF of an academic paper and (2) a markdown rendering produced by automated tools that may have errors. Output a corrected markdown that preserves the section/equation/citation structure of the PDF, keeps citation markers like `[1]` or `\cite{Smith2020}` intact, and uses LaTeX `$…$` for math. Do not add references that aren't in the PDF.

### Cost control

Workflow env vars:

- `LLM_REMEDIATION_MAX_PAPERS=50` — hard cap per run; prevents heuristic regressions from running up the bill.
- `LLM_REMEDIATION_DRY_RUN=false` — flip true to log what would be remediated without API calls.

Realistic spend: ~50–100 papers in the long tail × ~$0.45/paper = $25–45 over the lifetime of the corpus. Per-run delta is small once the back-fill is done.

## Workflow integration

Extend `.github/workflows/fetch_papers.yml`:

```yaml
jobs:
  fetch:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
      - name: Install pandoc                          # NEW
        run: sudo apt-get install -y pandoc
      - run: uv sync                                  # NEW (was stdlib-only before)
      - run: uv run python scripts/fetch_papers.py
      - name: Restore conversion cache                # NEW
        uses: actions/cache@v4
        with:
          path: |
            .cache/source
            .cache/citations.json
          key: convert-cache-${{ github.run_id }}
          restore-keys: convert-cache-
      - run: uv run python scripts/convert_papers.py  # NEW
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
      - run: |
          git add papers/ README.md
          git commit -m "chore: update papers and markdown [skip ci]" || true
          git push
```

`ANTHROPIC_API_KEY` is unavailable on PRs from forks (correct security posture), so LLM remediation runs only on `schedule` and `workflow_dispatch`.

### Per-paper error handling

Each paper wrapped in its own try/except. Failures logged to `.cache/conversion_errors.jsonl`:

```json
{"arxiv_id": "2604.23586", "stage": "latex_to_md", "error": "pandoc exited 1: missing \\usepackage{customthing}", "ts": "2026-05-02T14:23:00Z"}
```

Failed papers are skipped this run, retried next run (their `.md` is missing → re-enter the pipeline). After 3 consecutive failures → auto-added to `papers/.fixme.txt` for LLM remediation.

### Idempotency rules per stage

- **Stage 1 (fetch source):** skip if `.cache/source/<id>/` exists and was modified < 30 days ago.
- **Stage 2 (convert):** skip if `papers/<year>/<id>.md` exists and frontmatter `converter` matches what we'd run now.
- **Stage 2.5 (remediation):** skip if frontmatter `llm_remediated: true` AND heuristics no longer flag the file.
- **Stage 3 (citations):** skip if frontmatter `citations_resolved_at` is newer than `papers.csv`'s newest entry (so adding a new paper invalidates link resolution for older ones that may cite it).
- **Stage 4 (indexes):** always regenerate; cheap.

### Concurrency

- Stage 1: sequential (3-second arXiv rate limit, inherited from `fetch_papers.py`).
- Stages 2/3: `ThreadPoolExecutor(max_workers=8)`.
- Stage 2.5: sequential.

## Testing strategy

Functional pytest, minimal mocks per project conventions. Four hand-picked fixture papers:

- `2008.10010` (Wav2Lip): clean LaTeX, foundational citation target. Exercises Tier 1 + local-sibling resolution.
- A custom-macro LaTeX paper: pandoc edge cases.
- A PDF-only arXiv submission: Tier 2 (marker path).
- An `s2:`-prefixed paper: Tier 3 metadata-only.

Test files:

- `tests/test_citations.py` — pure unit tests for ref parsing, fuzzy title matching, resolution priority order.
- `tests/test_conversion.py` — given a fixture's source, run conversion, diff against `tests/fixtures/<id>.expected.md` golden.
- `tests/test_idempotency.py` — run pipeline twice on a fixture, assert second run produces zero file writes.
- `tests/test_remediation.py` — single recorded API response replayed offline.

End-to-end is the integration test by virtue of being committed to git: every PR diff shows exactly which papers regressed.

## Edge cases

| Case | Handling |
|------|----------|
| Withdrawn / replaced arXiv paper (404 on `e-print`) | Log to `conversion_errors.jsonl`, skip. |
| Multi-version arXiv paper | Always fetch latest (no `vN` suffix). Frontmatter records `arxiv_version`. |
| Paper without bibliography | Render body without refs section, `references_parsed: 0`. |
| Unicode in author names | Pandoc handles UTF-8; we NFC-normalize on write. |
| Cross-year reference link | Local-sibling resolver computes paths from `papers.csv` directly, not filesystem walks. |
| Self-citation | Resolves to its own file (harmless). Has unit test. |
| `papers/` already exists at script start | Abort with explicit error. |
| Paper drops out of `papers.csv` (relevance filter tightens) | Delete corresponding `.md` to keep corpus consistent with index. |
| `s2:` paper with no PDF anywhere | Render metadata-only stub (frontmatter + abstract) so the README link still resolves. |

## Open decisions (defaults chosen, easy to flip)

1. **Initial back-fill** — single PR titled `chore: initial markdown back-fill` containing all ~511 files. Reviewers can scan or trust.
2. **Dropped papers** — delete corresponding `.md` (keeps corpus consistent).
3. **`s2:` papers without PDFs** — render metadata-only stubs (preserves discoverability).
4. **Pandoc version** — pin `3.1.x` in workflow; document in README.

## Cost & runtime estimates

| Phase | Per-paper | 511-paper run |
|-------|-----------|---------------|
| Stage 1 (fetch) | ~3s (arXiv rate limit) | ~25 min |
| Stage 2 LaTeX path | ~5s (pandoc) | ~10 min over ~400 papers |
| Stage 2 PDF path (marker) | ~30s | ~50 min over ~100 papers |
| Stage 2.5 LLM | ~30s + ~$0.45 | ~$25–45 lifetime tail |
| Stage 3 citations | ~1s + S2 lookups | ~5 min, near-zero on cached re-runs |
| **Total back-fill** | — | **~90 min, ~$25–45 one-time** |
| **Weekly cron delta** | — | **~5 min, ~$0–2** |

## Out of scope (future work)

- Figure extraction & captioning.
- Cross-paper concept indexing (e.g., "find all papers that cite Wav2Lip and use diffusion").
- Hugging Face dataset publication (decided against: A was chosen for storage).
- Sub-second per-paper conversion (would require GPU; not justified at this volume).
