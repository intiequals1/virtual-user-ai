"""Webex adapter placeholder.

The adapter boundary is present to preserve shared-core vs adapter separation. Real
Webex behavior remains intentionally unimplemented in this baseline batch.
"""


class WebexMeetingAdapter:
    """Webex adapter placeholder for dry-run style progression."""

    def join(self, meeting_link: str) -> dict:
        return {
            "status": "placeholder",
            "component": "WebexMeetingAdapter",
            "action": "join",
            "meeting_link": meeting_link,
        }
