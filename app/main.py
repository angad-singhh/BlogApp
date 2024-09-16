from fastapi import FastAPI
from .routers import blogs, comment

app = FastAPI()

app.include_router(blogs.router)
app.include_router(comment.router)
