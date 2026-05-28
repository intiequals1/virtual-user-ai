# Continuous Documentation Entry 17 — V1 MVP Acceptance Criteria

## Context

The repository baseline is now clean enough for the next planning step. The active code baseline passed the focused placeholder smoke test, and the remaining conflict-marker exception is treated as a preserved historical Entry 15 artifact. The next step is to turn the README v1 scope into acceptance criteria.

## Source basis

The acceptance criteria are based on the repository README and the current baseline state:

- one shared AI core for trigger handling, policy decisions, orchestration, and memory
- platform adapters for meeting-specific behavior, with Webex first in v1
- explicit placeholder implementation until concrete functionality is imported
- small, testable import batches
- no architecture expansion beyond v1

## V1 MVP acceptance criteria

### AC1 — Meeting join boundary
The agent can accept a meeting link and either join through the Webex adapter in dry-run mode or return an explicit placeholder response without credential-dependent behavior.

Evidence target:
- Webex adapter exposes a join method or equivalent dry-run join path.
- The behavior is deterministic and testable without real Webex credentials.

### AC2 — Trigger routing
The shared core can route supported trigger events through the baseline pipeline.

Evidence target:
- Push-to-talk trigger is accepted.
- Chat trigger is accepted.
- Wake-word remains disabled by default for v1.

### AC3 — Policy decision gate
The PolicyEngine acts as an explicit approval gate before orchestration.

Evidence target:
- Empty or unsupported events are rejected or marked clearly.
- Wake-word is blocked or disabled by default in v1.
- Approval output is structured and testable.

### AC4 — Session orchestration
The SessionOrchestrator can process a routed and approved event.

Evidence target:
- The pipeline TriggerRouter -> PolicyEngine -> SessionOrchestrator runs in a smoke test.
- The output is structured.
- Placeholder status is explicit until real behavior is imported.

### AC5 — Audio-first response path
The v1 flow attempts audio delivery first where the adapter and media path support it.

Evidence target:
- Audio delivery attempt is represented by adapter/media calls.
- Dry-run behavior remains explicit.
- No real credential-dependent audio injection is required for baseline acceptance.

### AC6 — Chat fallback
If audio delivery fails, the system provides a chat fallback path.

Evidence target:
- The adapter exposes a chat fallback method or equivalent placeholder.
- A test can confirm fallback behavior in dry-run mode.

### AC7 — Session memory
The baseline preserves a minimal session memory or diagnostic log for meeting events.

Evidence target:
- Events, responses, or diagnostics are retained during a session object lifecycle.
- This remains local and deterministic for v1.

### AC8 — Human control
Human mute or stop control remains a documented v1 requirement.

Evidence target:
- Human control is represented in product documentation and later translated into a testable policy or adapter requirement.
- No autonomous interruption is introduced before this control path is clear.

### AC9 — AI disclosure
The agent must be explicitly represented as an AI participant.

Evidence target:
- README and product documentation state explicit AI disclosure.
- Future meeting-join implementation must include disclosure behavior before production use.

### AC10 — Scope protection
The v1 MVP must not include out-of-scope behavior.

Out of scope remains:
- autonomous interruptions
- hidden or deceptive participation
- emotion inference
- avatar or video presence
- persuasion or negotiation automation

Evidence target:
- Tests and documentation do not introduce these behaviors.
- Any future request touching these areas is deferred outside v1.

## Current validation status

Validated:
- focused placeholder core pipeline smoke test passed locally
- baseline import path is testable
- Python 3.9 compatibility issue in core models was resolved
- active conflict markers were removed, except preserved historical Entry 15 when deliberately excluded

Not yet validated:
- full root test suite
- end-to-end Webex integration
- real audio injection
- real meeting join with credentials
- consent and disclosure enforcement in runtime code
- CI execution

## Next tasks

1. Run the root and POC smoke tests after pulling the latest changes.
2. Decide whether to remove or archive `test.txt` as a non-project artifact.
3. Add focused acceptance tests for push-to-talk, chat fallback, and wake-word-disabled behavior.
4. Define the next small import batch: Webex dry-run join plus chat fallback or policy gate hardening.
5. Keep Entry 15 as historical evidence but exclude it from active conflict-marker scans.

## Working rule

Every new implementation batch must add or update a small test and a continuous documentation entry. Do not expand scope beyond v1 until the acceptance criteria above are satisfied.
