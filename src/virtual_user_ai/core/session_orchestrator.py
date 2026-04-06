<<<<<<< HEAD
=======
"""Shared v1 session orchestration path."""

>>>>>>> 2314bc3 (Add v1 POC scaffold batch with core, adapters, and smoke tests)
from __future__ import annotations

from dataclasses import dataclass, field

<<<<<<< HEAD
from virtual_user_ai.core.policy_engine import PolicyEngine
from virtual_user_ai.core.types import TriggerEvent
=======
from .policy_engine import PolicyEngine
from .trigger_router import TriggerEvent
>>>>>>> 2314bc3 (Add v1 POC scaffold batch with core, adapters, and smoke tests)


@dataclass
class SessionOrchestrator:
<<<<<<< HEAD
    policy_engine: PolicyEngine
    adapter: object
    meeting_memory: list[str] = field(default_factory=list)
    diagnostics: list[str] = field(default_factory=list)

    def handle_event(self, event: TriggerEvent) -> str:
        decision = self.policy_engine.evaluate(event)
        if not decision.approved:
            self.diagnostics.append(f"rejected:{decision.reason}")
            return "rejected"

        response = f"AI response to {event.user_id}: {event.text}"
        self.meeting_memory.append(response)

        sent_audio = self.adapter.send_audio(response)
        if sent_audio:
            self.diagnostics.append("response:audio")
            return "audio"

        self.adapter.send_chat_message(f"(audio failed) {response}")
        self.diagnostics.append("response:chat_fallback")
        return "chat_fallback"
=======
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
>>>>>>> 2314bc3 (Add v1 POC scaffold batch with core, adapters, and smoke tests)
