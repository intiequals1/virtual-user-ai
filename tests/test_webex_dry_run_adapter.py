from __future__ import annotations

import unittest

from virtual_user_ai.adapters.webex_meeting import WebexMeetingAdapter


class WebexDryRunAdapterTests(unittest.TestCase):
    def test_join_meeting_rejects_non_https_link(self) -> None:
        adapter = WebexMeetingAdapter(dry_run=True)

        joined = adapter.join_meeting("ftp://example.webex.com/meeting")

        self.assertFalse(joined)
        self.assertFalse(adapter.joined)
        self.assertIn("join:invalid_link", adapter.session_log)

    def test_join_meeting_records_dry_run_state(self) -> None:
        adapter = WebexMeetingAdapter(dry_run=True)

        joined = adapter.join_meeting("https://example.webex.com/meeting")
        state = adapter.participant_state()

        self.assertTrue(joined)
        self.assertTrue(state["joined"])
        self.assertTrue(state["dry_run"])
        self.assertIn("join:dry_run", state["events"])

    def test_chat_message_requires_joined_session(self) -> None:
        adapter = WebexMeetingAdapter(dry_run=True)

        sent = adapter.send_chat_message("hello")

        self.assertFalse(sent)
        self.assertIn("chat:not_joined", adapter.session_log)

    def test_chat_message_records_content_when_joined(self) -> None:
        adapter = WebexMeetingAdapter(dry_run=True)
        self.assertTrue(adapter.join_meeting("https://example.webex.com/meeting"))

        sent = adapter.send_chat_message("hello from dry run")

        self.assertTrue(sent)
        self.assertIn("chat:hello from dry run", adapter.session_log)


if __name__ == "__main__":
    unittest.main()
