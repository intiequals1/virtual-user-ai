# Voxtral Roadmap

## Objective
Integrate a Voxtral-based speech-understanding layer into Virtual User AI while preserving the shared-core-plus-adapters architecture.

## Phase 1 — Repository and architecture alignment
- create branch-specific adaptation docs
- define Voxtral provider boundary
- define self-hosting-first deployment assumptions

## Phase 2 — Voxtral provider stub
- add provider contracts
- add client stub
- add transcription, summary, and function-routing pipeline stubs
- add config examples

## Phase 3 — Shared-core integration
- connect meeting audio ingestion to Voxtral provider interface
- map summary outputs into memory and audit flows
- map voice intents into controlled function calls

## Phase 4 — Adapter consumption
- keep Webex as first real adapter track
- route meeting audio through the Voxtral provider boundary
- preserve chat fallback and dry-run paths

## Phase 5 — Evaluation and hardening
- add evaluation plan for transcription, latency, summaries, and invocation quality
- verify self-hosted deployment paths
- preserve smoke-test discipline

## Exit condition
The branch is successful when the repository contains a coherent Voxtral-oriented project plan, implementation path, and engineering scaffold that Codex can continue from incrementally.
