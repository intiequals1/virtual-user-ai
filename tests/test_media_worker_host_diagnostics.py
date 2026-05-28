from __future__ import annotations

import unittest

from virtual_user_ai.media.contracts import MediaRequest
from virtual_user_ai.media.host_diagnostics import HostMediaDiagnosticsProvider
from virtual_user_ai.media.worker import MediaWorker


class MediaWorkerHostDiagnosticsTests(unittest.TestCase):
    def test_worker_appends_host_mode_to_audio_failure_reason_when_diagnostics_are_available(self) -> None:
        diagnostics = HostMediaDiagnosticsProvider().inspect(
            platform="test-platform",
            tool_paths={
                "ffmpeg": None,
                "pactl": None,
                "pw-cli": None,
                "arecord": None,
                "aplay": None,
            },
        )
        worker = MediaWorker(injector_mode="fail", host_diagnostics=diagnostics)

        result = worker.process(MediaRequest(text="hello diagnostics"))

        self.assertFalse(result.success)
        self.assertEqual(result.output, "chat")
        self.assertEqual(result.reason, "audio injection failed; host mode: chat_only")

    def test_worker_preserves_existing_failure_reason_without_diagnostics(self) -> None:
        worker = MediaWorker(injector_mode="fail")

        result = worker.process(MediaRequest(text="hello no diagnostics"))

        self.assertFalse(result.success)
        self.assertEqual(result.reason, "audio injection failed")


if __name__ == "__main__":
    unittest.main()
