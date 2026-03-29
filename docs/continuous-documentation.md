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

## Entry 12 — Baseline consolidation batch 1
A first safe import batch was applied to reduce documentation-to-repository drift without expanding beyond v1.

What changed:
- README was rewritten to reflect project origin, real status, v1 scope, and baseline constraints.
- A missing-file audit was added and used to define a controlled import batch.
- Placeholder baseline modules were imported for shared core and initial Webex adapter boundaries.
- Placeholder directories were created for media/services/linux host setup to keep intended structure explicit.
- A minimal smoke-test placeholder was added for baseline integrity checks.
- `test.txt` was removed as a non-project import artifact.

What remains:
- concrete media/service/host setup implementations
- expanded smoke tests beyond placeholder checks
- additional adapter tracks after Webex baseline remains stable
