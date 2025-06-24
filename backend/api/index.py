from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from app.init_admin import create_admin_from_env
from app.routers import users

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Sécuriser plus tard
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)

@app.on_event("startup")
def startup_admin():
    create_admin_from_env()

handler = Mangum(app)
