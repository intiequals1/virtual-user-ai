<<<<<<< HEAD
"""Meeting platform adapters."""
=======
"""Meeting adapters (platform specific)."""

from .base import MeetingAdapter
from .mock_meeting import MockMeetingAdapter
from .webex_meeting import WebexMeetingAdapter

__all__ = ["MeetingAdapter", "MockMeetingAdapter", "WebexMeetingAdapter"]
>>>>>>> 2314bc3 (Add v1 POC scaffold batch with core, adapters, and smoke tests)
