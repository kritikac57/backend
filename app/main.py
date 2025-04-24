import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from app.routes import auth, food, users
from app.database import engine
from app.models import user, food as food_model  # Rename this import to avoid confusion


app = FastAPI()

# Create database tables
user.Base.metadata.create_all(bind=engine)
food_model.Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth.router, prefix="/api/v1")
app.include_router(food.router, prefix="/api/v1")  # This should now work
app.include_router(users.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "ReRasooi Backend Service"}