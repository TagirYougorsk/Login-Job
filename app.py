from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from UserController import UserController
from UserController import UserController

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(UserController.create_router())

uvicorn.run(app)