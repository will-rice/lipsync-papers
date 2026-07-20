# Semantic Similarity Filtering Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a corpus-anchored embedding-similarity admit path to `scripts/fetch_papers.py` so relevant papers without exact positive keywords are no longer dropped.

**Architecture:** A `SemanticGate` class embeds title+abstract of every paper in `papers.csv` with MiniLM and scores candidates as the mean cosine similarity to their top-10 nearest corpus papers (self-excluded for corpus members). The decision rule becomes `not blacklisted AND (keyword path OR score >= SEMANTIC_THRESHOLD)`. The threshold is calibrated leave-one-out over the corpus and committed as a constant.

**Tech Stack:** Python 3.12, `sentence-transformers` (`all-MiniLM-L6-v2`), torch tensors, pytest.

**Spec:** `docs/superpowers/specs/2026-07-20-semantic-similarity-filtering-design.md`

## Global Constraints

- Run everything with `uv run`; add dependencies with `uv add`.
- Constants over CLI arguments; thresholds are module constants in `scripts/fetch_papers.py`.
- Prefer torch over numpy; keep the batch dimension in `encode` calls.
- Model: `sentence-transformers/all-MiniLM-L6-v2`. `SEMANTIC_TOP_K = 10`, `SEMANTIC_MIN_CORPUS = 50`.
- `scripts/fetch_papers.py` uses `print()` for progress output — match it there. New standalone scripts use `logging.info` (repo-wide preference).
- Tests that load the model are marked `@pytest.mark.slow` (existing marker in `pyproject.toml`).
- Before every commit, pre-commit runs automatically via the git hook; if it rewrites files, re-stage and re-commit.
- No behavior change for papers admitted today: the keyword path must remain a strict subset of the new rule.

---

### Task 1: `SemanticGate` class

**Files:**

- Modify: `pyproject.toml` (via `uv add sentence-transformers`)
- Modify: `scripts/fetch_papers.py` (constants near line 428 after `ML_KEYWORDS`; class after the filter helpers near line 556)
- Create: `tests/test_fetch_filtering.py`

**Interfaces:**

- Produces: `SemanticGate(corpus: list[dict])` — corpus dicts have `arxiv_id`, `title`, `abstract` keys (same shape as `papers.csv` rows).
  - `SemanticGate.embed(papers: list[dict]) -> Tensor` — normalized `(len(papers), 384)` tensor.
  - `SemanticGate.score(paper: dict) -> float` — mean cosine similarity to the top-`SEMANTIC_TOP_K` nearest corpus papers, excluding the paper itself when it is a corpus member (matched by `arxiv_id`).
- Constants: `SEMANTIC_MODEL`, `SEMANTIC_TOP_K`, `SEMANTIC_MIN_CORPUS` (Task 2 adds `SEMANTIC_THRESHOLD`).

- [ ] **Step 1: Add the dependency**

```bash
uv add sentence-transformers
```

Expected: `pyproject.toml` gains `sentence-transformers>=...` and `uv.lock` updates. Torch is already in the lock via `marker-pdf`, so this is a small delta.

- [ ] **Step 2: Write the failing tests**

Create `tests/test_fetch_filtering.py`:

```python
"""Tests for the semantic relevance gate in fetch_papers."""

from __future__ import annotations

import pytest

from scripts.fetch_papers import SemanticGate, load_existing_papers

pytestmark = pytest.mark.slow

# Relevant to the corpus but contains NO POSITIVE_RELEVANCE_KEYWORDS phrase —
# exactly the class of paper the keyword gate misses.
RELEVANT_NO_KEYWORD = {
    "arxiv_id": "test-relevant",
    "title": "Diffusion-Based Portrait Video Generation from Audio",
    "abstract": "We present a diffusion framework that animates a single portrait "
    "photograph from a driving speech signal. A transformer motion generator maps "
    "audio features to expressive head and mouth dynamics, producing photorealistic "
    "portrait videos that are temporally coherent and identity preserving.",
}

OFF_TOPIC = {
    "arxiv_id": "test-offtopic",
    "title": "Beamforming Codebook Design for Millimeter-Wave Channels",
    "abstract": "We propose a hierarchical codebook construction for hybrid "
    "beamforming in millimeter-wave communication systems, analyzing achievable "
    "rates under hardware constraints and channel estimation error.",
}


@pytest.fixture(scope="module")
def corpus() -> list[dict]:
    papers = list(load_existing_papers().values())
    assert len(papers) >= 100, "papers.csv should hold the curated corpus"
    return papers


@pytest.fixture(scope="module")
def gate(corpus: list[dict]) -> SemanticGate:
    return SemanticGate(corpus)


def test_relevant_scores_higher_than_off_topic(gate: SemanticGate) -> None:
    assert gate.score(RELEVANT_NO_KEYWORD) > gate.score(OFF_TOPIC)


def test_corpus_paper_excludes_itself(corpus: list[dict]) -> None:
    small = SemanticGate(corpus[:2])
    # With self excluded, each paper's only neighbor is the other one, so both
    # scores equal cos(a, b) — and neither is inflated by self-similarity 1.0.
    score_a = small.score(corpus[0])
    score_b = small.score(corpus[1])
    assert score_a == pytest.approx(score_b, abs=1e-5)
    assert score_a < 0.999
```

