from motor.motor_asyncio import AsyncIOMotorClient
from typing import Literal

from config import MONGODB_URL
from utils.logger import Logger

logger = Logger(__name__)

logger.info("Connecting to MongoDB")
DB = AsyncIOMotorClient(MONGODB_URL)["MediConnect"]
logger.info("Connected to MongoDB")

ACCOUNTDB = DB["ACCOUNTDB"]

# For Login Signup

async def new_auth(email: str, password: str,_type:Literal["shop","user"]):
    if await ACCOUNTDB.find_one({"email": email}):
        return {'status':False, 'message':"Email already exists"}
    
    await ACCOUNTDB.insert_one({"email": email, "password": password,"type":_type})
    return {'status':True, 'message':"Signup Successful"}

async def check_auth(email: str, password: str):
    user = await ACCOUNTDB.find_one({"email": email})
    if user:
        if user["password"] == password:
            return {'status':True, 'message':"Login Successful"}
        return {'status':False, 'message':"Incorrect Password"}
    
    return {'status':False, 'message':"Email not found"}


# For Account Details

async def update_account(email: str, data: dict):
    await ACCOUNTDB.update_one({"email": email}, {"$set": data})
    return {'status':True, 'message':"Account Updated"}

async def get_account(email: str):
    account = await ACCOUNTDB.find_one({"email": email})
    if account:
        return {'status':True, 'data':account}
    
    return {'status':False, 'message':"Email not found"}
