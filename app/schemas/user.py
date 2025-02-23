from pydantic import BaseModel, EmailStr

# Esquema para crear usuario
class UserCreate(BaseModel):
    name: str
    email: str  # Usa EmailStr para validación de correo electrónico

# Esquema para leer usuario
class UserOut(UserCreate):
    id: int

    class Config:
        orm_mode = True  # Esto le permite a Pydantic usar datos del ORM (SQLAlchemy por ejemplo)
