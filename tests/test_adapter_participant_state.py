from __future__ import annotations

import unittest

from virtual_user_ai.adapters.webex_meeting import WebexMeetingAdapter
from virtual_user_ai.media.host_diagnostics import HostMediaDiagnosticsProvider
from virtual_user_ai.media.worker import MediaWorker


class AdapterParticipantStateTests(unittest.TestCase):
    def test_participant_state_exposes_serializable_last_media_result(self) -> None:
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
        adapter = WebexMeetingAdapter(media_worker=MediaWorker(injector_mode="fail", host_diagnostics=diagnostics))
        self.assertTrue(adapter.join_meeting("https://example.webex.com/meeting"))

        self.assertFalse(adapter.send_audio("hello diagnostics"))
        state = adapter.participant_state()

        self.assertEqual(
            state["last_media_result"],
            {
                "success": False,
                "output": "chat",
                "reason": "audio injection failed; host mode: chat_only",
                "wav_path": "/tmp/virtual-user-ai-hello_diagnostics.wav",
            },
        )
        self.assertIn("audio:failed:audio injection failed; host mode: chat_only", state["events"])


if __name__ == "__main__":
    unittest.main()
