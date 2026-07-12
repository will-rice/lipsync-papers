"""Tests for scripts/_convert/formatting.py."""

from __future__ import annotations

from pathlib import Path

import pytest

from scripts._convert.formatting import _PRETTIER, format_markdown

pytestmark = pytest.mark.skipif(
    not _PRETTIER.exists(), reason="prettier not installed (run `npm ci`)"
)


def test_format_markdown_normalizes_and_is_idempotent(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Prettier resolves ignore rules relative to the cwd, so run from the tree
    # holding the file — the same way the pipeline invokes it (from repo root).
    monkeypatch.chdir(tmp_path)
    p = tmp_path / "doc.md"
    p.write_text("#  Title\n\n* a\n* b\n", encoding="utf-8")  # extra space, * bullets

    format_markdown(["doc.md"])
    formatted = p.read_text(encoding="utf-8")
    assert formatted != "#  Title\n\n* a\n* b\n"  # Prettier changed it

    # A second pass must be a no-op.
    format_markdown(["doc.md"])
    assert p.read_text(encoding="utf-8") == formatted


def test_format_markdown_skips_patterns_matching_nothing(tmp_path: Path) -> None:
    # A glob that matches no files must not raise (Prettier would error on it).
    format_markdown([str(tmp_path / "missing" / "**" / "*.md")])
