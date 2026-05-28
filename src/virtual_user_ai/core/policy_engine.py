from __future__ import annotations

from virtual_user_ai.core.types import PolicyContext, PolicyDecision, TriggerEvent, TriggerType


class PolicyEngine:
    """Single approval gate for trigger events and v1 governance constraints."""

    def evaluate(
        self,
        event: TriggerEvent,
        context: PolicyContext | None = None,
    ) -> PolicyDecision:
        active_context = context or PolicyContext()

        if not active_context.human_control_active:
            return PolicyDecision(approved=False, reason="human control is not active")

        if event.trigger_type in {TriggerType.HUMAN_STOP, TriggerType.HUMAN_MUTE}:
            return PolicyDecision(approved=False, reason="human control command blocks response")

        if not active_context.consent_granted:
            return PolicyDecision(approved=False, reason="consent not granted")

        if not active_context.ai_disclosed:
            return PolicyDecision(approved=False, reason="ai participation not disclosed")

        if event.trigger_type == TriggerType.WAKE_WORD:
            return PolicyDecision(approved=False, reason="wake-word disabled by default in v1")

        if not event.text.strip():
            return PolicyDecision(approved=False, reason="empty event text")

        return PolicyDecision(approved=True, reason="approved")
