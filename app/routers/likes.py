from typing import Annotated
from fastapi import APIRouter, HTTPException, body
from ..models.blog import Likes
from ..config.db_config import likes_collection
from ..serializer.likes import decode_likes

router = APIRouter(prefix="/likes")


@router.get("/total/{bog_id}")
def get_all_likes(blog_id: str):
    data = decode_likes(likes_collection.find_one({"blog_id": blog_id}))
    total_likes = data.get("user_data")
    return {"Total likes": len(total_likes)}


@router.patch("/{blog_id}")
def like_a_blog(blog_id: str, user_id: Annotated[str, body()]):

    data = likes_collection.find_one({"blog_id": blog_id})
    if not data:
        raise HTTPException(status_code=404, detail="Blog not found")

    like_data = decode_likes(data)
    user_data = like_data.get("user_id", [])

    if user_id in user_data:
        raise HTTPException(status_code=400, detail="User have already liked the Blog")
    else:
        user_data.append(user_id)

    likes_collection.find_one_and_update({"blog_id": blog_id}, {"$set": user_data})
