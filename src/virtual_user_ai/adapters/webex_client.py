from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol


class WebexApiClient(Protocol):
    """Boundary for future Webex API behavior.

    Implementations behind this protocol must remain adapter-layer concerns.
    The shared core must not import Webex-specific clients.
    """

    def prepare_join(self, meeting_link: str) -> dict[str, object]:
        """Prepare a join operation without requiring network behavior."""

    def post_chat_message(self, meeting_id: str, text: str) -> dict[str, object]:
        """Post or simulate a chat message."""


@dataclass
class DryRunWebexApiClient:
    """In-memory client for tests and local development.

    This client performs no network calls and stores only diagnostic operations.
    """

    operations: list[str] = field(default_factory=list)

    def prepare_join(self, meeting_link: str) -> dict[str, object]:
        if not meeting_link.startswith("https://"):
            self.operations.append("prepare_join:invalid_link")
            return {
                "ok": False,
                "reason": "invalid meeting link",
                "meeting_id": None,
            }

        meeting_id = f"dry-run:{meeting_link}"
        self.operations.append("prepare_join:dry_run")
        return {
            "ok": True,
            "reason": "dry-run prepared",
            "meeting_id": meeting_id,
        }

    def post_chat_message(self, meeting_id: str, text: str) -> dict[str, object]:
        if not meeting_id:
            self.operations.append("post_chat_message:missing_meeting_id")
            return {
                "ok": False,
                "reason": "missing meeting id",
            }

        self.operations.append(f"post_chat_message:{text[:60]}")
        return {
            "ok": True,
            "reason": "dry-run chat recorded",
        }
