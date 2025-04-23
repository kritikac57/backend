from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime
from app.utils.constants import FoodStatus

class FoodEntry(Base):
    __tablename__ = "food_entries"

    id = Column(Integer, primary_key=True, index=True)
    food_type = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    expiry_date = Column(DateTime, nullable=False)
    donor_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String, default=FoodStatus.AVAILABLE)
    created_at = Column(DateTime, default=datetime.utcnow)

    donor = relationship("User", back_populates="food_entries")