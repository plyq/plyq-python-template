"""Telegram endpoints are specified here."""
import os

from flask import Blueprint, abort, request  # type: ignore

bp = Blueprint("routes", __name__)


@bp.route("/send", methods=["POST"])
def send():
    """Send message to telegram bot.

    :returns: bot response
    """
    message = request.get_data()
