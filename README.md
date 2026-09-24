# Lipsync Papers

Standalone paper discovery and conversion for Papers related to lipsync..

<!-- papers-index:start -->
# Papers

| Published | Identifier | Title | Source |
| --- | --- | --- | --- |
<!-- papers-index:end -->

## Architecture

`papers_pipeline` validates configuration, fetches source records through
adapters, normalizes and deduplicates them, applies topic gates, reconciles the
inventory with the corpus, selects deterministic budgeted batches, converts
inputs, formats changed files, updates the index, and commits each consistent
stage. Source continuations retain an opaque cursor and its exact UTC fetch
window across bounded runs under one shared deadline. Conversion failures are
isolated by paper; infrastructure failures stop the run.

The corpus is built to be browsed by people and LLMs. Every paper in `papers/`
starts with YAML front matter (identifier, title, authors, published date, URL,
source, DOI, arXiv ID, and categories), and the index below links each
converted paper to its local markdown file. Run `papers-pipeline front-matter`
to refresh the front matter of every converted paper from `papers.csv`.

## Configuration

`papers.yml` defines repository identity, enabled adapters, topic gates, fetch
policy, conversion budgets, and concurrency. Run
`uv run papers-pipeline validate --config papers.yml` before a manual run.
Unknown keys, duplicate adapters, and invalid ranges are rejected.

Adapter `lookback_days` is 1-365, `page_size` is 1-1000, `max_pages` is 1-100,
and `max_results` is 1-10000; Semantic Scholar's `page_size` is at most 100.
Semantic Scholar reads its API key from `SEMANTIC_SCHOLAR_API_KEY` when
`secret_env` names it (the nightly workflow exports that repository secret);
with `secret_env: null` it runs unauthenticated at a shared, low rate limit.
Other adapters use `secret_env: null`.

To fill in a source's history, set `backfill_start` (a date) on an arXiv,
Semantic Scholar, bioRxiv, or Hugging Face adapter; set it to `1991-08-01` for
the whole of arXiv. After its `lookback_days` window, each nightly run keeps
stepping further into the past in `backfill_days` chunks (default 30) until the
adapter's `max_pages` or `max_results` budget for the run is spent, resuming a
capped chunk first, until it reaches `backfill_start`. Progress is kept in
`.papers-state.yml`. New papers join the conversion backlog, so conversion
budgets bound how fast history turns into markdown. dblp and Papers with Code
cannot query past date ranges and reject `backfill_start`.

Papers with an arXiv ID convert from arXiv's HTML rendering
(`https://arxiv.org/html/<id>`): pandoc turns the LaTeXML article into markdown
with TeX math in under a second, and they cost `html_cost` in batch budgets.
Only when arXiv has no HTML for a paper does it fall back to its own input, for
example a PDF through marker, which takes minutes per paper on a CPU runner.

The supported `filters` are:

- `arxiv`: `search_query`
- `semantic_scholar`: `query`
- `dblp`: `query`
- `biorxiv_crossref`: `provider`, set to `biorxiv` or `crossref`
- `huggingface` and `papers_with_code`: no filter keys

Topic gates support `include_any`, `include_all`, `exclude_any`, and
`categories`. Set `plugin: topic_plugin:accept_topic` only when these gates
cannot express the repository rule; the plugin accepts `Paper` and returns
`TopicDecision`.

Fetch request timeouts are 1-120 seconds, retries are 0-5, backoff is 0-30
seconds, and the shared fetch deadline is 60-7200 seconds. Conversion allows
1-20 batches per run, 1-100 papers per batch, and a total cost budget of 1-1000. A run stops starting batches after `deadline_seconds` (default 10800, 600-18000) so it always pushes before the nightly step's 330-minute timeout. Each converter may run for 60-3600 seconds
before it is terminated. Per-paper HTML and LaTeX costs are 1-100; PDF cost is
1-1000. HTML and LaTeX concurrency is 1-4.
PDF concurrency is always exactly 1.

