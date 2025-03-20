from sqlalchemy.orm import Session
from app.repositories.animal_repo import createAnimal
from app.schemas.animal import AnimalCreate

def add_user(db: Session, animal: AnimalCreate):
    return createAnimal(db, animal)