from typing import Literal

from fastapi import APIRouter, Depends
from starlette.requests import Request

from makelele.core import security
from makelele.models.jokes import Response

router = APIRouter()


@router.get(
    "/joke/{category}",
    response_model=Response,
    name="joke",
    dependencies=[
        Depends(security.validate_request),
    ],
)
def get_joke(
    request: Request,
    category: Literal["golf"],
) -> Response:
    """
    #### Retrieves a joke from data respository

    """

    joke: Response = request.app.state.joker.joke(category)

    return joke
