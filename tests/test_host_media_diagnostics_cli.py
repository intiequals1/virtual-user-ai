from __future__ import annotations

import io
import unittest
from contextlib import redirect_stdout

from virtual_user_ai.media.diagnostics_cli import main, render_host_media_diagnostics


class HostMediaDiagnosticsCliTests(unittest.TestCase):
    def test_render_host_media_diagnostics_contains_required_sections(self) -> None:
        output = render_host_media_diagnostics(platform="test-platform")

        self.assertIn("Platform: test-platform", output)
        self.assertIn("Recommended media mode:", output)
        self.assertIn("Reason:", output)
        self.assertIn("Capabilities:", output)
        self.assertIn("- ffmpeg:", output)
        self.assertIn("- pactl:", output)
        self.assertIn("- pw-cli:", output)
        self.assertIn("- arecord:", output)
        self.assertIn("- aplay:", output)

    def test_cli_main_prints_diagnostics_and_returns_zero(self) -> None:
        buffer = io.StringIO()

        with redirect_stdout(buffer):
            result = main(["--platform", "test-platform"])

        self.assertEqual(result, 0)
        self.assertIn("Platform: test-platform", buffer.getvalue())
        self.assertIn("Recommended media mode:", buffer.getvalue())


if __name__ == "__main__":
    unittest.main()
