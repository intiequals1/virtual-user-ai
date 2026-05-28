# Continuous Documentation Entry 21 — Webex Real Integration Boundary

## Context

The Webex adapter currently works as a deterministic dry-run adapter. Local tests and CI now validate the baseline, policy gate, v1 acceptance criteria, and Webex dry-run join/chat behavior. Before adding any real Webex API calls or credentials, the boundary for real integration must be explicit.

## Purpose

This document defines what may be added later as real Webex integration and what remains outside the v1 boundary. The goal is to avoid uncontrolled scope expansion, unsafe credential handling, hidden meeting participation, or untested automation behavior.

## Current state

The current Webex adapter supports:

- dry-run join simulation
- invalid-link rejection
- joined/not-joined state
- chat message logging
- audio attempt via local media worker contract
- participant state diagnostics

It does not perform:

- real Webex authentication
- real meeting join
- real meeting audio capture
- real chat posting
- real participant control
- real media injection into a Webex meeting

## Allowed future integration scope

A future real Webex integration may add only the following, in small tested batches:

1. Credential configuration boundary
   - read credentials from environment variables or GitHub secrets only
   - never hardcode credentials
   - fail safely when credentials are missing

2. Webex API client boundary
   - isolate Webex API calls in the adapter layer
   - keep shared core independent of Webex-specific logic
   - preserve dry-run mode as the default local development mode

3. Meeting join preparation
   - validate meeting link format
   - prepare a join request or API call behind an explicit feature flag
   - return structured placeholder or dry-run output when real mode is disabled

4. Chat posting boundary
   - allow real chat posting only after explicit join and disclosure conditions are satisfied
   - retain chat fallback as a controlled behavior
   - log only minimal diagnostic metadata, not sensitive meeting content

5. Disclosure boundary
   - the AI participant must be explicitly identified as an AI participant before any real meeting interaction
   - no hidden, ambiguous, or deceptive participation is allowed

6. Human control boundary
   - human stop and mute commands must override automated responses
   - human control must remain available before, during, and after any response attempt

7. Testability boundary
   - every real integration step must include a dry-run test
   - credential-dependent tests must be isolated and optional
   - CI must not require private secrets for the normal baseline

## Required secrets for future real mode

The project may later define secrets such as:

```text
WEBEX_ACCESS_TOKEN
WEBEX_CLIENT_ID
WEBEX_CLIENT_SECRET
WEBEX_REFRESH_TOKEN
WEBEX_BOT_EMAIL
```

These names are provisional. They must not be introduced into runtime logic before the corresponding real integration design is reviewed.

## Prohibited behavior

The following remain out of scope for v1 and must not be introduced by Webex integration:

- hidden meeting participation
- impersonation of a human participant
- autonomous interruption of speakers
- emotion inference or sentiment surveillance
- automatic persuasion, negotiation, or decision pressure
- recording or storing meeting content without explicit authorization
- credential storage in repository files
- mandatory CI tests that require private credentials
- platform-specific logic leaking into shared core modules

## Real mode activation rule

Real Webex behavior must require explicit activation.

Recommended rule:

```text
Dry-run mode remains the default.
Real mode requires both credentials and an explicit configuration flag.
```

Example future flag names:

```text
VIRTUAL_USER_AI_WEBEX_REAL_MODE=true
VIRTUAL_USER_AI_REQUIRE_DISCLOSURE=true
```

## Acceptance criteria for first real-boundary implementation

Before any real Webex API call is implemented, the following should be testable:

1. missing credentials produce a safe blocked state
2. dry-run mode remains green without credentials
3. real mode cannot start without explicit disclosure configuration
4. human stop/mute policy blocks response generation
5. adapter state reports dry-run versus real-mode intent clearly
6. shared core remains free of Webex-specific imports

## Recommended next implementation batch

The next small v1-safe batch should not call the real Webex API yet. It should add configuration boundaries only:

- define a `WebexConfig` object
- load config from environment variables
- keep dry-run default
- add tests for missing credentials and explicit real-mode activation

## Working rule

Do not add Webex credentials, real API calls, or meeting automation until the configuration boundary is implemented, tested, documented, and CI remains green without secrets.
