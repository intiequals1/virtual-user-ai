"""Webex adapter placeholder for the first real adapter track."""

from __future__ import annotations

from dataclasses import dataclass

from .base import MeetingAdapter


@dataclass
class WebexMeetingAdapter(MeetingAdapter):
    """Dry-run Webex adapter with explicit placeholders for credentials/runtime deps."""

    dry_run: bool = True

    def send_audio(self, text: str) -> bool:
        if self.dry_run:
            return False
        # Placeholder: implement audio injection once Webex runtime and host audio are configured.
        raise NotImplementedError("Webex audio injection requires runtime dependencies and credentials")

    def send_chat_message(self, text: str) -> None:
        if self.dry_run:
            return
        # Placeholder: implement Webex chat API call once credentials are available.
        raise NotImplementedError("Webex chat integration requires credentials")
