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

## Entry 10 — Codex roadmap import batch
### What was imported
- `docs/codex-roadmap-first-prompt.md` was imported to capture the implementation roadmap and acceptance criteria.
- `docs/continuous-documentation-entry-10-codex-roadmap.md` was imported as a standalone log entry for roadmap rationale.

### What remains missing
- runnable source code for core modules, meeting adapters, media pipeline, host setup scripts, and tests described in the roadmap
- CI configuration and package structure that match the documented architecture

### What is runnable
- documentation-only repository navigation and review

### What is still placeholder-only
- all architecture components referenced in documentation (TriggerRouter, PolicyEngine, SessionOrchestrator, adapters, media worker, Linux host setup, smoke tests) remain documentation placeholders until code is imported
