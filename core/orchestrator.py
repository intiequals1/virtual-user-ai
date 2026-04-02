"""Core orchestration that imports shared core modules first."""

from __future__ import annotations

from core.dialogue import DialogueManager
from core.models import TriggerEvent
from core.policy import PolicyEngine
from core.triggers.router import TriggerRouter


class CoreOrchestrator:
    """Coordinates trigger routing, policy checks, and dialogue handling."""

    def __init__(
        self,
        router: TriggerRouter | None = None,
        policy_engine: PolicyEngine | None = None,
        dialogue_manager: DialogueManager | None = None,
    ) -> None:
        self._router = router or TriggerRouter()
        self._policy = policy_engine or PolicyEngine()
        self._dialogue = dialogue_manager or DialogueManager(policy_engine=self._policy)

    def handle_event(self, event: TriggerEvent) -> str:
        turn = self._router.route(event)
        return self._dialogue.process(turn)
