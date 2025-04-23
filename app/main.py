from fastapi import FastAPI
from app.routes import auth, food, users
from app.database import engine
from app.models import user, food

# Create tables
user.Base.metadata.create_all(bind=engine)
food.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(auth.router, prefix="/api/v1")
app.include_router(food.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "ReRasooi Backend Service"}