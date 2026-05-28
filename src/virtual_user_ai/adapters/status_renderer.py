from __future__ import annotations

from collections.abc import Mapping, Sequence


def render_participant_state(state: Mapping[str, object]) -> str:
    """Render adapter participant state as stable plain text."""

    lines = [
        f"Joined: {state.get('joined')}",
        f"Meeting ID: {state.get('meeting_id')}",
        f"Dry run: {state.get('dry_run')}",
        f"Real mode requested: {state.get('real_mode_requested')}",
        f"Real mode available: {state.get('real_mode_available')}",
    ]

    media_result = state.get("last_media_result")
    lines.append("Last media result:")
    if isinstance(media_result, Mapping):
        lines.extend(
            [
                f"- success: {media_result.get('success')}",
                f"- output: {media_result.get('output')}",
                f"- reason: {media_result.get('reason')}",
                f"- wav_path: {media_result.get('wav_path')}",
            ]
        )
    else:
        lines.append("- none")

    lines.append("Events:")
    events = state.get("events")
    if isinstance(events, Sequence) and not isinstance(events, (str, bytes)) and events:
        for event in events:
            lines.append(f"- {event}")
    else:
        lines.append("- none")

    return "\n".join(lines)
