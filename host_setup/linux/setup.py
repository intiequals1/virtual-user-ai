"""Linux host setup helpers."""

from __future__ import annotations


def setup_linux_host(*, dry_run: bool = True) -> dict[str, str]:
    """Prepare Linux host dependencies.

    Keeps dry-run support for CI and local validation environments.
    """

    if dry_run:
        return {
            "status": "dry-run",
            "detail": "Linux host setup skipped (dry run).",
        }

    # Placeholder for package install / service checks.
    return {
        "status": "not-implemented",
        "detail": "Linux host setup steps are not implemented yet.",
    }
