from fastapi import FastAPI
from .routers import blogs, comment, likes, user

app = FastAPI()

app.include_router(blogs.router)
app.include_router(comment.router)
app.include_router(likes.router)
app.include_router(user.router)


@app.get("/")
def home():
    return {"Status": 200, "Message": "Welcome to blogs API"}
