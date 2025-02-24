from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.db.session import get_db
from app.services.user_service import add_user, list_users
from app.schemas.user import UserCreate, UserOut
from typing import List

router = APIRouter()

@router.post("/users/", response_model=UserOut)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return add_user(db, user)

@router.get("/users/", response_model=List[UserOut])
def get_users_endpoint(db: Session = Depends(get_db)):
    return list_users(db)

@router.get("/some/")
def get_users_endpoint():
    return {"message": "test parece que tenia razon alv siuu "}