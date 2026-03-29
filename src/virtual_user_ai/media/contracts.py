<<<<<<< HEAD
from __future__ import annotations

from typing import Protocol


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
    if mode != "dry_run":
        raise ValueError(f"Unsupported injector mode in v1 import batch: {mode}")
    return DryRunInjector()


class LocalTTSProvider:
    """Placeholder local TTS implementation for import consistency."""

    def synthesize_to_file(self, text: str) -> str:
        safe = text.replace(" ", "_")[:40] or "empty"
        return f"/tmp/virtual-user-ai-{safe}.wav"


class DryRunInjector:
    """No-op injector used by default for local dry-runs."""

    def inject_file(self, wav_path: str) -> bool:
        return wav_path.endswith(".wav")
=======
"""Stable media worker contract boundary for v1."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MediaDeliveryResult:
    success: bool
    output_path: str | None = None
    error: str | None = None


class MediaWorker:
    """Placeholder media worker contract."""

    def synthesize_and_inject(self, text: str) -> MediaDeliveryResult:
        # Placeholder: provide concrete TTS and injector wiring in later batch.
        return MediaDeliveryResult(success=False, error="media_worker_not_configured")
>>>>>>> 2314bc3 (Add v1 POC scaffold batch with core, adapters, and smoke tests)
