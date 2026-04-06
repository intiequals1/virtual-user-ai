"""Contracts for media input/output components.

This module intentionally separates:
- TTS provider concerns
- Device detection concerns
- Audio injection concerns
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Protocol


@dataclass(frozen=True)
class TTSRequest:
    """Normalized request for generating speech."""

    text: str
    voice: str | None = None
    sample_rate_hz: int = 24_000
    format: str = "pcm_s16le"


@dataclass(frozen=True)
class SynthesizedAudio:
    """TTS output payload."""

    audio_bytes: bytes
    sample_rate_hz: int
    channels: int
    encoding: str


class TTSProvider(Protocol):
    """Service contract for text-to-speech providers."""

    async def synthesize(self, request: TTSRequest) -> SynthesizedAudio:
        """Generate audio for the provided request."""


@dataclass(frozen=True)
class AudioDevice:
    """Represents a discovered system audio device."""

    id: str
    name: str
    is_input: bool
    is_output: bool
    is_default: bool = False
    metadata: Mapping[str, Any] | None = None


class DeviceDetector(Protocol):
    """Discovery-only contract for locating audio devices."""

    def list_devices(self) -> list[AudioDevice]:
        """Return all known audio devices."""


class AudioInjector(Protocol):
    """Injection-only contract for writing audio into a target device/path."""

    def inject(self, audio: SynthesizedAudio, *, target_device_id: str | None = None) -> None:
        """Inject synthesized audio to a selected path.

        Note: successful host-level routing can be environment dependent.
        """
