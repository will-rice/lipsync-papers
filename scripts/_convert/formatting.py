"""Normalize generated markdown with the repo-pinned Prettier.

Kept dependency-light (standard library only) so the stdlib-only fetch script
can use it without pulling in the conversion pipeline's third-party deps.
"""

from __future__ import annotations

import glob
import subprocess
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
_PRETTIER = _REPO_ROOT / "node_modules" / ".bin" / "prettier"


def format_markdown(patterns: list[str]) -> None:
    """Format markdown matching *patterns* in place with Prettier.

    Patterns are Prettier globs (e.g. ``papers/**/*.md``) or plain file paths.
    Patterns that match nothing are dropped so Prettier does not error on an
    empty corpus; globs are passed through to Prettier so argv stays small.

    Raises:
        RuntimeError: if the pinned Prettier is not installed (run ``npm ci``).
    """
    if not _PRETTIER.exists():
        raise RuntimeError("Prettier is not installed; run `npm ci` before formatting markdown.")

    active = [p for p in patterns if glob.glob(p, recursive=True)]
    if not active:
        return

    subprocess.run([str(_PRETTIER), "--write", *active], check=True)

    # A rare markdown file only reaches a Prettier-stable form after a second
    # pass; after one --write it still fails `prettier --check` (and thus CI).
    # Re-format just those stragglers so the output is check-clean. --list-different
    # exits non-zero when it finds any, so we read stdout instead of check=True.
    stragglers = subprocess.run(
        [str(_PRETTIER), "--list-different", *active],
        capture_output=True,
        text=True,
    ).stdout.split()
    if stragglers:
        subprocess.run([str(_PRETTIER), "--write", *stragglers], check=True)
