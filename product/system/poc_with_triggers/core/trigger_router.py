<<<<<<< HEAD
"""Trigger router placeholder.

This module intentionally keeps v1 trigger routing explicit while concrete logic is
imported in later controlled batches.
"""


class TriggerRouter:
    """Single entry point for trigger events (placeholder baseline)."""

    def route(self, event: dict) -> dict:
        """Route an event through the shared trigger pipeline.

        Placeholder behavior returns a structured stub until real routing logic is
        imported.
        """
        return {
            "status": "placeholder",
            "component": "TriggerRouter",
            "received_event": event,
        }
=======
"""Trigger routing entry point for the POC.

TODO: Implement TriggerRouter behavior for push-to-talk, wake-word, and chat trigger events.
"""
>>>>>>> a37cbaa (Create POC skeleton under product/system/poc_with_triggers)
