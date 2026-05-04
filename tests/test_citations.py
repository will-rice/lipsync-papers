"""Tests for scripts/_convert/citations.py."""

from __future__ import annotations

from scripts._convert.citations import (
    Reference,  # noqa: F401 — imported for public API visibility in tests
    parse_bbl,
)


SAMPLE_BBL = r"""
\begin{thebibliography}{99}

\bibitem{Prajwal2020}
K.~R. Prajwal, Rudrabha Mukhopadhyay, Vinay~P. Namboodiri, and C.~V. Jawahar.
\newblock A lip sync expert is all you need for speech to lip generation in the
  wild.
\newblock In {\em ACM MM}, 2020.
\newblock arXiv:2008.10010.

\bibitem{Goodfellow2014}
Ian Goodfellow, Jean Pouget-Abadie, et al.
\newblock Generative adversarial nets.
\newblock In {\em NeurIPS}, 2014.

\end{thebibliography}
"""


def test_parse_bbl_extracts_two_entries() -> None:
    refs = parse_bbl(SAMPLE_BBL)
    assert len(refs) == 2
    keys = {r.key for r in refs}
    assert keys == {"Prajwal2020", "Goodfellow2014"}


def test_parse_bbl_extracts_arxiv_id() -> None:
    refs = {r.key: r for r in parse_bbl(SAMPLE_BBL)}
    assert refs["Prajwal2020"].arxiv_id == "2008.10010"
    assert refs["Goodfellow2014"].arxiv_id is None


def test_parse_bbl_extracts_year() -> None:
    refs = {r.key: r for r in parse_bbl(SAMPLE_BBL)}
    assert refs["Prajwal2020"].year == 2020
    assert refs["Goodfellow2014"].year == 2014


SAMPLE_PDF_REFS = """
## References

[1] K. R. Prajwal, R. Mukhopadhyay, V. P. Namboodiri, and C. V. Jawahar. A Lip Sync
Expert Is All You Need for Speech to Lip Generation In The Wild. In ACM MM, 2020.

[2] I. Goodfellow, J. Pouget-Abadie, et al. Generative Adversarial Nets. In NeurIPS, 2014.

[3] J. Ho, A. Jain, and P. Abbeel. Denoising Diffusion Probabilistic Models. NeurIPS, 2020.
"""


def test_parse_pdf_references_extracts_three_entries() -> None:
    from scripts._convert.citations import parse_pdf_references
    refs = parse_pdf_references(SAMPLE_PDF_REFS)
    assert len(refs) == 3
    assert [r.key for r in refs] == ["1", "2", "3"]


def test_parse_pdf_references_extracts_titles() -> None:
    from scripts._convert.citations import parse_pdf_references
    refs = {r.key: r for r in parse_pdf_references(SAMPLE_PDF_REFS)}
    assert "Lip Sync Expert" in refs["1"].title
    assert "Generative Adversarial Nets" in refs["2"].title
    assert "Denoising Diffusion Probabilistic Models" in refs["3"].title
