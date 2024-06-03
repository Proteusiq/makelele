from makelele.core import config
from makelele.models.jokes import Response
from makelele.services.joker import Jokes


def test_joke() -> None:
    category = "golf"
    jokes = Jokes(path=config.DEFAULT_JOKES_PATH)
    result = jokes.joke(category=category)
    assert isinstance(result, Response)
    assert result.joke in jokes.joker["jokes"][category]
