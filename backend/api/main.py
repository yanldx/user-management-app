from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from init_admin import create_admin_from_env

app = FastAPI()

# Configuration du CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # à restreindre selon le besoin (ex: ["http://localhost:3000"])
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import de tes routes
from api.app import users  # exemple
app.include_router(users.router)


@app.on_event("startup")
def startup_admin() -> None:
    """Create the initial admin user if required."""
    create_admin_from_env()
