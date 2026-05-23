"""Generate a daily digest of newly-added lipsync papers.

Compares the current papers.csv against the version at HEAD (the last committed
state) and writes a Markdown digest of the new papers to digests/YYYY-MM-DD.md.

If ANTHROPIC_API_KEY is set, each paper gets a 2-3 sentence "what's new / why
it matters" blurb from Claude, plus a top-level themes section. Otherwise the
digest is a plain list (title, authors, link, full abstract).

Usage::

    python scripts/generate_digest.py
    python scripts/generate_digest.py --since-days 1   # ignore git, take last N days
    python scripts/generate_digest.py --dry-run        # print to stdout, don't write
"""

from __future__ import annotations

import argparse
import csv
import io
import os
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PAPERS_CSV = REPO_ROOT / "papers.csv"
DIGESTS_DIR = REPO_ROOT / "digests"

SYSTEM_PROMPT = """You are a research analyst summarising newly-released papers
on lipsync, talking-head synthesis, audio-driven facial animation, and
audio-visual speech.

For each paper given, write a 2-3 sentence blurb that captures:
1. What the paper actually proposes (method, not marketing).
2. What is novel or interesting about it relative to existing work
   (e.g. wav2lip, SadTalker, EMO, Hallo, VASA, OmniHuman, Sonic, etc.).
3. Any concrete results worth flagging (benchmarks, FPS, resolution, modality).

Skip filler ("This paper presents...", "In recent years..."). Be specific. If
a paper is clearly off-topic (medical lip surgery, lithium batteries, power
grid "synchronization", etc.) say "OFF-TOPIC" and one short reason.

After the per-paper blurbs, add a "## Themes" section (2-4 bullets) noting any
patterns across today's batch: shared architectures, datasets, problem framings,
or notable gaps.

Output Markdown only. Use this exact structure:

## Papers

### <title>
<2-3 sentence blurb>

### <title>
<2-3 sentence blurb>

...

## Themes
- <bullet>
- <bullet>
"""


def load_csv_rows(text: str) -> dict[str, dict]:
    """Parse a papers.csv text blob, return dict keyed by arxiv_id."""
    reader = csv.DictReader(io.StringIO(text))
    return {row["arxiv_id"]: row for row in reader if row.get("arxiv_id")}


