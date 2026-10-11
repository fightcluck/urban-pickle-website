"""Development entrypoint for the Urban Pickle site.

Run with: uv run python run.py
"""

import os

from dotenv import load_dotenv

from app import create_app

load_dotenv()

app = create_app()


def main() -> None:
    debug = os.getenv("FLASK_ENV", "development") == "development"
    app.run(debug=debug, port=int(os.getenv("PORT", "5000")))


if __name__ == "__main__":
    main()
