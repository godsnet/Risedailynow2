from pathlib import Path

from main import RuntimeConfig, run_health_check


def test_health_check_creates_standard_directories(tmp_path: Path) -> None:
    assert run_health_check(tmp_path) is True
    assert {path.name for path in tmp_path.iterdir()} == {"assets", "output", "scripts"}


def test_default_configuration_is_safe(monkeypatch) -> None:
    monkeypatch.delenv("AUTOMOTIVAI_ENV", raising=False)
    monkeypatch.delenv("AUTOMOTIVAI_DRY_RUN", raising=False)
    config = RuntimeConfig.from_environment()
    assert config.environment == "development"
    assert config.dry_run is True


def test_false_values_disable_dry_run(monkeypatch) -> None:
    monkeypatch.setenv("AUTOMOTIVAI_DRY_RUN", "false")
    assert RuntimeConfig.from_environment().dry_run is False
