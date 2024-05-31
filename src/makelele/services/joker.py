

from pathlib import Path
from random import choice
from tomllib import loads
from typing import Literal

from makelele.models.jokes import Response

from makelele.core.messages import NO_VALID_PAYLOAD
from makelele.core.config import (
    DEFAULT_JOKES_PATH,
)


class Jokes(object):
    def __init__(self, path:Path=DEFAULT_JOKES_PATH):
    
        self.joker = loads(path.read_text())
        


    def joke(self, category: Literal["golf"]) -> Response:
        if category is None:
            raise ValueError(NO_VALID_PAYLOAD.format(category))

        jokes = self.joker["jokes"][category]
        response = Response(joke=choice(jokes))

        return response
