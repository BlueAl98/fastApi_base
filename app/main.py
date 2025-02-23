from fastapi import FastAPI
from app.core.db.session import engine, Base
from app.api.v1.endpoints import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mi API con FastAPI y MariaDB")

# Crear las tablas en la BD
app.include_router(router, prefix="/api/v1")
