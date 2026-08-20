# Security Policy

## Supported versions

Only the latest version on the `main` branch is actively maintained.

## Reporting a vulnerability

Please do not open a public issue for a suspected vulnerability. Use GitHub's private vulnerability reporting feature for this repository, or contact the repository owner through the GitHub profile associated with `godsnet/Risedailynow2`.

Never include OAuth refresh tokens, client secrets, private keys, or other credentials in issues, pull requests, commits, workflow logs, or generated artifacts. If a credential has been exposed, revoke it with the provider immediately and replace it through GitHub Actions Secrets.

## Secret handling

The project defaults to dry-run mode and does not require credentials for its health check. Live integrations must be explicitly implemented and must read credentials from environment variables or GitHub Actions Secrets rather than committed files.
