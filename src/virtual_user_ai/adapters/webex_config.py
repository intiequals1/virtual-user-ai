from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class WebexConfig:
    """Configuration boundary for Webex integration.

    Dry-run remains the default. Real mode requires explicit activation and credentials.
    """

    dry_run: bool = True
    real_mode_requested: bool = False
    access_token: str | None = None
    bot_email: str | None = None

    @classmethod
    def from_env(cls, env: Mapping[str, str] | None = None) -> "WebexConfig":
        source = env if env is not None else os.environ
        real_mode_requested = source.get("VIRTUAL_USER_AI_WEBEX_REAL_MODE", "").lower() == "true"
        dry_run = not real_mode_requested

        return cls(
            dry_run=dry_run,
            real_mode_requested=real_mode_requested,
            access_token=source.get("WEBEX_ACCESS_TOKEN"),
            bot_email=source.get("WEBEX_BOT_EMAIL"),
        )

    def credentials_available(self) -> bool:
        return bool(self.access_token and self.bot_email)

    def can_use_real_mode(self) -> bool:
        return self.real_mode_requested and self.credentials_available()

    def validation_reason(self) -> str:
        if not self.real_mode_requested:
            return "dry-run default"
        if not self.credentials_available():
            return "real mode requested but credentials are missing"
        return "real mode configured"
