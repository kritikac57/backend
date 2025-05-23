from pydantic import BaseModel, EmailStr, field_validator
from pydantic import ConfigDict
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
    name: str
    quantity: int
    expiry_date: datetime
    description: Optional[str] = None

    @field_validator('expiry_date')
    def validate_expiry(cls, v):
        if v < datetime.now():
            raise ValueError("Expiry date must be in the future")
        return v

class FoodEntry(FoodCreate):
    id: int
    donor_id: int
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)  # Replace orm_mode
