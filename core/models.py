"""Shared core data models used across dialogue, policy, and triggers."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class TriggerType(str, Enum):
    """Normalized trigger kinds routed by the core trigger router."""

    CHAT = "chat"
    PUSH_TO_TALK = "push_to_talk"
    WAKE_WORD = "wake_word"


@dataclass(slots=True)
class TriggerEvent:
    """Input event produced by any trigger source."""

    trigger_type: TriggerType
    payload: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class DialogueTurn:
    """Represents a single turn that can be evaluated by policy and dialogue."""

    text: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class PolicyDecision:
    """Result of centralized policy checks."""

    allowed: bool
    reason: str = ""
