# Continuous Documentation Entry 29 — CLI Usage Documentation

## Context

After the host media diagnostics CLI was introduced and validated, its safe usage needed to be visible in the repository entry point. The README was therefore updated with a concise diagnostics CLI section.

## Action taken

The README was updated:

```text
README.md
```

## Documented command

The README now documents:

```bash
python3 -m virtual_user_ai.media.diagnostics_cli
```

It also documents a deterministic platform-label option:

```bash
python3 -m virtual_user_ai.media.diagnostics_cli --platform darwin
```

## Documented output shape

The README now shows the expected output structure:

```text
Platform: darwin
Recommended media mode: file_only_audio_artifact
Reason: FFmpeg available but no host virtual microphone control detected
Capabilities:
- ffmpeg: available (...)
- pactl: missing (not found)
- pw-cli: missing (not found)
- arecord: missing (not found)
- aplay: missing (not found)
```

## Safety boundary

The README explicitly states that the diagnostics CLI:

- performs passive diagnostics only
- does not open audio devices
- does not create a virtual microphone
- does not run PulseAudio or PipeWire control commands
- does not execute FFmpeg
- does not add runtime dependencies

## Next step

Pull latest changes and run:

```bash
python3 -m pytest tests
python3 -m pytest product/system/poc_with_triggers/tests
```

If successful, verify CI and update the portfolio cockpit.
