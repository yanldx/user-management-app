import os
from sqlalchemy.orm import Session
from app.crud import SessionLocal
from app.models import User


def create_admin_from_env() -> None:
    """Create an initial admin user if INIT_ADMIN is provided."""
    creds = os.getenv("INIT_ADMIN")
    if not creds:
        return
    parts = [p.strip() for p in creds.split(",")]
    if len(parts) != 4:
        # Invalid format; expected First,Last,email,password
        return
    first, last, email, password = parts
    db: Session = SessionLocal()
    try:
        existing = db.query(User).filter(User.email == email).first()
        if not existing:
            admin = User(
                first_name=first,
                last_name=last,
                email=email,
                password=password,
            )
            db.add(admin)
            db.commit()
    finally:
        db.close()
