# modules/sql_executor.py

from modules.db_manager import execute_sql, query_sql
import config
import pandas as pd

def ejecutar_sql_manual(sql_texto, usuario):
    """Ejecuta comandos DDL o DML y devuelve respuesta estructurada.
    La documentación ya está integrada en execute_sql si corresponde (DDL)."""
    try:
        res = execute_sql(sql_texto, usuario=usuario)
        if not res.get("success", True):
            return {"error": f"❌ {res['message']}"}
        return {"success": f"⚡ {res['message']}"}
    except Exception as e:
        return {"error": f"❌ Error ejecutando SQL: {e}"}

def ejecutar_consulta_select(sql_texto):
    """Ejecuta un SELECT y devuelve resultados como DataFrame y metadatos."""
    try:
        result = query_sql(sql_texto)
        df = pd.DataFrame(result["rows"], columns=result["columns"])
        return {
            "dataframe": df,
            "response": result["rows"],
            "columns": result["columns"]
        }
    except Exception as e:
        return {"error": f"❌ Error en consulta: {e}"}