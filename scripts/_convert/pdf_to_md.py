"""Convert a PDF to markdown via marker-pdf."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path

from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered


@dataclass
class PdfConversionResult:
    body: str
    page_count: int


_CONVERTER: PdfConverter | None = None


def _get_converter() -> PdfConverter:
    """Lazily build the marker converter (loads ML models on first call)."""
    global _CONVERTER
    if _CONVERTER is None:
        logging.info("Loading marker models (one-time, ~30s)…")
        _CONVERTER = PdfConverter(artifact_dict=create_model_dict())
    return _CONVERTER


def convert_pdf_to_md(pdf_path: Path) -> PdfConversionResult:
    """Render *pdf_path* to markdown using marker-pdf."""
    converter = _get_converter()
    rendered = converter(str(pdf_path))
    body, _, images = text_from_rendered(rendered)
    page_count = converter.page_count if converter.page_count is not None else body.count("\f") + 1
    return PdfConversionResult(body=body, page_count=page_count)
