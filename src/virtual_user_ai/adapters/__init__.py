"""Meeting adapters (platform specific)."""

from .base import MeetingAdapter
from .mock_meeting import MockMeetingAdapter
from .webex_meeting import WebexMeetingAdapter

__all__ = ["MeetingAdapter", "MockMeetingAdapter", "WebexMeetingAdapter"]
