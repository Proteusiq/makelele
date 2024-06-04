from fastapi import APIRouter

from makelele.api.routes import heartbeat, io, joker

api_router = APIRouter()
api_router.include_router(heartbeat.router, tags=["health"], prefix="/health")
api_router.include_router(joker.router, tags=["joker"], prefix="/v1")
api_router.include_router(io.router, tags=["upload"], prefix="/v1")
