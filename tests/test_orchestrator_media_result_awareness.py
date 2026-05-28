from __future__ import annotations

import unittest

from virtual_user_ai.adapters.webex_meeting import WebexMeetingAdapter
from virtual_user_ai.core.policy_engine import PolicyEngine
from virtual_user_ai.core.session_orchestrator import SessionOrchestrator
from virtual_user_ai.core.trigger_router import TriggerRouter
from virtual_user_ai.media.worker import MediaWorker


class OrchestratorMediaResultAwarenessTests(unittest.TestCase):
    def test_orchestrator_records_media_reason_for_chat_fallback(self) -> None:
        router = TriggerRouter()
        adapter = WebexMeetingAdapter(media_worker=MediaWorker(injector_mode="fail"))
        self.assertTrue(adapter.join_meeting("https://example.webex.com/meeting"))
        orchestrator = SessionOrchestrator(policy_engine=PolicyEngine(), adapter=adapter)

        event = router.route("push_to_talk", "brief the room", "host")
        result = orchestrator.handle_event(event)

        self.assertEqual(result, "chat_fallback")
        self.assertIn("audio:failed:audio injection failed", adapter.session_log)
        self.assertIn("response:chat_fallback:audio injection failed", orchestrator.diagnostics)

    def test_orchestrator_keeps_audio_success_behavior(self) -> None:
        router = TriggerRouter()
        adapter = WebexMeetingAdapter()
        self.assertTrue(adapter.join_meeting("https://example.webex.com/meeting"))
        orchestrator = SessionOrchestrator(policy_engine=PolicyEngine(), adapter=adapter)

        event = router.route("chat", "hello", "host")
        result = orchestrator.handle_event(event)

        self.assertEqual(result, "audio")
        self.assertIn("audio:ok", adapter.session_log)
        self.assertIn("response:audio", orchestrator.diagnostics)


if __name__ == "__main__":
    unittest.main()
