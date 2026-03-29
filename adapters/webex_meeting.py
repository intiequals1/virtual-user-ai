"""Webex meeting adapter.

The implementation remains intentionally placeholder-friendly while the full
Webex automation surface is still under development.
"""

from __future__ import annotations

from adapters.base import JoinOptions, MeetingAdapter


class WebexMeetingAdapter(MeetingAdapter):
    provider = "webex"

    def join(self, options: JoinOptions) -> dict[str, str]:
        if options.dry_run:
            return {
                "provider": self.provider,
                "status": "dry-run",
                "detail": "Webex adapter placeholder path executed.",
                "meeting_url": options.meeting_url,
            }

        # Placeholder: concrete browser/device automation is wired later.
        return {
            "provider": self.provider,
            "status": "not-implemented",
            "detail": "Live Webex join flow is not implemented yet.",
            "meeting_url": options.meeting_url,
        }
