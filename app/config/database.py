import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

# Initialize MongoDB Async Client
client = AsyncIOMotorClient(MONGO_URI)

# Get the db name from URI or fallback to chat_app
db_name = "chat_app"
if "/" in MONGO_URI.rsplit("://", 1)[-1]:
    db_name = MONGO_URI.rsplit('/', 1)[-1].split('?')[0] or "chat_app"

db = client.get_database(db_name)

# Expose collections
user_collection = db.get_collection("users")
room_collection = db.get_collection("rooms")
message_collection = db.get_collection("messages")