"""Convert arXiv HTML to markdown via pandoc."""

from __future__ import annotations

import logging
import subprocess
from dataclasses import dataclass

PANDOC_TIMEOUT_SECONDS = 180


@dataclass
class HtmlConversionResult:
    body: str
    exit_code: int
    stderr: str


def convert_html_to_md(html: str) -> HtmlConversionResult:
    """Render an HTML document string to GitHub-flavored markdown."""
    cmd = [
        "pandoc",
        "--from=html",
        "--to=gfm",
        "--wrap=none",
    ]
    logging.info("Running: %s", " ".join(cmd))
    proc = subprocess.run(
        cmd,
        input=html,
        capture_output=True,
        text=True,
        timeout=PANDOC_TIMEOUT_SECONDS,
    )
    return HtmlConversionResult(
        body=proc.stdout,
        exit_code=proc.returncode,
        stderr=proc.stderr,
    )
