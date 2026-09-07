import sqlite3

DB_PATH = "data/adoptaya.db"


def conectar():
    """Crea y retorna una conexión a la base de datos SQLite."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # permite acceder a las columnas por nombre
    return conn


def inicializar_db():
    """Crea la tabla de mascotas si no existe todavía."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mascotas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            tipo TEXT NOT NULL,
            edad TEXT NOT NULL,
            estado TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    