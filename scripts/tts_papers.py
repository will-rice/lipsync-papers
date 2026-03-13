"""Text-to-speech reader for lipsync papers.

Reads paper titles and abstracts from ``papers.csv`` and converts them to
speech using Google Text-to-Speech (gTTS).  Audio is saved as MP3 files.

Requirements::

    pip install gTTS>=2.5

Usage::

    # Read the 3 most recent papers (saves to ./audio/)
    python scripts/tts_papers.py --latest 3

    # Read a specific paper by arXiv ID
    python scripts/tts_papers.py --paper 2008.10010

    # Search and read papers whose title/abstract match a keyword
    python scripts/tts_papers.py --search "talking head" --latest 2

    # Choose output directory
    python scripts/tts_papers.py --latest 1 --output /tmp/audio

    # Set language (default: en)
    python scripts/tts_papers.py --latest 1 --lang en
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
import textwrap
from pathlib import Path

try:
    from gtts import gTTS, gTTSError
except ImportError:
    print(
        "gTTS is required.  Install it with:\n\n"
        "    pip install gTTS>=2.5\n\n"
        "Or install all TTS dependencies:\n\n"
        "    pip install -r requirements-tts.txt",
        file=sys.stderr,
    )
    sys.exit(1)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
PAPERS_CSV = REPO_ROOT / "papers.csv"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "audio"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _safe_filename(text: str, maxlen: int = 60) -> str:
    """Return a filesystem-safe slug derived from *text*."""
    slug = re.sub(r"[^\w\s-]", "", text.lower())
    slug = re.sub(r"[\s_-]+", "_", slug).strip("_")
    return slug[:maxlen]


def _build_speech_text(paper: dict) -> str:
    """Compose a natural-sounding TTS script for a single paper."""
    title = paper.get("title", "Untitled")
    authors_raw = paper.get("authors", "")
    submitted = paper.get("submitted", "")
    abstract = paper.get("abstract", "")

    # Abbreviate long author lists (>3 names) for readability.
    authors_list = [a.strip() for a in authors_raw.split(",") if a.strip()]
    if len(authors_list) > 3:
        extra = len(authors_list) - 3
        noun = "other" if extra == 1 else "others"
        authors_text = ", ".join(authors_list[:3]) + f", and {extra} {noun}"
    else:
        authors_text = ", ".join(authors_list) if authors_list else "unknown authors"

    parts = [
        f"Title: {title}.",
        f"Authors: {authors_text}.",
    ]
    if submitted:
        parts.append(f"Submitted on {submitted}.")
    if abstract:
        parts.append(f"Abstract. {abstract}")

    return "  ".join(parts)


def load_papers(csv_path: Path) -> list[dict]:
    """Return all papers from *csv_path*, newest first."""
    if not csv_path.exists():
        return []
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def filter_papers(papers: list[dict], search: str | None) -> list[dict]:
    """Return papers whose title or abstract contain *search* (case-insensitive)."""
    if not search:
        return papers
    term = search.lower()
    return [
        p for p in papers
        if term in p.get("title", "").lower() or term in p.get("abstract", "").lower()
    ]


def tts_paper(paper: dict, output_dir: Path, lang: str) -> Path:
    """Generate an MP3 file for *paper* and return the output path.

    Raises ``gTTSError`` on network or API failure.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    arxiv_id = paper.get("arxiv_id", "unknown")
    title_slug = _safe_filename(paper.get("title", arxiv_id))
    filename = f"{arxiv_id}_{title_slug}.mp3"
    out_path = output_dir / filename

    speech_text = _build_speech_text(paper)
    tts = gTTS(text=speech_text, lang=lang, slow=False)
    tts.save(str(out_path))
    return out_path


def print_paper_summary(paper: dict, index: int | None = None) -> None:
    """Pretty-print a brief summary of a paper to stdout."""
    prefix = f"[{index}] " if index is not None else ""
    title = paper.get("title", "Untitled")
    submitted = paper.get("submitted", "")
    arxiv_id = paper.get("arxiv_id", "")
    print(f"\n{prefix}{title}")
    print(f"    arXiv: {arxiv_id}  |  Submitted: {submitted}")
    abstract = paper.get("abstract", "")
    if abstract:
        wrapped = textwrap.fill(abstract, width=80, initial_indent="    ", subsequent_indent="    ")
        print(wrapped[:400] + ("…" if len(wrapped) > 400 else ""))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert lipsync paper titles and abstracts to speech (MP3).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    select = parser.add_mutually_exclusive_group()
    select.add_argument(
        "--paper",
        metavar="ARXIV_ID",
        help="Read a single paper identified by its arXiv ID (e.g. 2008.10010).",
    )
    select.add_argument(
        "--latest",
        type=int,
        metavar="N",
        default=1,
        help="Read the N most recent papers (default: 1).",
    )

    parser.add_argument(
        "--search",
        metavar="TERM",
        help="Filter papers to those whose title or abstract match TERM.",
    )
    parser.add_argument(
        "--output",
        metavar="DIR",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Directory to save MP3 files (default: {DEFAULT_OUTPUT_DIR}).",
    )
    parser.add_argument(
        "--lang",
        metavar="CODE",
        default="en",
        help="BCP 47 language code for gTTS (default: en).",
    )
    parser.add_argument(
        "--csv",
        metavar="FILE",
        type=Path,
        default=PAPERS_CSV,
        help=f"Path to the papers CSV file (default: {PAPERS_CSV}).",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    papers = load_papers(args.csv)
    if not papers:
        print(f"No papers found in {args.csv}.", file=sys.stderr)
        sys.exit(1)

    # Apply optional keyword filter.
    if args.search:
        papers = filter_papers(papers, args.search)
        if not papers:
            print(f"No papers matched the search term '{args.search}'.", file=sys.stderr)
            sys.exit(1)

    # Select paper(s).
    if args.paper:
        target = next((p for p in papers if p.get("arxiv_id") == args.paper), None)
        if target is None:
            print(f"Paper '{args.paper}' not found in {args.csv}.", file=sys.stderr)
            sys.exit(1)
        selected = [target]
    else:
        selected = papers[: args.latest]

    print(f"Converting {len(selected)} paper(s) to speech → {args.output}/")

    for i, paper in enumerate(selected, start=1):
        print_paper_summary(paper, index=i)
        try:
            out_path = tts_paper(paper, args.output, args.lang)
            print(f"    ✓ Saved: {out_path.name}")
        except gTTSError as exc:
            print(
                f"    [error] gTTS failed for '{paper.get('arxiv_id')}': {exc}\n"
                "    Check your internet connection and try again.",
                file=sys.stderr,
            )
            sys.exit(1)

    print(f"\nDone. {len(selected)} MP3 file(s) written to: {args.output}")


if __name__ == "__main__":
    main()
