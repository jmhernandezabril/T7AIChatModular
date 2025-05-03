# modules/db_manager.py
import os
import sqlite3
from config import DB_PATH, DB_ENGINE
from modules.doc_manager import documentar_sql


def connect_db():
    """Devuelve una conexión según el motor configurado: SQLite."""
    engine = DB_ENGINE.lower()
    if engine == "sqlite":
        folder = os.path.dirname(DB_PATH)
        if folder and not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)
        return sqlite3.connect(DB_PATH)
    else:
        raise ValueError(f"Motor de base de datos no soportado: {engine}")


def execute_sql(sql: str, usuario: str = "t7AI") -> dict:
    """
    Ejecuta sentencias DDL (CREATE, ALTER, DROP), documenta la acción
    y devuelve dict con {success: bool, message: str}.
    """
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()

        tipo = sql.strip().split()[0].upper()
        documentar_sql(sql, tipo=tipo, usuario=usuario)

        return {"success": True, "message": "SQL ejecutado correctamente."}
    except Exception as e:
        return {"success": False, "message": f"Error ejecutando SQL: {e}"}


def query_sql(sql: str) -> dict:
    """
    Ejecuta consultas SELECT y devuelve resultados como {columns: [...], rows: [...]}.
    """
    conn = None
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(sql)
        cols = [c[0] for c in cur.description]
        rows = cur.fetchall()
        conn.close()

        return {"columns": cols, "rows": [dict(zip(cols, r)) for r in rows]}
    except Exception as e:
        if conn:
            conn.close()
        raise


def create_table_if_not_exists(sql_create: str, table_name: str, usuario: str = "t7AI") -> dict:
    """
    Verifica existencia de la tabla y crea solo si no existe (case-insensitive).
    """
    # Comprobar si ya existe ignorando mayúsculas/minúsculas
    check = query_sql(
        f"SELECT name FROM sqlite_master WHERE type='table' "
        f"AND lower(name) = lower('{table_name}');"
    )
    if check.get("rows"):
        return {"success": True, "message": f"La tabla '{table_name}' ya existe."}

    # Si no existe, ejecutar la creación
    return execute_sql(sql_create, usuario)