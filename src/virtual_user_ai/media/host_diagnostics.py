from __future__ import annotations

import shutil
from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class HostMediaCapability:
    """One detected or missing host media capability."""

    name: str
    available: bool
    detail: str


@dataclass(frozen=True)
class HostMediaDiagnostics:
    """Structured host media diagnostics for audio-path planning."""

    platform: str
    capabilities: tuple[HostMediaCapability, ...]
    recommended_mode: str
    reason: str

    def capability_map(self) -> dict[str, bool]:
        return {capability.name: capability.available for capability in self.capabilities}


class HostMediaDiagnosticsProvider:
    """Detects host media tooling without opening devices or routing audio."""

    TOOL_NAMES = (
        "ffmpeg",
        "pactl",
        "pw-cli",
        "arecord",
        "aplay",
    )

    def inspect(self, platform: str, tool_paths: Mapping[str, str | None] | None = None) -> HostMediaDiagnostics:
        paths = tool_paths if tool_paths is not None else {tool: shutil.which(tool) for tool in self.TOOL_NAMES}
        capabilities = tuple(
            HostMediaCapability(
                name=tool,
                available=bool(paths.get(tool)),
                detail=str(paths.get(tool)) if paths.get(tool) else "not found",
            )
            for tool in self.TOOL_NAMES
        )
        capability_map = {capability.name: capability.available for capability in capabilities}

        if capability_map.get("pactl"):
            return HostMediaDiagnostics(
                platform=platform,
                capabilities=capabilities,
                recommended_mode="pulseaudio_virtual_source",
                reason="PulseAudio/PipeWire pactl tooling available",
            )
        if capability_map.get("pw-cli"):
            return HostMediaDiagnostics(
                platform=platform,
                capabilities=capabilities,
                recommended_mode="pipewire_diagnostics_only",
                reason="PipeWire tooling available without pactl virtual-source control",
            )
        if capability_map.get("ffmpeg"):
            return HostMediaDiagnostics(
                platform=platform,
                capabilities=capabilities,
                recommended_mode="file_only_audio_artifact",
                reason="FFmpeg available but no host virtual microphone control detected",
            )

        return HostMediaDiagnostics(
            platform=platform,
            capabilities=capabilities,
            recommended_mode="chat_only",
            reason="No supported local media tooling detected",
        )
