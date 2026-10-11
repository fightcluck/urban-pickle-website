# Urban Pickle

Marketing site for [Urban Pickle](https://www.courtsite.my/centre/Urban%20Pickle/cmcbibxfl08jw087xkm8ycrfv) — pickleball club on Jalan Tun Razak, Kuala Lumpur.

Two parallel frontends share the same venue copy (`app/content.py` / `notes.txt`):

| Version | Path | Use |
|---------|------|-----|
| **Flask** (dev / dynamic) | `app/` | Local server with routes |
| **Static** (GitHub Pages) | `static_site/` → builds `docs/` | Host on GitHub Pages |

Booking goes to [Courtsite](https://www.courtsite.my/centre/Urban%20Pickle/cmcbibxfl08jw087xkm8ycrfv/select/hourly?serviceId=&categoryId=clc8tlc5bbt2p6ogmj1xm2h3a).

## Pages

| Flask URL | Static file | Purpose |
|-----------|-------------|---------|
| `/` | `docs/index.html` | Homepage |
| `/pricing` | `docs/pricing.html` | Court & equipment rates |
| `/gallery` | `docs/gallery.html` | Photos |
| `/corporate` | `docs/corporate.html` | Corporate + contact |
| `/booking` | (Book nav → Courtsite) | Booking |

## Flask setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
uv sync
cp .env.example .env        # optional; set SECRET_KEY
uv run python run.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Static site (GitHub Pages)

```bash
uv run python static_site/build.py
cd docs && python3 -m http.server 8080   # local preview
```

Then in GitHub: **Settings → Pages → Deploy from a branch → `main` / `/docs`**.

Details: [static_site/README.md](static_site/README.md).

## Project layout

- `pyproject.toml` / `uv.lock` — dependencies (managed with uv)
- `app/` — Flask app, routes, templates, static CSS
- `static_site/` — Jinja templates + `build.py` for the static site
- `docs/` — **built** static output (commit this for GitHub Pages)
- `gallery/` — court photos (source; copied into `docs/gallery/` on build)
- `.cursor/rules/` — always-on agent conventions
- `.cursor/skills/` — workflows for create / maintain / upgrade
- `AGENTS.md` — entrypoint for AI agents

## Common uv commands

| Command | Purpose |
|---------|---------|
| `uv sync` | Create/update `.venv` from the lockfile |
| `uv run python run.py` | Run the Flask dev server |
| `uv run python static_site/build.py` | Rebuild `docs/` for GitHub Pages |
| `uv add <package>` | Add a dependency |
| `uv lock --upgrade` | Refresh the lockfile to newer compatible versions |

## Content edits

- Canonical hours/pricing/maps notes: `notes.txt` → wired in `app/content.py`
- Flask page layout: `app/templates/`
- Static page layout: `static_site/templates/` (then rebuild)
- Photos: drop `.webp` / `.jpg` / `.png` into `gallery/` (rebuild static after)

## Agent help

See [AGENTS.md](AGENTS.md) and project skills under `.cursor/skills/`.