def previous_papers() -> dict[str, dict]:
    """Load papers.csv as of git HEAD; empty dict if file did not exist there."""
    try:
        out = subprocess.run(
            ["git", "show", "HEAD:papers.csv"],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError:
        return {}
    return load_csv_rows(out.stdout)


def current_papers() -> dict[str, dict]:
    if not PAPERS_CSV.exists():
        return {}
    return load_csv_rows(PAPERS_CSV.read_text(encoding="utf-8"))


def papers_from_last_days(papers: dict[str, dict], days: int) -> list[dict]:
    cutoff = (datetime.now(tz=timezone.utc).date()).toordinal() - days
    out = []
    for p in papers.values():
        sub = p.get("submitted", "")[:10]
        try:
            if date.fromisoformat(sub).toordinal() >= cutoff:
                out.append(p)
        except ValueError:
            continue
    return out


def render_plain_digest(new_papers: list[dict], today: date) -> str:
    """Fallback when ANTHROPIC_API_KEY is unset."""
    lines = [f"# Lipsync Digest — {today.isoformat()}", ""]
    lines.append(f"{len(new_papers)} new paper(s) since the previous run.")
    lines.append("")
    lines.append("## Papers")
    lines.append("")
    for p in sorted(new_papers, key=lambda r: r.get("submitted", ""), reverse=True):
        title = p.get("title", "(untitled)").strip()
        url = p.get("url", "").strip()
        authors = p.get("authors", "").strip()
        if authors.count(",") >= 4:
            authors = ", ".join(authors.split(", ")[:4]) + " et al."
        submitted = p.get("submitted", "")[:10]
        abstract = p.get("abstract", "").strip()
        lines.append(f"### [{title}]({url})")
        lines.append(f"**{authors}** · {submitted}")
        lines.append("")
        if abstract:
            lines.append(abstract)
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_llm_digest(new_papers: list[dict], today: date) -> str:
    """Use Claude to produce a curated digest. Requires ANTHROPIC_API_KEY."""
    import anthropic

    client = anthropic.Anthropic()

    papers_block_lines = []
    for i, p in enumerate(
        sorted(new_papers, key=lambda r: r.get("submitted", ""), reverse=True), 1
    ):
        title = p.get("title", "").strip()
        authors = p.get("authors", "").strip()
        submitted = p.get("submitted", "")[:10]
        url = p.get("url", "").strip()
        abstract = p.get("abstract", "").strip()
        papers_block_lines.append(
            f"--- Paper {i} ---\n"
            f"Title: {title}\n"
            f"Authors: {authors}\n"
            f"Submitted: {submitted}\n"
            f"URL: {url}\n"
            f"Abstract: {abstract}\n"
        )
    papers_block = "\n".join(papers_block_lines)

    user_msg = (
        f"Today is {today.isoformat()}. {len(new_papers)} new paper(s) were "
        f"added to the lipsync paper list since the previous run.\n\n"
        f"Summarise them following the format in the system prompt.\n\n"
        f"{papers_block}"
    )

    with client.messages.stream(
        model="claude-opus-4-7",
        max_tokens=16000,
        system=[
            {
                "type": "text",
                "text": SYSTEM_PROMPT,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[{"role": "user", "content": user_msg}],
    ) as stream:
        message = stream.get_final_message()

    body_parts: list[str] = []
    for block in message.content:
        if block.type == "text":
            body_parts.append(block.text)
    body = "".join(body_parts).strip()

    paper_links = []
    for p in sorted(new_papers, key=lambda r: r.get("submitted", ""), reverse=True):
        paper_links.append(
            f"- [{p.get('title', '').strip()}]({p.get('url', '').strip()}) — "
            f"{p.get('submitted', '')[:10]}"
        )

    header = (
        f"# Lipsync Digest — {today.isoformat()}\n\n"
        f"{len(new_papers)} new paper(s) since the previous run.\n\n"
    )
    references = "\n\n## References\n\n" + "\n".join(paper_links) + "\n"
    return header + body + references


def write_github_output(key: str, value: str) -> None:
    """Emit a step output for the GitHub Actions runner, if available."""
    gha_out = os.environ.get("GITHUB_OUTPUT")
    if not gha_out:
        return
    with open(gha_out, "a", encoding="utf-8") as f:
        f.write(f"{key}={value}\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--since-days",
        type=int,
        default=None,
        metavar="N",
        help="Ignore git history; include all papers submitted in the last N days.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the digest to stdout instead of writing a file.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    today = datetime.now(tz=timezone.utc).date()

    current = current_papers()
    if not current:
        print("papers.csv missing or empty; nothing to summarise.", file=sys.stderr)
        write_github_output("digest_path", "")
        return 0

    if args.since_days is not None:
        new_papers = papers_from_last_days(current, args.since_days)
        source = f"last {args.since_days} day(s)"
    else:
        prev = previous_papers()
        new_papers = [p for pid, p in current.items() if pid not in prev]
        source = "git diff against HEAD"

    if not new_papers:
        print(f"No new papers ({source}). Skipping digest.", file=sys.stderr)
        write_github_output("digest_path", "")
        return 0

    print(
        f"Found {len(new_papers)} new paper(s) ({source}).",
        file=sys.stderr,
    )

    use_llm = bool(os.environ.get("ANTHROPIC_API_KEY"))
    if use_llm:
        try:
            digest = render_llm_digest(new_papers, today)
        except Exception as exc:  # noqa: BLE001
            print(
                f"LLM digest failed ({exc!r}); falling back to plain digest.",
                file=sys.stderr,
            )
            digest = render_plain_digest(new_papers, today)
    else:
        print("ANTHROPIC_API_KEY not set; using plain digest.", file=sys.stderr)
        digest = render_plain_digest(new_papers, today)

    if args.dry_run:
        sys.stdout.write(digest)
        return 0

    DIGESTS_DIR.mkdir(exist_ok=True)
    out_path = DIGESTS_DIR / f"{today.isoformat()}.md"
    out_path.write_text(digest, encoding="utf-8")
    print(f"Wrote digest to {out_path.relative_to(REPO_ROOT)}.", file=sys.stderr)

    write_github_output("digest_path", str(out_path.relative_to(REPO_ROOT)))
    write_github_output("digest_date", today.isoformat())
    write_github_output("digest_count", str(len(new_papers)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
