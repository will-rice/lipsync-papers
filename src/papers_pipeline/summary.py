from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class SourceCounts:
    source: str
    fetched: int
    accepted: int
    deduplicated: int
    rejected: int
    capped: bool
    complete: bool


@dataclass
class RunSummary:
    sources: tuple[SourceCounts, ...] = ()
    inventory: int = 0
    generated: int = 0
    pending: int = 0
    attempted: int = 0
    succeeded: int = 0
    failed: int = 0
    deferred: int = 0
    promoted_to_fixme: int = 0
    timings: dict[str, float] = field(default_factory=dict)
    events: list[str] = field(default_factory=list)
    fixme_paths: list[str] = field(default_factory=list)

    def to_markdown(self) -> str:
        source_rows = "\n".join(
            (
                f"| {item.source} | {item.fetched} | {item.accepted} | "
                f"{item.deduplicated} | {item.rejected} | "
                f"{item.capped} | {item.complete} |"
            )
            for item in self.sources
        )
        timing_rows = "\n".join(
            f"| {name} | {seconds:.3f} |"
            for name, seconds in sorted(self.timings.items())
        )
        events = [*(f"- {event}" for event in self.events)]
        events.extend(f"- fixme: {path}" for path in self.fixme_paths)
        if not events:
            events.append("- none")

        return (
            "\n".join(
                [
                    "# Papers pipeline summary",
                    "",
                    "## Sources",
                    "",
                    (
                        "| Source | Fetched | Accepted | Deduplicated | Rejected "
                        "| Capped | Complete |"
                    ),
                    "|---|---:|---:|---:|---:|---|---|",
                    source_rows,
                    "",
                    "## Inventory and conversion",
                    "",
                    f"- inventory: {self.inventory}",
                    f"- generated: {self.generated}",
                    f"- pending: {self.pending}",
                    f"- attempted: {self.attempted}",
                    f"- succeeded: {self.succeeded}",
                    f"- failed: {self.failed}",
                    f"- deferred: {self.deferred}",
                    f"- promoted_to_fixme: {self.promoted_to_fixme}",
                    "",
                    "## Timings",
                    "",
                    "| Stage | Seconds |",
                    "|---|---:|",
                    timing_rows,
                    "",
                    "## Continuation and failures",
                    "",
                    *events,
                ]
            )
            + "\n"
        )


def write_actions_summary(path: Path | None, summary: RunSummary) -> None:
    if path is None:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(summary.to_markdown())
