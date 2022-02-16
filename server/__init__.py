# Flask modules.
from flask import Flask

# Project modules.
from server.blueprints.api import api
from server.blueprints.content import content

# Standard library modules.
import os
from typing import Any, Callable, Dict


def create_app(version: str = None) -> Flask:
    """Main application factory.
    Args:
        version: A string to override the application version. If not provided,
          the version will be retrieved from git.
    Returns:
        The main application.
    """

    # If we haven't been given a version, then get it from Git.
    if version is None:
        with os.popen("git describe --dirty --always --tags") as pf:
            version = pf.read().strip()

    # Initialise the core application.
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    with app.app_context():
        # Register views and setup context processor.
        app.register_blueprint(api)
        app.register_blueprint(content)
        app.context_processor(_make_context_processor(version))

    return app


def _make_context_processor(version: str) -> Callable[[], Dict[str, Any]]:
    # Make the context processor function. Note this uses (or "captures")
    # `version`. We do this so we can give the resultant function object to
    # Flask and still use the version, without it being a global.
    def context_processor() -> Dict[str, Any]:
        return {
            "version": version,
        }

    return context_processor
