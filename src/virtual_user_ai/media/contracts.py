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
