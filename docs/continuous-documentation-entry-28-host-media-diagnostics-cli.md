# Continuous Documentation Entry 28 — Host Media Diagnostics CLI

## Context

After host media diagnostics were introduced as a safe boundary, the next useful step was to expose them through a simple CLI-oriented rendering path. This helps inspect the host media situation without changing runtime behavior or touching audio devices.

## Action taken

A diagnostics CLI module was added:

```text
src/virtual_user_ai/media/diagnostics_cli.py
```

A focused test file was added:

```text
tests/test_host_media_diagnostics_cli.py
```

## Behavior

The CLI rendering path prints:

- platform label
- recommended media mode
- reason
- capability list

Example structure:

```text
Platform: darwin
Recommended media mode: file_only_audio_artifact
Reason: FFmpeg available but no host virtual microphone control detected
Capabilities:
- ffmpeg: available (...)
- pactl: missing (not found)
```

## Scope control

This batch does not add:

- shell command execution beyond passive `shutil.which` detection
- audio device access
- microphone creation
- PulseAudio/PipeWire control commands
- FFmpeg execution
- new dependencies

## Tests added

The tests validate:

1. diagnostics rendering includes required sections
2. CLI main prints diagnostics and returns zero

## Next step

Pull latest changes and run:

```bash
python3 -m pytest tests
python3 -m pytest product/system/poc_with_triggers/tests
```

If successful, verify CI and update the portfolio cockpit.
