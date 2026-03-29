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
