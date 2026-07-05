"""Convert a PDF to markdown via marker-pdf.

Conversion is run in an isolated subprocess (``_pdf_worker``) so that native
crashes in pdfium/torch — e.g. a glibc ``malloc_consolidate`` SIGABRT — do
not propagate to the parent process and kill the entire conversion run.
"""

from __future__ import annotations

import json
import logging
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]  # lipsync-papers/
_WORKER_MODULE = "scripts._convert._pdf_worker"
_CONVERT_TIMEOUT = 300  # seconds per PDF
_MAX_STDERR_LEN = 500  # characters of subprocess stderr to include in error messages
_MAX_STDOUT_PREVIEW = 200  # characters of stdout to show when JSON parsing fails


@dataclass
class PdfConversionResult:
    body: str
    page_count: int


def convert_pdf_to_md(pdf_path: Path) -> PdfConversionResult:
    """Render *pdf_path* to markdown using marker-pdf.

    Spawns a fresh subprocess for each conversion so that any native-level
    crash (SIGABRT, SIGSEGV, …) in marker-pdf's C dependencies is contained
    to the child process and surfaces here as a plain :class:`RuntimeError`.
    """
    logging.info("Converting PDF via subprocess: %s", pdf_path.name)
    try:
        result = subprocess.run(
            [sys.executable, "-m", _WORKER_MODULE, str(pdf_path)],
            capture_output=True,
            text=True,
            timeout=_CONVERT_TIMEOUT,
            cwd=_REPO_ROOT,
        )
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(
            f"PDF conversion timed out after {_CONVERT_TIMEOUT}s: {pdf_path.name}"
        ) from exc

    if result.returncode != 0:
        stderr = result.stderr.strip()
        raise RuntimeError(
            f"PDF conversion subprocess exited {result.returncode}: {stderr[:_MAX_STDERR_LEN]}"
        )

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"PDF worker produced invalid JSON: {result.stdout[:_MAX_STDOUT_PREVIEW]}"
        ) from exc

    return PdfConversionResult(body=data["body"], page_count=data["page_count"])
