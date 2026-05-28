from __future__ import annotations

import unittest

from virtual_user_ai.adapters.webex_meeting import WebexMeetingAdapter
from virtual_user_ai.core.policy_engine import PolicyEngine
from virtual_user_ai.core.session_orchestrator import SessionOrchestrator
from virtual_user_ai.core.trigger_router import TriggerRouter
from virtual_user_ai.media.host_diagnostics import HostMediaDiagnosticsProvider
from virtual_user_ai.media.worker import MediaWorker


class OrchestratorHostDiagnosticsEndToEndTests(unittest.TestCase):
    def test_host_diagnostics_reason_reaches_orchestrator_chat_fallback(self) -> None:
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
        media_worker = MediaWorker(injector_mode="fail", host_diagnostics=diagnostics)
        adapter = WebexMeetingAdapter(media_worker=media_worker)
        self.assertTrue(adapter.join_meeting("https://example.webex.com/meeting"))
        orchestrator = SessionOrchestrator(policy_engine=PolicyEngine(), adapter=adapter)
        event = TriggerRouter().route("push_to_talk", "brief the room", "host")

        result = orchestrator.handle_event(event)

        expected_reason = "audio injection failed; host mode: chat_only"
        self.assertEqual(result, "chat_fallback")
        self.assertIn(f"audio:failed:{expected_reason}", adapter.session_log)
        self.assertIn(f"response:chat_fallback:{expected_reason}", orchestrator.diagnostics)
        self.assertEqual(adapter.last_media_result.reason, expected_reason)


if __name__ == "__main__":
    unittest.main()
