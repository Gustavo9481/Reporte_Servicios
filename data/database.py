# MODULO: data/database.py
""" Gestión de conexión a la base de datos. """

from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

import os
from pathlib import Path

# Creación y ubicación de la base de datos dentro de carpeta data/.
DB_PATH = Path("./data/dB.sqlite3")
DOMAIN_DIR = DB_PATH.parent

# Comprobación de la existencia del directorio.
if not DOMAIN_DIR.exists():
    os.makedirs(DOMAIN_DIR, exist_ok=True)

SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# .. .................................................... función -> get_db ..󰌠
def get_db() -> Generator:
    """ Gestiona la conexión a DB. """

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# .. .......................................... función -> create_db_tables ..󰌠
def create_db_tables() -> None:
    """ Crea las tablas en la DB. """

    from . import models

    Base.metadata.create_all(bind=engine)
