"""Explicit error types for the papers pipeline."""


class PipelineError(RuntimeError):
    """Base class for explicit pipeline failures."""


class ConfigError(PipelineError):
    """Configuration cannot safely run."""


class InfrastructureError(PipelineError):
    """Shared infrastructure cannot safely continue."""


class SourceUnavailableError(InfrastructureError):
    """A paper source's API could not be used this run; other sources can."""


class PaperError(PipelineError):
    """One paper failed without invalidating unrelated work."""
