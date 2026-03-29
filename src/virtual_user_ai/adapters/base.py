<<<<<<< HEAD
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
=======
"""Adapter contract separating shared core from platform implementations."""

from __future__ import annotations

from abc import ABC, abstractmethod


class MeetingAdapter(ABC):
    """Abstract meeting adapter contract for v1 orchestration."""

    @abstractmethod
    def send_audio(self, text: str) -> bool:
        """Return True when audio delivery succeeds; False triggers chat fallback."""

    @abstractmethod
    def send_chat_message(self, text: str) -> None:
        """Send a chat message into the active meeting context."""
>>>>>>> 2314bc3 (Add v1 POC scaffold batch with core, adapters, and smoke tests)
