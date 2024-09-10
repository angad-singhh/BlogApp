from fastapi import APIRouter
from ..models.models import Blog

router = APIRouter()


@router.get("/")
def root():
    return {"Hi from root"}


@router.post("/createBlog")
def create_blog(blog: Blog):
    new_blog = blog.model_dump()
    return new_blog
