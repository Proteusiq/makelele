from io import BytesIO
from typing import Annotated

from fastapi import APIRouter, Depends, File, UploadFile, responses

from makelele.core import security
from makelele.core.config import (
    DEFAULT_JOKES_PATH,
)
from makelele.models.jokes import Jokes as JokesModel
from makelele.services import io

router = APIRouter(
    dependencies=[Depends(security.validate_request)],
)


@router.post(
    "/joker",
)
async def create_upload_file(
    file: Annotated[UploadFile, File(description="A toml file with custom jokes")],
):
    if not file:
        return {"message": "No upload file sent"}
    else:
        contents = await file.read()

        # load contents for validation
        jokes_contents = io.load(contents)

        # validate before saving
        JokesModel(**jokes_contents)

        # save only if valid
        io.save(contents=contents, path=DEFAULT_JOKES_PATH)

        return {"message": f"{file.filename} upload successful"}


@router.get(
    "/joker",
    response_class=responses.StreamingResponse,
)
async def download_file():
    response = responses.StreamingResponse(
        BytesIO(DEFAULT_JOKES_PATH.read_bytes()), media_type="text/toml"
    )
    response.headers["Content-Disposition"] = "attachment; filename=joker.toml"

    return response
