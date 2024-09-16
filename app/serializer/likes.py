def decode_likes(doc) -> dict:
    return {
        "likes_id": str(doc["_id"]),
        "blog_id": doc["blog_id"],
        "user_id": doc["user_id"],
    }