- [ ] **Step 3: Run tests to verify they fail**

```bash
uv run pytest tests/test_fetch_filtering.py -v
```

Expected: FAIL at import with `ImportError: cannot import name 'SemanticGate'`.

- [ ] **Step 4: Implement `SemanticGate`**

In `scripts/fetch_papers.py`, after the `ML_KEYWORDS` list (around line 428), add:

```python
# Semantic gate – papers without an exact positive keyword can still be
# admitted when they are close (in MiniLM embedding space) to the curated
# corpus. See docs/superpowers/specs/2026-07-20-semantic-similarity-filtering-design.md.
SEMANTIC_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
SEMANTIC_TOP_K = 10
SEMANTIC_MIN_CORPUS = 50
```

After `_is_relevant_lipsync_paper` (around line 556), add:

```python
class SemanticGate:
    """Scores papers by cosine similarity to the curated corpus.

    The score is the mean similarity to the top-k nearest corpus papers.  A
    paper that is itself in the corpus is excluded from its own neighbor set,
    so re-scoring existing papers stays meaningful.
    """

    def __init__(self, corpus: list[dict]):
        from sentence_transformers import SentenceTransformer

        self.model = SentenceTransformer(SEMANTIC_MODEL)
        self.index = {p["arxiv_id"]: i for i, p in enumerate(corpus)}
        self.corpus_embeddings = self.embed(corpus)

    def embed(self, papers: list[dict]):
        return self.model.encode(
            [f"{p['title']}. {p['abstract']}" for p in papers],
            convert_to_tensor=True,
            normalize_embeddings=True,
        )

    def score(self, paper: dict) -> float:
        row = self.index.get(paper["arxiv_id"])
        embedding = self.corpus_embeddings[row] if row is not None else self.embed([paper])[0]
        sims = self.corpus_embeddings @ embedding
        if row is not None:
            sims[row] = -1.0
        k = min(SEMANTIC_TOP_K, len(sims) - (0 if row is None else 1))
        return float(sims.topk(k).values.mean())
```

Notes for the implementer:

- The `sentence_transformers` import is deliberately inside `__init__`: it drags in torch (~2 s), and `--help`, keyword-only paths, and most tests never need it.
- `sims` is a fresh tensor produced by the matmul, so the in-place `sims[row] = -1.0` cannot corrupt `corpus_embeddings`.
- No `torch` import is needed — `topk`/`mean` are tensor methods.

- [ ] **Step 5: Run tests to verify they pass**

```bash
uv run pytest tests/test_fetch_filtering.py -v
```

Expected: 2 passed. First run downloads the model (~80 MB).

- [ ] **Step 6: Commit**

```bash
git add pyproject.toml uv.lock scripts/fetch_papers.py tests/test_fetch_filtering.py
git commit -m "Add SemanticGate for corpus-anchored abstract similarity"
```

---

### Task 2: Calibrate and commit `SEMANTIC_THRESHOLD`

**Files:**

- Create: `scripts/calibrate_semantic_threshold.py`
- Modify: `scripts/fetch_papers.py` (add `SEMANTIC_THRESHOLD` constant)

**Interfaces:**

