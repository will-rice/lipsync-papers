from collections.abc import Sequence
from pathlib import Path

from papers_pipeline.batching import expected_markdown
from papers_pipeline.errors import InfrastructureError
from papers_pipeline.inventory import inventory_order
from papers_pipeline.models import Paper

_START_MARKER = b"<!-- papers-index:start -->"
_END_MARKER = b"<!-- papers-index:end -->"
# The README lists only the tail of papers.csv; the CSV and papers/ hold all.
RECENT_PAPERS = 30
# One small file per publication year, so a reader (or an LLM) can find any
# paper by title without loading papers.csv, which carries every abstract.
TITLE_INDEX_DIRECTORY = "index"


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


def title_index_paths(root: Path, papers: Sequence[Paper]) -> list[Path]:
    """Files of the title index: an overview and one file per publication year."""
    directory = root / TITLE_INDEX_DIRECTORY
    years = sorted({paper.published.year for paper in papers}, reverse=True)
    return [directory / "README.md", *(directory / f"{year}.md" for year in years)]


def write_title_index(root: Path, papers: Sequence[Paper]) -> None:
    """Write the title index: every paper, one line each, grouped by year.

    A line holds the publication date, the title and a link to the paper's
    markdown, or to its source while it is not converted.
    """
    directory = root / TITLE_INDEX_DIRECTORY
    directory.mkdir(exist_ok=True)
    by_year: dict[int, list[Paper]] = {}
    for paper in sorted(papers, key=inventory_order, reverse=True):
        by_year.setdefault(paper.published.year, []).append(paper)
    overview = [
        "# Title index",
        "",
        f"{len(papers)} papers by publication year, newest first. Each year lists"
        " one paper per line: date, title, and a link to its markdown, or to its"
        " source when it is not converted.",
        "",
    ]
    for year, year_papers in by_year.items():
        count = f"{len(year_papers)} paper{'' if len(year_papers) == 1 else 's'}"
        overview.append(f"- [{year}]({year}.md): {count}")
        lines = [f"# {year}", ""]
        for paper in year_papers:
            markdown = expected_markdown(root, paper)
            link = f"../papers/{markdown.name}" if markdown.exists() else paper.url
            title = (
                paper.title.replace("\\", "\\\\")
                .replace("[", "\\[")
                .replace("]", "\\]")
                .replace("\n", " ")
            )
            lines.append(f"- {paper.published.date().isoformat()} [{title}]({link})")
        (directory / f"{year}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (directory / "README.md").write_text("\n".join(overview) + "\n", encoding="utf-8")


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
    recent = sorted(papers, key=inventory_order)[-RECENT_PAPERS:]
    rows = [
        "# Papers",
        "",
        f"The {len(recent)} most recent of {len(papers)} papers. Every paper is"
        " listed in [papers.csv](papers.csv) and converted under"
        " [papers/](papers/).",
        "",
        "| Published | Identifier | Title | Source |",
        "| --- | --- | --- | --- |",
    ]
    for paper in reversed(recent):
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


def _escape_cell(value: str) -> str:
    return value.replace("\\", "\\\\").replace("|", "\\|").replace("\n", " ")
