from sqlalchemy.orm import Session
from app.models.product import Product  # Asegúrate de importar el modelo correcto
from app.schemas.product import ProductCreate

def create_product(db: Session, product: ProductCreate):
    # Convertimos ProductCreate (Pydantic) a Product (SQLAlchemy)
    db_product = Product(name=product.name, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session):
    return db.query(Product).all()