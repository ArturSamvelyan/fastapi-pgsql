import os
import time
import random
import string

from fastapi import FastAPI, Request, HTTPException
from loguru import logger

app = FastAPI()


@app.middleware("http")
async def log_request(request: Request, call_next):
    rid = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    start_time = time.time()

    logger.debug(
        "RID={rid} Request_Path={req_path}; User_IP={user_ip}; User-Agent={user_agent}; Start_Time={start_time}",
        rid=rid,
        req_path=request.url.path,
        user_ip=request.client.host,
        user_agent=request.headers['User-Agent'],
        start_time=f"{start_time} s",
    )

    response = await call_next(request)

    end_time = time.time()
    process_time = (end_time - start_time) * 1000

    logger.debug(
        "RID={rid} Request_Path={req_path}; User_IP={user_ip}; User-Agent={user_agent}; End_Time={end_time}; "
        "Completed_In={completed_in}",
        rid=rid,
        req_path=request.url.path,
        user_ip=request.client.host,
        user_agent=request.headers['User-Agent'],
        end_time=f"{end_time} s",
        completed_in='{0:.3f} ms'.format(process_time)
    )

    return response


@app.on_event("startup")
async def startup_event():
    logger_level = os.getenv(
        "LOGGER_LEVEL",
        default="DEBUG"
    )
    logger_filename = os.getenv(
        "LOGGER_FILENAME",
        default="debug.log"
    )
    logger.add(
        logger_filename,
        format="{time} {level} {message}",
        level=logger_level,
        rotation="100 MB"
    )


@app.get("/")
def index():
    return {"ping": "pong"}
