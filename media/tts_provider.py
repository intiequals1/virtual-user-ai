"""Configurable TTS provider factory and provider implementations."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from .contracts import SynthesizedAudio, TTSProvider, TTSRequest


@dataclass(frozen=True)
class TTSProviderConfig:
    """Configuration for selecting a provider implementation."""

    provider: str = "mock"
    default_voice: str | None = None
    model: str | None = None
    options: Mapping[str, Any] | None = None


class MockTTSProvider:
    """Deterministic local mock provider for development/testing."""

    def __init__(self, *, default_voice: str | None = None) -> None:
        self._default_voice = default_voice or "alloy"

    async def synthesize(self, request: TTSRequest) -> SynthesizedAudio:
        voice = request.voice or self._default_voice
        # Placeholder payload - caller can still exercise pipeline end-to-end.
        payload = f"MOCK_TTS|voice={voice}|text={request.text}".encode("utf-8")
        return SynthesizedAudio(
            audio_bytes=payload,
            sample_rate_hz=request.sample_rate_hz,
            channels=1,
            encoding=request.format,
        )


class OpenAITTSProvider:
    """Example OpenAI-backed provider placeholder.

    This intentionally does not hard-wire SDK/network behavior in this environment.
    """

    def __init__(self, *, model: str | None = None, default_voice: str | None = None) -> None:
        self._model = model or "gpt-4o-mini-tts"
        self._default_voice = default_voice or "alloy"

    async def synthesize(self, request: TTSRequest) -> SynthesizedAudio:
        raise NotImplementedError(
            "OpenAI TTS integration is not enabled in this environment. "
            "Use provider='mock' or wire SDK calls for your deployment."
        )


def create_tts_provider(config: TTSProviderConfig | Mapping[str, Any] | None = None) -> TTSProvider:
    """Create a TTS provider from config.

    Kept configurable by accepting either a typed config object or raw mapping.
    """

    if config is None:
        resolved = TTSProviderConfig()
    elif isinstance(config, TTSProviderConfig):
        resolved = config
    else:
        resolved = TTSProviderConfig(
            provider=str(config.get("provider", "mock")),
            default_voice=config.get("default_voice"),
            model=config.get("model"),
            options=config.get("options"),
        )

    provider = resolved.provider.strip().lower()
    if provider == "mock":
        return MockTTSProvider(default_voice=resolved.default_voice)
    if provider in {"openai", "openai_tts"}:
        return OpenAITTSProvider(model=resolved.model, default_voice=resolved.default_voice)

    raise ValueError(f"Unsupported TTS provider: {resolved.provider}")