- Consumes: `SemanticGate`, `load_existing_papers` from Task 1.
- Produces: `SEMANTIC_THRESHOLD: float` constant in `scripts/fetch_papers.py`, used by Task 3.

- [ ] **Step 1: Write the calibration script**

Create `scripts/calibrate_semantic_threshold.py`:

```python
"""Calibrate SEMANTIC_THRESHOLD via leave-one-out scoring of the corpus.

Scores every paper in papers.csv against the rest of the corpus (SemanticGate
already excludes a corpus paper from its own neighbors), prints score
percentiles, and scores known-negative abstracts to confirm separation.

Run manually when the threshold needs revisiting; commit the chosen value as
SEMANTIC_THRESHOLD in scripts/fetch_papers.py and paste the table in the PR::

    uv run python scripts/calibrate_semantic_threshold.py
"""

import logging

import torch
from tqdm import tqdm

from scripts.fetch_papers import SemanticGate, load_existing_papers

# Off-topic abstracts of the kind the blacklist exists for; their scores must
# sit clearly below the chosen threshold.
KNOWN_NEGATIVES = [
    {
        "arxiv_id": "neg-radar",
        "title": "Contactless Vital Sign Monitoring with mmWave Radar",
        "abstract": "We develop a millimeter-wave radar pipeline that estimates "
        "heart rate and respiration from chest micro-motion, with a signal "
        "processing chain robust to body movement and multipath clutter.",
    },
    {
        "arxiv_id": "neg-clinical",
        "title": "Surgical Outcomes of Cleft Lip Repair in Infants",
        "abstract": "A retrospective cohort study of primary cleft lip repair "
        "evaluating scar quality, symmetry, and complication rates across two "
        "surgical techniques over five years of follow-up.",
    },
    {
        "arxiv_id": "neg-grid",
        "title": "Grid-Forming Inverter Control for Power System Synchronization",
        "abstract": "We analyze droop-based grid-forming inverter controllers and "
        "their transient synchronization stability under large load steps in "
        "low-inertia power systems.",
    },
]

PERCENTILES = [0.01, 0.02, 0.05, 0.10, 0.25, 0.50]


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    corpus = list(load_existing_papers().values())
    gate = SemanticGate(corpus)
    scores = torch.tensor([gate.score(p) for p in tqdm(corpus, desc="LOO scoring")])

    logging.info("Leave-one-out score percentiles over %d corpus papers:", len(corpus))
    for q in PERCENTILES:
        logging.info("  p%-3d %.3f", int(q * 100), torch.quantile(scores, q))

    logging.info("Known-negative scores (must sit clearly below the threshold):")
    for paper in KNOWN_NEGATIVES:
        logging.info("  %.3f  %s", gate.score(paper), paper["title"])


if __name__ == "__main__":
    main()
```

Note: `tqdm` and `torch` are already installed transitively (sentence-transformers). LOO scoring is fast — corpus members hit the embedding-reuse path in `score`, so no re-encoding happens.

- [ ] **Step 2: Run the calibration**

```bash
uv run python scripts/calibrate_semantic_threshold.py
```

Expected output shape (values will differ):

```
Leave-one-out score percentiles over 542 corpus papers:
  p1   0.41
  p2   0.44
  p5   0.47
  ...
Known-negative scores (must sit clearly below the threshold):
  0.21  Contactless Vital Sign Monitoring with mmWave Radar
  ...
```

Sanity checks before choosing:

- All three known-negative scores must be well below the p5 value (gap ≥ ~0.1). If a negative lands near p5, escalate — the spec's approach needs revisiting rather than silently picking a higher threshold.
- Save the printed table; it goes in the PR description.

- [ ] **Step 3: Commit the threshold**

In `scripts/fetch_papers.py`, extend the semantic constants block with the measured p5 value rounded to two decimals (example value shown — use the real one):

```python
# Calibrated 2026-07-20 as the p5 of leave-one-out corpus scores; see
# scripts/calibrate_semantic_threshold.py for the procedure.
SEMANTIC_THRESHOLD = 0.47
```

```bash
git add scripts/calibrate_semantic_threshold.py scripts/fetch_papers.py
git commit -m "Calibrate semantic threshold at corpus p5 via leave-one-out"
```

---

### Task 3: Wire the semantic path into the decision rule

**Files:**

