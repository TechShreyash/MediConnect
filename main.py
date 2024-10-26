from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from utils import database
from utils.logger import Logger

app = FastAPI()
logger = Logger(__name__)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"status": "Api Is Running"}