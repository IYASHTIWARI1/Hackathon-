import os
import json
from fastapi import FastAPI
app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Server is running!"}


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BANKS_FILE = os.path.join(BASE_DIR, "..", "whitelist", "banks.json")

with open(BANKS_FILE, "r") as f:
    banks_data = json.load(f)


print("Banks loaded:", banks_data.keys())   # ✅ console me output dega

app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Server is running!"}




import os
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

# local imports
from core.config import settings
from middlewares.headers import security_headers
from middlewares.ip_filter import ip_filter
from middlewares.limits import body_size_limit, concurrency_limit
from middlewares.timeout import TimeoutMiddleware
from routers import auth, users, upload
from core.error import global_exception_handler
from core.logging_config import setup_logging

# App create
app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Server is running!"}



# Logging
logger = setup_logging()
logger.info("Starting FastAPI app...")

# Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.middleware("http")(security_headers)
app.middleware("http")(ip_filter)
app.middleware("http")(body_size_limit)
app.middleware("http")(concurrency_limit)
app.add_middleware(TimeoutMiddleware, timeout=15)

# Routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(upload.router)

# Static files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "static"))
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Global error handler
app.add_exception_handler(Exception, global_exception_handler)

# Test route
@app.get("/ping")
def ping():
    return {"status": "ok"}

from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}
from fastapi import FastAPI
from routers import upload

app = FastAPI()

# routers
app.include_router(upload.router)

@app.get("/ping")
def ping():
    return {"status": "ok"}
@app.get("/banks")
def get_banks():
    return banks_data
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use ["http://localhost:3000"] for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Server is running!"}
from fastapi import FastAPI, UploadFile, File
import hashlib

app = FastAPI()

# Whitelist SHA256 set (aapke stored SHAs)
whitelist = {
      "d2a5372c6a0b5f34f4820a4ef7b1187c3bb7eab93c1baf22714de3e962f91a65"
      "9fcb34d02953f7a36fddf9b6d293b5f0a7eddfaf2a132f19bc44e1a5a52bdf99"
      "3e82b0b2e3cb7d244e4a532c7d9b46e2279cb09eac7fc84d2d7db3b21c6e1db8"
      "7a8f5f9a53c2c6efb5a0c7f3d1c4d92f8c9d8e5a2f3b7d0a4b6f7e9c8d1f2a3b"

    # aur bhi SHAs yahan add karo
}

def get_sha256(file_bytes: bytes) -> str:
    return hashlib.sha256(file_bytes).hexdigest()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_bytes = await file.read()
    sha256_hash = get_sha256(file_bytes)

    # Verdict check
    if sha256_hash in whitelist:
        verdict = "good"
    else:
        verdict = "bad"

    return {
        "filename": file.filename,
        "sha256": sha256_hash,
        "verdict": verdict,
        "message": "File uploaded safely (not executed)"
    }