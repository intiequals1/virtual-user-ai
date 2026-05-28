# Continuous Documentation Entry 18 — CI Baseline

## Context

After baseline cleanup, smoke-test stabilization, and v1 acceptance-test creation, the repository reached a testable state. The next safe step was to make these tests repeatable outside the local machine.

## Action taken

A GitHub Actions workflow was added:

```text
.github/workflows/ci.yml
```

The workflow runs on:
- push to `main`
- pull request targeting `main`

## CI validation scope

The CI baseline installs Python 3.9 and pytest, then runs:

```bash
python -m pytest tests
python -m pytest product/system/poc_with_triggers/tests
```

This covers:
- root smoke tests
- v1 acceptance tests
- POC placeholder smoke tests
- core pipeline smoke test

## Why Python 3.9

The local validation environment currently uses Python 3.9.6. The CI baseline therefore uses Python 3.9 to mirror the local baseline and avoid false confidence from a newer runtime.

## Scope control

This batch does not add:
- deployment
- packaging
- release automation
- real Webex credentials
- platform-specific integration secrets
- broad linting or formatting gates

Those may be added later after the v1 baseline remains stable.

## Current status

The repository now has a minimal CI gate for smoke and acceptance tests. Future implementation batches should keep the workflow green before expanding functionality.

## Next step

Decide the next small v1-safe implementation batch:

1. Policy Gate Hardening: consent, AI disclosure, human mute/stop control.
2. Webex dry-run join and chat fallback refinement.
3. Media path refinement behind existing contracts.

Recommended next step: Policy Gate Hardening, because it protects the ethical and governance boundaries before deeper adapter implementation.
