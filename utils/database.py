from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGODB_URL
from utils.logger import Logger

logger = Logger(__name__)

logger.info("Connecting to MongoDB")
DB = AsyncIOMotorClient(MONGODB_URL)["MediConnect"]
logger.info("Connected to MongoDB")

AUTHDB = DB["AUTHDB"]
SHOPDB = DB["SHOPDB"]