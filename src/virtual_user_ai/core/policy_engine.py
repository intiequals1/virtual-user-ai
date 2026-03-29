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
