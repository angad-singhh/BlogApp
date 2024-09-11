from fastapi import APIRouter
from ..models.blog import Blog, UpdateBlog
import datetime
from bson import ObjectId
from ..config.db_config import blogs_collection
from ..serializer.blog import decodeBlog, decodeBlogs

router = APIRouter()


@router.get("/")
def root():
    return {"Hi from root"}


@router.post("/blogs/create")
def create_blog(blog: Blog):
    new_blog = blog.model_dump()
    curr_date = datetime.date.today()
    new_blog["date"] = str(curr_date)
    doc = blogs_collection.insert_one(new_blog)
    doc_id = str(doc.inserted_id)
    return {"status": "Success", "_id": doc_id}


@router.get("/blogs/all")
def get_all_blogs():
    docs = blogs_collection.find()
    decoded_data = decodeBlogs(docs)
    return {"Status": "Success", "Blogs": decoded_data}


@router.get("/blogs/{_id}")
def get_blog_with_id(_id: str):
    doc = blogs_collection.find_one({"_id": ObjectId(_id)})
    decoded_data = decodeBlog(doc)
    return {"Status": "Success", "Blog": decoded_data}


@router.patch("/blogs/update")
def update_blog(_id: str, doc: UpdateBlog):
    res = doc.model_dump(exclude_unset=True)
    blogs_collection.find_one_and_update({"_id": ObjectId(_id)}, {"$set": res})

    updated = blogs_collection.find_one({"_id": ObjectId(_id)})
    decoded_data = decodeBlog(updated)

    return {"Status": "Success", "UpdatedBlog": decoded_data}


@router.delete("/blogs/delete")
def delete_blog(_id: str):
    blogs_collection.find_one_and_delete({"_id": ObjectId(_id)})
    return {"Status": "Deleted successfully"}
