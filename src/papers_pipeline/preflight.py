import shutil
from collections.abc import Callable

from papers_pipeline.config import PipelineConfig
from papers_pipeline.errors import InfrastructureError

ToolLookup = Callable[[str], str | None]

_PDF_ADAPTERS = {
    "arxiv",
    "huggingface",
    "semantic_scholar",
    "biorxiv_crossref",
    "papers_with_code",
}
_PANDOC_ADAPTERS = {"dblp", "biorxiv_crossref"}


def required_tools(config: PipelineConfig) -> tuple[str, ...]:
    enabled = {adapter.name for adapter in config.adapters if adapter.enabled}
    tools: set[str] = {"prettier"}
    if enabled & _PDF_ADAPTERS:
        tools.add("marker_single")
    if enabled & _PANDOC_ADAPTERS:
        tools.add("pandoc")
    return tuple(sorted(tools))


def validate_required_tools(
    config: PipelineConfig,
    lookup: ToolLookup = shutil.which,
) -> None:
    missing = [tool for tool in required_tools(config) if lookup(tool) is None]
    if missing:
        raise InfrastructureError(f"missing required tools: {', '.join(missing)}")
