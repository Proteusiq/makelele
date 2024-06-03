from pathlib import Path

from decouple import config
from starlette.datastructures import Secret

APP_VERSION = "0.1.0"
APP_NAME = "Makelele Joker"
API_PREFIX = "/api"


API_KEY: Secret = config("API_KEY", cast=Secret)
IS_DEBUG: bool = config("IS_DEBUG", cast=bool, default=False)

DEFAULT_JOKES_PATH: Path = config("DEFAULT_JOKES_PATH", cast=lambda x: Path(x))
