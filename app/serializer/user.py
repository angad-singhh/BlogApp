def decode_user(doc) -> dict:
    return {"name": doc["name"], "email": doc["email"]}


def decode_users(docs) -> list:
    return [decode_user(doc) for doc in docs]
