from typing import Callable

from fastapi import FastAPI
from loguru import logger

from makelele.core.config import DEFAULT_JOKES_PATH
from makelele.services.joker import Jokes


def _startup_model(app: FastAPI) -> None:
   
    jokes_instance = Jokes(path=DEFAULT_JOKES_PATH)
    app.state.joker = jokes_instance


def _shutdown_model(app: FastAPI) -> None:
    app.state.joker = None


def start_app_handler(app: FastAPI) -> Callable:
    def startup() -> None:
        logger.info("Running app start handler.")
        _startup_model(app)

    return startup


def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        logger.info("Running app shutdown handler.")
        _shutdown_model(app)

    return shutdown
