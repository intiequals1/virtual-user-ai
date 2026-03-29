from __future__ import annotations

from dataclasses import dataclass, field

from virtual_user_ai.core.policy_engine import PolicyEngine
from virtual_user_ai.core.types import TriggerEvent


@dataclass
class SessionOrchestrator:
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
