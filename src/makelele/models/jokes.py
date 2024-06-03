from pydantic import BaseModel


class Response(BaseModel):
    joke: str
