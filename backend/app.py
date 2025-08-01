"""
The entrypoint point of backend app. All configurations are here
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.v1 import router


app = FastAPI()
app.include_router(router, prefix='/v1', tags=['API version 1'])

origins = [
    'http://127.0.0.1:9001',
    'https://127.0.0.1:9001',
    'http://localhost:9001',
    'https://localhost:9001',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
