import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()  # carga las variables definidas en el archivo .env


def get_db_connection():
    """Crea y retorna una conexión a la base de datos MySQL."""
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )