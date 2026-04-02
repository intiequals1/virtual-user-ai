"""Media worker orchestration for detection, synthesis, and injection."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from media.contracts import AudioInjector, DeviceDetector, TTSRequest
from media.device_detection import EmptyDeviceDetector
from media.tts_provider import create_tts_provider
from media.virtual_mic import create_injector


@dataclass
class MediaWorkerService:
    """Coordinates TTS generation and optional injection."""

    tts_provider: Any
    injector: AudioInjector
    detector: DeviceDetector

    async def speak(
        self,
        text: str,
        *,
        voice: str | None = None,
        target_device_id: str | None = None,
        inject: bool = True,
    ) -> None:
        request = TTSRequest(text=text, voice=voice)
        audio = await self.tts_provider.synthesize(request)

        if inject:
            self.injector.inject(audio, target_device_id=target_device_id)


def create_media_worker_service(config: Mapping[str, Any] | None = None) -> MediaWorkerService:
    """Build MediaWorkerService from nested config.

    Expected shape:
    {
      "tts": {...},
      "injector": {...},
      "device_detection": {"enabled": true}
    }
    """

    config = config or {}
    tts = create_tts_provider(config.get("tts"))
    injector = create_injector(config.get("injector"))

    # Keep detection separate from injection; no implicit coupling here.
    detector = EmptyDeviceDetector()

    return MediaWorkerService(tts_provider=tts, injector=injector, detector=detector)
