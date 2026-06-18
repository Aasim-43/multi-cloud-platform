from fastapi import FastAPI

from app.database import engine
from app.models.user import User
from app.routes.auth import router as auth_router

app = FastAPI()

User.metadata.create_all(bind=engine)

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)

@app.get("/")
def root():
    return {"message": "Multi Cloud Platform Running"}