from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, User
from app.schemas import UserCreate
from app.config import get_database_url

# Build the database URL using environment variables
DATABASE_URL = get_database_url()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base.metadata.create_all(bind=engine)

def create_user(user: UserCreate):
    db = SessionLocal()
    db_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=user.password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return db_user

def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users

def delete_user(user_id: int):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        db.close()
        return False
    db.delete(user)
    db.commit()
    db.close()
    return True
    