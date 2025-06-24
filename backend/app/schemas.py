from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr

    model_config = {
        "from_attributes": True
    }
