from __future__ import annotations

from dataclasses import dataclass, field

from virtual_user_ai.core.policy_engine import PolicyEngine
from virtual_user_ai.core.types import PolicyContext, TriggerEvent


@dataclass
class SessionOrchestrator:
    """Routes approved events to audio-first output with chat fallback."""

    policy_engine: PolicyEngine
    adapter: object
    meeting_memory: list[str] = field(default_factory=list)
    diagnostics: list[str] = field(default_factory=list)

    def _last_audio_failure_reason(self) -> str:
        media_result = getattr(self.adapter, "last_media_result", None)
        reason = getattr(media_result, "reason", None)
        if isinstance(reason, str) and reason:
            return reason
        return "audio delivery failed"

    def handle_event(self, event: TriggerEvent, context: PolicyContext | None = None) -> str:
        decision = self.policy_engine.evaluate(event, context=context)
        if not decision.approved:
            self.diagnostics.append(f"not_allowed:{decision.reason}")
            return "not_allowed"

        response = f"AI response to {event.user_id}: {event.text}"
        self.meeting_memory.append(response)

        sent_audio = self.adapter.send_audio(response)
        if sent_audio:
            self.diagnostics.append("response:audio")
            return "audio"

        fallback_reason = self._last_audio_failure_reason()
        self.adapter.send_chat_message(f"(audio failed: {fallback_reason}) {response}")
        self.diagnostics.append(f"response:chat_fallback:{fallback_reason}")
        return "chat_fallback"
