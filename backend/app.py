"""
The entrypoint point of backend app. All configurations are here
"""
import os
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1 import router
from core.auto_migrate import run_migrations
from dotenv import load_dotenv
from contextlib import asynccontextmanager


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("uvicorn.access")
logger.setLevel(logging.INFO)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # run_migrations()
    yield


load_dotenv()

CLIENT_PORT = os.getenv('CLIENT_PORT')

app = FastAPI(lifespan=lifespan)
app.include_router(router, prefix='/v1', tags=['API version 1'])

origins = [
    f'http://127.0.0.1:{CLIENT_PORT}',
    f'https://127.0.0.1:{CLIENT_PORT}',
    f'http://localhost:{CLIENT_PORT}',
    f'https://localhost:{CLIENT_PORT}',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
