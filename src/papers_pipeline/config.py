"""Configuration schema and preflight validation for the papers pipeline."""

import re
from datetime import date
from pathlib import Path
from typing import Any, Literal, Mapping

import yaml
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    ValidationError,
    field_validator,
    model_validator,
)

from papers_pipeline.errors import ConfigError as ConfigError

AdapterName = Literal[
    "arxiv",
    "huggingface",
    "semantic_scholar",
    "dblp",
    "biorxiv_crossref",
    "papers_with_code",
]

_FIELD_MESSAGES: dict[tuple[str, ...], str] = {
    ("concurrency", "pdf"): "concurrency.pdf must equal 1",
    ("conversion", "max_papers"): "conversion.max_papers must be between 1 and 100",
    (
        "conversion",
        "timeout_seconds",
    ): "conversion.timeout_seconds must be between 60 and 3600",
    (
        "fetch",
        "total_deadline_seconds",
    ): "fetch.total_deadline_seconds must be between 60 and 7200",
}

_TOPIC_PLUGIN_PATTERN = re.compile(
    r"^[A-Za-z_][A-Za-z0-9_]*(\.[A-Za-z_][A-Za-z0-9_]*)*:[A-Za-z_][A-Za-z0-9_]*$"
)
_ALLOWED_FILTER_KEYS: dict[AdapterName, frozenset[str]] = {
    "arxiv": frozenset({"search_query"}),
    "huggingface": frozenset(),
    "semantic_scholar": frozenset({"query"}),
    "dblp": frozenset({"query"}),
    "biorxiv_crossref": frozenset({"provider"}),
    "papers_with_code": frozenset(),
}


class StrictModel(BaseModel):
    """Base model that rejects unknown fields."""

    model_config = ConfigDict(extra="forbid")


# Adapters whose source APIs filter by date range, so a past window is cheap.
_BACKFILL_ADAPTERS = frozenset(
    {"arxiv", "biorxiv_crossref", "huggingface", "semantic_scholar"}
)


class AdapterConfig(StrictModel):
    """Configuration for one paper source adapter."""

    name: AdapterName
    enabled: bool = True
    secret_env: str | None = None
    lookback_days: int = Field(ge=1, le=365)
    page_size: int = Field(ge=1, le=1000)
    max_pages: int = Field(ge=1, le=100)
    max_results: int = Field(ge=1, le=10000)
    filters: dict[str, str] = Field(default_factory=dict)
    backfill_start: date | None = Field(
        default=None,
        description="Walk history back to this date, backfill_days per run.",
    )
    backfill_days: int = Field(default=30, ge=1, le=365)

    @model_validator(mode="after")
    def validate_filters(self) -> "AdapterConfig":
        allowed_keys = _ALLOWED_FILTER_KEYS[self.name]
        unsupported_keys = sorted(set(self.filters) - allowed_keys)
        if unsupported_keys:
            raise ValueError(_unsupported_filter_message(self.name, allowed_keys))
        if self.name == "biorxiv_crossref":
            provider = self.filters.get("provider")
            if provider is not None and provider not in {"biorxiv", "crossref"}:
                raise ValueError(
                    "biorxiv_crossref.filters.provider must be biorxiv or crossref"
                )
        if self.name == "semantic_scholar" and self.page_size > 100:
            raise ValueError("semantic_scholar.page_size must be at most 100")
        # The nightly workflow exports only this secret to the pipeline.
        if self.name == "semantic_scholar" and self.secret_env not in {
            None,
            "SEMANTIC_SCHOLAR_API_KEY",
        }:
            raise ValueError(
                "semantic_scholar.secret_env must be SEMANTIC_SCHOLAR_API_KEY or null"
            )
        if self.backfill_start is not None and self.name not in _BACKFILL_ADAPTERS:
            raise ValueError(
                f"{self.name} cannot backfill: it does not query past date ranges"
            )
        return self


class TopicConfig(StrictModel):
    """Keyword and plugin selection for paper discovery."""

    include_any: list[str] = Field(default_factory=list)
    include_all: list[str] = Field(default_factory=list)
    exclude_any: list[str] = Field(default_factory=list)
    categories: list[str] = Field(default_factory=list)
    plugin: str | None = None

    @field_validator("plugin")
    @classmethod
    def validate_plugin(cls, value: str | None) -> str | None:
        if value is None or _TOPIC_PLUGIN_PATTERN.match(value):
            return value
        raise ValueError("topic.plugin must use module:function format")


