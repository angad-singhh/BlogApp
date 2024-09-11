from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    description: str
    author: str
    content: str
    tags: list[str]


class UpdateBlog(BaseModel):
    title: str | None = None
    description: str | None = None
    author: str | None = None
    content: str | None = None
    tags: list[str] | None = None
