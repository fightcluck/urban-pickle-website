# Urban Pickle

Flask + Jinja2 + Tailwind (CDN) site for [Urban Pickle](https://www.courtsite.my/centre/Urban%20Pickle/cmcbibxfl08jw087xkm8ycrfv) — pickleball club on Jalan Tun Razak, Kuala Lumpur.

Venue copy lives in `app/content.py`. Booking redirects to [Courtsite](https://www.courtsite.my/centre/Urban%20Pickle/cmcbibxfl08jw087xkm8ycrfv/select/hourly?serviceId=&categoryId=clc8tlc5bbt2p6ogmj1xm2h3a).

## Pages

| URL | Purpose |
|-----|---------|
| `/` | Homepage |
| `/pricing` | Court & equipment rates |
| `/gallery` | Photos from `gallery/` |
| `/corporate` | Corporate packages + contact |
| `/booking` | Redirects to Courtsite hourly booking |

## Setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
uv sync
cp .env.example .env        # optional; set SECRET_KEY
uv run python run.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Project layout

- `pyproject.toml` / `uv.lock` — dependencies (managed with uv)
- `app/` — Flask app, routes, templates, static CSS
- `gallery/` — court photos (served at `/gallery/media/<filename>`)
- `.cursor/rules/` — always-on agent conventions
- `.cursor/skills/` — workflows for create / maintain / upgrade
- `AGENTS.md` — entrypoint for AI agents

## Common uv commands

| Command | Purpose |
|---------|---------|
| `uv sync` | Create/update `.venv` from the lockfile |
| `uv run python run.py` | Run the dev server |
| `uv add <package>` | Add a dependency |
| `uv lock --upgrade` | Refresh the lockfile to newer compatible versions |

## Content edits

- Canonical hours/pricing/maps notes: `notes.txt` → wired in `app/content.py`
- Page layout/copy: `app/templates/`
- Photos: drop `.webp` / `.jpg` / `.png` into `gallery/`
- Nav/layout: `app/templates/base.html`

## Agent help

See [AGENTS.md](AGENTS.md) and project skills under `.cursor/skills/`.
