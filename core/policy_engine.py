"""Policy gate for v1 POC.

This is baseline placeholder logic and not production-ready.
"""


class PolicyEngine:
    """Approves or denies normalized trigger events."""

    def evaluate(self, event_payload: dict) -> dict:
        text = (event_payload or {}).get("text", "")
        allowed = bool(text and text.strip())
        return {
            "allowed": allowed,
            "reason": "ok" if allowed else "empty_text",
            "event": event_payload,
        }