class FetchConfig(StrictModel):
    """HTTP retry and deadline limits."""

    request_timeout_seconds: float = Field(ge=1, le=120)
    retries: int = Field(ge=0, le=5)
    backoff_seconds: float = Field(ge=0, le=30)
    total_deadline_seconds: int = Field(ge=60, le=7200)


class ConversionConfig(StrictModel):
    """Conversion budget and batching limits."""

    max_batches_per_run: int = Field(ge=1, le=20)
    max_papers: int = Field(ge=1, le=100)
    max_cost: int = Field(ge=1, le=1000)
    timeout_seconds: int = Field(default=1800, ge=60, le=3600)
    # Stop starting batches after this long so the run still pushes its work
    # before the workflow step's timeout kills it.
    deadline_seconds: int = Field(default=10800, ge=600, le=18000)
    html_cost: int = Field(ge=1, le=100)
    latex_cost: int = Field(ge=1, le=100)
    pdf_cost: int = Field(ge=1, le=1000)

    @model_validator(mode="after")
    def costs_fit_budget(self) -> "ConversionConfig":
        for field in ("html_cost", "latex_cost", "pdf_cost"):
            if getattr(self, field) > self.max_cost:
                raise ValueError(
                    f"conversion.{field} must not exceed conversion.max_cost"
                )
        return self


class ConcurrencyConfig(StrictModel):
    """Concurrency caps for each conversion type."""

    html: int = Field(ge=1, le=4)
    latex: int = Field(ge=1, le=4)
    pdf: Literal[1]


class RepositoryConfig(StrictModel):
    """Repository metadata copied into the rendered template."""

    name: str = Field(min_length=1)
    slug: str = Field(pattern=r"^[a-z0-9][a-z0-9-]*-papers$")
    description: str = Field(min_length=1)


class PipelineConfig(StrictModel):
    """Top-level rendered configuration."""

    repository: RepositoryConfig
    adapters: list[AdapterConfig]
    topic: TopicConfig
    fetch: FetchConfig
    conversion: ConversionConfig
    concurrency: ConcurrencyConfig

    @model_validator(mode="after")
    def unique_adapters(self) -> "PipelineConfig":
        names = [adapter.name for adapter in self.adapters]
        if len(names) != len(set(names)):
            raise ValueError("adapters must have unique names")
        return self


def _unsupported_filter_message(
    adapter_name: AdapterName, allowed_keys: frozenset[str]
) -> str:
    if not allowed_keys:
        return f"{adapter_name}.filters does not support any keys"
    supported = ", ".join(sorted(allowed_keys))
    return f"{adapter_name}.filters only supports: {supported}"


def _format_validation_error(error: ValidationError) -> str:
    first_issue = error.errors()[0]
    location = tuple(str(part) for part in first_issue["loc"])
    if location in _FIELD_MESSAGES:
        return _FIELD_MESSAGES[location]
    path = ".".join(location) or "config"
    message = str(first_issue["msg"])
    if message.startswith("Value error, "):
        message = message.removeprefix("Value error, ")
    if message.startswith(("topic.plugin", "conversion.")) or ".filters" in message:
        return message
    return f"{path}: {message}"


def _read_config(path: Path) -> Mapping[str, Any]:
    data = yaml.safe_load(path.read_text())
    if not isinstance(data, dict):
        raise ConfigError("config: expected a mapping at the top level")
    return data


def load_config(path: Path, environ: Mapping[str, str]) -> PipelineConfig:
    """Load and validate a rendered pipeline configuration file."""

    try:
        raw_config = _read_config(path)
        config = PipelineConfig.model_validate(raw_config)
    except OSError as error:
        raise ConfigError(str(error)) from error
    except yaml.YAMLError as error:
        raise ConfigError(str(error)) from error
    except ValidationError as error:
        raise ConfigError(_format_validation_error(error)) from error

    for adapter in config.adapters:
        if (
            adapter.enabled
            and adapter.secret_env
            and not environ.get(adapter.secret_env)
        ):
            raise ConfigError(f"{adapter.name}: missing secret {adapter.secret_env}")
    return config
