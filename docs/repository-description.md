# Repository Description

## What this repository is
**Virtual User AI** is a planning-first repository for building an AI meeting participant that can operate across:
- Microsoft Teams
- Zoom
- Google Meet
- Cisco Webex

The intended architecture is one shared, platform-agnostic AI core with separate platform adapters.

## Current state
At present, this repository is primarily documentation-driven and defines implementation direction, scope boundaries, and phased execution plans.

Current content includes:
- roadmap and phased implementation guidance
- continuous project documentation log
- baseline repository metadata (`README.md`, `LICENSE`)

## Intended v1 capabilities
The v1 product direction in this repository targets:
- joining meetings from links
- listening to audio context
- speaking when explicitly invoked
- chat fallback when audio output fails
- maintaining meeting memory/state
- honoring human mute/stop override controls
- explicit AI disclosure during participation

## Intended v1 non-goals
Out of scope for v1:
- autonomous interruption behavior
- emotion inference
- hidden/deceptive participation
- video/avatar presence
- persuasion/negotiation automation

## Planned project structure (target)
As implementation is added, the repository is expected to include:
- `core/` for trigger routing, policy, and orchestration
- `adapters/` for platform-specific integrations
- `media/` for TTS and host audio injection contracts
- `host_setup/linux/` for virtual audio routing scripts
- `tests/` for smoke and regression checks
- CI workflows for compile and smoke validation

## Engineering principles
- Keep shared logic platform-agnostic.
- Isolate provider/platform details behind contracts.
- Prefer incremental, testable changes.
- Keep docs synchronized with code.
- Preserve explicit human control and AI transparency.
