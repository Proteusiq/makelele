from pathlib import Path

from tomllib import loads


def save(contents: bytes, path: Path) -> None:
    jokes = loads(contents.decode())
    assert "jokes" in jokes.keys()
    path.write_bytes(contents)
