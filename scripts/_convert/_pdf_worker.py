"""Standalone entry point for marker-pdf conversion.

This module is invoked as a subprocess by :func:`pdf_to_md.convert_pdf_to_md`
so that native crashes in pdfium/torch (e.g. glibc ``malloc_consolidate``
heap-corruption SIGABRT) do not kill the parent conversion process.

Usage (internal — do not call directly)::

    python -m scripts._convert._pdf_worker <pdf_path>

Outputs a single JSON line to stdout::

    {"body": "...", "page_count": 12}

Exits with code 1 and writes an error message to stderr on failure.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: _pdf_worker.py <pdf_path>", file=sys.stderr)
        sys.exit(1)

    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        print(f"PDF not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    from marker.converters.pdf import PdfConverter
    from marker.models import create_model_dict
    from marker.output import text_from_rendered

    converter = PdfConverter(artifact_dict=create_model_dict())
    rendered = converter(str(pdf_path))
    body, _, _images = text_from_rendered(rendered)
    page_count = (
        converter.page_count if converter.page_count is not None else body.count("\f") + 1
    )  # \f = form-feed page separator used by marker-pdf
    print(json.dumps({"body": body, "page_count": page_count}))


if __name__ == "__main__":
    main()
