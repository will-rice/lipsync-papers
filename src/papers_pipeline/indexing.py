from collections.abc import Sequence
from pathlib import Path

from papers_pipeline.batching import expected_markdown
from papers_pipeline.errors import InfrastructureError
from papers_pipeline.models import Paper

_START_MARKER = b"<!-- papers-index:start -->"
_END_MARKER = b"<!-- papers-index:end -->"


def write_index(root: Path, papers: Sequence[Paper]) -> Path:
    path = root / "README.md"
    try:
        existing = path.read_bytes()
    except OSError as error:
        raise InfrastructureError(
            "README generated-section markers are unavailable"
        ) from error
    start = _unique_marker_offset(existing, _START_MARKER, "start")
    end = _unique_marker_offset(existing, _END_MARKER, "end")
    if start >= end:
        raise InfrastructureError("README generated-section markers are out of order")

    generated = ("\n" + _render_index(root, papers)).encode("utf-8")
    content = existing[: start + len(_START_MARKER)] + generated + existing[end:]
    if existing == content:
        return path

    path.write_bytes(content)
    return path


def _unique_marker_offset(content: bytes, marker: bytes, name: str) -> int:
    count = content.count(marker)
    if count == 0:
        raise InfrastructureError(f"README generated section is missing {name} marker")
    if count > 1:
        raise InfrastructureError(
            f"README generated section has duplicate {name} marker"
        )
    return content.index(marker)


def _render_index(root: Path, papers: Sequence[Paper]) -> str:
    rows = [
        "# Papers",
        "",
        "| Published | Identifier | Title | Source |",
        "| --- | --- | --- | --- |",
    ]
    for paper in sorted(papers, key=_paper_sort_key, reverse=True):
        rows.append(
            "| "
            + " | ".join(
                [
                    paper.published.isoformat(),
                    _escape_cell(paper.identifier),
                    f"[{_escape_cell(paper.title)}]({_escape_cell(_link(root, paper))})",
                    _escape_cell(paper.source),
                ]
            )
            + " |"
        )
    return "\n".join(rows) + "\n"


def _link(root: Path, paper: Paper) -> str:
    """Link to the paper's markdown once generated, so the corpus is browsable."""
    markdown = expected_markdown(root, paper)
    return markdown.relative_to(root).as_posix() if markdown.exists() else paper.url


def _paper_sort_key(paper: Paper) -> tuple[object, ...]:
    return (paper.published, paper.identifier)


def _escape_cell(value: str) -> str:
    return value.replace("\\", "\\\\").replace("|", "\\|").replace("\n", " ")
