from pydantic import BaseModel


class Home(BaseModel):
    name: str
    message: str
