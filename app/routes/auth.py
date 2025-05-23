from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.schemas.schemas import UserCreate, Token
from app.models.user import User
from app.utils.security import get_password_hash, create_access_token
from app.database import get_db
# Add missing imports
from fastapi.security import OAuth2PasswordRequestForm
from app.utils.security import get_current_user
router = APIRouter()


@router.post("/register", response_model=Token)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(user.password)
    new_user = User(
        email=user.email,
        hashed_password=hashed_password,
        full_name=user.full_name,
        role=user.role
    )
    db.add(new_user)
    db.commit()

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


# app/routes/auth.py
@router.post("/login", response_model=Token)
async def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
):
    # Add proper error handling
    try:
        user = db.query(User).filter(User.email == form_data.username).first()
        if not user or not verify_password(form_data.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        return {"access_token": create_access_token({"sub": user.email}), "token_type": "bearer"}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Database error")