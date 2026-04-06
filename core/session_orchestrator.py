"""Session orchestration boundary for v1 POC.

This is baseline integration-seam code and not production-ready.
"""

from dataclasses import dataclass


@dataclass
class OrchestrationResult:
    status: str
    mode: str
    detail: str


class SessionOrchestrator:
    """Coordinates response mode selection for the shared core."""

    def process(self, policy_result: dict) -> OrchestrationResult:
        if not policy_result.get("allowed", False):
            return OrchestrationResult(
                status="rejected",
                mode="none",
                detail=policy_result.get("reason", "policy_denied"),
            )

        return OrchestrationResult(
            status="accepted",
            mode="audio_first_with_chat_fallback",
            detail="baseline_orchestration_path",
        )
