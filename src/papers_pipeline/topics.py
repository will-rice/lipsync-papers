from collections.abc import Callable
from dataclasses import dataclass
from importlib import import_module
from typing import cast

from pydantic import ValidationError

from papers_pipeline.config import TopicConfig
from papers_pipeline.errors import ConfigError
from papers_pipeline.models import Paper


@dataclass(frozen=True)
class TopicDecision:
    accepted: bool
    reason: str


def build_topic_gate(config: TopicConfig) -> Callable[[Paper], TopicDecision]:
    plugin = config.plugin
    if plugin is not None:
        plugin = _validated_plugin_reference(plugin)
        function = _load_plugin(plugin)

        def plugin_gate(paper: Paper) -> TopicDecision:
            decision = function(paper)
            if not isinstance(decision, TopicDecision):
                raise ConfigError("topic plugin must return TopicDecision")
            return decision

        return plugin_gate

    def gate(paper: Paper) -> TopicDecision:
        text = _search_text(paper)
        for term in config.exclude_any:
            if term.casefold() in text:
                return TopicDecision(False, f"matched excluded term: {term}")
        missing_required_terms = [
            term for term in config.include_all if term.casefold() not in text
        ]
        if missing_required_terms:
            return TopicDecision(
                False,
                f"missing required terms: {', '.join(missing_required_terms)}",
            )
        if config.include_any and not any(
            term.casefold() in text for term in config.include_any
        ):
            return TopicDecision(
                False,
                f"missing included term: {', '.join(config.include_any)}",
            )
        if config.categories and not set(config.categories).intersection(
            paper.categories
        ):
            return TopicDecision(
                False,
                f"missing included category: {', '.join(config.categories)}",
            )
        return TopicDecision(True, "accepted")

    return gate


def _validated_plugin_reference(plugin: str) -> str:
    try:
        TopicConfig(
            include_any=[],
            include_all=[],
            exclude_any=[],
            categories=[],
            plugin=plugin,
        )
    except ValidationError as error:
        raise ConfigError("topic.plugin must use module:function format") from error
    return plugin


def _load_plugin(plugin: str) -> Callable[[Paper], object]:
    module_name, function_name = plugin.split(":", 1)
    try:
        function = getattr(import_module(module_name), function_name)
    except (ImportError, AttributeError) as error:
        raise ConfigError(f"invalid topic plugin: {plugin}") from error
    if not callable(function):
        raise ConfigError(f"invalid topic plugin: {plugin}")
    return cast(Callable[[Paper], object], function)


def _search_text(paper: Paper) -> str:
    return f"{paper.title} {paper.abstract}".casefold()
