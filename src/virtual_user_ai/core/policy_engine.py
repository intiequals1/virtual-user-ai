from __future__ import annotations

from virtual_user_ai.core.types import PolicyDecision, TriggerEvent, TriggerType


class PolicyEngine:
    """Single approval gate for trigger events."""

    def evaluate(self, event: TriggerEvent) -> PolicyDecision:
        if event.trigger_type == TriggerType.WAKE_WORD:
            return PolicyDecision(approved=False, reason="wake-word disabled by default in v1")
        if not event.text.strip():
            return PolicyDecision(approved=False, reason="empty event text")
        return PolicyDecision(approved=True, reason="approved")
