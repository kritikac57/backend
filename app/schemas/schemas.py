from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from enum import Enum

class UserRole(str, Enum):
    admin = "admin"
    ngo = "ngo"
    user = "user"

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    role: UserRole = UserRole.user

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    id: int
    is_active: bool

    model_config = ConfigDict(from_attributes=True)  # Replace orm_mode

class FoodCreate(BaseModel):
    food_type: str
    quantity: int
    expiry_date: datetime

class FoodEntry(FoodCreate):
    id: int
    donor_id: int
    status: str
    created_at: datetime

    class Config:
        orm_mode = True