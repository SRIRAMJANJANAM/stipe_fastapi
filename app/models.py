from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_DETAILS = os.getenv("MONGO_DETAILS", "mongodb://localhost:27017")

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.ecommerce

product_collection = database.get_collection("products")
cart_collection = database.get_collection("carts")


#uvicorn app.main:app --reload
