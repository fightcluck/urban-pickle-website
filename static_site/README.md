# Static site (GitHub Pages)

Jinja-built static HTML that mirrors the Flask marketing site. Output goes to [`docs/`](../docs/) so GitHub Pages can serve it directly from the `main` branch.

## Why this exists

- Shared layout via Jinja (`static_site/templates/base.html`) — less duplication than hand-copied HTML
- Same venue data as Flask: [`app/content.py`](../app/content.py) + [`notes.txt`](../notes.txt)
- No Python server at runtime — only HTML/CSS/images in `docs/`

The Flask app under `app/` is unchanged and still available for local `uv run python run.py`.

## Build

```bash
uv sync
uv run python static_site/build.py
```

This regenerates `docs/` (pages, `css/`, `gallery/`, `.nojekyll`).

Preview locally:

```bash
cd docs && python3 -m http.server 8080
# open http://127.0.0.1:8080/
```

## GitHub Pages setup

1. Commit the built `docs/` folder (and `static_site/` sources).
2. Repo **Settings → Pages**:
   - Source: **Deploy from a branch**
   - Branch: `main`
   - Folder: **/docs**
3. Site URL (project pages): `https://<user>.github.io/<repo>/`

Relative links are used, so the same `docs/` works for project Pages or a custom domain.

## Edit workflow

1. Update `notes.txt` / `app/content.py` and/or `static_site/templates/`
2. Run `uv run python static_site/build.py`
3. Commit `docs/` if you want Pages to update
