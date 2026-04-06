"""Core trigger adapters and unified router."""

from core.triggers.chat_trigger import ChatTrigger
from core.triggers.push_to_talk import PushToTalkTrigger
from core.triggers.router import TriggerRouter
from core.triggers.wake_word import WakeWordTrigger

__all__ = [
    "ChatTrigger",
    "PushToTalkTrigger",
    "TriggerRouter",
    "WakeWordTrigger",
]
