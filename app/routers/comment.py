from fastapi import APIRouter, HTTPException
from ..models.blog import Comments
import datetime
from ..config.db_config import comment_collection
from ..serializer.comments import decode_comments

router = APIRouter(prefix="/comment")


@router.get("/all/{blog_id}")
def get_all_comments(blog_id: str):
    all_comments = comment_collection.find({"blog_id": blog_id})
    data = decode_comments(all_comments)
    if not data:
        raise HTTPException(404, {"message": "No comments found on this post"})

    return {
        "status": 200,
        "message": "comments fetched successfully",
        "blog id": blog_id,
        "Comments": data,
    }


@router.post("/{blog_id}")
def create_comment(blog_id: str, comment: Comments):
    new_comment = comment.model_dump()
    curr_date = datetime.date.today()
    new_comment["date"] = str(curr_date)
    new_comment["blog_id"] = blog_id

    doc = comment_collection.insert_one(new_comment)
    doc_id = str(doc.inserted_id)
    return {"status": "Success", "comment_id": doc_id}
