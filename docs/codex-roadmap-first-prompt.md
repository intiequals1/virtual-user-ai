# Codex Roadmap Plan — First Prompt

## Purpose
This roadmap translates the first product prompt into an execution plan Codex can follow inside the repository.

## Source prompt scope
Build **Virtual User** as a cross-platform meeting participant for:
- Microsoft Teams
- Zoom
- Google Meet
- Cisco Webex

Core architectural decision:
- **one shared AI core**
- **four meeting adapters**

## Product boundaries for v1
Codex should treat the following as in scope for the first implementation cycle:
- join a meeting from a link
- listen to audio
- speak back when directly invoked
- post text to meeting chat if audio fails
- keep a meeting memory
- expose human mute/stop controls
- clearly disclose that the participant is AI

Codex should treat the following as out of scope for v1:
- autonomous interruptions
- emotion inference
- hidden participation
- video/avatar presence
- automated persuasion or negotiation

## Primary engineering principle
Keep the shared core platform-agnostic. Platform-specific behavior must stay inside adapter modules.

## Delivery order
1. shared trigger and policy path
2. session orchestrator
3. media worker and TTS injection path
4. first real adapter: Webex
5. host-level audio plumbing for Linux
6. hardening and smoke tests
7. CI baseline
8. additional adapters later

## Phase 1 — Shared core stabilization
### Goal
Make the core invocation and response path reliable before adding more platform complexity.

### Codex tasks
- preserve `TriggerRouter` as the single entry point for push-to-talk, wake-word, and chat-trigger events
- preserve `PolicyEngine` as the single approval gate
- preserve `SessionOrchestrator` as the single response pipeline owner
- keep output fallback behavior: audio first, chat fallback second
- avoid platform-specific logic in `core/`

### Acceptance criteria
- all trigger types route into one pipeline
- rejected events are logged
- successful responses are logged
- chat fallback works when audio injection fails

## Phase 2 — Media path hardening
### Goal
Keep the media path runnable locally and easy to upgrade later.

### Codex tasks
- maintain `media/contracts.py` as the stable contract boundary
- keep `create_tts_provider()` configurable
- keep `create_injector()` configurable
- support local file-spool and FFmpeg injection modes
- keep device detection separate from actual injection

### Acceptance criteria
- local synthesis works without cloud credentials
- FFmpeg path accepts explicit or auto-detected targets
- device detection can generate a machine-readable report

## Phase 3 — Webex implementation track
### Goal
Advance the first real platform adapter without destabilizing the shared core.

### Codex tasks
- treat `adapters/webex_meeting.py` as the first real adapter target
- keep dry-run support for local development
- isolate join, leave, chat, mute, unmute, reconnect, and participant-state logic inside the adapter
- connect `send_audio()` to the media worker contract
- leave unsupported or credential-dependent operations behind explicit placeholders until real secrets are available

### Acceptance criteria
- adapter can run in dry-run mode
- adapter can call the media worker
- adapter can preserve chat fallback behavior
- adapter exposes participant/session state for diagnostics

## Phase 4 — Linux host audio setup
### Goal
Provide a reproducible path from generated speech to a selectable host microphone source.

### Codex tasks
- maintain the Linux host setup package under `host_setup/linux`
- keep create, validate, and destroy scripts separate
- keep environment-driven configuration in `host_audio.env.example`
- keep validation artifacts and logs under runtime data paths

### Acceptance criteria
- create script builds a virtual sink/source pair on supported hosts
- validate script produces a captured WAV and an analysis JSON
- destroy script removes created modules cleanly

## Phase 5 — Quality gate
### Goal
Protect the POC from regression while it evolves.

### Codex tasks
- preserve smoke tests under `tests/test_smoke.py`
- preserve import/package hygiene
- extend CI without making it heavy too early
- prefer small, testable increments

### Acceptance criteria
- compile step passes
- smoke tests pass
- CI remains lightweight and fast

## Codex working rules
- do not rewrite architecture unless a concrete defect requires it
- prefer incremental changes over large refactors
- keep docs synchronized with code changes
- do not add autonomous or deceptive AI behavior to v1
- maintain explicit AI disclosure and human override assumptions

## Immediate next tasks for Codex
1. complete missing repository import in batches
2. normalize package imports if needed for repository execution
3. add remaining POC files that are still only local
4. extend Webex adapter toward real join and chat integration behind config gates
5. prepare the next adapter after Webex only when smoke tests stay green

## Definition of success for the first prompt
Codex succeeds if the repository becomes a clean, runnable, documented POC that demonstrates:
- unified invocation
- policy-controlled behavior
- media output path
- one real adapter track
- Linux host audio preparation
- repeatable smoke validation
