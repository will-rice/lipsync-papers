"""YAML front matter that makes each paper's markdown self-describing."""

import re
from collections.abc import Iterable
from pathlib import Path

import yaml

from papers_pipeline.batching import expected_markdown
from papers_pipeline.models import Paper

_FRONT_MATTER = re.compile(r"\A---\n(?P<block>.*?)\n---\n+", re.DOTALL)


def with_front_matter(paper: Paper, markdown: str) -> str:
    """Return markdown led by the paper's metadata, replacing any prior block."""
    block = yaml.safe_dump(
        _metadata(paper), sort_keys=False, allow_unicode=True, width=1_000_000
    )
    return f"---\n{block}---\n\n{_FRONT_MATTER.sub('', markdown, count=1)}"


def write_front_matter(root: Path, papers: Iterable[Paper]) -> list[Path]:
    """Refresh front matter on every generated paper; return the files changed."""
    changed: list[Path] = []
    for paper in papers:
        path = expected_markdown(root, paper)
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        existing = _FRONT_MATTER.match(text)
        # Compare parsed metadata so formatter-only differences are not changes.
        if existing and yaml.safe_load(existing["block"]) == _metadata(paper):
            continue
        path.write_text(with_front_matter(paper, text), encoding="utf-8")
        changed.append(path)
    return changed


def _metadata(paper: Paper) -> dict[str, object]:
    return {
        "identifier": paper.identifier,
        "title": paper.title,
        "authors": list(paper.authors),
        "published": paper.published.isoformat(),
        "url": paper.url,
        "source": paper.source,
        "doi": paper.doi,
        "arxiv_id": paper.arxiv_id,
        "categories": list(paper.categories),
    }
