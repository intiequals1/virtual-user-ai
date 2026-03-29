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
