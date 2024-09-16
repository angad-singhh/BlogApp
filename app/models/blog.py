from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    authorID: str
    content: str
    tags: list[str]


class UpdateBlog(BaseModel):
    title: str | None = None
    author_id: str | None = None
    content: str | None = None
    tags: list[str] | None = None


class Comments(BaseModel):
    content: str
    user_id: str


class Likes(BaseModel):
    user_id: list[str] = []
    blog_id: str
