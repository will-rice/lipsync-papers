from datetime import datetime, timedelta
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

InputFormat = Literal["html", "latex", "pdf"]


class FrozenModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class SourceRecord(FrozenModel):
    source: str
    source_id: str
    title: str
    abstract: str
    authors: tuple[str, ...]
    published: datetime
    url: str
    input_format: InputFormat
    input_url: str
    categories: tuple[str, ...] = Field(default_factory=tuple)
    doi: str | None = None
    arxiv_id: str | None = None


class Paper(FrozenModel):
    identifier: str
    title: str
    abstract: str
    authors: tuple[str, ...]
    published: datetime
    url: str
    source: str
    input_format: InputFormat
    input_url: str
    categories: tuple[str, ...] = Field(default_factory=tuple)
    doi: str | None = None
    arxiv_id: str | None = None


class FailureAttempt(FrozenModel):
    occurred_at: datetime
    error: str


class SourceContinuation(FrozenModel):
    cursor: str
    window_start: datetime
    window_end: datetime

    @model_validator(mode="after")
    def validate_window(self) -> "SourceContinuation":
        for name, value in (
            ("window_start", self.window_start),
            ("window_end", self.window_end),
        ):
            if value.tzinfo is None or value.utcoffset() is None:
                raise ValueError(f"{name} must be timezone-aware")
            if value.utcoffset() != timedelta(0):
                raise ValueError(f"{name} must use UTC")
        if self.window_start > self.window_end:
            raise ValueError("window_start must not be after window_end")
        return self


class BackfillProgress(FrozenModel):
    """How far back a source's history has been fetched."""

    covered_from: datetime
    continuation: SourceContinuation | None = None


class PipelineState(BaseModel):
    model_config = ConfigDict(extra="forbid")

    continuations: dict[str, SourceContinuation] = Field(default_factory=dict)
    backfill: dict[str, BackfillProgress] = Field(default_factory=dict)
    failures: dict[str, list[FailureAttempt]] = Field(default_factory=dict)

    @model_validator(mode="before")
    @classmethod
    def discard_legacy_cursors(cls, value: object) -> object:
        if isinstance(value, dict) and "cursors" in value:
            migrated = dict(value)
            migrated.pop("cursors")
            return migrated
        return value
