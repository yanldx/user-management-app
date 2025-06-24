from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from init_admin import create_admin_from_env
from routers.users import router as users_router

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(users_router)

@app.on_event("startup")
def startup_admin():
    print("🚀 Running admin init script...")
    create_admin_from_env()
    