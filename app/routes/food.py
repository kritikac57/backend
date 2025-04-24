from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.food import FoodEntry
from app.schemas.schemas import FoodCreate
from app.database import get_db
from app.utils.security import get_current_user
from app.models.user import User  # Add this import


router = APIRouter()


@router.post("/food-entries")
async def create_food_entry(
        food: FoodCreate,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    if current_user.role not in [UserRole.ADMIN, UserRole.USER]:
        raise HTTPException(status_code=403, detail="Not authorized to create food entries")

    new_food = FoodEntry(
        food_type=food.food_type,
        quantity=food.quantity,
        expiry_date=food.expiry_date,
        donor_id=current_user.id
    )
    db.add(new_food)
    db.commit()
    return {"message": "Food entry created successfully"}


@router.get("/food-stats")
async def get_food_stats(db: Session = Depends(get_db)):
    stats = {
        "available": db.query(FoodEntry).filter(FoodEntry.status == "available").count(),
        "in_transit": db.query(FoodEntry).filter(FoodEntry.status == "in-transit").count(),
        "delivered": db.query(FoodEntry).filter(FoodEntry.status == "delivered").count()
    }
    return stats