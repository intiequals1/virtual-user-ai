# Codex Roadmap Plan — First Prompt

## Purpose
This roadmap translates the first product prompt into a practical execution plan based on the **current state of this repository**.

## Source prompt scope
Build **Virtual User** as a cross-platform meeting participant for:
- Microsoft Teams
- Zoom
- Google Meet
- Cisco Webex

Core architectural decision:
- **one shared AI core**
- **four meeting adapters**

## Repository context analysis (as of March 29, 2026)
### What exists today
The repository currently contains documentation artifacts and planning notes:
- roadmap and continuous documentation files under `docs/`
- a minimal `README.md`
- no implemented runtime packages yet (`core/`, `adapters/`, `media/`, `host_setup/`, `tests/` are not present)

### Gap between plan and repository
The roadmap assumes components that are not yet checked in. The immediate challenge is to create a clean scaffold and import structure before feature work begins.

### Practical implication
The next phase should prioritize establishing a runnable project skeleton with placeholder contracts so later work can be added incrementally without architecture drift.

## Product boundaries for v1
Treat the following as in scope for the first implementation cycle:
- join a meeting from a link
- listen to audio
- speak back when directly invoked
- post text to meeting chat if audio fails
- keep a meeting memory
- expose human mute/stop controls
- clearly disclose that the participant is AI

Treat the following as out of scope for v1:
- autonomous interruptions
- emotion inference
- hidden participation
- video/avatar presence
- automated persuasion or negotiation

## Primary engineering principle
Keep the shared core platform-agnostic. Platform-specific behavior must stay inside adapter modules.

## Updated delivery sequence for the current repository
1. repository bootstrap and package scaffolding
2. shared trigger/policy/session core contracts
3. media contracts and local TTS/injection abstraction
4. first functional adapter track (Webex) with dry-run mode
5. Linux host audio setup scripts and validation flow
6. smoke tests and lightweight CI baseline
7. incremental adapters for Teams/Zoom/Meet

## Execution plan

### Phase 0 — Repository bootstrap (new)
#### Goal
Create a reliable baseline so the project is importable, testable, and safe for incremental implementation.

#### Tasks
- add Python package structure:
  - `core/`
  - `adapters/`
  - `media/`
  - `host_setup/linux/`
  - `tests/`
- add `__init__.py` files and consistent import paths
- add base config model (`config.py` or `settings.py`)
- add starter CLI entrypoint for local dry-run execution
- add `.gitignore`, formatting/lint placeholders, and dependency manifest

#### Acceptance criteria
- `python -m compileall` passes
- imports resolve from repository root
- basic CLI dry-run command executes

### Phase 1 — Shared core stabilization
#### Goal
Make the invocation and response path reliable before adapter complexity increases.

#### Tasks
- implement `TriggerRouter` as the single entry for push-to-talk, wake-word, and chat-trigger events
- implement `PolicyEngine` as the approval gate
- implement `SessionOrchestrator` as the response pipeline owner
- enforce output fallback: audio first, chat fallback second
- keep `core/` free from platform-specific branches

#### Acceptance criteria
- all trigger types route into one pipeline
- rejected events are logged
- successful responses are logged
- chat fallback works when audio injection fails

### Phase 2 — Media path hardening
#### Goal
Keep the media path locally runnable and provider-agnostic.

#### Tasks
- define and preserve `media/contracts.py` as the stable boundary
- implement configurable factories:
  - `create_tts_provider()`
  - `create_injector()`
- support local file-spool and FFmpeg injection modes
- keep device detection separate from injection execution

#### Acceptance criteria
- local synthesis works without cloud credentials
- FFmpeg mode accepts explicit or auto-detected targets
- device detection emits a machine-readable report

### Phase 3 — Webex implementation track
#### Goal
Implement the first real adapter without destabilizing shared core behavior.

#### Tasks
- implement `adapters/webex_meeting.py` with dry-run support
- isolate join, leave, chat, mute/unmute, reconnect, and participant-state logic in adapter scope
- connect `send_audio()` to media worker contracts
- keep credential-dependent operations behind explicit TODO/config gates

#### Acceptance criteria
- dry-run mode functions locally
- adapter invokes media worker contract
- chat fallback remains available
- adapter exposes diagnostics for participant/session state

### Phase 4 — Linux host audio setup
#### Goal
Provide reproducible host routing from generated speech to virtual microphone source.

#### Tasks
- keep setup package under `host_setup/linux/`
- provide separate scripts for create/validate/destroy workflows
- keep environment-driven configuration in `host_audio.env.example`
- persist validation logs and artifacts in runtime paths

#### Acceptance criteria
- create script builds virtual sink/source pair on supported hosts
- validate script outputs captured WAV + analysis JSON
- destroy script removes created modules cleanly

### Phase 5 — Quality gate
#### Goal
Prevent regressions while implementation accelerates.

#### Tasks
- add and preserve smoke tests under `tests/test_smoke.py`
- validate package/import hygiene
- add lightweight CI for compile + smoke runs
- enforce small, testable increments

#### Acceptance criteria
- compile step passes
- smoke tests pass
- CI remains lightweight and fast

## Immediate next steps (actionable, repo-aware)
1. **Create scaffolding PR** with package directories, base contracts, and placeholder classes.
2. **Add minimal runnable path**: one CLI command that accepts a trigger and prints/logs orchestrator flow.
3. **Introduce smoke tests** that validate imports and a dry-run response pipeline.
4. **Implement media contract stubs** with local no-cloud fallback.
5. **Implement Webex dry-run adapter** wired to the shared orchestrator.
6. **Add Linux host setup placeholders** for create/validate/destroy scripts with clear TODO markers.
7. **Document every increment** in `docs/continuous-documentation.md` after each PR.

## Codex working rules
- do not rewrite architecture unless a concrete defect requires it
- prefer incremental changes over large refactors
- keep docs synchronized with code changes
- do not add autonomous or deceptive AI behavior to v1
- maintain explicit AI disclosure and human override assumptions

## Definition of success for the first prompt
Success means the repository becomes a clean, runnable, documented POC demonstrating:
- unified invocation
- policy-controlled behavior
- media output path
- one real adapter track
- Linux host audio preparation
- repeatable smoke validation
