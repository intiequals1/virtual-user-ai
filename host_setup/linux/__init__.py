"""Linux host setup track.

Imported after shared adapter core/media layers to keep optional setup isolated.
"""

from .setup import setup_linux_host

__all__ = ["setup_linux_host"]
