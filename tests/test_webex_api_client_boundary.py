from __future__ import annotations

import unittest

from virtual_user_ai.adapters.webex_client import DryRunWebexApiClient
from virtual_user_ai.adapters.webex_meeting import WebexMeetingAdapter


class WebexApiClientBoundaryTests(unittest.TestCase):
    def test_dry_run_client_prepare_join_rejects_invalid_link(self) -> None:
        client = DryRunWebexApiClient()

        result = client.prepare_join("not-a-webex-link")

        self.assertFalse(result["ok"])
        self.assertEqual(result["reason"], "invalid meeting link")
        self.assertIsNone(result["meeting_id"])
        self.assertIn("prepare_join:invalid_link", client.operations)

    def test_dry_run_client_prepare_join_returns_meeting_id(self) -> None:
        client = DryRunWebexApiClient()

        result = client.prepare_join("https://example.webex.com/meeting")

        self.assertTrue(result["ok"])
        self.assertEqual(result["reason"], "dry-run prepared")
        self.assertEqual(result["meeting_id"], "dry-run:https://example.webex.com/meeting")
        self.assertIn("prepare_join:dry_run", client.operations)

    def test_adapter_uses_api_client_for_join_and_chat(self) -> None:
        client = DryRunWebexApiClient()
        adapter = WebexMeetingAdapter(api_client=client)

        joined = adapter.join_meeting("https://example.webex.com/meeting")
        sent = adapter.send_chat_message("hello through client boundary")
        state = adapter.participant_state()

        self.assertTrue(joined)
        self.assertTrue(sent)
        self.assertEqual(state["meeting_id"], "dry-run:https://example.webex.com/meeting")
        self.assertIn("prepare_join:dry_run", client.operations)
        self.assertIn("post_chat_message:hello through client boundary", client.operations)
        self.assertIn("chat:hello through client boundary", state["events"])


if __name__ == "__main__":
    unittest.main()
