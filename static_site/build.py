"""Build the static Urban Pickle site into docs/ for GitHub Pages.

Usage:
    uv run python static_site/build.py

Does not modify the Flask app. Reuses app/content.py and project gallery/.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = Path(__file__).resolve().parent / "templates"
OUT = ROOT / "docs"
GALLERY_SRC = ROOT / "gallery"
CSS_SRC = ROOT / "app" / "static" / "css" / "site.css"

IMAGE_SUFFIXES = {".webp", ".jpg", ".jpeg", ".png", ".gif", ".avif"}

# All pages live at the docs/ root so relative links work on GitHub Pages
# (project site or custom domain) without a BASE_PATH.
PAGES = {
    "home": "index.html",
    "pricing": "pricing.html",
    "gallery": "gallery.html",
    "corporate": "corporate.html",
}


def gallery_images() -> list[str]:
    if not GALLERY_SRC.is_dir():
        return []
    return sorted(
        p.name
        for p in GALLERY_SRC.iterdir()
        if p.is_file() and p.suffix.lower() in IMAGE_SUFFIXES
    )


def asset(path: str) -> str:
    """Relative path from a page at docs/ root to an asset."""
    return path.lstrip("/")


def media(filename: str) -> str:
    return f"gallery/{filename}"


def clean_out() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    (OUT / "css").mkdir()
    (OUT / "gallery").mkdir()


def copy_assets() -> None:
    shutil.copy2(CSS_SRC, OUT / "css" / "site.css")
    if GALLERY_SRC.is_dir():
        for p in GALLERY_SRC.iterdir():
            if p.is_file() and p.suffix.lower() in IMAGE_SUFFIXES:
                shutil.copy2(p, OUT / "gallery" / p.name)
    # Stop GitHub Pages from running Jekyll (allows _* paths if needed later)
    (OUT / ".nojekyll").write_text("", encoding="utf-8")


def build() -> None:
    sys.path.insert(0, str(ROOT))
    from app import content as site  # noqa: WPS433 — shared venue copy

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES)),
        autoescape=select_autoescape(["html", "xml"]),
    )
    env.globals.update(
        site=site,
        pages=PAGES,
        asset=asset,
        media=media,
    )

    clean_out()
    copy_assets()

    images = gallery_images()
    renders = {
        "home": ("home.html", PAGES["home"], {}),
        "pricing": ("pricing.html", PAGES["pricing"], {}),
        "gallery": ("gallery.html", PAGES["gallery"], {"images": images}),
        "corporate": ("corporate.html", PAGES["corporate"], {}),
    }

    for page_id, (template_name, out_name, extra) in renders.items():
        html = env.get_template(template_name).render(page=page_id, **extra)
        (OUT / out_name).write_text(html, encoding="utf-8")
        print(f"  wrote docs/{out_name}")

    print(f"Done → {OUT} ({len(images)} gallery images)")


if __name__ == "__main__":
    build()
