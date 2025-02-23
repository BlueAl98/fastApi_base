from sqlalchemy.orm import Session
from app.repositories.user_repo import create_user, get_users
from app.schemas.user import UserCreate

def add_user(db: Session, user: UserCreate):
    return create_user(db, user)

def list_users(db: Session):
    return get_users(db)