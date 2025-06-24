from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from api.app.init_admin import create_admin_from_env
from api.app.routers import users

app = FastAPI()

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # À sécuriser plus tard
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(users.router)

# Init admin au démarrage
@app.on_event("startup")
def startup_admin():
    create_admin_from_env()

# Handler pour Vercel
handler = Mangum(app)
