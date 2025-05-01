import os
from datetime import datetime
import sqlparse
from config import BASE_DATOS_DOC_PATH


def documentar_sql(sql_texto, tipo="CREATE", usuario="t7AI"):
    """Documenta cambios estructurales en la base de datos usando Frontmatter YAML,
    evitando duplicar el contenido ya existente, y registrando tiempo con milisegundos."""
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

    # Solo documentamos DDL
    accion = sql.split()[0].upper()
    if accion not in ("CREATE", "ALTER", "DROP"):
        return

    # Extraer nombre de la tabla
    nombre_tabla = extraer_nombre_tabla(sql)
    if not nombre_tabla:
        return

    # Asegurar existencia del MD
    os.makedirs(os.path.dirname(BASE_DATOS_DOC_PATH), exist_ok=True)
    if not os.path.exists(BASE_DATOS_DOC_PATH):
        with open(BASE_DATOS_DOC_PATH, "w", encoding="utf-8") as f:
            f.write("# Registro de Cambios en Base de Datos\n\n")

    # Leer contenido actual
    with open(BASE_DATOS_DOC_PATH, "r", encoding="utf-8") as f:
        contenido = f.read()

    # Generar bloque YAML
    ahora = datetime.now()
    fecha = ahora.strftime("%Y-%m-%d")
    hora = ahora.strftime("%H:%M:%S.%f")[:-3]

    yaml_block = [
        "```yaml",
        f"table: {nombre_tabla}",
        f"date: {fecha}",
        f"time: {hora}",
        f"user: {usuario}",
        f"action: {accion}",
        "sql: |"
    ] + [f"  {line}" for line in sql.splitlines()] + ["```", ""]

    bloque_final = "\n".join(yaml_block)

    # Evitar duplicados si el bloque lógico ya existe (sin campos dinámicos)
    bloque_sin_dinamicos = "\n".join([
        l for l in yaml_block
        if not l.startswith(("date:", "time:", "user:")) and not l.startswith("```yaml")
    ])

    if bloque_sin_dinamicos.strip() in contenido:
        return

    # Anexar y guardar
    with open(BASE_DATOS_DOC_PATH, "a", encoding="utf-8") as f:
        f.write(bloque_final + "\n")


def extraer_nombre_tabla(sql):
    """Extrae el nombre de la tabla incluso con IF NOT EXISTS"""
    tokens = sql.replace("(", " ").replace("\n", " ").split()
    tokens = [t.strip().upper() for t in tokens]
    if "TABLE" in tokens:
        idx = tokens.index("TABLE")
        try:
            if tokens[idx + 1] == "IF":
                return tokens[idx + 4].lower()
            return tokens[idx + 1].lower()
        except IndexError:
            return None
    return None