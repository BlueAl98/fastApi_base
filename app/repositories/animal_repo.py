from sqlalchemy.orm import Session
from app.models.animal import Animal
from app.schemas.animal import AnimalCreate, AnimalOut

def createAnimal(db: Session, animal: AnimalCreate):
    db_animal = Animal(name = animal.name)
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)
    return db_animal