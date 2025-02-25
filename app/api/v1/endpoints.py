from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.db.session import get_db
from app.services.user_service import add_user, list_users
from app.services.product_service import list_products, add_product
from app.schemas.user import UserCreate, UserOut
from app.schemas.product import ProductCreate, ProductOut
from typing import List

router = APIRouter()

@router.post("/users/", response_model=UserOut)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return add_user(db, user)

@router.get("/users/", response_model=List[UserOut])
def get_users_endpoint(db: Session = Depends(get_db)):
    return list_users(db)

@router.post("/products/", response_model=ProductOut)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return add_product(db, product)

@router.get("/products/", response_model=List[ProductOut])
def get_products(db: Session = Depends(get_db)):
    return list_products(db)