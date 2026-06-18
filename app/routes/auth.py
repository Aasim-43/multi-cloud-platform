from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.schemas.user import *
from app.models.user import User
from app.database import SessionLocal
from app.auth.password import *
from app.auth.jwt_handler import *

router = APIRouter()

@router.post("/register")
def register(user:UserCreate):

    db = SessionLocal()

    hashed = hash_password(
        user.password
    )

    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed
    )

    db.add(new_user)

    db.commit()

    return {"message":"User Created"}


@router.post("/login")
def login(user:UserLogin):

    db = SessionLocal()

    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user:

        return {"error":"User not found"}

    if not verify_password(
        user.password,
        db_user.password
    ):

        return {"error":"Wrong password"}

    token = create_token(
        {
            "email":db_user.email,
            "role":db_user.role
        }
    )

    return {
        "access_token":token
    }