import os
from datetime import datetime
import sqlparse
from config import BASE_DATOS_DOC_PATH

def documentar_sql(sql_texto, tipo="CREATE", usuario="t7AI"):
    """Documenta cambios estructurales en la base de datos usando Frontmatter YAML."""
    # 1) Formatear y limpiar comentarios
    sql = sqlparse.format(
        sql_texto,
        reindent=True,
        keyword_case='upper',
        strip_comments=True
    ).strip()
    if not sql:
        return

    # 2) Reestructurar el cuerpo para legibilidad por columnas
    if "(" in sql and ")" in sql:
        head, rest = sql.split("(", 1)
        body, tail = rest.rsplit(")", 1)
        cols = [c.strip() for c in body.split(",")]
        pretty_body = ",\n  ".join(cols)
        sql = f"{head}(\n  {pretty_body}\n){tail}".strip()

    accion = sql.split()[0].upper()
    if accion not in ("CREATE", "ALTER", "DROP"):
        return

    # Extraer nombre de la tabla
    nombre_tabla = extraer_nombre_tabla(sql)
    if not nombre_tabla:
        return

    # Asegurar existencia del directorio y archivo MD
    os.makedirs(os.path.dirname(BASE_DATOS_DOC_PATH), exist_ok=True)
    if not os.path.exists(BASE_DATOS_DOC_PATH):
        with open(BASE_DATOS_DOC_PATH, "w", encoding="utf-8") as f:
            f.write("# Registro de Cambios en Base de Datos\n\n")

    # Leer contenido actual
    with open(BASE_DATOS_DOC_PATH, "r", encoding="utf-8") as f:
        contenido = f.read()

    # Generar Frontmatter YAML
    fecha = datetime.now().strftime("%Y-%m-%d")
    hora  = datetime.now().strftime("%H:%M")
    yaml_block = (
        "```yaml\n"
        f"table: {nombre_tabla}\n"
        f"date: {fecha}\n"
        f"time: {hora}\n"
        f"user: {usuario}\n"
        f"action: {accion}\n"
        "sql: |\n"
    )
    for line in sql.splitlines():
        yaml_block += f"  {line}\n"
    yaml_block += "```\n\n"

    # Anexar el bloque al final (solo cambios de esquema)
    contenido += yaml_block

    # Guardar MD actualizado
    with open(BASE_DATOS_DOC_PATH, "w", encoding="utf-8") as f:
        f.write(contenido)


def extraer_nombre_tabla(sql):
    """Extrae el nombre de la tabla desde el SQL y limpia signos sobrantes."""
    tokens = sql.replace("(", " ").split()
    if len(tokens) < 3 or tokens[1].upper() != "TABLE":
        return None
    return tokens[2].strip("`; \n")