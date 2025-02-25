from sqlalchemy.orm import Session

from app.repositories.product_repo import create_product, get_products
from app.schemas.product import ProductCreate

def add_product(db: Session, product: ProductCreate):
    return create_product(db, product)

def list_products(db: Session):
    return get_products(db)