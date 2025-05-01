import json
import config
from modules.db_manager import execute_sql
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI

llm = ChatOpenAI(
    openai_api_key=config.OPENAI_API_KEY,
    model_name=config.AI_MODEL,
    temperature=0.0
)

create_table_prompt = PromptTemplate(
    input_variables=["user_input"],
    template="""
Eres un asistente que convierte instrucciones en JSON.
Recibe esta instrucción en lenguaje natural y devuelve exclusivamente un JSON válido sin ningún texto adicional.

La estructura del JSON debe ser exactamente:
{{
  "table": "nombre_tabla",
  "columns": [
    {{"name": "nombre_columna", "type": "tipo_sql"}}
  ]
}}

Ejemplo válido:
{{
  "table": "usuarios",
  "columns": [
    {{"name": "id", "type": "INTEGER PRIMARY KEY AUTOINCREMENT"}},
    {{"name": "nombre", "type": "TEXT NOT NULL"}}
  ]
}}

Ahora genera el JSON para este input:
{user_input}
Recuerda: SOLO el JSON. Nada más.
"""
)

create_table_chain = LLMChain(llm=llm, prompt=create_table_prompt)

def procesar_peticion_llm(user_input, usuario):
    invoke_resp = create_table_chain.invoke({"user_input": user_input})
    json_str = invoke_resp.get("text", str(invoke_resp)).strip()

    if json_str.startswith("```json"):
        json_str = json_str.replace("```json", "").replace("```", "").strip()

    spec = json.loads(json_str)
    table = spec.get("table", "").strip()
    columns = spec.get("columns", [])

    if not table or not isinstance(columns, list):
        raise ValueError("❌ JSON inválido recibido del LLM")

    if any("name" not in c or "type" not in c for c in columns):
        raise ValueError("❌ Formato de columnas inválido.")

    if table.upper() in config.RESERVED_SQL_WORDS:
        table = f"{table.lower()}_tabla"

    sql = f"CREATE TABLE IF NOT EXISTS {table} (" + ", ".join(
        f"{col['name']} {col['type']}" for col in columns
    ) + ");"

    res = execute_sql(sql, usuario=usuario)
    if not res.get("success", True):
        raise Exception(res['message'])

    return f"⚡ Tabla creada: {table}"