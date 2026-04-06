<<<<<<< HEAD
"""Shared core orchestration components."""
=======
"""Shared core components for trigger, policy, and orchestration."""

from .policy_engine import PolicyEngine
from .session_orchestrator import SessionOrchestrator
from .trigger_router import TriggerEvent, TriggerRouter

__all__ = ["TriggerEvent", "TriggerRouter", "PolicyEngine", "SessionOrchestrator"]
>>>>>>> 2314bc3 (Add v1 POC scaffold batch with core, adapters, and smoke tests)
