"""Session response pipeline owner for the v1 POC baseline.

Concrete audio-first and chat-fallback behavior is intentionally deferred to
later controlled import batches. The placeholder keeps the core pipeline
importable and smoke-testable.
"""

from __future__ import annotations


class SessionOrchestrator:
    """Owner of response pipeline execution in the shared AI core."""

    def run(self, policy_result: dict) -> dict:
        """Return placeholder pipeline output for an evaluated event.

        The output remains explicit until concrete media and chat delivery
        behavior is imported.
        """
        return {
            "status": "placeholder",
            "component": "SessionOrchestrator",
            "policy_result": policy_result,
            "output_mode": "not_implemented",
        }
