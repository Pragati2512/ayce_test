from typing import Optional
import requests
import uvicorn
import os
from datetime import datetime

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse
from src.db.db import ORM_Config
from src.routers.users import user_router
from fastapi import FastAPI

orm = ORM_Config()
orm.create_database_if_not_exists()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=["*"]
)

app.include_router(user_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}



if __name__ == '__main__':
    # Set the logging level of Uvicorn to WARNING
    # uvicorn_logger = logging.getLogger("uvicorn")
    # uvicorn_logger.setLevel(logging.WARNING)
    uvicorn.run(app, host="localhost", port=8000, log_level='debug')
