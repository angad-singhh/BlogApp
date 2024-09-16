def decode_comment(doc) -> dict:
    return {
        "comment_id": str(doc["_id"]),
        "content": doc["content"],
        "date": doc["date"],
        "user_id": doc["user_id"],
        "blog_id": doc["blog_id"],
    }


def decode_comments(docs) -> list:
    return [decode_comment(doc) for doc in docs]
