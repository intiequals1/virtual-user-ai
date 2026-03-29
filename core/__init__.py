<<<<<<< HEAD
"""Shared core package exports."""

from core.dialogue import DialogueManager
from core.models import DialogueTurn, PolicyDecision, TriggerEvent, TriggerType
from core.orchestrator import CoreOrchestrator
from core.policy import PolicyEngine

__all__ = [
    "CoreOrchestrator",
    "DialogueManager",
    "DialogueTurn",
    "PolicyDecision",
    "PolicyEngine",
    "TriggerEvent",
    "TriggerType",
]
=======
"""Shared core package for Virtual User AI POC (v1 baseline)."""
>>>>>>> 665e639 (Baseline repo audit and first shared-core import batch)
