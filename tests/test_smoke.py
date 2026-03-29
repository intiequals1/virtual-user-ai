from adapters.base import AdapterLayer, JoinOptions, bootstrap_layers
from adapters.mock_meeting import MockMeetingAdapter
from adapters.webex_meeting import WebexMeetingAdapter
from host_setup.linux import setup_linux_host


def test_layer_bootstrap_order_keeps_webex_and_linux_after_shared_layers():
    assert bootstrap_layers() == [
        AdapterLayer.CORE,
        AdapterLayer.MEDIA,
        AdapterLayer.WEBEX,
        AdapterLayer.HOST_SETUP_LINUX,
    ]


def test_mock_adapter_dry_run_stays_available():
    adapter = MockMeetingAdapter()
    result = adapter.join(JoinOptions(meeting_url="https://example.invalid", dry_run=True))
    assert result["status"] == "simulated"


def test_webex_adapter_allows_placeholder_dry_run():
    adapter = WebexMeetingAdapter()
    result = adapter.join(JoinOptions(meeting_url="https://webex.com/meet/demo", dry_run=True))
    assert result["provider"] == "webex"
    assert result["status"] == "dry-run"


def test_linux_host_setup_dry_run_stays_available():
    result = setup_linux_host(dry_run=True)
    assert result["status"] == "dry-run"
