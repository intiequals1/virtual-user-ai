"""Smoke test for the v1 core placeholder pipeline.

The goal of this test is deliberately narrow: verify that the current baseline
is importable and that the shared core pipeline can pass a trigger event through
TriggerRouter -> PolicyEngine -> SessionOrchestrator without expanding scope.
"""

from product.system.poc_with_triggers.core.policy_engine import PolicyEngine
from product.system.poc_with_triggers.core.session_orchestrator import SessionOrchestrator
from product.system.poc_with_triggers.core.trigger_router import TriggerRouter


def test_core_pipeline_placeholder_smoke() -> None:
    event = {
        "trigger_type": "push_to_talk",
        "meeting_id": "demo-meeting",
        "speaker": "human-user",
        "text": "Virtual User AI, summarize the last decision.",
    }

    routed_event = TriggerRouter().route(event)
    policy_result = PolicyEngine().evaluate(routed_event)
    output = SessionOrchestrator().run(policy_result)

    assert routed_event["component"] == "TriggerRouter"
    assert routed_event["supported"] is True
    assert routed_event["trigger_type"] == "push_to_talk"

    assert policy_result["component"] == "PolicyEngine"
    assert policy_result["approved"] is True
    assert policy_result["routed_event"] == routed_event

    assert output["component"] == "SessionOrchestrator"
    assert output["status"] == "placeholder"
    assert output["policy_result"] == policy_result
    assert output["output_mode"] == "not_implemented"
