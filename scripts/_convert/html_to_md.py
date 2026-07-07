"""Convert arXiv/ar5iv HTML (LaTeXML output) to clean markdown via pandoc.

The raw page is chrome-heavy (banners, nav buttons, base64 icons), so conversion
extracts the ``<article>`` element, cleans it, and converts with raw HTML
disabled so LaTeXML's styling markup is dropped instead of passed through.
"""

import re
import subprocess
import urllib.parse
from dataclasses import dataclass

PANDOC_TIMEOUT_SECONDS = 180

# Quality gate: a converted body must look like a paper, not an error page.
MIN_PAPER_CHARS = 2000
MIN_PAPER_HEADINGS = 3

_ARTICLE_RE = re.compile(r"<article\b.*?</article>", re.DOTALL | re.IGNORECASE)
_TOC_NAV_RE = re.compile(r'<nav[^>]*class="[^"]*ltx_TOC[^"]*".*?</nav>', re.DOTALL)
_DATA_URI_IMG_RE = re.compile(r'<img[^>]*src="data:[^"]*"[^>]*>')
_IMG_SRC_RE = re.compile(r'(<img[^>]*\bsrc=")([^"]+)(")')
_EQN_TABLE_RE = re.compile(r'<table[^>]*class="[^"]*ltx_equation[^"]*".*?</table>', re.DOTALL)
_MATH_EL_RE = re.compile(r"<math\b.*?</math>", re.DOTALL)
_INTERNAL_LINK_RE = re.compile(r"\[([^\]]*)\]\(#[^)]*\)")
_BLANK_LINES_RE = re.compile(r"\n{3,}")


@dataclass
class HtmlConversionResult:
    body: str
    exit_code: int
    stderr: str


def convert_html_to_md(html: str, base_url: str) -> HtmlConversionResult:
    """Render a LaTeXML HTML page to GitHub-flavored markdown.

    Args:
        html: Full page HTML as served by arxiv.org/html or ar5iv.
        base_url: Final page URL, used to absolutize relative image paths.
    """
    match = _ARTICLE_RE.search(html)
    if match is None:
        return HtmlConversionResult(body="", exit_code=3, stderr="no <article> element")

    article = clean_article_html(match.group(0), base_url)

    cmd = [
        "pandoc",
        "--from=html",
        "--to=gfm-raw_html",
        "--wrap=none",
    ]
    proc = subprocess.run(
        cmd,
        input=article,
        capture_output=True,
        text=True,
        timeout=PANDOC_TIMEOUT_SECONDS,
    )
    return HtmlConversionResult(
        body=clean_markdown(proc.stdout),
        exit_code=proc.returncode,
        stderr=proc.stderr,
    )


def clean_article_html(article: str, base_url: str) -> str:
    """Strip non-content markup from an ``<article>`` element and fix image URLs."""
    article = _TOC_NAV_RE.sub("", article)
    article = _DATA_URI_IMG_RE.sub("", article)
    # LaTeXML lays out each display equation as a table row; keep only the math.
    article = _EQN_TABLE_RE.sub(lambda m: "".join(_MATH_EL_RE.findall(m.group(0))), article)
    article = _IMG_SRC_RE.sub(
        lambda m: m.group(1) + urllib.parse.urljoin(base_url, m.group(2)) + m.group(3),
        article,
    )
    return article


def clean_markdown(body: str) -> str:
    """Unwrap intra-document anchor links (dead after conversion) and tidy spacing."""
    body = _INTERNAL_LINK_RE.sub(r"\1", body)
    return _BLANK_LINES_RE.sub("\n\n", body).strip() + "\n"


def looks_like_paper(body: str) -> bool:
    """Return True when *body* has the length and section structure of a paper."""
    headings = [line for line in body.splitlines() if line.startswith("#")]
    return (
        len(body) >= MIN_PAPER_CHARS
        and len(headings) >= MIN_PAPER_HEADINGS
        and "data:image" not in body
    )
