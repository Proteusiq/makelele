from tomllib import loads

from makelele.core.config import (
    DEFAULT_JOKES_PATH,
)


def save(contents: bytes) -> None:
    jokes = loads(contents.decode())
    assert "jokes" in jokes.keys()
    DEFAULT_JOKES_PATH.write_bytes(contents)
