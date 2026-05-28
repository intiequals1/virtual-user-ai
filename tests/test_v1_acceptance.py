from __future__ import annotations

import unittest

from virtual_user_ai.adapters.webex_meeting import WebexMeetingAdapter
from virtual_user_ai.core.policy_engine import PolicyEngine
from virtual_user_ai.core.session_orchestrator import SessionOrchestrator
from virtual_user_ai.core.trigger_router import TriggerRouter
from virtual_user_ai.core.types import TriggerType


class V1AcceptanceTests(unittest.TestCase):
    def test_push_to_talk_is_routed_and_can_produce_audio_response(self) -> None:
        router = TriggerRouter()
        adapter = WebexMeetingAdapter(dry_run=True)
        self.assertTrue(adapter.join_meeting("https://example.webex.com/meeting"))
        orchestrator = SessionOrchestrator(policy_engine=PolicyEngine(), adapter=adapter)

        event = router.route("push_to_talk", "status update please", "host")
        result = orchestrator.handle_event(event)

        self.assertEqual(event.trigger_type, TriggerType.PUSH_TO_TALK)
        self.assertEqual(result, "audio")
        self.assertIn("response:audio", orchestrator.diagnostics)

    def test_chat_trigger_uses_chat_fallback_when_audio_is_not_available(self) -> None:
        router = TriggerRouter()
        adapter = WebexMeetingAdapter(dry_run=True)
        orchestrator = SessionOrchestrator(policy_engine=PolicyEngine(), adapter=adapter)

        event = router.route("chat", "fallback test", "host")
        result = orchestrator.handle_event(event)

        self.assertEqual(event.trigger_type, TriggerType.CHAT)
        self.assertEqual(result, "chat_fallback")
        self.assertIn("response:chat_fallback:audio delivery failed", orchestrator.diagnostics)

    def test_wake_word_is_disabled_by_default_in_v1(self) -> None:
        router = TriggerRouter()
        adapter = WebexMeetingAdapter(dry_run=True)
        self.assertTrue(adapter.join_meeting("https://example.webex.com/meeting"))
        orchestrator = SessionOrchestrator(policy_engine=PolicyEngine(), adapter=adapter)

        event = router.route("wake_word", "Virtual User AI", "host")
        result = orchestrator.handle_event(event)

        self.assertEqual(event.trigger_type, TriggerType.WAKE_WORD)
        self.assertEqual(result, "not_allowed")
        self.assertIn("not_allowed:wake-word disabled by default in v1", orchestrator.diagnostics)


if __name__ == "__main__":
    unittest.main()
