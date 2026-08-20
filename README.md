# AutoMotivAI

AutoMotivAI is a Python automation foundation for motivational-content workflows. The current release focuses on a reliable runtime health check, safe local defaults, and a CI-ready project structure. External generation or publishing integrations should be implemented as explicit adapters and enabled only through repository secrets.

## Requirements

Python 3.10 or newer is required. The application has no mandatory third-party runtime dependency for its health check.

## Run locally

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
pip install -e '.[test]'
python main.py health
pytest
```

The health command creates `assets/`, `output/`, and `scripts/` when they are missing. It defaults to dry-run mode and does not contact external services.

## Configuration

| Variable | Default | Purpose |
|---|---|---|
| `AUTOMOTIVAI_ENV` | `development` | Runtime environment label. |
| `AUTOMOTIVAI_DRY_RUN` | `true` | Prevents live integration actions unless explicitly disabled. |
| `LOG_LEVEL` | `INFO` | Logging verbosity. |

Credentials must be stored in GitHub Actions Secrets or a local secret manager. Do not commit OAuth tokens, client secrets, JSON credential files, PEM files, or generated media.

## Project layout

```text
.
├── .github/workflows/ci.yml
├── assets/
├── output/
├── scripts/
├── main.py
├── pyproject.toml
├── requirements.txt
└── tests/
```

## CI

Every push and pull request to `main` runs syntax checks, tests, and the safe health command on supported Python versions. A manual workflow dispatch is also available from the GitHub Actions tab.

## Security note

A credential-like value was previously committed to the repository documentation. It has been removed from the current version, but removing a value from the latest commit does not invalidate copies in Git history. Revoke or rotate the corresponding credential in the provider console before enabling any live integration, then store the replacement only as a GitHub Actions Secret.
