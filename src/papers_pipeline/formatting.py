from collections.abc import Sequence
from pathlib import Path

from papers_pipeline.convert import CommandRunner

_FORMATTER = "prettier"
_FORMATTER_TIMEOUT = 300.0
_FORMATTER_SAFE_SUFFIXES = {".md", ".yml", ".yaml", ".json"}


async def format_changed(paths: Sequence[Path], runner: CommandRunner) -> None:
    selected = tuple(
        sorted(
            {
                Path(path)
                for path in paths
                if Path(path).suffix in _FORMATTER_SAFE_SUFFIXES
            }
        )
    )
    if not selected:
        return

    await runner.run(
        [_FORMATTER, "--write", *(str(path) for path in selected)],
        timeout=_FORMATTER_TIMEOUT,
    )


def shard_paths(
    paths: Sequence[Path], shard_index: int, shard_count: int
) -> tuple[Path, ...]:
    if shard_count < 1:
        raise ValueError("shard_count must be at least 1")
    if shard_index < 0 or shard_index >= shard_count:
        raise ValueError("shard_index must be within shard_count")

    unique_paths = {Path(path) for path in paths}
    ordered = tuple(sorted(unique_paths))
    return tuple(
        path
        for position, path in enumerate(ordered)
        if position % shard_count == shard_index
    )
