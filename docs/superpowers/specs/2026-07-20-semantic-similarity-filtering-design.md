# Semantic Similarity Filtering — Design

**Date:** 2026-07-20
**Status:** Draft for review

## Problem

`scripts/fetch_papers.py` admits a paper only when its title+abstract contains one of 20
exact phrases (`POSITIVE_RELEVANCE_KEYWORDS`) plus an ML keyword. Relevant papers that
phrase their contribution differently — "portrait animation", "audio-conditioned avatar",
"co-speech facial motion" — are silently dropped. The 250-entry negative blacklist also
keeps growing because precision currently depends entirely on exact string matching.

Recall is lost in two places:

1. **Candidate generation** — a paper is only fetched if one of the 10 `SEARCH_QUERIES`
   matches its title/abstract on arXiv / HF Papers.
2. **The positive-relevance gate** — a fetched candidate is dropped unless it contains an
   exact positive phrase.

This design fixes (2) with an embedding-based semantic gate, and uses the safety it
provides to modestly widen (1).

## Approach

**Corpus-anchored embedding similarity as an additional admit path.** The ~540 papers
already curated in `papers.csv` define what "relevant" means. A candidate is scored by its
similarity to that corpus; a high score admits it even when no positive keyword matches.

Alternatives considered:

- **LLM relevance judge** (Claude, key already in CI): best nuance, but non-deterministic —
  the re-prune pass in `main()` re-filters every existing paper each run, so a flaky judge
  would churn the corpus. Also adds per-run API cost and a hard key dependency to fetching.
- **Hybrid** (embeddings + LLM judge on a borderline band): deferred. Add only if the
  embedding gate alone shows precision problems.

## Design

### Model

`sentence-transformers/all-MiniLM-L6-v2` via the `sentence-transformers` package — the
same model family the `papers-mcp` Space already uses for hybrid search over this corpus.
CPU-only, ~80 MB, embeds the full corpus in seconds on a GitHub Actions runner.

### Scoring

- Embed `f"{title}. {abstract}"` for every paper in `papers.csv` (the reference set) and
  for each candidate. Normalized embeddings, cosine similarity.
- Candidate score = **mean similarity to its top-k nearest corpus papers**, `K = 10`.
  - Not the centroid: the corpus is multi-modal (lipsync, visual dubbing, reenactment,
    3D facial animation), and a centroid blurs the modes.
  - Not max-sim: a single outlier corpus paper would admit its whole off-topic
    neighborhood; top-k mean requires a real cluster of support.
- When scoring a paper that is itself in the reference set (the re-prune pass), exclude
  it from its own neighbor set — otherwise self-similarity of 1.0 makes the semantic
  path a guaranteed pass and the prune inert.

### Decision rule

```
admit(paper) = not blacklisted(paper)
               and ( (ml_signal(paper) and positive_keyword(paper))   # existing path
                     or top_k_mean_sim(paper) >= SEMANTIC_THRESHOLD ) # new path
```

- The negative blacklist applies to **both** paths — it is cheap, precise, and encodes
  hard-won precision decisions.
- The ML-keyword gate applies only to the keyword path. Similarity to an all-ML corpus
  already encodes ML-ness; requiring exact ML phrases on the semantic path would
  reintroduce the recall problem this design removes.
- Implementation shape: a `SemanticGate` class built once in `main()` from the loaded
  corpus (model + reference embeddings), passed into the relevance check. Lazy model
  load so `--help` and tests that don't touch the gate stay fast.

### Threshold and calibration

- `SEMANTIC_THRESHOLD` is a module constant (per repo convention: constants over CLI args).
- Calibrated by **leave-one-out over the corpus**: score every existing paper against the
  rest; pick the threshold at roughly the 5th percentile, so ≥95 % of known positives
  would pass on the semantic path alone. Sanity-check against known negatives (abstracts
  that previously required blacklist entries) to confirm separation.
- Calibration is a one-off `scripts/calibrate_semantic_threshold.py` run manually when the
  threshold needs revisiting; its percentile table goes in the PR description, and the
  chosen value is committed as the constant.

### Corpus drift and bootstrap

- Papers admitted by the semantic path join `papers.csv` and therefore tomorrow's
  reference set. Drift is bounded: every addition already sits within threshold of an
  existing cluster, and the blacklist still applies. Acceptable for v1; revisit only if
  the corpus visibly drifts.
- If the corpus has fewer than `SEMANTIC_MIN_CORPUS = 50` papers (fresh `--full` backfill
  from an empty CSV), the semantic path is disabled and filtering is keyword-only. The
  current CSV (~540 rows) is far above this.

### Search query widening

With the semantic gate guarding precision, add a small set of broader `SEARCH_QUERIES`
that the keyword gate could never have tolerated:

- `"portrait animation"`
- `"audio-driven avatar"`
- `"co-speech"`
- `"head synthesis"`

Each query costs API round-trips at the 3 s rate limit, so the list stays short. Further
widening is a follow-up once semantic precision is observed in practice.

### Observability

Admitted-by-semantic-only papers are logged with their score
(`+ 2507.01234 [sem 0.63] Title …`) so the daily Actions log shows exactly what the new
path contributes. No `papers.csv` schema change.

### Dependencies and CI

- `uv add sentence-transformers` (pulls CPU torch; ~1–2 min extra install in the daily
  workflow, mitigated by uv's cache).
- Model weights download (~80 MB) on first use per runner; optionally added to the
  existing `actions/cache` block if it proves slow.

## Testing

- Unit tests in `tests/test_fetch_filtering.py` (pytest functional style, real model —
  minimal mocks per repo convention), marked `slow` since they download the model:
  - A relevant abstract with **no** positive keyword (e.g. portrait-animation phrasing)
    passes the semantic path.
  - An off-topic abstract (e.g. radar/wireless) fails it.
  - A corpus paper scored under the re-prune pass excludes itself from its neighbors.
  - Corpus below `SEMANTIC_MIN_CORPUS` disables the semantic path.
- Existing keyword-path behavior is covered by asserting the decision rule is a strict
  superset: everything admitted before is still admitted.

## Out of scope

- Replacing the negative blacklist or keyword gates.
- LLM judge (future option if embedding precision disappoints).
- Backfilling historically missed papers (a one-off `--full --days` style re-run after
  this lands will pick them up naturally; noted as a follow-up task, not part of this
  change).
- Any change to the markdown conversion pipeline.

## Open questions for review

1. Is ~95 % leave-one-out recall the right calibration point, or should the threshold be
   set more conservatively (higher precision) for v1?
2. Should the four new search queries land in the same change, or only after the gate has
   run for a week or two?
