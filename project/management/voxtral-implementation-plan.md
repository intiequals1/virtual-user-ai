# Voxtral Implementation Plan

## Goal
Implement a Voxtral-oriented speech-understanding path for Virtual User AI that can run locally, on private servers, or on cloud instances.

## Scope
### In scope
- provider abstraction for Voxtral
- transcription pipeline stub
- summary pipeline stub
- function-call mapping stub
- deployment examples for self-hosting
- evaluation and rollout documents

### Out of scope
- production-grade live credentials
- platform-specific completion claims
- autonomous behavior outside v1 boundaries

## Work packages
1. define provider contracts
2. implement client stub and configuration model
3. define transcription and summary flow interfaces
4. define function-routing interface
5. define deployment examples
6. define evaluation criteria
7. document integration with shared core and adapters

## Implementation order
1. contracts and config
2. provider client stub
3. pipelines
4. deployment artifacts
5. evaluation artifacts
6. branch documentation update

## Acceptance criteria
- repository contains a coherent Voxtral engineering scaffold
- scaffold is self-hosting-compatible by design
- no architecture drift into platform adapters
- documents are sufficient for Codex continuation
