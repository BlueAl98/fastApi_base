from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.db.session import get_db
from app.schemas.user import UserCreate, UserOut
from app.schemas.animal import AnimalOut, AnimalCreate
from app.services.user_service import add_user, list_users
from app.services.animal_service import createAnimal


router = APIRouter()


@router.post("/users/", response_model=UserOut)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return add_user(db, user)


@router.get("/users/", response_model=List[UserOut])
def get_users_endpoint(db: Session = Depends(get_db)):
    return list_users(db)

@router.post("/animals/", response_model= AnimalOut)
def createAnimal_endpoint(animal: AnimalCreate, db:Session = Depends(get_db)):
    return createAnimal(db, animal= animal)
