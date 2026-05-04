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


def test_resolve_local_sibling_priority(tmp_path) -> None:
    from scripts._convert.citations import (
        Reference,
        ResolutionContext,
        resolve_reference,
    )
    ctx = ResolutionContext(
        corpus_arxiv_to_year={"2008.10010": "2020", "2006.11239": "2020"},
        current_year="2026",
        s2_cache={},
    )
    ref = Reference(key="x", raw="…", arxiv_id="2008.10010")
    resolve_reference(ref, ctx)
    assert ref.resolved_url == "../2020/2008.10010.md"


def test_resolve_external_arxiv_fallback() -> None:
    from scripts._convert.citations import (
        Reference,
        ResolutionContext,
        resolve_reference,
    )
    ctx = ResolutionContext(
        corpus_arxiv_to_year={},
        current_year="2026",
        s2_cache={},
    )
    ref = Reference(key="x", raw="…", arxiv_id="9999.99999")
    resolve_reference(ref, ctx)
    assert ref.resolved_url == "https://arxiv.org/abs/9999.99999"


def test_resolve_doi_fallback() -> None:
    from scripts._convert.citations import (
        Reference,
        ResolutionContext,
        resolve_reference,
    )
    ctx = ResolutionContext(
        corpus_arxiv_to_year={},
        current_year="2026",
        s2_cache={},
    )
    ref = Reference(key="x", raw="…", doi="10.1145/3394171.3413532")
    resolve_reference(ref, ctx)
    assert ref.resolved_url == "https://doi.org/10.1145/3394171.3413532"


def test_resolve_s2_lookup_promotes_to_arxiv(fixtures_dir) -> None:
    import json
    from scripts._convert.citations import (
        Reference,
        ResolutionContext,
        resolve_reference,
    )
    cache = json.loads((fixtures_dir / "citations_in.json").read_text())
    ctx = ResolutionContext(
        corpus_arxiv_to_year={"2006.11239": "2020"},
        current_year="2026",
        s2_cache=cache,
    )
    ref = Reference(key="x", raw="…", title="Denoising Diffusion Probabilistic Models")
    resolve_reference(ref, ctx)
    # arXiv ID was found via S2, then matched against corpus → local sibling
    assert ref.arxiv_id == "2006.11239"
    assert ref.resolved_url == "../2020/2006.11239.md"


def test_resolve_unresolvable_remains_none() -> None:
    from scripts._convert.citations import (
        Reference,
        ResolutionContext,
        resolve_reference,
    )
    ctx = ResolutionContext(
        corpus_arxiv_to_year={},
        current_year="2026",
        s2_cache={"title:nonexistent paper title that should not match": {"data": []}},
    )
    ref = Reference(key="x", raw="…", title="Nonexistent paper title that should not match")
    resolve_reference(ref, ctx)
    assert ref.resolved_url is None
