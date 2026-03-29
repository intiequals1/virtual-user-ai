"""Shared trigger routing entry point for v1 events."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


TriggerType = Literal["push_to_talk", "wake_word", "chat_trigger"]


@dataclass(frozen=True)
class TriggerEvent:
    """Normalized trigger payload for all supported trigger types."""

    trigger_type: TriggerType
    text: str
    source: str = "local"


class TriggerRouter:
    """Single routing entry point from trigger source into orchestrator."""

    def route(self, event: TriggerEvent, orchestrator: object) -> dict[str, str]:
        if not hasattr(orchestrator, "handle_event"):
            raise TypeError("orchestrator must expose handle_event(event)")
        return orchestrator.handle_event(event)
