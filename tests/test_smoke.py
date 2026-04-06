from __future__ import annotations

import unittest

from virtual_user_ai.adapters.webex_meeting import WebexMeetingAdapter
from virtual_user_ai.core.policy_engine import PolicyEngine
from virtual_user_ai.core.session_orchestrator import SessionOrchestrator
from virtual_user_ai.core.trigger_router import TriggerRouter


class SmokeTests(unittest.TestCase):
    def test_trigger_to_audio_path(self) -> None:
        router = TriggerRouter()
        adapter = WebexMeetingAdapter(dry_run=True)
        self.assertTrue(adapter.join_meeting("https://example.webex.com/meeting"))
        orchestrator = SessionOrchestrator(policy_engine=PolicyEngine(), adapter=adapter)

        event = router.route("push_to_talk", "status update please", "host")
        result = orchestrator.handle_event(event)

        self.assertEqual(result, "audio")
        self.assertIn("response:audio", orchestrator.diagnostics)

    def test_chat_fallback_when_audio_fails(self) -> None:
        router = TriggerRouter()
        adapter = WebexMeetingAdapter(dry_run=True)
        orchestrator = SessionOrchestrator(policy_engine=PolicyEngine(), adapter=adapter)

        event = router.route("chat", "fallback test", "host")
        result = orchestrator.handle_event(event)

        self.assertEqual(result, "chat_fallback")
        self.assertIn("response:chat_fallback", orchestrator.diagnostics)


if __name__ == "__main__":
    unittest.main()
