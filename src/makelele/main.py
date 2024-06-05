from contextlib import asynccontextmanager

from fastapi import FastAPI
from loguru import logger
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from makelele.api.routes.router import api_router
from makelele.core.config import (
    API_PREFIX,
    APP_NAME,
    APP_VERSION,
    DEFAULT_JOKES_PATH,
    IS_DEBUG,
)
from makelele.services.joke import Jokes

observer = Observer()


@asynccontextmanager
async def lifespan(app: FastAPI):
    class FileHandler(FileSystemEventHandler):
        def on_modified(self, event):
            logger.info(f"path={event.src_path} event={event.event_type}")
            app.state.joker = Jokes(path=DEFAULT_JOKES_PATH)

    # Observe and Load the Jokes toml
    observer.schedule(FileHandler(), path=DEFAULT_JOKES_PATH.parent, recursive=False)
    observer.start()

    app.state.joker = Jokes(path=DEFAULT_JOKES_PATH)

    yield
    # Clean up the Jokes and release the resources
    app.state.joker = None

    observer.stop()
    observer.join()


app = FastAPI(title=APP_NAME, version=APP_VERSION, debug=IS_DEBUG, lifespan=lifespan)
app.include_router(api_router, prefix=API_PREFIX)
