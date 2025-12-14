from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()


MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("MONGO_DB_NAME", "sf6")

client = MongoClient(
    MONGO_URI,
    server_api=ServerApi("1")
)

db = client[DB_NAME]

def ping_db():
    try:
        client.admin.command("ping")
        return True
    except Exception as e:
        print(e)
        return False
