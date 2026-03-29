"""Virtual microphone injection abstractions and factory."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from .contracts import AudioInjector, SynthesizedAudio


@dataclass(frozen=True)
class InjectorConfig:
    """Configuration for selecting an injection backend."""

    injector: str = "noop"
    target_device_id: str | None = None
    options: Mapping[str, Any] | None = None


class NoopAudioInjector:
    """No-op injector used in non-routable or test environments."""

    def __init__(self, *, target_device_id: str | None = None) -> None:
        self._target_device_id = target_device_id

    def inject(self, audio: SynthesizedAudio, *, target_device_id: str | None = None) -> None:
        _ = (audio, target_device_id or self._target_device_id)
        # Intentionally no host audio routing.


class LoggingAudioInjector:
    """Injector that logs intent; useful when host routing is environment dependent."""

    def __init__(self, *, target_device_id: str | None = None) -> None:
        self._target_device_id = target_device_id

    def inject(self, audio: SynthesizedAudio, *, target_device_id: str | None = None) -> None:
        effective_target = target_device_id or self._target_device_id or "<unspecified>"
        print(
            "[virtual_mic] inject requested "
            f"bytes={len(audio.audio_bytes)} sample_rate={audio.sample_rate_hz} "
            f"channels={audio.channels} encoding={audio.encoding} target={effective_target}"
        )


def create_injector(config: InjectorConfig | Mapping[str, Any] | None = None) -> AudioInjector:
    """Create an audio injector from config.

    Kept configurable by accepting either a typed config object or raw mapping.
    """

    if config is None:
        resolved = InjectorConfig()
    elif isinstance(config, InjectorConfig):
        resolved = config
    else:
        resolved = InjectorConfig(
            injector=str(config.get("injector", "noop")),
            target_device_id=config.get("target_device_id"),
            options=config.get("options"),
        )

    injector = resolved.injector.strip().lower()
    if injector == "noop":
        return NoopAudioInjector(target_device_id=resolved.target_device_id)
    if injector == "logging":
        return LoggingAudioInjector(target_device_id=resolved.target_device_id)

    raise ValueError(f"Unsupported injector: {resolved.injector}")
