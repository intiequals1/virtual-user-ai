# Continuous Documentation Entry 30 — Media Worker Host Diagnostics Link

## Context

After the host media diagnostics CLI was documented, the next controlled step was to allow the media worker to receive host diagnostics as optional context. The worker should not execute diagnostics itself and should not run host commands. It should only use already-created diagnostics to make fallback reasons more informative.

## Action taken

The media worker was updated:

```text
src/virtual_user_ai/media/worker.py
```

A focused test file was added:

```text
tests/test_media_worker_host_diagnostics.py
```

## Behavior change

`MediaWorker` now accepts optional `host_diagnostics`.

When audio injection fails and diagnostics are available, the failure reason includes the recommended host mode:

```text
audio injection failed; host mode: chat_only
```

When diagnostics are not provided, the previous behavior remains unchanged:

```text
audio injection failed
```

## Scope control

This batch does not add:

- shell command execution in the worker
- audio device access
- microphone creation
- FFmpeg execution
- PulseAudio/PipeWire commands
- new dependencies

## Tests added

The tests validate:

1. media worker appends host mode when diagnostics are provided
2. media worker preserves the old fallback reason when diagnostics are absent

## Next step

Pull latest changes and run:

```bash
python3 -m pytest tests
python3 -m pytest product/system/poc_with_triggers/tests
```

If successful, verify CI and update the portfolio cockpit.
