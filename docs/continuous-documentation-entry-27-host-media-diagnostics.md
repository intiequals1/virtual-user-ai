# Continuous Documentation Entry 27 — Host Media Diagnostics

## Context

After the media path and orchestrator fallback behavior were stabilized, the next less-familiar product area was host-level media diagnostics. This batch introduces diagnostics only. It does not open audio devices, create virtual microphones, or route audio into meetings.

## Action taken

A host diagnostics boundary was added:

```text
src/virtual_user_ai/media/host_diagnostics.py
```

A focused test file was added:

```text
tests/test_host_media_diagnostics.py
```

## Diagnostic model

The new model includes:

- `HostMediaCapability`
- `HostMediaDiagnostics`
- `HostMediaDiagnosticsProvider`

The provider checks for local tooling names such as:

```text
ffmpeg
pactl
pw-cli
arecord
aplay
```

## Recommendation behavior

The diagnostics provider recommends one of the following modes:

```text
pulseaudio_virtual_source
pipewire_diagnostics_only
file_only_audio_artifact
chat_only
```

## Tests added

The tests validate deterministic recommendations for:

1. `pactl` available
2. only `pw-cli` available
3. only `ffmpeg` available
4. no tools available

## Scope control

This batch does not add:

- real microphone access
- virtual source creation
- PulseAudio or PipeWire commands
- FFmpeg execution
- real audio routing
- meeting audio injection
- new dependencies

## Next step

Pull latest changes and run:

```bash
python3 -m pytest tests
python3 -m pytest product/system/poc_with_triggers/tests
```

If successful, verify CI and update the portfolio cockpit.
