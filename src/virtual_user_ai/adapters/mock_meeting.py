"""Local mock adapter for smoke validation."""

from __future__ import annotations

from dataclasses import dataclass, field

from .base import MeetingAdapter


@dataclass
class MockMeetingAdapter(MeetingAdapter):
    force_audio_failure: bool = False
    sent_audio: list[str] = field(default_factory=list)
    sent_chat: list[str] = field(default_factory=list)

    def send_audio(self, text: str) -> bool:
        self.sent_audio.append(text)
        return not self.force_audio_failure

    def send_chat_message(self, text: str) -> None:
        self.sent_chat.append(text)
