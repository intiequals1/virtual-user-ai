"""Push-to-talk trigger adapter for normalized core events."""

from __future__ import annotations

from core.models import TriggerEvent, TriggerType


class PushToTalkTrigger:
    """Builds push-to-talk trigger events for core routing."""

    trigger_type = TriggerType.PUSH_TO_TALK

    def to_event(self, text: str) -> TriggerEvent:
        return TriggerEvent(trigger_type=self.trigger_type, payload={"text": text})
