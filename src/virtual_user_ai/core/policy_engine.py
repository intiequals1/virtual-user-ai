<<<<<<< HEAD
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
=======
"""Simple v1 policy gate for trigger events."""

from __future__ import annotations

from .trigger_router import TriggerEvent


class PolicyEngine:
    """Approves trigger events for the POC unless explicit stop phrases are used."""

    BLOCKLIST = {"stop", "mute", "do not respond"}

    def approve(self, event: TriggerEvent) -> tuple[bool, str]:
        normalized = event.text.strip().lower()
        if normalized in self.BLOCKLIST:
            return False, "blocked_by_policy"
        return True, "approved"
>>>>>>> 2314bc3 (Add v1 POC scaffold batch with core, adapters, and smoke tests)
