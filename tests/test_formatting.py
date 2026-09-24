import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Sequence

import pytest

from papers_pipeline.convert import CommandRunner
from papers_pipeline.errors import InfrastructureError, PaperError
from papers_pipeline.formatting import format_changed, shard_paths
from papers_pipeline.indexing import write_index
from papers_pipeline.models import Paper


def paper(identifier: str, *, published: datetime) -> Paper:
    return Paper(
        identifier=identifier,
        title=f"{identifier} title",
        abstract=f"{identifier} abstract",
        authors=("A. Author",),
        published=published,
        url=f"https://example.test/{identifier}",
        source="arxiv",
        input_format="pdf",
        input_url=f"https://example.test/{identifier}.pdf",
        categories=("cs.CL",),
    )


class RecordingRunner(CommandRunner):
    def __init__(self) -> None:
        self.calls: list[list[str]] = []

    async def run(
        self, argv: Sequence[str], timeout: float
    ) -> subprocess.CompletedProcess[str]:
        self.calls.append(list(argv))
        return subprocess.CompletedProcess(
            args=list(argv), returncode=0, stdout="", stderr=""
        )


class RaisingRunner(CommandRunner):
    def __init__(self, error: Exception) -> None:
        self.error = error

    async def run(
        self, argv: Sequence[str], timeout: float
    ) -> subprocess.CompletedProcess[str]:
        raise self.error


@pytest.mark.asyncio
async def test_format_changed_passes_exact_paths_and_sorts_deduplicates(
    tmp_path: Path,
) -> None:
    first = tmp_path / "generated papers" / "b.md"
    second = tmp_path / "generated papers" / "a.md"
    third = tmp_path / "README.md"
    unsupported = tmp_path / "notes.txt"
    for path in (first, second, third):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("x", encoding="utf-8")
    unsupported.write_text("x", encoding="utf-8")

    runner = RecordingRunner()

    await format_changed([first, third, second, first, third, unsupported], runner)

    assert runner.calls == [
        [
            "prettier",
            "--write",
            str(third),
            str(second),
            str(first),
        ]
    ]
    assert all("*" not in arg for arg in runner.calls[0])
    assert "generated papers" in runner.calls[0][3]
    assert str(unsupported) not in runner.calls[0]


@pytest.mark.asyncio
async def test_format_changed_is_noop_for_empty_or_unsupported_input() -> None:
    runner = RecordingRunner()

    await format_changed([], runner)
    await format_changed([Path("notes.txt"), Path("script.py")], runner)

    assert runner.calls == []


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("error", "expected_match"),
    [
        (
            InfrastructureError("missing conversion tool: prettier"),
            "missing conversion tool",
        ),
        (
            PaperError("prettier exited 1"),
            "prettier exited 1",
        ),
        (
            InfrastructureError("conversion infrastructure timeout: prettier"),
            "conversion infrastructure timeout",
        ),
    ],
)
async def test_format_changed_propagates_command_runner_classification(
    error: Exception, expected_match: str, tmp_path: Path
) -> None:
    target = tmp_path / "README.md"
    target.write_text("x", encoding="utf-8")

    with pytest.raises(type(error), match=expected_match):
        await format_changed([target], RaisingRunner(error))


def test_shard_paths_partitions_sorted_corpus_exactly_once(tmp_path: Path) -> None:
    corpus = [
        tmp_path / "z.md",
        tmp_path / "alpha.md",
        tmp_path / "beta.md",
        tmp_path / "a file.md",
        tmp_path / "middle.md",
    ]

    shards = [
        shard_paths(
            list(reversed(corpus)) + [corpus[1], corpus[3], corpus[1]], index, 3
        )
        for index in range(3)
    ]
    ordered = tuple(sorted(corpus))

    assert shards[0] == tuple(
        path for position, path in enumerate(ordered) if position % 3 == 0
    )
    assert shards[1] == tuple(
        path for position, path in enumerate(ordered) if position % 3 == 1
    )
    assert shards[2] == tuple(
        path for position, path in enumerate(ordered) if position % 3 == 2
    )
    assert set(shards[0]).isdisjoint(shards[1])
    assert set(shards[0]).isdisjoint(shards[2])
    assert set(shards[1]).isdisjoint(shards[2])
    assert tuple(sorted(path for shard in shards for path in shard)) == ordered


