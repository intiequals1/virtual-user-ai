from __future__ import annotations

from dataclasses import dataclass, field

from virtual_user_ai.media.worker import MediaWorker


@dataclass
class WebexMeetingAdapter:
    """First real adapter track with dry-run behavior for v1 import stage."""

    dry_run: bool = True
    media_worker: MediaWorker = field(default_factory=MediaWorker)
    joined: bool = False
    session_log: list[str] = field(default_factory=list)

    def join_meeting(self, meeting_link: str) -> bool:
        if not meeting_link.startswith("https://"):
            self.session_log.append("join:invalid_link")
            return False

        self.joined = True
        mode = "dry_run" if self.dry_run else "placeholder_real_mode"
        self.session_log.append(f"join:{mode}")
        return True

    def leave_meeting(self) -> None:
        self.joined = False
        self.session_log.append("leave")

    def send_audio(self, text: str) -> bool:
        if not self.joined:
            self.session_log.append("audio:not_joined")
            return False
        ok = self.media_worker.speak(text)
        self.session_log.append("audio:ok" if ok else "audio:failed")
        return ok

    def send_chat_message(self, text: str) -> bool:
        if not self.joined:
            self.session_log.append("chat:not_joined")
            return False
        self.session_log.append(f"chat:{text[:60]}")
        return True

    def mute(self) -> None:
        self.session_log.append("mute:placeholder")

    def unmute(self) -> None:
        self.session_log.append("unmute:placeholder")

    def reconnect(self) -> None:
        self.session_log.append("reconnect:placeholder")

    def participant_state(self) -> dict[str, object]:
        return {
            "joined": self.joined,
            "dry_run": self.dry_run,
            "events": list(self.session_log),
        }
