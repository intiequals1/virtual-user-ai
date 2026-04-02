"""Centralized policy checks for core orchestration."""

from __future__ import annotations

from core.models import DialogueTurn, PolicyDecision


class PolicyEngine:
    """Single entrypoint for policy checks used by orchestration and routing."""

    def evaluate(self, turn: DialogueTurn) -> PolicyDecision:
        """Evaluate a dialogue turn and return a policy decision."""
        if not turn.text.strip():
            return PolicyDecision(allowed=False, reason="empty_input")
        return PolicyDecision(allowed=True)
