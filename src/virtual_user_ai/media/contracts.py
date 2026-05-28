from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class MediaRequest:
    """Structured request for the media path.

    The request remains text-first. Real TTS and audio injection can be added
    behind the provider and injector contracts later.
    """

    text: str
    preferred_output: str = "audio"
    fallback_output: str = "chat"


@dataclass(frozen=True)
class MediaResult:
    """Structured result from the media path."""

    success: bool
    output: str
    reason: str
    wav_path: str | None = None


class TTSProvider(Protocol):
    def synthesize_to_file(self, text: str) -> str:
        ...


class AudioInjector(Protocol):
    def inject_file(self, wav_path: str) -> bool:
        ...


def create_tts_provider(mode: str = "local") -> TTSProvider:
    if mode != "local":
        raise ValueError(f"Unsupported tts mode in v1 import batch: {mode}")
    return LocalTTSProvider()


def create_injector(mode: str = "dry_run") -> AudioInjector:
    if mode == "dry_run":
        return DryRunInjector()
    if mode == "fail":
        return FailingInjector()
    raise ValueError(f"Unsupported injector mode in v1 import batch: {mode}")


class LocalTTSProvider:
    """Placeholder local TTS implementation for import consistency."""

    def synthesize_to_file(self, text: str) -> str:
        safe = text.replace(" ", "_")[:40] or "empty"
        return f"/tmp/virtual-user-ai-{safe}.wav"


class DryRunInjector:
    """No-op injector used by default for local dry-runs."""

    def inject_file(self, wav_path: str) -> bool:
        return wav_path.endswith(".wav")


class FailingInjector:
    """Deterministic failure injector for fallback tests."""

    def inject_file(self, wav_path: str) -> bool:
        return False
