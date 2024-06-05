import pytest
from makelele.core import config
from makelele.services.joke import Jokes
from starlette.routing import _DefaultLifespan
from starlette.testclient import TestClient

config.API_KEY = "example_key"
config.DEFAULT_JOKES_PATH = "src" / config.DEFAULT_JOKES_PATH


from makelele.main import app  # noqa: E402


@pytest.fixture()
def test_client():
    app.router.lifespan_context = _DefaultLifespan(app.router)
    app.state.joker = Jokes(path=config.DEFAULT_JOKES_PATH)
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture()
def jokes():
    yield Jokes(path=config.DEFAULT_JOKES_PATH)
