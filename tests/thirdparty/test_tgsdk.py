import pytest

from app.thirdparty.proxy import MirrorProxy
from app.thirdparty.tgsdk import TelegramBot


@pytest.fixture(scope="function")
def mirror_proxy_bot(monkeypatch: pytest.MonkeyPatch) -> TelegramBot:
    bot = TelegramBot(token="")
    monkeypatch.setattr(bot, "_proxy", MirrorProxy())
    return bot


class TestTelegramBot:
    def test_check0(self, mirror_proxy_bot: TelegramBot) -> None:
        expected = (
            {"args": (), "kwargs": {}, "method": "GET", "request": "getMe",},
            MirrorProxy.STATUS,
        )
        actual = mirror_proxy_bot.check()
        assert expected == actual

    def test_send0(self, mirror_proxy_bot: TelegramBot) -> None:
        expected = (
            {
                "args": (),
                "kwargs": {"data": {"chat_id": "channel0", "text": "Hi"}},
                "method": "POST",
                "request": "sendMessage",
            },
            MirrorProxy.STATUS,
        )
        actual = mirror_proxy_bot.send("channel0", "Hi")
        assert expected == actual
