from flask import (
    render_template, request, jsonify,
    send_file, g, session
)
import config
from modules.db_manager import execute_sql, query_sql
import pandas as pd
from io import BytesIO
import json

from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI


def register_chat_routes(app):
    app.last_query_df = pd.DataFrame()

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

    @app.before_request
    def load_user():
        g.user_id = session.get("user_id", "t7AI")

    @app.route("/")
    def index():
        return render_template(
            "base.html",
            app_name=config.APP_NAME,
            ai_model=config.AI_MODEL,
            ai_provider=config.AI_PROVIDER,
            font_family=config.FONT_FAMILY,
            saludo_inicial=config.SALUDO_INICIAL,
            texto_caja_mensaje=config.TEXTO_CAJA_MENSAJE
        )

    @app.route("/chat", methods=["POST"])
    def chat():
        user_id = g.user_id
        user_input = request.json.get("message", "").strip()

        if not user_input:
            return jsonify({"response": "🤖 Por favor, ingresa un comando."})

        first = user_input.split()[0].upper()
        ddl_cmds = config.DDL_COMMANDS
        dml_cmds = config.DML_COMMANDS
        query_cmds = ("SELECT",)

        # 🧠 CASO 1: Petición en lenguaje natural → JSON → CREATE TABLE
        if first not in ddl_cmds + dml_cmds + query_cmds:
            try:
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

                res = execute_sql(sql, usuario=user_id)
                if not res.get("success", True):
                    return jsonify({"response": f"❌ {res['message']}"})

                return jsonify({"response": f"⚡ Tabla creada: {table}"})

            except Exception as e:
                return jsonify({"response": f"❌ Error NL→SQL: {e}"})


        # 🧠 CASO 2: SQL Manual (DDL)
        if first in ddl_cmds:
            try:
                res = execute_sql(user_input, usuario=user_id)
                if not res.get("success", True):
                    return jsonify({"response": f"❌ {res['message']}"})
                return jsonify({"response": f"⚡ {res['message']}"})
            except Exception as e:
                return jsonify({"response": f"❌ Error ejecutando SQL: {e}"})

        # 🧠 CASO 3: SELECT
        if first in query_cmds:
            try:
                result = query_sql(user_input)
                df = pd.DataFrame(result["rows"], columns=result["columns"])
                app.last_query_df = df
                return jsonify({
                    "response": result["rows"],
                    "columns": result["columns"]
                })
            except Exception as e:
                return jsonify({"response": f"❌ Error en consulta: {e}"})

        # 🧠 CASO 4: DML
        if first in dml_cmds:
            try:
                res = execute_sql(user_input, usuario=user_id)
                return jsonify({"response": f"⚡ {res['message']}"})
            except Exception as e:
                return jsonify({"response": f"❌ Error ejecutando SQL: {e}"})

        return jsonify({"response": f"🤖 {user_input}"})


    @app.route("/download_excel")
    def download_excel():
        df = getattr(app, "last_query_df", pd.DataFrame())
        if df.empty:
            return "No hay datos para exportar", 400

        output = BytesIO()
        df.to_excel(output, index=False)
        output.seek(0)
        return send_file(
            output,
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            as_attachment=True,
            download_name="datos.xlsx"
        )