"""Device detection is intentionally separate from audio injection."""

from __future__ import annotations

from dataclasses import dataclass

from .contracts import AudioDevice, DeviceDetector


@dataclass(frozen=True)
class StaticDeviceDetector(DeviceDetector):
    """Simple detector backed by static configured devices."""

    devices: list[AudioDevice]

    def list_devices(self) -> list[AudioDevice]:
        return list(self.devices)


class EmptyDeviceDetector(DeviceDetector):
    """Detector used in environments where host devices are not enumerable."""

    def list_devices(self) -> list[AudioDevice]:
        return []
