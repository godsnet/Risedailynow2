"""AutoMotivAI runtime entry point.

This repository currently provides the automation foundation and environment
validation. Upload/generation integrations should be added behind explicit
adapters once their credentials and content pipeline are configured.
"""

from __future__ import annotations

import argparse
import logging
import os
from dataclasses import dataclass
from pathlib import Path

LOGGER = logging.getLogger("automotivai")
PROJECT_DIR = Path(__file__).resolve().parent
REQUIRED_DIRECTORIES = ("assets", "output", "scripts")


@dataclass(frozen=True)
class RuntimeConfig:
    """Non-secret runtime configuration loaded from environment variables."""

    environment: str
    dry_run: bool

    @classmethod
    def from_environment(cls) -> "RuntimeConfig":
        environment = os.getenv("AUTOMOTIVAI_ENV", "development").strip() or "development"
        dry_run = os.getenv("AUTOMOTIVAI_DRY_RUN", "true").strip().lower() not in {"0", "false", "no"}
        return cls(environment=environment, dry_run=dry_run)


def ensure_project_directories(project_dir: Path = PROJECT_DIR) -> list[Path]:
    """Create and return the standard project directories."""
    directories = []
    for name in REQUIRED_DIRECTORIES:
        directory = project_dir / name
        directory.mkdir(parents=True, exist_ok=True)
        directories.append(directory)
    return directories


def run_health_check(project_dir: Path = PROJECT_DIR) -> bool:
    """Validate the local runtime without requiring external credentials."""
    directories = ensure_project_directories(project_dir)
    config = RuntimeConfig.from_environment()
    LOGGER.info("AutoMotivAI environment: %s", config.environment)
    LOGGER.info("Dry-run mode: %s", config.dry_run)
    for directory in directories:
        LOGGER.info("Ready: %s", directory.relative_to(project_dir))
    LOGGER.info("Health check passed.")
    return True


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run AutoMotivAI runtime checks.")
    parser.add_argument("command", nargs="?", choices=("health",), default="health")
    parser.add_argument("--log-level", default=os.getenv("LOG_LEVEL", "INFO"), choices=("DEBUG", "INFO", "WARNING", "ERROR"))
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    logging.basicConfig(level=getattr(logging, args.log_level), format="%(levelname)s %(message)s")
    run_health_check()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


class AutoMotivAI:
    """Backward-compatible facade for existing callers."""

    def start(self) -> None:
        LOGGER.info("Starting AutoMotivAI...")

    def run(self) -> bool:
        return run_health_check()

    def __init__(self) -> None:
        self.config = RuntimeConfig.from_environment()


__all__ = ["AutoMotivAI", "RuntimeConfig", "main", "run_health_check"]
