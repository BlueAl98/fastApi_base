from fastapi import FastAPI
from app.core.db.session import engine, Base
from app.api.v1.endpoints import router
from app.core.middleware.middleware import app_id_middleware

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mi API con FastAPI y MariaDB")

app.middleware("http")(app_id_middleware)


# Crear las tablas en la BD
app.include_router(router, prefix="/api/v1")
