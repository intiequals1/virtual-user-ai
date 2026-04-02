# Virtual User AI

Virtual User AI is a **cross-platform AI meeting participant** project targeting Microsoft Teams, Zoom, Google Meet, and Cisco Webex.

## Project origin
The repository was started from a product prompt that defined one central architectural constraint:

- keep **one shared AI core** for trigger handling, policy, and orchestration
- keep **platform-specific behavior in adapters**

This origin is captured in the repository planning docs and remains the baseline for all implementation work in v1.

## Current status (as of March 29, 2026)
The repository is still in an **incremental import and stabilization phase**.

What is currently true:
- planning and continuity docs are present
- architecture direction is documented
- code import is in progress and not yet complete
- work is being added in small, ordered batches to avoid architectural drift

## v1 boundaries
In scope for v1:
- join/listen/respond flow behind a shared core
- direct-invocation response path (push-to-talk/chat-trigger)
- audio-first output with chat fallback
- explicit AI disclosure and human override controls

Out of scope for v1:
- autonomous interruptions
- hidden/deceptive participation
- emotion inference and advanced persuasion behavior
- avatar/video presence

## Repository note
This repository should be treated as a **POC baseline under active construction**. Placeholder components may exist to preserve architecture and integration seams, but are **not production-ready** unless explicitly documented as such.
