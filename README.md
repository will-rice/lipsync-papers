# lipsync-papers

A curated, automatically-updated collection of papers on **lip sync**, talking-head synthesis, audio-driven face animation, and related topics — starting from [Wav2Lip](https://arxiv.org/abs/2008.10010) (2020) and growing every week.

## How it works

* Papers are sourced from [arXiv](https://arxiv.org/) via its public API.
* A [GitHub Actions workflow](.github/workflows/fetch_papers.yml) runs every **Monday at 06:00 UTC** to pull papers submitted in the previous week.
* The full paper list is stored in [`papers.csv`](papers.csv) and the table below is regenerated automatically on every update.

## Running locally

```bash
# Incremental fetch (last 8 days)
python scripts/fetch_papers.py

# Full historical fetch (everything since 2020-01-01)
python scripts/fetch_papers.py --full

# Custom window
python scripts/fetch_papers.py --days 30
```

No third-party dependencies are required — the script uses only the Python standard library.

## Triggering a manual update

Open the **Actions** tab → **Fetch Lipsync Papers** → **Run workflow**.  
Select *full = true* to back-fill from 2020, or leave it as *false* for an incremental update.

## Search terms

The following keyword queries are used against arXiv title and abstract fields:

`lip sync` · `lip synchronization` · `wav2lip` · `talking head` · `talking face` · `audio-driven face` · `speech-driven face` · `audio visual speech` · `face reenactment` · `neural dubbing`

## Papers

<!-- PAPERS_TABLE_START -->
| Date | Title | Authors |
|------|-------|---------|
<!-- PAPERS_TABLE_END -->
