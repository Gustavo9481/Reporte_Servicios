# Script para crear la base de datos SQLite.
from data.database import create_db_tables

if __name__ == "__main__":
    create_db_tables()
    print("Database created successfully")
