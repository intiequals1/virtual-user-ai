# Continuous Documentation

## Entry 1 — Project framing
Virtual User AI is defined as a cross-platform meeting participant for Teams, Zoom, Google Meet, and Webex.
The core architectural decision is one shared AI core plus multiple meeting adapters.

## Entry 2 — Trigger decision
All three invocation modes are supported:
- push-to-talk
- wake-word
- chat trigger

For v1, push-to-talk and chat trigger are enabled by default.
Wake-word remains available but disabled by default.

## Entry 3 — POC architecture
The POC includes:
- TriggerRouter
- PolicyEngine
- SessionOrchestrator
- MockMeetingAdapter
- Webex adapter skeleton
- media worker and TTS injection service

## Entry 4 — Media path
A runnable media path was introduced:
1. response text is sent to a media worker
2. the worker synthesizes audio
3. the injector routes audio toward a virtual microphone target
4. chat fallback remains available if audio delivery fails

## Entry 5 — Device detection
Runtime detection was added for PulseAudio, PipeWire, ALSA, FFmpeg, and local audio tooling.
This allows the host to recommend a viable injection target.

## Entry 6 — Linux host setup
A Linux host setup package was added to create a virtual sink/source pair and validate it end to end.
This closes the gap between code-level audio generation and host-level microphone routing.

## Entry 7 — Hardening sprint
A hardening sprint was executed to improve stability:
- media worker wiring corrected
- package `__init__.py` files added
- `.gitignore` added
- smoke tests added
- compile and smoke validation passed locally

## Entry 8 — CI baseline
A lightweight CI baseline was defined to run byte-compilation and smoke tests for POC changes.

## Entry 9 — Current repository import status
The repository now contains an initial repository description and a continuous documentation file.
More project files should be added incrementally to avoid losing structure or overwriting existing contents.

## Entry 10 — Codex roadmap added
A dedicated Codex roadmap was added under `docs/codex-roadmap-first-prompt.md` to anchor implementation sequencing and v1 boundaries.

## Entry 11 — Repository baseline audit and first code import batch
A repository audit was executed against the documented POC target structure.

Findings:
- core, adapters, media, host setup, tests, and CI baseline implementation files were not yet present in the repository.

Action taken (next batch only):
- imported phase-1 shared-core baseline files:
  - `core/trigger_router.py`
  - `core/policy_engine.py`
  - `core/session_orchestrator.py`

Scope control:
- no adapter/media/host setup import in this batch
- no broad refactor
- architecture preserved: shared core separated from adapter layer
- placeholders remain explicitly non-production
