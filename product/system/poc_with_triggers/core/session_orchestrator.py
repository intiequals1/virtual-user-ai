"""Session orchestrator placeholder for v1 baseline consolidation."""


class SessionOrchestrator:
    """Owner of response pipeline execution (placeholder baseline)."""

    def run(self, policy_result: dict) -> dict:
        """Return placeholder pipeline output.

        Real media/chat fallback behavior is intentionally deferred to future batches.
        """
        return {
            "status": "placeholder",
            "component": "SessionOrchestrator",
            "policy_result": policy_result,
            "output_mode": "not_implemented",
        }
