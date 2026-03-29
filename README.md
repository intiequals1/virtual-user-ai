# virtual-user-ai

Virtual User AI is a v1 proof-of-concept for a cross-platform AI meeting participant.

## Current POC scope
- Shared core pipeline: trigger -> policy -> session orchestration.
- Adapter boundary: platform behavior stays in adapters.
- Local mock adapter for smoke validation.
- Webex adapter kept as dry-run placeholder until credentials/runtime dependencies are available.

## Repository structure (current)
- `src/virtual_user_ai/core/` shared trigger, policy, and orchestration path
- `src/virtual_user_ai/adapters/` adapter contract + mock + Webex placeholder
- `src/virtual_user_ai/media/` media contract placeholder
- `tests/` smoke tests for core + fallback behavior
- `docs/` roadmap and continuous documentation log

## What is intentionally still placeholder
- Real Webex join/chat/audio runtime integration.
- Concrete media worker wiring for TTS and host audio injection.
- Linux host audio setup scripts.
- Teams/Zoom/Google Meet adapters.

## Run local smoke checks
```bash
PYTHONPATH=src python -m pytest -q
```
