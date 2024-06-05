from fastapi import APIRouter

from makelele.api.routes import heartbeat, home, io, joke

api_router = APIRouter()
api_router.include_router(home.router, tags=["home"])
api_router.include_router(heartbeat.router, tags=["health"], prefix="/health")
api_router.include_router(joke.router, tags=["joker"], prefix="/v1")
api_router.include_router(io.router, tags=["upload"], prefix="/v1")
