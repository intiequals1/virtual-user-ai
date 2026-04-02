"""Smoke placeholder tests for baseline integrity."""

from ..core import (
    PolicyEngine,
    SessionOrchestrator,
    TriggerRouter,
)
from ..adapters import WebexMeetingAdapter


def test_smoke_core_pipeline_placeholders() -> None:
    router = TriggerRouter()
    policy = PolicyEngine()
    orchestrator = SessionOrchestrator()

    routed = router.route({"type": "push_to_talk"})
    approved = policy.evaluate(routed)
    result = orchestrator.run(approved)

    assert routed["component"] == "TriggerRouter"
    assert approved["approved"] is True
    assert result["component"] == "SessionOrchestrator"


def test_smoke_webex_placeholder_join() -> None:
    adapter = WebexMeetingAdapter()
    result = adapter.join("https://example.invalid/meeting")

    assert result["component"] == "WebexMeetingAdapter"
    assert result["action"] == "join"
