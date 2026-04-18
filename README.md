# contacts

Headless personal CRM for the AI age.

> [!WARNING]
> Work in progress. The product vision, architecture, and data model are still being shaped.

## Quickstart

```bash
make install
source .venv/bin/activate
contacts --help
contacts doctor
```

You can also run the CLI without activating the environment:

```bash
uv run contacts --help
uv run contacts doctor
uv run contacts init-data-dir
```

Configuration is read from `.env` and environment variables prefixed with `CONTACTS_`.
