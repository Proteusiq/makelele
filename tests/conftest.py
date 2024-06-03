import pytest
from starlette.config import environ
from starlette.testclient import TestClient

from makelele.core import config

config.API_KEY = "example_key"
config.DEFAULT_JOKES_PATH  = "src" / config.DEFAULT_JOKES_PATH


from makelele.main import get_app  # noqa: E402


@pytest.fixture()
def test_client():
    app = get_app()
    with TestClient(app) as test_client:
        yield test_client
