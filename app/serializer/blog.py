def decodeBlog(doc) -> dict:
    return {
        "_id": str(doc["_id"]),
        "title": doc["title"],
        "description": doc["description"],
        "author": doc["author"],
        "content": doc["content"],
        "tags": doc["tags"],
        "date": doc["date"],
    }


def decodeBlogs(docs) -> list:
    return [decodeBlog(doc) for doc in docs]
