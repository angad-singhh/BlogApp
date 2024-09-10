from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    description: str
    author: str
    content: str
    tags: list
