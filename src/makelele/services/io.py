from pathlib import Path

from tomllib import loads


def load(contents: bytes) -> dict:
    return loads(contents.decode())


def save(contents: bytes, path: Path) -> None:
    path.write_bytes(contents)
