# MODULO: data
# Gestión de conexión a la base de datos.
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Creación de la base de datos dentro de carpeta data/.
SQLALCHEMY_DATABASE_URL = "sqlite:///./data/dB.sqlite3"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_db_tables():
    from . import models

    Base.metadata.create_all(bind=engine)
