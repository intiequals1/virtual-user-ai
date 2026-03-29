"""Shared meeting adapter interfaces and common layers.

This module intentionally exposes the shared ``core`` and ``media`` layers first.
Platform- or provider-specific tracks (for example Webex) are imported only after
these common layers are initialized.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class AdapterLayer(str, Enum):
    """Order-sensitive layers used by the runtime bootstrap path."""

    CORE = "core"
    MEDIA = "media"
    WEBEX = "webex"
    HOST_SETUP_LINUX = "host_setup_linux"


SHARED_LAYER_ORDER: tuple[AdapterLayer, ...] = (
    AdapterLayer.CORE,
    AdapterLayer.MEDIA,
)

OPTIONAL_LAYER_ORDER: tuple[AdapterLayer, ...] = (
    AdapterLayer.WEBEX,
    AdapterLayer.HOST_SETUP_LINUX,
)


@dataclass(slots=True)
class JoinOptions:
    """Runtime options for joining a meeting."""

    meeting_url: str
    display_name: str = "Virtual User"
    dry_run: bool = True


class MeetingAdapter(ABC):
    """Abstract base for all provider adapters."""

    provider: str

    @abstractmethod
    def join(self, options: JoinOptions) -> dict[str, str]:
        """Join (or simulate joining) a meeting and return run metadata."""


def bootstrap_layers() -> list[AdapterLayer]:
    """Return the expected runtime layer import order."""

    return [*SHARED_LAYER_ORDER, *OPTIONAL_LAYER_ORDER]


# Import provider-specific tracks only after shared layers are defined.
from adapters.webex_meeting import WebexMeetingAdapter  # noqa: E402
