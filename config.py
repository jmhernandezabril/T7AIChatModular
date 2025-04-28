# config.py

# Apariencia general
FONT_FAMILY = "Poppins"
FONT_URL = "https://fonts.googleapis.com/css2?family=Poppins&display=swap"
FONT_SIZE = "14px"

APP_NAME = "MINIcrm"

# Configuración de AI
AI_PROVIDER = "OpenAI"
AI_MODEL = "gpt-3.5-turbo"

# Mensaje inicial
SALUDO_INICIAL = "Hola. Por favor, ¿me indica sus datos de acceso?"

# Paths de documentación y base de datos
DOCS_FOLDER = "docs/tecnico/"
BASE_DATOS_DOC_PATH = DOCS_FOLDER + "AZ_base_datos.md"
FAISS_INDEX_PATH = "vector_memory/index_faiss"
DB_PATH = "data/t7ai.db"