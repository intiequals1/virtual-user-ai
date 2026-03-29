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

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
## Entry 11 — Repository import batch: shared core + Webex dry-run adapter
The next missing import batch was added from the local project structure as a minimal v1-consistent skeleton.

Included in this batch:
- shared core modules for trigger routing, policy gating, and orchestration
- stable media contracts plus a dry-run media worker path
- Webex adapter as the first real adapter track in dry-run mode
- smoke tests for trigger-to-audio and chat fallback behavior

Explicit placeholders retained (not complete features):
- Webex mute, unmute, and reconnect are placeholders
- real credential-backed Webex join/chat flows are not imported yet
- non-Webex adapters are intentionally not imported in this batch
=======
## Entry 11 — Repository import batch: shared-core POC scaffold
A safe incremental repository-import batch was completed to establish the local v1 POC structure without expanding scope.

### Added in this batch
- `src/virtual_user_ai/` package scaffold with explicit shared core modules:
  - TriggerRouter
  - PolicyEngine
  - SessionOrchestrator
- `src/virtual_user_ai/adapters/` contract boundary and implementations:
  - abstract `MeetingAdapter`
  - `MockMeetingAdapter` for local smoke validation
  - `WebexMeetingAdapter` dry-run placeholder with explicit credential/runtime dependency markers
- `src/virtual_user_ai/media/contracts.py` placeholder media contract
- `tests/test_smoke.py` to validate audio success and chat fallback behavior
- README expanded to document current structure and explicit placeholders

### Still missing after this batch
- Real meeting join/leave/chat integration for Webex
- TTS provider + injector implementation behind media contracts
- Linux host setup package (`host_setup/linux`)
- CI baseline workflow and additional adapter tracks (Teams, Zoom, Google Meet)
>>>>>>> 2314bc3 (Add v1 POC scaffold batch with core, adapters, and smoke tests)
=======
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
>>>>>>> 665e639 (Baseline repo audit and first shared-core import batch)
=======
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
>>>>>>> f9403bb (docs: update import batch status in README and continuous log)
