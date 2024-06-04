from typing import Annotated

from fastapi import APIRouter, Depends, File, UploadFile

from makelele.core import security
from makelele.services import io

router = APIRouter()


@router.post(
    "/jokes",
    dependencies=[Depends(security.validate_request)],
)
async def create_upload_file(
    file: Annotated[UploadFile, File(description="A toml file with custom jokes")],
):
    if not file:
        return {"message": "No upload file sent"}
    else:
        contents = await file.read()
        io.save(contents=contents)

        return {"message": f"{file.filename} upload successful"}
