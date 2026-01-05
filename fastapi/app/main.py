from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time
import sys

from . import models
from .database import engine
from .routers import auth, users, items

# 2.1 Check if running in a virtual environment
if sys.prefix == sys.base_prefix:
    print("WARNING: You are NOT running in a virtual environment. Please activate it!")

# 3.7 Database Integration (Create tables)
# 3.1 App initialization
models.Base.metadata.create_all(bind=engine)

# 3.1 FastAPI App Initialisation
app = FastAPI(
    title="FastAPI Project",
    description="A project to demonstrate FastAPI features",
    version="1.0.0",
)

# 3.6 Middleware ( CORS )
origins = [
    "http://localhost",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3.6 Logging middleware / Request tracing
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    print(f"Request: {request.method} {request.url} - Duration: {process_time:.4f}s")
    return response

# 3.1 Path operations (GET)
@app.get("/")
def read_root():
    return {"Hello": "FastAPI"}

# Include routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(items.router)
