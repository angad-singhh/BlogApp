from typing import Annotated
from fastapi import APIRouter, HTTPException, Body
from ..models.blog import Likes
from ..config.db_config import likes_collection
from ..serializer.likes import decode_likes

router = APIRouter(prefix="/likes", tags=["Likes"])


@router.get("/total/{bog_id}")
def get_all_likes(blog_id: str):
    data = likes_collection.find_one({"blog_id": blog_id})
    if data is None:
        raise HTTPException(status_code=404, detail="Blog not found")

    decode_likes(data)
    total_likes = data.get("user_id")
    return {"Total likes": len(total_likes)}


@router.patch("/{blog_id}")
def like_a_blog(blog_id: str, user_id: Annotated[str, Body()]):

    data = likes_collection.find_one({"blog_id": blog_id})
    if data is None:
        like_dict = {"blog_id": blog_id, "user_id": [user_id]}
        doc = likes_collection.insert_one(like_dict)
        return {"Status": 201}

    like_data = decode_likes(data)
    user_data = like_data.get("user_id", [])

    if user_id in user_data:
        raise HTTPException(status_code=400, detail="User have already liked the Blog")

    user_data.append(user_id)

    res = likes_collection.find_one_and_update(
        {"blog_id": blog_id}, {"$set": {"user_id": user_data}}
    )

    if res is None:
        raise HTTPException(status_code=500, detail="Failed to update the likes")

    return {"status": "Success", "updated_likes": user_data}
