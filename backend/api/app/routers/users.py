from fastapi import APIRouter, HTTPException
from typing import List
from app import crud, schemas

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate):
    db_user = crud.create_user(user)
    return db_user

@router.get("/", response_model=List[schemas.UserOut])
def read_users():
    return crud.get_users()

@router.delete("/{user_id}")
def delete_user(user_id: int):
    success = crud.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted"}
    