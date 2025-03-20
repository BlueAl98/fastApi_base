from sqlalchemy import Column, Integer, String
from app.core.db.session import Base

class Animal(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable= False)