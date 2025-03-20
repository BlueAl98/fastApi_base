from pydantic import BaseModel

class AnimalCreate(BaseModel):
    name: str


class AnimalOut(AnimalCreate):
    id: int

    class Config:
        from_attributes = True