@pytest.mark.parametrize(
    ("shard_index", "shard_count"),
    [(-1, 3), (0, 0), (3, 3), (1, -2)],
)
def test_shard_paths_validates_bounds(
    tmp_path: Path, shard_index: int, shard_count: int
) -> None:
    with pytest.raises(ValueError):
        shard_paths([tmp_path / "a.md"], shard_index, shard_count)


def test_write_index_is_deterministic_and_skips_unchanged_rewrites(
    tmp_path: Path,
) -> None:
    readme = tmp_path / "README.md"
    readme.write_text(
        "# Custom documentation\n\n"
        "<!-- papers-index:start -->\n"
        "old generated content\n"
        "<!-- papers-index:end -->\n"
        "\n## Hand-written notes\n\nKeep this exactly.\n",
        encoding="utf-8",
    )
    papers = (
        paper("paper:3", published=datetime(2025, 1, 3, 9, tzinfo=timezone.utc)),
        paper("paper:1", published=datetime(2025, 1, 1, 9, tzinfo=timezone.utc)),
        paper("paper:2", published=datetime(2025, 1, 2, 9, tzinfo=timezone.utc)),
    )

    index_path = write_index(tmp_path, papers)
    first_content = index_path.read_text(encoding="utf-8")
    first_mtime = index_path.stat().st_mtime_ns

    second_path = write_index(tmp_path, tuple(reversed(papers)))
    second_content = second_path.read_text(encoding="utf-8")
    second_mtime = second_path.stat().st_mtime_ns

    assert index_path == second_path
    assert first_content == second_content
    assert first_mtime == second_mtime
    assert first_content.endswith("\n")
    assert first_content.count("|") > 0


def test_write_index_preserves_bytes_outside_generated_section(tmp_path: Path) -> None:
    prefix = (
        b"# Custom documentation\r\n\r\n"
        b"Keep  trailing spaces.  \r\n"
        b"<!-- papers-index:start -->"
    )
    suffix = (
        b"<!-- papers-index:end -->\r\n"
        b"\r\n## Hand-written notes\r\n\r\nDo not rewrite me.\r\n"
    )
    readme = tmp_path / "README.md"
    readme.write_bytes(prefix + b"\nold\n" + suffix)

    write_index(
        tmp_path,
        (paper("paper:1", published=datetime(2025, 1, 1, tzinfo=timezone.utc)),),
    )
    first = readme.read_bytes()
    write_index(
        tmp_path,
        (paper("paper:1", published=datetime(2025, 1, 1, tzinfo=timezone.utc)),),
    )

    assert first.startswith(prefix)
    assert first.endswith(suffix)
    assert readme.read_bytes() == first


@pytest.mark.parametrize(
    ("content", "message"),
    [
        ("# no markers\n", "missing start marker"),
        (
            "<!-- papers-index:start -->\nmissing end\n",
            "missing end marker",
        ),
        (
            "<!-- papers-index:end -->\n<!-- papers-index:start -->\n",
            "markers are out of order",
        ),
        (
            "<!-- papers-index:start -->\n<!-- papers-index:start -->\n"
            "<!-- papers-index:end -->\n",
            "duplicate start marker",
        ),
        (
            "<!-- papers-index:start -->\n<!-- papers-index:end -->\n"
            "<!-- papers-index:end -->\n",
            "duplicate end marker",
        ),
    ],
)
def test_write_index_rejects_invalid_marker_layout(
    tmp_path: Path,
    content: str,
    message: str,
) -> None:
    readme = tmp_path / "README.md"
    readme.write_text(content, encoding="utf-8")

    with pytest.raises(InfrastructureError, match=message):
        write_index(tmp_path, ())

    assert readme.read_text(encoding="utf-8") == content
