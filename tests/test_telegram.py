"""Tests main app behaviour"""
import json
from typing import Generator

import pytest
from flask.testing import FlaskClient  # type: ignore
from pytest import MonkeyPatch

from app import create_app


@pytest.fixture
def client(monkeypatch: MonkeyPatch) -> Generator[FlaskClient, None, None]:
    """Monkeypatch app client."""
    monkeypatch.setenv("FLASK_ENV", "TEST")
    app = create_app()

    with app.test_client() as client:
        yield client


def test_check0(client: FlaskClient) -> None:
    """Test real chat status check."""
    response = client.get("/check")
    actual_data = json.loads(response.data)
    assert actual_data["ok"]
    assert actual_data["result"]["is_bot"]
