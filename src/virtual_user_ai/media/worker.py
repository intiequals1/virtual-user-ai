from __future__ import annotations

from virtual_user_ai.media.contracts import create_injector, create_tts_provider


class MediaWorker:
    def __init__(self, tts_mode: str = "local", injector_mode: str = "dry_run") -> None:
        self.tts = create_tts_provider(tts_mode)
        self.injector = create_injector(injector_mode)

    def speak(self, text: str) -> bool:
        wav_path = self.tts.synthesize_to_file(text)
        return self.injector.inject_file(wav_path)
