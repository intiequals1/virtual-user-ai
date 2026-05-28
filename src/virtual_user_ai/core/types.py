from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class TriggerType(str, Enum):
    PUSH_TO_TALK = "push_to_talk"
    WAKE_WORD = "wake_word"
    CHAT = "chat"
    HUMAN_STOP = "human_stop"
    HUMAN_MUTE = "human_mute"


@dataclass(frozen=True)
class TriggerEvent:
    trigger_type: TriggerType
    text: str
    user_id: str


@dataclass(frozen=True)
class PolicyContext:
    consent_granted: bool = True
    ai_disclosed: bool = True
    human_control_active: bool = True


@dataclass(frozen=True)
class PolicyDecision:
    approved: bool
    reason: str
