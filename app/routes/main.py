"""Home, Pricing, and Gallery routes."""

from pathlib import Path

from flask import (
    Blueprint,
    current_app,
    render_template,
    send_from_directory,
    abort,
)

main_bp = Blueprint("main", __name__)

IMAGE_SUFFIXES = {".webp", ".jpg", ".jpeg", ".png", ".gif", ".avif"}


@main_bp.route("/")
def home():
    return render_template("home.html")


@main_bp.route("/pricing")
def pricing():
    return render_template("pricing.html")


@main_bp.route("/gallery")
def gallery():
    gallery_dir: Path = current_app.config["GALLERY_DIR"]
    images: list[str] = []
    if gallery_dir.is_dir():
        images = sorted(
            p.name
            for p in gallery_dir.iterdir()
            if p.is_file() and p.suffix.lower() in IMAGE_SUFFIXES
        )
    return render_template("gallery.html", images=images)


@main_bp.route("/gallery/media/<path:filename>")
def gallery_media(filename: str):
    """Serve photos from the project-root gallery/ folder."""
    gallery_dir: Path = current_app.config["GALLERY_DIR"]
    # Reject path traversal
    safe = Path(filename).name
    if safe != filename or ".." in filename:
        abort(404)
    target = gallery_dir / safe
    if not target.is_file():
        abort(404)
    return send_from_directory(gallery_dir, safe)
