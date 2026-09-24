import hashlib
import re
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

from papers_pipeline.config import ConversionConfig
from papers_pipeline.models import Paper

_SUFFIX_LENGTH = 12
_SLUG_LIMIT = 80


@dataclass(frozen=True)
class Backlog:
    generated: tuple[Paper, ...]
    blocked: tuple[Paper, ...]
    pending: tuple[Paper, ...]


@dataclass(frozen=True)
class Batch:
    papers: tuple[Paper, ...]
    estimated_cost: int


def expected_markdown(root: Path, paper: Paper) -> Path:
    return (
        root
        / "papers"
        / f"{_identifier_slug(paper.identifier)}--{_identifier_digest(paper.identifier)}.md"
    )


def infer_backlog(papers: Iterable[Paper], root: Path) -> Backlog:
    generated: list[Paper] = []
    blocked: list[Paper] = []
    pending: list[Paper] = []

    for paper in sorted(papers, key=lambda item: item.identifier):
        expected = expected_markdown(root, paper)
        if expected.exists():
            generated.append(paper)
        elif expected.with_suffix(".fixme.txt").exists():
            blocked.append(paper)
        else:
            pending.append(paper)

    return Backlog(tuple(generated), tuple(blocked), tuple(pending))


def select_batch(pending: Iterable[Paper], config: ConversionConfig) -> Batch:
    selected: list[Paper] = []
    estimated_cost = 0

    for paper in sorted(pending, key=lambda item: item.identifier):
        if len(selected) >= config.max_papers:
            break

        cost = _paper_cost(paper, config)
        if cost > config.max_cost or estimated_cost + cost > config.max_cost:
            break

        selected.append(paper)
        estimated_cost += cost

    return Batch(papers=tuple(selected), estimated_cost=estimated_cost)


def _paper_cost(paper: Paper, config: ConversionConfig) -> int:
    return {
        "html": config.html_cost,
        "latex": config.latex_cost,
        "pdf": config.pdf_cost,
    }[paper.input_format]


def _identifier_slug(identifier: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", identifier.casefold()).strip("-")
    if not slug:
        return "paper"
    return slug[:_SLUG_LIMIT].rstrip("-") or "paper"


def _identifier_digest(identifier: str) -> str:
    return hashlib.sha256(identifier.encode("utf-8")).hexdigest()[:_SUFFIX_LENGTH]
