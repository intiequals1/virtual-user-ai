from __future__ import annotations

from virtual_user_ai.media.contracts import MediaRequest, MediaResult, create_injector, create_tts_provider


class MediaWorker:
    def __init__(self, tts_mode: str = "local", injector_mode: str = "dry_run") -> None:
        self.tts = create_tts_provider(tts_mode)
        self.injector = create_injector(injector_mode)

    def process(self, request: MediaRequest) -> MediaResult:
        if not request.text.strip():
            return MediaResult(
                success=False,
                output=request.fallback_output,
                reason="empty media text",
                wav_path=None,
            )

        wav_path = self.tts.synthesize_to_file(request.text)
        injected = self.injector.inject_file(wav_path)
        if injected:
            return MediaResult(
                success=True,
                output=request.preferred_output,
                reason="audio injected",
                wav_path=wav_path,
            )

        return MediaResult(
            success=False,
            output=request.fallback_output,
            reason="audio injection failed",
            wav_path=wav_path,
        )

    def speak(self, text: str) -> bool:
        """Backward-compatible bool wrapper for existing adapter tests."""
        return self.process(MediaRequest(text=text)).success
