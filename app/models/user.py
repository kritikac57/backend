from sqlalchemy import Column, Integer, String, Boolean, Enum
from app.database import Base
from app.utils.constants import UserRole
# Fix: Add missing imports
from sqlalchemy.orm import relationship  # Add this in both files

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    role = Column(Enum(UserRole), default=UserRole.USER)
    is_active = Column(Boolean, default=True)

    # Add relationship for food donations
    food_entries = relationship("FoodEntry", back_populates="donor")