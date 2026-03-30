# Voxtral Adaptation Overview

## Purpose
This branch adapts Virtual User AI toward a Voxtral-centered audio understanding path.

## Strategic change
The project now treats Voxtral as the preferred speech-understanding layer for:
- meeting transcription
- audio question answering
- summary generation
- voice-triggered function routing

## What stays unchanged
- one shared AI core
- multiple meeting adapters
- explicit AI disclosure
- human override
- controlled v1 scope

## What changes
- the audio understanding path is standardized around a Voxtral provider abstraction
- self-hosting becomes more realistic for local, private-server, and cloud-instance deployments
- the implementation roadmap now includes a dedicated Voxtral integration stream

## Expected outcome
The product should move from a generic speech layer to a more coherent open speech-understanding architecture that supports self-hosting and hybrid deployment more naturally.
