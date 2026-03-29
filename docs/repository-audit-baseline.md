# Repository Audit Baseline (March 29, 2026)

## Documented POC files/folders expected
Based on repository docs, roadmap, and continuous documentation, the following POC structure is expected:

- `core/` shared components
  - `core/trigger_router.py`
  - `core/policy_engine.py`
  - `core/session_orchestrator.py`
- `adapters/` platform and mock adapters
  - `adapters/mock_meeting_adapter.py`
  - `adapters/webex_meeting.py`
- `media/` media worker contracts/factories
  - `media/contracts.py`
  - configurable TTS/injector creation paths
- `host_setup/linux/` host-audio setup package
  - create/validate/destroy scripts
  - `host_audio.env.example`
- `tests/test_smoke.py`
- CI baseline workflow files

## Missing before this batch
All expected POC code folders/files above were missing before this baseline import batch.

## Imported in this batch (next missing batch only)
Following delivery order phase 1, only the shared core baseline was imported:

- `core/__init__.py`
- `core/trigger_router.py`
- `core/policy_engine.py`
- `core/session_orchestrator.py`

## Remaining gaps after this batch
Still missing and intentionally deferred to later batches:

- `adapters/mock_meeting_adapter.py`
- `adapters/webex_meeting.py`
- full `media/` package and contracts
- `host_setup/linux/` package and scripts
- `tests/test_smoke.py`
- CI workflow baseline files
