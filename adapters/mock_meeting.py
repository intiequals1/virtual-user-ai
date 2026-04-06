"""Mock meeting adapter used for tests and local dry runs."""

from __future__ import annotations

from adapters.base import JoinOptions, MeetingAdapter


class MockMeetingAdapter(MeetingAdapter):
    provider = "mock"

    def join(self, options: JoinOptions) -> dict[str, str]:
        status = "simulated" if options.dry_run else "connected"
        return {
            "provider": self.provider,
            "status": status,
            "meeting_url": options.meeting_url,
            "display_name": options.display_name,
        }
