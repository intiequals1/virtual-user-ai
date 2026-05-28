from __future__ import annotations

import unittest

from virtual_user_ai.adapters.status_renderer import render_participant_state
from virtual_user_ai.adapters.webex_meeting import WebexMeetingAdapter
from virtual_user_ai.media.host_diagnostics import HostMediaDiagnosticsProvider
from virtual_user_ai.media.worker import MediaWorker


class AdapterStatusRendererTests(unittest.TestCase):
    def test_render_participant_state_includes_media_result_and_events(self) -> None:
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

        output = render_participant_state(adapter.participant_state())

        self.assertIn("Joined: True", output)
        self.assertIn("Dry run: True", output)
        self.assertIn("Last media result:", output)
        self.assertIn("- success: False", output)
        self.assertIn("- output: chat", output)
        self.assertIn("- reason: audio injection failed; host mode: chat_only", output)
        self.assertIn("Events:", output)
        self.assertIn("- join:dry_run", output)
        self.assertIn("- audio:failed:audio injection failed; host mode: chat_only", output)

    def test_render_participant_state_handles_empty_media_result_and_events(self) -> None:
        output = render_participant_state(
            {
                "joined": False,
                "meeting_id": None,
                "dry_run": True,
                "real_mode_requested": False,
                "real_mode_available": False,
                "last_media_result": None,
                "events": [],
            }
        )

        self.assertIn("Last media result:\n- none", output)
        self.assertIn("Events:\n- none", output)


if __name__ == "__main__":
    unittest.main()
