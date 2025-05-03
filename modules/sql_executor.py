# modules/sql_executor.py

from modules.db_manager import execute_sql, query_sql

def ejecutar_sql_manual(sql_texto, usuario):
    """
    Ejecuta comandos DDL o DML y devuelve respuesta estructurada.
    """
    try:
        res = execute_sql(sql_texto, usuario=usuario)
        if not res.get("success", True):
            return {"error": f"❌ {res['message']}"}
        return {"success": f"⚡ {res['message']}"}
    except Exception as e:
        return {"error": f"❌ Error ejecutando SQL: {e}"}

def ejecutar_consulta_select(sql_texto):
    """
    Ejecuta un SELECT y devuelve resultados como DataFrame y metadatos.
    Si pandas (y numpy) no está disponible, devuelve el listado de filas.
    """
    try:
        result = query_sql(sql_texto)
        # Importación perezosa de pandas
        import pandas as pd
        df = pd.DataFrame(result["rows"], columns=result["columns"])
        return {
            "dataframe": df,
            "response": result["rows"],
            "columns": result["columns"]
        }
    except ImportError:
        # Fallback si no hay pandas/numpy
        result = query_sql(sql_texto)
        return {
            "dataframe": result["rows"],
            "response": result["rows"],
            "columns": result["columns"]
        }
    except Exception as e:
        return {"error": f"❌ Error en consulta: {e}"}