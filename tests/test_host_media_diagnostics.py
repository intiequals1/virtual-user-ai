from __future__ import annotations

import unittest

from virtual_user_ai.media.host_diagnostics import HostMediaDiagnosticsProvider


class HostMediaDiagnosticsTests(unittest.TestCase):
    def test_recommends_pulseaudio_virtual_source_when_pactl_is_available(self) -> None:
        provider = HostMediaDiagnosticsProvider()

        diagnostics = provider.inspect(
            platform="linux",
            tool_paths={
                "ffmpeg": "/usr/bin/ffmpeg",
                "pactl": "/usr/bin/pactl",
                "pw-cli": None,
                "arecord": None,
                "aplay": None,
            },
        )

        self.assertEqual(diagnostics.recommended_mode, "pulseaudio_virtual_source")
        self.assertEqual(diagnostics.reason, "PulseAudio/PipeWire pactl tooling available")
        self.assertTrue(diagnostics.capability_map()["pactl"])

    def test_recommends_pipewire_diagnostics_when_only_pw_cli_is_available(self) -> None:
        provider = HostMediaDiagnosticsProvider()

        diagnostics = provider.inspect(
            platform="linux",
            tool_paths={
                "ffmpeg": "/usr/bin/ffmpeg",
                "pactl": None,
                "pw-cli": "/usr/bin/pw-cli",
                "arecord": None,
                "aplay": None,
            },
        )

        self.assertEqual(diagnostics.recommended_mode, "pipewire_diagnostics_only")
        self.assertEqual(diagnostics.reason, "PipeWire tooling available without pactl virtual-source control")
        self.assertTrue(diagnostics.capability_map()["pw-cli"])

    def test_recommends_file_only_when_only_ffmpeg_is_available(self) -> None:
        provider = HostMediaDiagnosticsProvider()

        diagnostics = provider.inspect(
            platform="darwin",
            tool_paths={
                "ffmpeg": "/opt/homebrew/bin/ffmpeg",
                "pactl": None,
                "pw-cli": None,
                "arecord": None,
                "aplay": None,
            },
        )

        self.assertEqual(diagnostics.recommended_mode, "file_only_audio_artifact")
        self.assertEqual(diagnostics.reason, "FFmpeg available but no host virtual microphone control detected")
        self.assertTrue(diagnostics.capability_map()["ffmpeg"])

    def test_recommends_chat_only_when_no_tools_are_available(self) -> None:
        provider = HostMediaDiagnosticsProvider()

        diagnostics = provider.inspect(
            platform="unknown",
            tool_paths={
                "ffmpeg": None,
                "pactl": None,
                "pw-cli": None,
                "arecord": None,
                "aplay": None,
            },
        )

        self.assertEqual(diagnostics.recommended_mode, "chat_only")
        self.assertEqual(diagnostics.reason, "No supported local media tooling detected")
        self.assertFalse(any(diagnostics.capability_map().values()))


if __name__ == "__main__":
    unittest.main()
