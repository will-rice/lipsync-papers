from datetime import datetime, timezone
from pathlib import Path

import pytest

from papers_pipeline.batching import (
    Batch,
    Backlog,
    expected_markdown,
    infer_backlog,
    select_batch,
)
from papers_pipeline.config import ConversionConfig
from papers_pipeline.models import InputFormat, Paper


def paper(identifier: str, *, input_format: InputFormat = "pdf") -> Paper:
    return Paper(
        identifier=identifier,
        title=f"{identifier} title",
        abstract=f"{identifier} abstract",
        authors=("A. Author",),
        published=datetime(2024, 1, 2, tzinfo=timezone.utc),
        url=f"https://example.test/{identifier}",
        source="arxiv",
        input_format=input_format,
        input_url=f"https://example.test/{identifier}.{input_format}",
        categories=("cs.CL",),
    )


@pytest.fixture
def papers() -> tuple[Paper, ...]:
    return (
        paper("arxiv:1-2", input_format="pdf"),
        paper("arxiv:1/2", input_format="html"),
        paper("arxiv:2", input_format="latex"),
        paper("arxiv:3", input_format="pdf"),
    )


@pytest.fixture
def config() -> ConversionConfig:
    return ConversionConfig(
        max_batches_per_run=1,
        max_papers=10,
        max_cost=10,
        html_cost=2,
        latex_cost=3,
        pdf_cost=5,
    )


def test_backlog_is_empty_for_empty_inventory(tmp_path: Path) -> None:
    result = infer_backlog((), tmp_path)

    assert result == Backlog(generated=(), blocked=(), pending=())


def test_backlog_partitions_generated_blocked_and_pending_in_sorted_order(
    tmp_path: Path, papers: tuple[Paper, ...]
) -> None:
    generated = expected_markdown(tmp_path, papers[0])
    generated.parent.mkdir(parents=True)
    generated.write_text("# complete", encoding="utf-8")

    blocked = expected_markdown(tmp_path, papers[1]).with_suffix(".fixme.txt")
    blocked.write_text("manual repair required", encoding="utf-8")

    result = infer_backlog(reversed(papers), tmp_path)

    assert result.generated == (papers[0],)
    assert result.blocked == (papers[1],)
    assert result.pending == (papers[2], papers[3])


def test_expected_markdown_is_collision_resistant_for_similar_identifiers(
    tmp_path: Path, papers: tuple[Paper, ...]
) -> None:
    first = expected_markdown(tmp_path, papers[0])
    second = expected_markdown(tmp_path, papers[1])

    assert first != second

    first.parent.mkdir(parents=True)
    first.write_text("# complete", encoding="utf-8")

    result = infer_backlog((papers[0], papers[1]), tmp_path)

    assert result.generated == (papers[0],)
    assert result.pending == (papers[1],)


def test_select_batch_is_bounded_by_count(
    config: ConversionConfig, papers: tuple[Paper, ...]
) -> None:
    limited = config.model_copy(update={"max_papers": 2, "max_cost": 100})

    batch = select_batch(reversed(papers), limited)

    assert batch == Batch(papers=(papers[0], papers[1]), estimated_cost=7)
    assert len(batch.papers) <= limited.max_papers
    assert batch.estimated_cost <= limited.max_cost


def test_select_batch_is_bounded_by_cost(
    config: ConversionConfig, papers: tuple[Paper, ...]
) -> None:
    limited = config.model_copy(update={"max_cost": 6, "max_papers": 10})

    batch = select_batch(reversed(papers), limited)

    assert batch == Batch(papers=(papers[0],), estimated_cost=5)
    assert batch.estimated_cost <= limited.max_cost


def test_select_batch_stops_before_an_oversized_first_paper(
    config: ConversionConfig, papers: tuple[Paper, ...]
) -> None:
    limited = config.model_copy(update={"max_cost": 4, "max_papers": 10})

    batch = select_batch(reversed(papers), limited)

    assert batch == Batch(papers=(), estimated_cost=0)


def test_select_batch_uses_stable_sorted_order_for_reversed_input(
    config: ConversionConfig, papers: tuple[Paper, ...]
) -> None:
    limited = config.model_copy(update={"max_papers": 3, "max_cost": 100})

    batch = select_batch(reversed(papers), limited)

    assert [paper.identifier for paper in batch.papers] == [
        "arxiv:1-2",
        "arxiv:1/2",
        "arxiv:2",
    ]


def test_arxiv_papers_cost_as_html_since_they_convert_from_arxiv_html() -> None:
    config = ConversionConfig(
        max_batches_per_run=1,
        max_papers=10,
        max_cost=10,
        html_cost=1,
        latex_cost=2,
        pdf_cost=10,
    )
    on_arxiv = paper("arxiv:2401.00001").model_copy(update={"arxiv_id": "2401.00001"})

    batch = select_batch([on_arxiv, paper("doi:10.1/x")], config)

    assert batch.estimated_cost == 1
    assert batch.papers == (on_arxiv,)