## Run locally

```bash
uv sync --locked --extra dev
uv tool install marker-pdf==1.10.1
uv pip install --no-deps pypandoc-binary==1.15
mkdir -p "$HOME/.local/bin"
ln -sf "$(uv run python -c 'import pypandoc; print(pypandoc.get_pandoc_path())')" \
  "$HOME/.local/bin/pandoc"
npm install --global prettier@3.6.2
uv run papers-pipeline validate --config papers.yml
uv run papers-pipeline nightly --config papers.yml
uv run papers-pipeline format-corpus --shard-index 0 --shard-count 8
uv run papers-pipeline front-matter
```

All tests use checked-in fixtures and run without source APIs or converter
tools:

```bash
UV_OFFLINE=true uv run pytest
uv run pre-commit run --all-files
```

## State, backlog, and recovery

The nightly command derives backlog from `papers.csv` versus files under
`papers/`. `.papers-state.yml` stores each source's opaque cursor together with
the exact UTC window start/end and consecutive failure attempts. A capped run
reuses that window until enumeration completes; only the following run creates
a fresh lookback window. Legacy cursor-only state is discarded rather than
being resumed against a different window. Count and cost budgets select
deterministic batches.

A paper failure does not stop peers. A third consecutive scheduled failure
creates a colocated `.fixme.txt`; fix the input and remove the marker to retry.
Permanent per-paper download failures (including HTTP 404/410 and invalid input
URLs) count toward that paper's failure history without cancelling peers.
Authentication, rate limits, outages, network/timeouts, disk failures, missing
tools, and resource exhaustion fail the run explicitly.

## Formatting

Nightly formatting receives only changed paper files and indexes. Complete
corpus formatting runs only through the manual sharded workflow.

## Automation and summaries

The nightly Actions summary reports per-source fetched, accepted,
deduplicated, and rejected counts; inventory, generated, pending, attempted,
succeeded, failed, and fixme counts; timings; continuation, cap, retry, and
deadline events; and fixme paths.

The weekly template workflow runs Copier against an explicit release,
validates the result, and opens a pull request. It never updates `main`
directly.

## alphaXiv collection

The `Sync alphaXiv collection` workflow adds arXiv papers from `papers.csv` to
an existing alphaXiv collection through the official alphaXiv MCP server
(`https://api.alphaxiv.org/mcp/v1`). Configure the `ALPHAXIV_API_KEY` Actions
secret with an API key from alphaXiv Settings > API Keys and the
`ALPHAXIV_COLLECTION` repository variable with the exact folder name. The
workflow is skipped while the variable is unset. Use `workflow_dispatch` for
the initial population.

The workflow also runs after every completed `Nightly papers` workflow,
including safe partial runs that commit inventory before a later conversion
failure. Synchronization is additive and idempotent: existing papers and
manually managed collection entries are preserved, and no remote paper is
removed.

## Updating from the template

Run the weekly workflow, or wait for its schedule. It resolves an immutable
release from `will-rice/papers-template`, runs Copier, refreshes the lock,
validates configuration, runs pre-commit and the offline test suite, and opens
an update pull request for review. Resolve any `.rej` file as a failed update;
never bypass validation or push an update directly to `main`.

## Ownership boundary

Copier owns pipeline code, tests, workflows, configuration scaffolding, and
support files. `papers/`, `papers.csv`, `.papers-state.yml`, and caches remain
repository-owned across Copier updates.

## Migration gate

Adoption by an existing papers repository is a separate migration. Do not begin a migration
until this generated repository smoke test passes on the exact immutable
template release selected for migration. Rehearse fixture
adoption first; then migrate lipsync-papers, tts-papers, asr-papers, and
birdclef-papers separately. Each migration must preserve corpus and Git
history, add `papers.yml`, `.papers-state.yml`, and `.copier-answers.yml`, keep
scheduling disabled, inspect the manual workflow and continuation behavior,
and only then re-enable the schedule.
