import os

# Apariencia general
FONT_FAMILY = "Poppins"
FONT_URL = "https://fonts.googleapis.com/css2?family=Poppins&display=swap"
FONT_SIZE = "14px"

# Nombre de la aplicación (usado en index.html)
APP_NAME    = "ONEapp"

# Configuración de AI
AI_PROVIDER = "OpenAI"
AI_MODEL = "gpt-3.5-turbo"
# Añadimos la API Key (por defecto desde variable de entorno)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Mensaje inicial
SALUDO_INICIAL = "Hola!"
TEXTO_CAJA_MENSAJE = "Escriba aquí su mensaje..."

# Paths de documentación y base de datos
DOCS_FOLDER = "docs/tecnico/"
BASE_DATOS_DOC_PATH = DOCS_FOLDER + "AZ_base_datos.md"
FAISS_INDEX_PATH = "vector_memory/index_faiss"
DB_PATH = "data/t7ai.db"

# Comandos a detectar/documentar en chat_routes.py
DDL_COMMANDS = (
    # DDL básicos
    "CREATE",     # CREATE TABLE, CREATE VIEW, CREATE INDEX, CREATE SEQUENCE, …
    "ALTER",      # ALTER TABLE, ALTER INDEX, …
    "DROP",       # DROP TABLE, DROP VIEW, DROP INDEX, …
    "TRUNCATE",   # TRUNCATE TABLE

    # Renombrados y comentarios
    "COMMENT",    # COMMENT ON TABLE/COLUMN …
    "RENAME",     # RENAME TABLE … TO …

    # Control de permisos (DCL, opcional)
    "GRANT",      # GRANT SELECT/INSERT/… ON …
    "REVOKE",     # REVOKE …

    # Mantenimiento (opcionales)
    "VACUUM",     # VACUUM [FULL] …
    "ANALYZE",    # ANALYZE …
    "CLUSTER",    # CLUSTER …
)
DML_COMMANDS = (
    "INSERT",     # Inserta nuevos registros en una tabla
    "UPDATE",     # Modifica valores de registros existentes
    "DELETE",     # Elimina registros de una tabla
    "MERGE",      # Fusiona datos: inserta o actualiza según condiciones (SQL estándar)
    "UPSERT",     # Inserta o actualiza registros (variante de MERGE en algunos SGBD)
    "REPLACE",    # (MySQL) Reemplaza registros: similar a INSERT con llave única
    "COPY",       # (PostgreSQL) Copia datos entre tablas y archivos
    "LOAD",       # (MySQL) LOAD DATA INFILE: carga datos desde un archivo
    "CALL",       # Invoca procedimientos almacenados
    "EXEC",       # Ejecuta procedimientos (SQL Server)
    # Puedes añadir más según tus necesidades (e.g., TRUNCATE como DML)
)
# Palabras reservadas SQL para validación de nombres de tabla
RESERVED_SQL_WORDS = {
    "SELECT", "INSERT", "DELETE", "UPDATE", "WHERE", "FROM", "JOIN", "GROUP",
    "BY", "ORDER", "IF", "TABLE", "VALUES", "INTO", "SET", "AND", "OR", "NOT",
    "CREATE", "DROP", "ALTER", "PRIMARY", "KEY", "NULL", "IS"
}