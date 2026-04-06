"""Wake-word trigger adapter for normalized core events."""

from __future__ import annotations

from core.models import TriggerEvent, TriggerType


class WakeWordTrigger:
    """Builds wake-word trigger events for core routing."""

    trigger_type = TriggerType.WAKE_WORD

    def to_event(self, text: str) -> TriggerEvent:
        return TriggerEvent(trigger_type=self.trigger_type, payload={"text": text})
