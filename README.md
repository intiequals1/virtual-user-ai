# virtual-user-ai

## Origin and project intent
`virtual-user-ai` started as a practical effort to build a controllable AI meeting participant that can operate across multiple platforms without duplicating core logic for each platform.

The repository follows one architectural premise from the beginning:
- **one shared AI core** for trigger handling, policy decisions, orchestration, and memory
- **platform adapters** for meeting-specific behavior (Webex first in v1)

## Current repository state (as of 2026-03-29)
This repository is in a **baseline consolidation** phase.

What is true right now:
- documentation exists for scope, architecture, and execution order
- v1 boundaries are documented and intentionally constrained
- repository import is still in progress and uses explicit placeholders where implementation is not yet imported
- the next safe step is controlled batch import, not architecture refactor

## v1 scope
### In scope (v1)
- join from a meeting link
- listen to meeting audio
- speak only when directly invoked
- fallback to chat when audio output fails
- keep session memory
- expose human mute/stop control
- keep explicit AI disclosure

### Out of scope (v1)
- autonomous interruptions
- hidden/deceptive participation
- emotion inference
- avatar/video presence
- persuasion/negotiation automation

## Architecture guardrails
- keep shared logic in `product/system/poc_with_triggers/core/`
- keep platform-specific logic in `product/system/poc_with_triggers/adapters/`
- keep media contracts separate in `product/system/poc_with_triggers/media/`
- keep placeholders explicit until real implementation is imported
- prefer small, testable import batches

## Implementation status snapshot
- **Shared core:** placeholder baseline imported for `TriggerRouter`, `PolicyEngine`, and `SessionOrchestrator`
- **Adapters:** Webex adapter placeholder baseline imported (no credential-dependent behavior implemented)
- **Media/services/host setup:** directory placeholders present for controlled follow-up imports
- **Tests:** smoke-test placeholder present to keep baseline checks explicit

## Repository hygiene note
`test.txt` is treated as a non-project import artifact and should be removed from the stable baseline.

## Next steps
1. continue missing-file imports in small v1-safe batches
2. replace placeholders with concrete implementations incrementally
3. keep continuous documentation synchronized with every import batch
4. preserve core-vs-adapter separation and avoid architecture expansion beyond v1
