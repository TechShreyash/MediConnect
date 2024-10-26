from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import Literal
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

# signup and login
async def api_auth(request: Request):
    data: dict = await request.json()
    logger.info(f"Auth Data: {data}")

    request_type: Literal["new_auth", "check_auth"] = data.get("request_type")
    email: str = data.get("email")
    password: str = data.get("password")

    if request_type == "new_auth":
        results = await database.new_auth(email, password)
    elif request_type == "check_auth":
        results = await database.check_auth(email, password)
    else:
        results = False, "Invalid Request Type"

    return results

@app.post("/api/medicine")
async def api_auth(request: Request):
    data: dict = await request.json()
    logger.info(f"Med_data: {data}")

    request_type: Literal["update_med", "get_med","add_med"] = data.get('request_type')
    email: str = data.get("email")
    Med_data: dict = data.get("Med_data")

    if request_type == "add_med":
        results = await database.add_medicine(email, Med_data)
        
    elif request_type == "update_med":
        results = await database.update_medicine(email, Med_data)
    elif request_type == "get_med":
        results = await database.add_medicine(email)

    return results
