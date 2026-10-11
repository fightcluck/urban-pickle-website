"""Urban Pickle Flask application factory."""

from pathlib import Path

from flask import Flask

from app import content


def create_app() -> Flask:
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
    )
    app.config["SECRET_KEY"] = __import__("os").environ.get(
        "SECRET_KEY", "dev-only-change-me"
    )
    app.config["GALLERY_DIR"] = Path(app.root_path).parent / "gallery"

    @app.context_processor
    def inject_site():
        return {"site": content}

    from app.routes.main import main_bp
    from app.routes.corporate import corporate_bp
    from app.routes.booking import booking_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(corporate_bp)
    app.register_blueprint(booking_bp)

    return app
