from __future__ import annotations

from dataclasses import dataclass, field

from virtual_user_ai.adapters.webex_client import DryRunWebexApiClient, WebexApiClient
from virtual_user_ai.adapters.webex_config import WebexConfig
from virtual_user_ai.media.worker import MediaWorker


@dataclass
class WebexMeetingAdapter:
    """First real adapter track with dry-run behavior for v1 import stage."""

    dry_run: bool = True
    media_worker: MediaWorker = field(default_factory=MediaWorker)
    config: WebexConfig | None = None
    api_client: WebexApiClient | None = None
    joined: bool = False
    meeting_id: str | None = None
    session_log: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.config is not None:
            self.dry_run = self.config.dry_run
        if self.api_client is None:
            self.api_client = DryRunWebexApiClient()

    def join_meeting(self, meeting_link: str) -> bool:
        if self.config is not None and self.config.real_mode_requested and not self.config.can_use_real_mode():
            self.session_log.append(f"join:blocked:{self.config.validation_reason()}")
            return False

        assert self.api_client is not None
        prepared = self.api_client.prepare_join(meeting_link)
        if not prepared["ok"]:
            self.session_log.append(f"join:blocked:{prepared['reason']}")
            return False

        self.meeting_id = str(prepared["meeting_id"])
        self.joined = True
        mode = "dry_run" if self.dry_run else "placeholder_real_mode"
        self.session_log.append(f"join:{mode}")
        return True

    def leave_meeting(self) -> None:
        self.joined = False
        self.meeting_id = None
        self.session_log.append("leave")

    def send_audio(self, text: str) -> bool:
        if not self.joined:
            self.session_log.append("audio:not_joined")
            return False
        ok = self.media_worker.speak(text)
        self.session_log.append("audio:ok" if ok else "audio:failed")
        return ok

    def send_chat_message(self, text: str) -> bool:
        if not self.joined or not self.meeting_id:
            self.session_log.append("chat:not_joined")
            return False
        assert self.api_client is not None
        result = self.api_client.post_chat_message(self.meeting_id, text)
        self.session_log.append(f"chat:{text[:60]}" if result["ok"] else f"chat:failed:{result['reason']}")
        return bool(result["ok"])

    def mute(self) -> None:
        self.session_log.append("mute:placeholder")

    def unmute(self) -> None:
        self.session_log.append("unmute:placeholder")

    def reconnect(self) -> None:
        self.session_log.append("reconnect:placeholder")

    def participant_state(self) -> dict[str, object]:
        return {
            "joined": self.joined,
            "meeting_id": self.meeting_id,
            "dry_run": self.dry_run,
            "real_mode_requested": self.config.real_mode_requested if self.config else False,
            "real_mode_available": self.config.can_use_real_mode() if self.config else False,
            "events": list(self.session_log),
        }
