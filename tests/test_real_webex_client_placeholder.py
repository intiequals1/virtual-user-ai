from __future__ import annotations

import unittest

from virtual_user_ai.adapters.webex_client import RealWebexApiClientPlaceholder
from virtual_user_ai.adapters.webex_config import WebexConfig


class RealWebexClientPlaceholderTests(unittest.TestCase):
    def test_placeholder_blocks_when_real_mode_not_requested(self) -> None:
        config = WebexConfig.from_env({})
        client = RealWebexApiClientPlaceholder(config=config)

        result = client.prepare_join("https://example.webex.com/meeting")

        self.assertFalse(result["ok"])
        self.assertEqual(result["reason"], "real mode not requested")
        self.assertIn("prepare_join:blocked:real mode not requested", client.operations)

    def test_placeholder_blocks_when_credentials_are_missing(self) -> None:
        config = WebexConfig.from_env({"VIRTUAL_USER_AI_WEBEX_REAL_MODE": "true"})
        client = RealWebexApiClientPlaceholder(config=config)

        result = client.prepare_join("https://example.webex.com/meeting")

        self.assertFalse(result["ok"])
        self.assertEqual(result["reason"], "real mode credentials missing")
        self.assertIn("prepare_join:blocked:real mode credentials missing", client.operations)

    def test_placeholder_blocks_even_when_real_mode_is_configured(self) -> None:
        config = WebexConfig.from_env(
            {
                "VIRTUAL_USER_AI_WEBEX_REAL_MODE": "true",
                "WEBEX_ACCESS_TOKEN": "token-placeholder",
                "WEBEX_BOT_EMAIL": "bot@example.com",
            }
        )
        client = RealWebexApiClientPlaceholder(config=config)

        join_result = client.prepare_join("https://example.webex.com/meeting")
        chat_result = client.post_chat_message("meeting-id-placeholder", "hello")

        self.assertFalse(join_result["ok"])
        self.assertEqual(join_result["reason"], "prepare_join not implemented")
        self.assertFalse(chat_result["ok"])
        self.assertEqual(chat_result["reason"], "post_chat_message not implemented")
        self.assertIn("prepare_join:blocked:prepare_join not implemented", client.operations)
        self.assertIn("post_chat_message:blocked:post_chat_message not implemented", client.operations)


if __name__ == "__main__":
    unittest.main()
