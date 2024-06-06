from fastapi import APIRouter
from starlette.requests import Request

from makelele.core.config import APP_NAME
from makelele.models.home import Home

router = APIRouter()


@router.get("/", response_model=Home, name="home")
def get_home(
    request: Request,
) -> Home:
    categories = request.app.state.joker.joker["jokes"]
    categories_names = (name for name in categories.keys())
    categories_details = ",".join(
        f"{name}({len(categories[name])})" for name in categories_names
    )

    home = Home(
        name=APP_NAME,
        message=f"Enjoy 🍺: number of categories = {len(categories)!r} : names = [{categories_details}].",
    )

    return home
