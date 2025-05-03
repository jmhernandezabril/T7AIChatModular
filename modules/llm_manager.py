# modules/llm_manager.py
import traceback
import re
import config
from modules.db_manager import execute_sql, create_table_if_not_exists
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

# Instancia del LLM
llm = ChatOpenAI(
    openai_api_key=config.OPENAI_API_KEY,
    model_name=config.AI_MODEL,
    temperature=config.AI_TEMPERATURE
)

# Prompt unificado
UNIFIED_PROMPT = PromptTemplate(
    input_variables=["user_input"],
    template="""
Eres un asistente experto en bases de datos y conversación.

1) Si el usuario pide crear, alterar o eliminar una tabla (en inglés o en español),
   responde con la instrucción SQL únicamente, en texto plano, terminado en punto y coma.
   No uses backticks, ni ```sql, ni explicaciones.

2) Para cualquier otro mensaje (saludos, small-talk, preguntas generales),
   responde en lenguaje natural en español, sin generar SQL.

Ejemplos:
- crea una tabla usuarios con columnas id y nombre
  → CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nombre TEXT);

- ¿Hola, cómo estás?
  → ¡Hola! Estoy muy bien, gracias. ¿En qué puedo ayudarte hoy?

Petición de usuario:
{user_input}
"""
)

unified_chain = LLMChain(llm=llm, prompt=UNIFIED_PROMPT)

def procesar_peticion_llm(user_input: str, usuario: str) -> str:
    """
    Distingue entre DDL (CREATE, DROP, ALTER, etc.) y small-talk;
    ejecuta SQL y maneja errores y existencia de tabla.
    """
    # 1) Llamada al LLM
    try:
        respuesta = unified_chain.run(user_input).strip()
    except Exception as e:
        traceback.print_exc()
        return f"❌ Error de comunicación con LLM: {e}"

    # 2) Limpia backticks/fences
    cleaned = re.sub(r"```(?:sql)?", "", respuesta).replace("```", "").strip()
    upper = cleaned.upper()

    # 3) Detectar DDL (inglés/español)
    sql_verbs = ("CREATE ", "DROP ", "ALTER ", "TRUNCATE ")
    sql_verbs_es = ("CREA ", "CREAR ", "ELIMINAR ", "MODIFICAR ", "RENAME ", "GRANT ", "REVOKE ")

    if any(upper.startswith(v) for v in (*sql_verbs, *sql_verbs_es)):
        # CREATE TABLE IF NOT EXISTS
        match = re.match(
            r"CREATE\s+TABLE\s+IF\s+NOT\s+EXISTS\s+([a-zA-Z0-9_]+)",
            cleaned, flags=re.IGNORECASE
        )
        if match:
            tabla = match.group(1)
            result = create_table_if_not_exists(cleaned, tabla, usuario)
        else:
            # Otros DDL se ejecutan directamente
            try:
                result = execute_sql(cleaned, usuario)
            except Exception as e:
                traceback.print_exc()
                return f"❌ Excepción al ejecutar SQL: {e}"

        msg = result.get("message", "").strip()
        success = result.get("success", False)

        if success and not msg.lower().startswith("la tabla"):
            return f"⚡ Instrucción ejecutada correctamente: {cleaned}"
        return f"⚠️ {msg}"

    # 4) Small-talk
    return cleaned