- Modify: `scripts/fetch_papers.py` — `_is_relevant_lipsync_paper` (line 552), `_collect_from_source` (line 775), `main` (lines 839–860)
- Modify: `tests/test_fetch_filtering.py`

**Interfaces:**

- Consumes: `SemanticGate`, `SEMANTIC_THRESHOLD`, `SEMANTIC_MIN_CORPUS` from Tasks 1–2.
- Produces: `_is_relevant_lipsync_paper(paper: dict, gate: SemanticGate | None) -> bool` — the only admit decision; `gate=None` means keyword-only (bootstrap / small corpus).

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_fetch_filtering.py` (extend the existing import from `scripts.fetch_papers` with `SEMANTIC_THRESHOLD` and `_is_relevant_lipsync_paper`):

```python
def test_semantic_path_admits_missing_keyword_paper(gate: SemanticGate) -> None:
    assert gate.score(RELEVANT_NO_KEYWORD) >= SEMANTIC_THRESHOLD
    assert _is_relevant_lipsync_paper(RELEVANT_NO_KEYWORD, gate)


def test_off_topic_paper_rejected(gate: SemanticGate) -> None:
    assert gate.score(OFF_TOPIC) < SEMANTIC_THRESHOLD
    assert not _is_relevant_lipsync_paper(OFF_TOPIC, gate)


def test_no_gate_falls_back_to_keyword_only() -> None:
    assert not _is_relevant_lipsync_paper(RELEVANT_NO_KEYWORD, None)


def test_blacklist_overrides_semantic_path(gate: SemanticGate) -> None:
    blacklisted = dict(RELEVANT_NO_KEYWORD)
    blacklisted["abstract"] += " We additionally evaluate on cleft lip patients."
    assert not _is_relevant_lipsync_paper(blacklisted, gate)


def test_keyword_path_is_preserved(corpus: list[dict]) -> None:
    # Every corpus paper was admitted by the keyword path; the new rule must
    # remain a strict superset of the old one.
    assert all(_is_relevant_lipsync_paper(p, None) for p in corpus)
```

If `test_semantic_path_admits_missing_keyword_paper` fails after implementation, print both scores (`gate.score(...)`) and compare against the Task 2 percentile table — the fix is choosing p2 instead of p5 (a threshold change with rationale), not weakening the test.

- [ ] **Step 2: Run tests to verify the new ones fail**

```bash
uv run pytest tests/test_fetch_filtering.py -v
```

Expected: the two `_is_relevant_lipsync_paper` signature-dependent tests fail with `TypeError: _is_relevant_lipsync_paper() takes 1 positional argument but 2 were given`.

- [ ] **Step 3: Implement the decision rule**

Replace `_is_relevant_lipsync_paper` (line 552):

```python
def _is_relevant_lipsync_paper(paper: dict, gate: "SemanticGate | None") -> bool:
    """Return True if paper passes the blacklist plus a keyword or semantic gate."""
    if _is_excluded(paper):
        return False
    if _has_ml_signal(paper) and _has_positive_relevance_signal(paper):
        return True
    return gate is not None and gate.score(paper) >= SEMANTIC_THRESHOLD
```

(The class is defined below this function; the string annotation avoids reordering. `from __future__ import annotations` is already at the top of the file, so a plain annotation also works — match whichever placement you end up with.)

In `_collect_from_source`, add a `gate` parameter and log the score for semantic-only admits:

```python
def _collect_from_source(
    source_name: str,
    fetch_fn,
    keywords_list: list[str],
    start_date: date,
    end_date: date,
    existing: dict[str, dict],
    gate: "SemanticGate | None",
) -> int:
```

and replace the admit block inside the loop:

```python
        for paper in papers:
            pid = paper["arxiv_id"]
            if pid not in existing and _is_relevant_lipsync_paper(paper, gate):
                existing[pid] = paper
                new_count += 1
                if _has_ml_signal(paper) and _has_positive_relevance_signal(paper):
                    print(f"  + {pid}: {paper['title'][:70]}")
                else:
                    print(f"  + {pid} [sem {gate.score(paper):.2f}]: {paper['title'][:70]}")
