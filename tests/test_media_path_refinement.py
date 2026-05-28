from __future__ import annotations

import unittest

from virtual_user_ai.media.contracts import MediaRequest, MediaResult
from virtual_user_ai.media.worker import MediaWorker


class MediaPathRefinementTests(unittest.TestCase):
    def test_media_worker_returns_structured_audio_success(self) -> None:
        worker = MediaWorker()

        result = worker.process(MediaRequest(text="hello meeting"))

        self.assertIsInstance(result, MediaResult)
        self.assertTrue(result.success)
        self.assertEqual(result.output, "audio")
        self.assertEqual(result.reason, "audio injected")
        self.assertEqual(result.wav_path, "/tmp/virtual-user-ai-hello_meeting.wav")

    def test_media_worker_returns_chat_fallback_on_injection_failure(self) -> None:
        worker = MediaWorker(injector_mode="fail")

        result = worker.process(MediaRequest(text="hello fallback"))

        self.assertFalse(result.success)
        self.assertEqual(result.output, "chat")
        self.assertEqual(result.reason, "audio injection failed")
        self.assertEqual(result.wav_path, "/tmp/virtual-user-ai-hello_fallback.wav")

    def test_media_worker_returns_chat_fallback_on_empty_text(self) -> None:
        worker = MediaWorker()

        result = worker.process(MediaRequest(text="   "))

        self.assertFalse(result.success)
        self.assertEqual(result.output, "chat")
        self.assertEqual(result.reason, "empty media text")
        self.assertIsNone(result.wav_path)

    def test_speak_bool_wrapper_remains_backward_compatible(self) -> None:
        worker = MediaWorker()

        self.assertTrue(worker.speak("hello"))


if __name__ == "__main__":
    unittest.main()
