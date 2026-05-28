from __future__ import annotations

import argparse
import platform as platform_module
from collections.abc import Sequence

from virtual_user_ai.media.host_diagnostics import HostMediaDiagnosticsProvider


def render_host_media_diagnostics(platform: str | None = None) -> str:
    """Render host media diagnostics as stable plain text."""

    detected_platform = platform or platform_module.system().lower()
    diagnostics = HostMediaDiagnosticsProvider().inspect(platform=detected_platform)
    lines = [
        f"Platform: {diagnostics.platform}",
        f"Recommended media mode: {diagnostics.recommended_mode}",
        f"Reason: {diagnostics.reason}",
        "Capabilities:",
    ]
    for capability in diagnostics.capabilities:
        status = "available" if capability.available else "missing"
        lines.append(f"- {capability.name}: {status} ({capability.detail})")
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Inspect local host media diagnostics without opening audio devices.")
    parser.add_argument("--platform", default=None, help="Optional platform label for deterministic diagnostics output.")
    args = parser.parse_args(argv)

    print(render_host_media_diagnostics(platform=args.platform))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
