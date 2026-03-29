"""Core dialogue processing that always uses shared policy checks first."""

from __future__ import annotations

from core.models import DialogueTurn
from core.policy import PolicyEngine


class DialogueManager:
    """Handles dialogue after centralized policy approval."""

    def __init__(self, policy_engine: PolicyEngine | None = None) -> None:
        self._policy = policy_engine or PolicyEngine()

    def process(self, turn: DialogueTurn) -> str:
        """Process a dialogue turn with policy gatekeeping."""
        decision = self._policy.evaluate(turn)
        if not decision.allowed:
            return f"blocked:{decision.reason}"
        return turn.text.strip()
