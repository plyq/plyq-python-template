"""Telegram SDK."""
from typing import Any, Dict, Tuple

from app.thirdparty.proxy import URLBaseProxy


class TelegramBot:
    """Wrapper for telegram bot commands."""

    BASE_URL = "https://api.telegram.org/bot"

    def __init__(self, token: str) -> None:
        """
        :param token: personal API token
        """
        self._token = token
        self._url = "%s%s" % (self.BASE_URL, self._token)
        self._proxy = URLBaseProxy(self._url)

    def check(self) -> Tuple[Dict[str, Any], int]:
        """Check that bot is alive.

        :returns: base bot info
        """
        return self._proxy.get("getMe")

    def send(self, chat: str, message: str) -> Tuple[Dict[str, Any], int]:
        """Send message to chat.

        :param chat: chat id
        :param message: message to send
        :returns: base bot info
        """
        data = {
            "chat_id": chat,
            "text": message,
        }
        return self._proxy.post("sendMessage", data=data)
