from fastapi import APIRouter
from starlette.requests import Request

from makelele.core.config import APP_NAME
from makelele.models.home import Home

router = APIRouter()


@router.get("/", response_model=Home, name="home")
def get_home(
    request: Request,
) -> Home:
    categories = request.app.state.joker.joker["jokes"].keys()
    categories_names = ",".join(category for category in categories)

    home = Home(
        name=APP_NAME,
        message=f"There are {len(categories)}: {categories_names}. Enjoy 🍺",
    )

    return home
