import os
import json
from fastapi import FastAPI

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BANKS_FILE = os.path.join(BASE_DIR, "..", "whitelist", "banks.json")

with open(BANKS_FILE, "r") as f:
    banks_data = json.load(f)


print("Banks loaded:", banks_data.keys())   # ✅ console me output dega

app = FastAPI()
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


