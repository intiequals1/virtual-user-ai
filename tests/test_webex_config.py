from __future__ import annotations

import unittest

from virtual_user_ai.adapters.webex_config import WebexConfig
from virtual_user_ai.adapters.webex_meeting import WebexMeetingAdapter


class WebexConfigTests(unittest.TestCase):
    def test_dry_run_is_default_without_environment(self) -> None:
        config = WebexConfig.from_env({})

        self.assertTrue(config.dry_run)
        self.assertFalse(config.real_mode_requested)
        self.assertFalse(config.credentials_available())
        self.assertFalse(config.can_use_real_mode())
        self.assertEqual(config.validation_reason(), "dry-run default")

    def test_real_mode_requested_without_credentials_is_blocked(self) -> None:
        config = WebexConfig.from_env({"VIRTUAL_USER_AI_WEBEX_REAL_MODE": "true"})
        adapter = WebexMeetingAdapter(config=config)

        joined = adapter.join_meeting("https://example.webex.com/meeting")

        self.assertFalse(config.dry_run)
        self.assertTrue(config.real_mode_requested)
        self.assertFalse(config.credentials_available())
        self.assertFalse(config.can_use_real_mode())
        self.assertFalse(joined)
        self.assertIn(
            "join:blocked:real mode requested but credentials are missing",
            adapter.session_log,
        )

    def test_real_mode_requires_explicit_flag_and_credentials(self) -> None:
        config = WebexConfig.from_env(
            {
                "VIRTUAL_USER_AI_WEBEX_REAL_MODE": "true",
                "WEBEX_ACCESS_TOKEN": "token-placeholder",
                "WEBEX_BOT_EMAIL": "bot@example.com",
            }
        )
        adapter = WebexMeetingAdapter(config=config)

        joined = adapter.join_meeting("https://example.webex.com/meeting")
        state = adapter.participant_state()

        self.assertFalse(config.dry_run)
        self.assertTrue(config.real_mode_requested)
        self.assertTrue(config.credentials_available())
        self.assertTrue(config.can_use_real_mode())
        self.assertTrue(joined)
        self.assertFalse(state["dry_run"])
        self.assertTrue(state["real_mode_requested"])
        self.assertTrue(state["real_mode_available"])
        self.assertIn("join:placeholder_real_mode", state["events"])


if __name__ == "__main__":
    unittest.main()
