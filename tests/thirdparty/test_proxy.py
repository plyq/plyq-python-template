"""Test telegram SDK."""
import json

from app.thirdparty.proxy import MirrorProxy, URLBaseProxy


class TestURLBaseProxy:
    """Use httpbin.org as an url of our proxy."""

    proxy = URLBaseProxy("http://httpbin.org")

    def test_get0(self) -> None:
        """Test ``get()`` method."""
        params = {"a": "b"}
        expected = params, 200
        actual_all, status = self.proxy.get("get", params=params)
        actual = actual_all["args"], status
        assert expected == actual

    def test_post0(self) -> None:
        """Test ``post()`` method."""
        data = {"a": 10}
        expected = data, 200
        actual_all, status = self.proxy.post("post", data=json.dumps(data))
        actual = actual_all["json"], status
        assert expected == actual


class TestMirrorProxy:
    """Use httpbin.org as an url of our proxy."""

    proxy = MirrorProxy()

    def test_get0(self) -> None:
        """Test ``get()`` method."""
        params = {"a": "b"}
        expected = (
            dict(method="GET", request="get", args=(), kwargs={"params": params}),
            self.proxy.STATUS,
        )
        actual = self.proxy.get("get", params=params)
        assert expected == actual

    def test_post0(self) -> None:
        """Test ``post()`` method."""
        data = {"a": 10}
        expected = (
            dict(method="POST", request="post", args=(), kwargs={"data": data}),
            self.proxy.STATUS,
        )
        actual = self.proxy.post("post", data=data)
        assert expected == actual
