from flask import Flask  # type: ignore
from flask.logging import default_handler  # type: ignore
from flask_cors import CORS  # type: ignore

from app.config import Config


def create_app(config: Config):
    app = Flask(__name__)
    app.config.from_object(config)

    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config["CORS_HEADERS"] = "Content-Type"

    from app import telegram

    app.register_blueprint(telegram.bp)

    return app
