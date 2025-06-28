"""
The entrypoint point of backend app. All configurations are here
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

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
