from makelele.models.jokes import Response


def test_joke(jokes) -> None:
    category = "golf"
    result = jokes.joke(category=category)
    assert isinstance(result, Response)
    assert result.joke in jokes.joker["jokes"][category]
