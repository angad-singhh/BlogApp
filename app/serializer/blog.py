def decode_blog(doc) -> dict:
    return {
        "_id": str(doc["_id"]),
        "title": doc["title"],
        "description": doc["description"],
        "author": doc["author"],
        "content": doc["content"],
        "tags": doc["tags"],
        "date": doc["date"],
    }


def decode_blogs(docs) -> list:
    return [decode_blog(doc) for doc in docs]
