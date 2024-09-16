from fastapi import APIRouter, HTTPException
from ..models.blog import Blog, UpdateBlog
import datetime
from bson import ObjectId
from ..config.db_config import blogs_collection
from ..serializer.blog import decode_blog, decode_blogs

router = APIRouter(prefix="/blogs", tags=["Blogs"])


@router.post("/create")
def create_blog(blog: Blog):
    new_blog = blog.model_dump()
    curr_date = datetime.date.today()
    new_blog["date"] = str(curr_date)
    doc = blogs_collection.insert_one(new_blog)
    doc_id = str(doc.inserted_id)
    return {"status": "Success", "_id": doc_id}


@router.get("/all")
def get_all_blogs():
    docs = blogs_collection.find()
    if docs is None:
        raise HTTPException(status_code=404, detail="No blogs found")
    decoded_data = decode_blogs(docs)
    return {"Status": "Success", "Blogs": decoded_data}


@router.get("/{_id}")
def get_blog_with_id(_id: str):
    doc = blogs_collection.find_one({"_id": ObjectId(_id)})
    decoded_data = decode_blog(doc)
    return {"Status": "Success", "Blog": decoded_data}


@router.patch("/update")
def update_blog(_id: str, doc: UpdateBlog):
    res = doc.model_dump(exclude_unset=True)
    blogs_collection.find_one_and_update({"_id": ObjectId(_id)}, {"$set": res})

    updated = blogs_collection.find_one({"_id": ObjectId(_id)})
    decoded_data = decode_blog(updated)

    return {"Status": "Success", "UpdatedBlog": decoded_data}


@router.delete("/delete")
def delete_blog(_id: str):
    blogs_collection.find_one_and_delete({"_id": ObjectId(_id)})
    return {"Status": "Deleted successfully"}
