from typing import Annotated
from fastapi import APIRouter, HTTPException
from ..models.user import User
from ..config.db_config import user_collection
from ..serializer.user import decode_user, decode_users

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/register")
def register_user(user: User):
    user_dict = user.model_dump()
    if user_collection.find_one({"email": user_dict["email"]}):
        raise HTTPException(status_code=400, detail="Email Id already registered")
    else:
        doc = user_collection.insert_one(user_dict)
        doc_id = str(doc.inserted_id)

    return {"status": "Success", "user_id": doc_id}


@router.get("/details/{user_id}")
def get_user_details(user_id: str):
    user_data = user_collection.find_one({"user_id": user_id})
    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"User_data": decode_user(user_data)}


@router.get("/all")
def get_all_users():
    docs = user_collection.find()
    if docs is None:
        raise HTTPException(status_code=404, detail="No Users found")

    data = decode_users(docs)

    return {"Users": data}
