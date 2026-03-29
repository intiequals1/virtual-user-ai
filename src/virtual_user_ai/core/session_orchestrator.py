"""Shared v1 session orchestration path."""

from __future__ import annotations

from dataclasses import dataclass, field

from .policy_engine import PolicyEngine
from .trigger_router import TriggerEvent


@dataclass
class SessionOrchestrator:
    """Routes approved events to audio-first output with chat fallback."""

    adapter: object
    policy: PolicyEngine = field(default_factory=PolicyEngine)

    def handle_event(self, event: TriggerEvent) -> dict[str, str]:
        approved, reason = self.policy.approve(event)
        if not approved:
            return {"status": "rejected", "reason": reason}

        response_text = f"Acknowledged: {event.text}"
        audio_sent = bool(self.adapter.send_audio(response_text))
        if audio_sent:
            return {"status": "responded", "mode": "audio"}

        self.adapter.send_chat_message(response_text)
        return {"status": "responded", "mode": "chat_fallback"}
