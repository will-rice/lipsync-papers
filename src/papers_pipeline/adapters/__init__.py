from collections.abc import Mapping

from papers_pipeline.config import PipelineConfig

from .arxiv import ArxivAdapter
from .base import Adapter, FetchPage, FetchWindow, collect_records
from .biorxiv_crossref import BiorxivCrossrefAdapter
from .dblp import DblpAdapter
from .huggingface import HuggingFaceAdapter
from .papers_with_code import PapersWithCodeAdapter
from .semantic_scholar import SemanticScholarAdapter


def build_adapters(
    config: PipelineConfig,
    environ: Mapping[str, str],
) -> dict[str, Adapter]:
    semantic_config = next(
        (item for item in config.adapters if item.name == "semantic_scholar"),
        None,
    )
    semantic_key = ""
    if (
        semantic_config is not None
        and semantic_config.enabled
        and semantic_config.secret_env is not None
    ):
        semantic_key = environ.get(semantic_config.secret_env, "")
    return {
        "arxiv": ArxivAdapter(),
        "huggingface": HuggingFaceAdapter(),
        "semantic_scholar": SemanticScholarAdapter(semantic_key),
        "dblp": DblpAdapter(),
        "biorxiv_crossref": BiorxivCrossrefAdapter(),
        "papers_with_code": PapersWithCodeAdapter(),
    }


__all__ = [
    "Adapter",
    "ArxivAdapter",
    "BiorxivCrossrefAdapter",
    "DblpAdapter",
    "FetchPage",
    "FetchWindow",
    "HuggingFaceAdapter",
    "PapersWithCodeAdapter",
    "SemanticScholarAdapter",
    "build_adapters",
    "collect_records",
]