```

In `main()`, build the gate after loading and thread it through (replacing lines 839–860):

```python
    existing = load_existing_papers()
    print(f"Loaded {len(existing)} existing papers from {PAPERS_CSV.name}.")

    # The curated corpus anchors the semantic gate; below SEMANTIC_MIN_CORPUS
    # (fresh backfill) filtering is keyword-only.
    gate = None
    if len(existing) >= SEMANTIC_MIN_CORPUS:
        print(f"Building semantic gate from {len(existing)} corpus papers …")
        gate = SemanticGate(list(existing.values()))

    # Remove any previously saved papers that no longer pass relevance gates.
    before = len(existing)
    existing = {pid: p for pid, p in existing.items() if _is_relevant_lipsync_paper(p, gate)}
    removed = before - len(existing)
    if removed:
        print(f"Removed {removed} existing paper(s) failing relevance filters.")

    new_count = 0
    new_count += _collect_from_source(
        "arXiv", fetch_papers, SEARCH_QUERIES, start_date, end_date, existing, gate
    )
    new_count += _collect_from_source(
        "Hugging Face Papers",
        fetch_huggingface_papers,
        SEARCH_QUERIES,
        start_date,
        end_date,
        existing,
        gate,
    )
```

- [ ] **Step 4: Run the full new test file**

```bash
uv run pytest tests/test_fetch_filtering.py -v
```

Expected: 7 passed.

- [ ] **Step 5: Run the fast suite to catch regressions**

```bash
uv run pytest -m "not slow"
```

Expected: all pass (no existing test calls `_is_relevant_lipsync_paper`, but verify).

- [ ] **Step 6: Commit**

```bash
git add scripts/fetch_papers.py tests/test_fetch_filtering.py
git commit -m "Admit papers by semantic similarity when keywords miss them"
```

---

### Task 4: Widen search queries and update README

**Files:**

- Modify: `scripts/fetch_papers.py` (`SEARCH_QUERIES`, line 53)
- Modify: `README.md` ("How it works" filter bullet)

**Interfaces:**

- Consumes: nothing new; pure config/docs.

- [ ] **Step 1: Add the new search queries**

Append to `SEARCH_QUERIES`:

```python
    "portrait animation",
    "audio-driven avatar",
    "co-speech",
    "head synthesis",
]
```

- [ ] **Step 2: Update the README filter bullet**

Replace:

```markdown
- Results are filtered with a negative-keyword blacklist plus an ML signal check and a positive lipsync/talking-face relevance gate.
```

with:

```markdown
- Results are filtered with a negative-keyword blacklist plus two admit paths: a positive lipsync/talking-face keyword gate (with an ML signal check), or semantic similarity of the abstract to the curated corpus (MiniLM embeddings, top-k mean against `papers.csv`).
```

- [ ] **Step 3: Commit**

```bash
git add scripts/fetch_papers.py README.md
git commit -m "Widen search queries now that semantic gate guards precision"
```

---

### Task 5: End-to-end verification

**Files:** none created; verifies the whole change.

- [ ] **Step 1: Full test suite and pre-commit**

```bash
uv run pytest
uv run pre-commit run -a
```

Expected: all tests pass (slow ones included), pre-commit clean.

- [ ] **Step 2: Live fetch over a 30-day window**

```bash
uv run python scripts/fetch_papers.py --days 30
```

Verify in the output:

- `Building semantic gate from ~542 corpus papers …` appears.
- `Removed 0 existing paper(s)` — i.e. the prune line does NOT appear (all existing papers pass via the keyword path; any removals mean a regression).
- New admits: lines with `[sem 0.xx]` are the papers the keyword gate would have missed. Read each semantic admit's title/abstract in the `papers.csv` diff and confirm they are on-topic. A few off-topic admits → raise `SEMANTIC_THRESHOLD` one calibration step (p5 → p10 direction) and re-run; systematically bad admits → stop and reassess.

- [ ] **Step 3: Review and commit the fetched papers**

```bash
git diff --stat papers.csv README.md
git add papers.csv README.md
git commit -m "chore: update papers and markdown"
```

(Uses the existing bot-commit convention for corpus updates. If the diff contains anything questionable, fix the threshold first — do not commit bad papers.)

- [ ] **Step 4: Confirm plan completion**

All checkboxes above ticked; branch ready for PR per `superpowers:finishing-a-development-branch`.
