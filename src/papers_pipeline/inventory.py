import csv
from collections.abc import Sequence
from datetime import datetime
from pathlib import Path
from typing import cast

from papers_pipeline.models import InputFormat, Paper

INVENTORY_FIELDS: tuple[str, ...] = (
    "identifier",
    "title",
    "abstract",
    "authors",
    "published",
    "url",
    "source",
    "input_format",
    "input_url",
    "categories",
    "doi",
    "arxiv_id",
)


def write_inventory(path: Path, papers: Sequence[Paper]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=INVENTORY_FIELDS,
            lineterminator="\n",
        )
        writer.writeheader()
        for paper in sorted(papers, key=lambda item: item.identifier):
            writer.writerow(_paper_row(paper))


def read_inventory(path: Path) -> list[Paper]:
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        return []

    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [
            Paper(
                identifier=row["identifier"],
                title=row["title"],
                abstract=row["abstract"],
                authors=tuple(filter(None, row["authors"].split("|"))),
                published=datetime.fromisoformat(row["published"]),
                url=row["url"],
                source=row["source"],
                input_format=cast(InputFormat, row["input_format"]),
                input_url=row["input_url"],
                categories=tuple(filter(None, row["categories"].split("|"))),
                doi=row["doi"] or None,
                arxiv_id=row["arxiv_id"] or None,
            )
            for row in reader
        ]


def _paper_row(paper: Paper) -> dict[str, str]:
    return {
        "identifier": paper.identifier,
        "title": paper.title,
        "abstract": paper.abstract,
        "authors": "|".join(paper.authors),
        "published": paper.published.isoformat(),
        "url": paper.url,
        "source": paper.source,
        "input_format": paper.input_format,
        "input_url": paper.input_url,
        "categories": "|".join(paper.categories),
        "doi": paper.doi or "",
        "arxiv_id": paper.arxiv_id or "",
    }
