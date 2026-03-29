"""Unified trigger routing for all core trigger types."""

from __future__ import annotations

from core.models import DialogueTurn, TriggerEvent, TriggerType


class TriggerRouter:
    """Converts trigger events into normalized dialogue turns."""

    def route(self, event: TriggerEvent) -> DialogueTurn:
        text = str(event.payload.get("text", ""))

        # Keep routing logic unified and minimal in the core package.
        if event.trigger_type in {
            TriggerType.CHAT,
            TriggerType.PUSH_TO_TALK,
            TriggerType.WAKE_WORD,
        }:
            return DialogueTurn(text=text, metadata={"trigger_type": event.trigger_type.value})

        raise ValueError(f"unsupported trigger type: {event.trigger_type}")
