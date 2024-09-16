from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("MONGODB_URI")

if not uri:
    raise ValueError("MongoDB URI is not set in environment variables")

client = MongoClient(uri, server_api=ServerApi("1"))

db = client.blogsDB
blogs_collection = db["blogs"]
comment_collection = db["comments"]
likes_collection = db["likes"]
user_collection = db["users"]

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
