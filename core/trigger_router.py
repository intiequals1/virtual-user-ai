"""Trigger routing entry point for v1 POC.

This is intentionally lightweight baseline code and not production-ready.
"""

from dataclasses import dataclass
from typing import Literal

TriggerType = Literal["push_to_talk", "wake_word", "chat_trigger"]


@dataclass(frozen=True)
class TriggerEvent:
    trigger_type: TriggerType
    text: str


class TriggerRouter:
    """Single trigger entry point that normalizes invocation events."""

    def route(self, event: TriggerEvent) -> dict:
        return {
            "accepted": True,
            "trigger_type": event.trigger_type,
            "text": event.text,
        }
