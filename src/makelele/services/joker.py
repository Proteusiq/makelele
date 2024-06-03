from pathlib import Path
from random import choice
from typing import Literal

from tomllib import loads

from makelele.core.config import (
    DEFAULT_JOKES_PATH,
)
from makelele.core.messages import NO_VALID_PAYLOAD
from makelele.models.jokes import Response


class Jokes:
    def __init__(self, path: Path = DEFAULT_JOKES_PATH):
        self.joker = loads(path.read_text())

    def joke(self, category: Literal["golf"]) -> Response:
        if category is None:
            raise ValueError(NO_VALID_PAYLOAD.format(category))

        jokes = self.joker["jokes"][category]
        response = Response(joke=choice(jokes))

        return response
