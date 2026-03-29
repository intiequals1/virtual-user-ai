"""Smoke tests for shared core and adapter boundary."""

from virtual_user_ai.adapters import MockMeetingAdapter
from virtual_user_ai.core import SessionOrchestrator, TriggerEvent, TriggerRouter


def test_audio_path_success() -> None:
    adapter = MockMeetingAdapter(force_audio_failure=False)
    orchestrator = SessionOrchestrator(adapter=adapter)
    router = TriggerRouter()

    result = router.route(TriggerEvent(trigger_type="push_to_talk", text="hello"), orchestrator)

    assert result["status"] == "responded"
    assert result["mode"] == "audio"
    assert adapter.sent_chat == []


def test_chat_fallback_when_audio_fails() -> None:
    adapter = MockMeetingAdapter(force_audio_failure=True)
    orchestrator = SessionOrchestrator(adapter=adapter)
    router = TriggerRouter()

    result = router.route(TriggerEvent(trigger_type="chat_trigger", text="status update"), orchestrator)

    assert result["status"] == "responded"
    assert result["mode"] == "chat_fallback"
    assert len(adapter.sent_chat) == 1
