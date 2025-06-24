import os
from sqlalchemy.orm import Session
from .crud import SessionLocal
from .models import User

def create_admin_from_env() -> None:
    """Create an initial admin user if INIT_ADMIN and INIT_ADMIN_PASSWORD are set."""
    email = os.getenv("INIT_ADMIN")
    password = os.getenv("INIT_ADMIN_PASSWORD")

    if not email or not password:
        print("❌ Missing INIT_ADMIN or INIT_ADMIN_PASSWORD")
        return

    db: Session = SessionLocal()
    try:
        existing = db.query(User).filter(User.email == email).first()
        if not existing:
            admin = User(
                first_name="Admin",
                last_name="User",
                email=email,
                password=password,
            )
            db.add(admin)
            db.commit()
            print(f"✅ Admin created: {email}")
        else:
            print(f"ℹ️ Admin already exists: {email}")
    except Exception as e:
        print(f"❌ Failed to create admin: {e}")
    finally:
        db.close()