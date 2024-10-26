from motor.motor_asyncio import AsyncIOMotorClient
from typing import Literal

from config import MONGODB_URL
from utils.logger import Logger

logger = Logger(__name__)

logger.info("Connecting to MongoDB")
DB = AsyncIOMotorClient(MONGODB_URL)["MediConnect"]
logger.info("Connected to MongoDB")

AUTHDB = DB["AUTHDB"]

# For Login Signup

async def new_auth(email: str, password: str,_type:Literal["shop","user"]):
    if await AUTHDB.find_one({"email": email}):
        return {'status':False, 'message':"Email already exists"}
    
    await AUTHDB.insert_one({"email": email, "password": password,"type":_type})
    return {'status':True, 'message':"Signup Successful"}

async def check_auth(email: str, password: str):
    user = await AUTHDB.find_one({"email": email})
    if user:
        if user["password"] == password:
            return {'status':True, 'message':"Login Successful"}
        return {'status':False, 'message':"Incorrect Password"}
    
    return {'status':False, 'message':"Email not found"}
