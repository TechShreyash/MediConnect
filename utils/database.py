import certifi
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Literal

from config import MONGODB_URL
from utils.logger import Logger

logger = Logger(__name__)

logger.info("Connecting to MongoDB")
DB = AsyncIOMotorClient(MONGODB_URL, tls=True, tlsCAFile=certifi.where())["MediConnect"]
logger.info("Connected to MongoDB")

ACCOUNTDB = DB["ACCOUNTDB"]

# For Login Signup


async def new_auth(email: str, data):
    if await ACCOUNTDB.find_one({"email": email}):
        return {"status": False, "message": "Email already exists"}
    print(data)
    await ACCOUNTDB.insert_one(data)
    return {"status": True, "message": "Signup Successful"}


async def check_auth(email: str, password: str):
    user = await ACCOUNTDB.find_one({"email": email})
    if user:
        if user["password"] == password:
            return {"status": True, "message": "Login Successful"}
        return {"status": False, "message": "Incorrect Password"}

    return {"status": False, "message": "Email not found"}


async def get_shops():
    shops = []
    async for shop in ACCOUNTDB.find({"type": "shop"}):
        shop.pop("_id")
        shop.pop("password")
        shops.append(shop)
    return {"status": True, "shops": shops}


# For Account Details


async def update_account(email: str, data: dict):
    await ACCOUNTDB.update_one({"email": email}, {"$set": data}, upsert=True)
    return {"status": True, "message": "Account Updated"}


async def get_account(email: str):
    account = await ACCOUNTDB.find_one({"email": email})
    if account:
        return {"status": True, "data": account}

    return {"status": False, "message": "Email not found"}


# for medicinces


async def add_medicine(email: str, data: dict):
    await ACCOUNTDB.update_one(
        {"email": email}, {"$push": {"medicine": data}}, upsert=True
    )
    return {"status": True, "message": "Medicine added"}


async def update_medicine(email: str, data: dict):
    await ACCOUNTDB.update_one(
        {"email": email, "medicine.id": data["id"]},
        {"$set": {"medicine.$": data}},
        upsert=True,
    )
    return {"status": True, "message": "Medicine updated"}


async def get_medicines(email: str):
    shop_data = await ACCOUNTDB.find_one({"email": email})
    if shop_data:
        if shop_data.get("medicine", []) != []:
            return {"status": True, "medicine": shop_data["medicine"]}
    return {"status": True, "medicine": []}

async def buy_medicines(email: str, medicine_id: int, sold_data: int):
    await ACCOUNTDB.update_one(
        {"email": email, "medicine.id": medicine_id["id"]},
        {"$inc":{'quantity': -sold_data,"soldunit":sold_data}}
    )