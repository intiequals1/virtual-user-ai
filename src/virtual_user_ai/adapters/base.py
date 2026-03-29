from __future__ import annotations

from typing import Protocol


class MeetingAdapter(Protocol):
    def join_meeting(self, meeting_link: str) -> bool:
        ...

    def leave_meeting(self) -> None:
        ...

    def send_audio(self, text: str) -> bool:
        ...

    def send_chat_message(self, text: str) -> bool:
        ...
