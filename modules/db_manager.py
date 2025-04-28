# modules/db_manager.py

import os
import sqlite3
from config import DB_PATH
from modules.doc_manager import documentar_sql

def connect_db():
    """Crea carpeta data/ y abre conexión SQLite."""
    folder = os.path.dirname(DB_PATH)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    return sqlite3.connect(DB_PATH)

def execute_sql(sql, usuario="t7AI"):
    """
    Ejecuta sentencias DDL (CREATE, ALTER, DROP), documenta la acción
    y devuelve un dict con status y mensaje.
    """
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()

        # Documentar en MD
        tipo = sql.strip().split()[0].upper()
        documentar_sql(sql, tipo=tipo, usuario=usuario)

        return {"status": "ok", "message": "SQL ejecutado correctamente."}
    except Exception as e:
        return {"status": "error", "message": f"Error ejecutando SQL: {e}"}

def query_sql(sql):
    """
    Ejecuta consultas SELECT y devuelve resultados como lista de dicts.
    """
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(sql)
        cols = [c[0] for c in cur.description]
        data = cur.fetchall()
        conn.close()

        rows = [dict(zip(cols, row)) for row in data]
        return {"columns": cols, "rows": rows}
        
    except Exception as e:
        # En caso de error de consulta, se propaga para que el caller lo maneje
        raise