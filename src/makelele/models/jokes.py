from pydantic import BaseModel


class Response(BaseModel):
    joke: str


class Joke(BaseModel):
    golf: list[str]


class Jokes(BaseModel):
    jokes: Joke
