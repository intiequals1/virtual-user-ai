from __future__ import annotations

from virtual_user_ai.core.types import TriggerEvent, TriggerType


class TriggerRouter:
    """Single entry point for trigger events."""

    def route(self, trigger_type: str, text: str, user_id: str) -> TriggerEvent:
        return TriggerEvent(trigger_type=TriggerType(trigger_type), text=text, user_id=user_id)
