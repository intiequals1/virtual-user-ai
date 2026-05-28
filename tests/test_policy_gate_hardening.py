from __future__ import annotations

import unittest

from virtual_user_ai.adapters.webex_meeting import WebexMeetingAdapter
from virtual_user_ai.core.policy_engine import PolicyEngine
from virtual_user_ai.core.session_orchestrator import SessionOrchestrator
from virtual_user_ai.core.trigger_router import TriggerRouter
from virtual_user_ai.core.types import PolicyContext


class PolicyGateHardeningTests(unittest.TestCase):
    def test_event_without_consent_is_not_allowed(self) -> None:
        router = TriggerRouter()
        adapter = WebexMeetingAdapter(dry_run=True)
        self.assertTrue(adapter.join_meeting("https://example.webex.com/meeting"))
        orchestrator = SessionOrchestrator(policy_engine=PolicyEngine(), adapter=adapter)

        event = router.route("push_to_talk", "status update please", "host")
        result = orchestrator.handle_event(event, context=PolicyContext(consent_granted=False))

        self.assertEqual(result, "not_allowed")
        self.assertIn("not_allowed:consent not granted", orchestrator.diagnostics)
        self.assertEqual(orchestrator.meeting_memory, [])

    def test_event_without_ai_disclosure_is_not_allowed(self) -> None:
        router = TriggerRouter()
        adapter = WebexMeetingAdapter(dry_run=True)
        self.assertTrue(adapter.join_meeting("https://example.webex.com/meeting"))
        orchestrator = SessionOrchestrator(policy_engine=PolicyEngine(), adapter=adapter)

        event = router.route("chat", "fallback test", "host")
        result = orchestrator.handle_event(event, context=PolicyContext(ai_disclosed=False))

        self.assertEqual(result, "not_allowed")
        self.assertIn("not_allowed:ai participation not disclosed", orchestrator.diagnostics)
        self.assertEqual(orchestrator.meeting_memory, [])

    def test_human_stop_command_blocks_response(self) -> None:
        router = TriggerRouter()
        adapter = WebexMeetingAdapter(dry_run=True)
        self.assertTrue(adapter.join_meeting("https://example.webex.com/meeting"))
        orchestrator = SessionOrchestrator(policy_engine=PolicyEngine(), adapter=adapter)

        event = router.route("human_stop", "stop", "host")
        result = orchestrator.handle_event(event)

        self.assertEqual(result, "not_allowed")
        self.assertIn("not_allowed:human control command blocks response", orchestrator.diagnostics)
        self.assertEqual(orchestrator.meeting_memory, [])


if __name__ == "__main__":
    unittest.main()
