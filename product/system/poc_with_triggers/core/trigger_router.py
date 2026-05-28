"""Trigger routing entry point for the v1 POC baseline.

This module intentionally keeps v1 trigger routing explicit while concrete
routing logic is imported in later controlled batches.
"""

from __future__ import annotations


class TriggerRouter:
    """Single entry point for trigger events in the shared AI core."""

    SUPPORTED_TRIGGER_TYPES = {"push_to_talk", "chat", "wake_word"}

    def route(self, event: dict) -> dict:
        """Route an invocation event through the shared trigger pipeline.

        Placeholder behavior returns a structured routing result until concrete
        trigger logic is imported. This keeps the v1 baseline importable and
        testable without expanding architecture scope.
        """
        trigger_type = event.get("trigger_type", "unknown")
        is_supported = trigger_type in self.SUPPORTED_TRIGGER_TYPES

        return {
            "status": "placeholder",
            "component": "TriggerRouter",
            "trigger_type": trigger_type,
            "supported": is_supported,
            "received_event": event,
        }
