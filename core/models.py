"""Shared core data models used across dialogue, policy, and triggers.

The current local development environment uses Python 3.9.6. dataclass(slots=True)
requires Python 3.10+, so the v1 baseline keeps plain dataclasses for now.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict


class TriggerType(str, Enum):
    """Normalized trigger kinds routed by the core trigger router."""

    CHAT = "chat"
    PUSH_TO_TALK = "push_to_talk"
    WAKE_WORD = "wake_word"


@dataclass
class TriggerEvent:
    """Input event produced by any trigger source."""

    trigger_type: TriggerType
    payload: Dict[str, Any] = field(default_factory=dict)


@dataclass
class DialogueTurn:
    """Represents a single turn that can be evaluated by policy and dialogue."""

    text: str
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class PolicyDecision:
    """Result of centralized policy checks."""

    allowed: bool
    reason: str = ""
