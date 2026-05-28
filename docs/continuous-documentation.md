# Continuous Documentation

## Entry 1 — Project framing
Virtual User AI is defined as a cross-platform meeting participant for Teams, Zoom, Google Meet, and Webex.
The architectural decision is one shared core plus multiple meeting adapters.

## Entry 2 — Trigger decision
Supported invocation modes:
- push-to-talk
- wake-word
- chat trigger

For v1, push-to-talk and chat trigger are enabled by default. Wake-word remains available but disabled by default.

## Entry 3 — POC architecture
The POC includes:
- TriggerRouter
- PolicyEngine
- SessionOrchestrator
- MockMeetingAdapter
- Webex adapter skeleton
- media worker interface

## Entry 4 — Current repository import status
The repository contains documentation and a baseline code structure. Project files should continue to be added incrementally to avoid losing structure or overwriting existing contents.

## Entry 5 — Codex roadmap import batch
Imported:
- docs/codex-roadmap-first-prompt.md
- docs/continuous-documentation-entry-10-codex-roadmap.md

Remaining gaps at that time:
- runnable source code for core modules, meeting adapters, media pipeline, host setup scripts, and tests
- CI configuration and package structure matching the documented architecture

## Entry 6 — POC repository skeleton added
A baseline POC repository skeleton was added under product/system/poc_with_triggers with directories for core, adapters, media, services, config, tests, and Linux host setup.

## Entry 7 — Repository baseline audit and first shared-core import batch
A repository audit was executed against the documented POC target structure.

Action taken:
- imported phase-1 shared-core baseline files
- kept adapter, media, and host setup out of scope for that batch
- preserved the shared-core and adapter separation
- kept placeholders explicitly non-production

## Entry 8 — Shared-core POC scaffold import batch
A safe incremental repository-import batch established the local v1 POC structure without expanding scope.

Added:
- src/virtual_user_ai package scaffold
- shared core modules
- adapter boundary and placeholder implementations
- media contract placeholder
- smoke test file
- README structure updates

Still missing after this batch:
- real Webex integration
- concrete media provider and delivery implementation
- Linux host setup package
- CI baseline workflow
- additional adapter tracks

## Entry 9 — Shared core plus Webex dry-run adapter batch
A minimal v1-consistent skeleton was added.

Included:
- shared core modules for trigger routing, policy gating, and orchestration
- media contracts and dry-run worker path
- Webex adapter in dry-run mode
- smoke tests for baseline behavior

Explicit placeholders retained:
- Webex mute, unmute, and reconnect
- credential-backed Webex flows
- non-Webex adapters

## Entry 10 — Baseline hygiene and smoke-test stabilization
Conflict markers were removed from active baseline and package files.

Actions taken:
- cleaned root tests, POC tests, POC Webex adapter, git ignore, and src/virtual_user_ai modules
- cleaned core package exports
- made core/models.py compatible with Python 3.9
- added product/system/poc_with_triggers/tests/test_core_pipeline_smoke.py

Validation:
- local smoke test passed: 1 passed in 0.01s

Next step:
- pull latest changes locally
- re-run the repository conflict-marker scan
- run smoke tests again
- derive v1-MVP acceptance criteria from README and repository state