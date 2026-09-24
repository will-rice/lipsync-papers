from datetime import datetime, timezone
from pathlib import Path

import pytest
import yaml

from papers_pipeline.batching import expected_markdown
from papers_pipeline.cli import app
from papers_pipeline.front_matter import with_front_matter, write_front_matter
from papers_pipeline.indexing import write_index
from papers_pipeline.inventory import write_inventory
from papers_pipeline.models import Paper

PAPER = Paper(
    identifier="arxiv:2401.12345",
    title="Neural Speech: A Study",
    abstract="Abstract.",
    authors=("A. Author", "B. Author"),
    published=datetime(2024, 1, 2, tzinfo=timezone.utc),
    url="https://arxiv.org/abs/2401.12345",
    source="arxiv",
    input_format="pdf",
    input_url="https://arxiv.org/pdf/2401.12345",
    categories=("cs.SD", "eess.AS"),
    arxiv_id="2401.12345",
)


def front_matter(text: str) -> dict[str, object]:
    _, block, _ = text.split("---\n", 2)
    metadata = yaml.safe_load(block)
    assert isinstance(metadata, dict)
    return metadata


def test_front_matter_describes_the_paper_above_its_body() -> None:
    text = with_front_matter(PAPER, "# Neural Speech\n\nBody.\n")

    assert text.startswith("---\n")
    assert text.endswith("---\n\n# Neural Speech\n\nBody.\n")
    assert front_matter(text) == {
        "identifier": "arxiv:2401.12345",
        "title": "Neural Speech: A Study",
        "authors": ["A. Author", "B. Author"],
        "published": "2024-01-02T00:00:00+00:00",
        "url": "https://arxiv.org/abs/2401.12345",
        "source": "arxiv",
        "doi": None,
        "arxiv_id": "2401.12345",
        "categories": ["cs.SD", "eess.AS"],
    }


def test_front_matter_replaces_an_existing_block() -> None:
    legacy = '---\narxiv_id: "2401.12345"\ntitle: Old\n---\n\n# Neural Speech\n'

    text = with_front_matter(PAPER, legacy)

    assert front_matter(text)["title"] == "Neural Speech: A Study"
    assert text.count("---\n") == 2
    assert text.endswith("---\n\n# Neural Speech\n")


def test_write_front_matter_updates_only_generated_papers_that_differ(
    tmp_path: Path,
) -> None:
    pending = PAPER.model_copy(update={"identifier": "arxiv:2401.99999"})
    path = expected_markdown(tmp_path, PAPER)
    path.parent.mkdir()
    path.write_text("# Neural Speech\n", encoding="utf-8")

    assert write_front_matter(tmp_path, [PAPER, pending]) == [path]
    # Reformatting the block (as prettier may) does not count as a change.
    path.write_text(
        path.read_text(encoding="utf-8").replace("title: ", "title:  "),
        encoding="utf-8",
    )
    assert write_front_matter(tmp_path, [PAPER, pending]) == []
    assert not expected_markdown(tmp_path, pending).exists()


def test_index_links_generated_papers_to_their_markdown(tmp_path: Path) -> None:
    pending = PAPER.model_copy(
        update={"identifier": "arxiv:2401.99999", "title": "Pending"}
    )
    path = expected_markdown(tmp_path, PAPER)
    path.parent.mkdir()
    path.write_text("# Neural Speech\n", encoding="utf-8")
    readme = tmp_path / "README.md"
    readme.write_text(
        "<!-- papers-index:start -->\n<!-- papers-index:end -->\n", encoding="utf-8"
    )

    text = write_index(tmp_path, [PAPER, pending]).read_text(encoding="utf-8")

    assert f"[Neural Speech: A Study](papers/{path.name})" in text
    assert "[Pending](https://arxiv.org/abs/2401.12345)" in text


def test_front_matter_command_skips_papers_already_up_to_date(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    write_inventory(tmp_path / "papers.csv", [PAPER])
    path = expected_markdown(tmp_path, PAPER)
    path.parent.mkdir()
    path.write_text(with_front_matter(PAPER, "# Neural Speech\n"), encoding="utf-8")
    monkeypatch.chdir(tmp_path)

    assert app(["front-matter"]) == 0
    assert capsys.readouterr().out == "front matter updated: 0 papers\n"
