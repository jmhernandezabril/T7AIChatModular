from flask import (
    render_template, request, jsonify,
    send_file, g, session
)
import config
import pandas as pd
from io import BytesIO
import json

from modules.sql_executor import ejecutar_sql_manual, ejecutar_consulta_select
from modules.llm_manager import procesar_peticion_llm

def register_chat_routes(app):
    app.last_query_df = pd.DataFrame()

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

        # 🧠 CASO 1: Instrucción en lenguaje natural → LLM → CREATE TABLE
        if first not in ddl_cmds + dml_cmds + query_cmds:
            respuesta = procesar_peticion_llm(user_input, user_id)
            return jsonify({"response": respuesta})

        # 🧠 CASO 2: SQL Manual DDL
        if first in ddl_cmds:
            resultado = ejecutar_sql_manual(user_input, user_id)
            return jsonify({"response": resultado.get("error") or resultado.get("success")})

        # 🧠 CASO 3: SELECT
        if first in query_cmds:
            resultado = ejecutar_consulta_select(user_input)
            if "error" in resultado:
                return jsonify({"response": resultado["error"]})
            app.last_query_df = resultado["dataframe"]
            return jsonify({
                "response": resultado["response"],
                "columns": resultado["columns"]
            })

        # 🧠 CASO 4: SQL Manual DML
        if first in dml_cmds:
            resultado = ejecutar_sql_manual(user_input, user_id)
            return jsonify({"response": resultado.get("error") or resultado.get("success")})

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