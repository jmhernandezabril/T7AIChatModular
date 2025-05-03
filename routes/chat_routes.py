# routes/chat_routes.py

from flask import (
    render_template, request, jsonify,
    send_file, g, session
)
import pandas as pd
from io import BytesIO

from services.chat_service import ChatService  # asegúrate de que este path es correcto
import config

def register_chat_routes(app):
    # Estado global para la última SELECT
    app.last_query_df = None
    app.last_query_columns = []

    # Servicio que mezcla SQL + LLM
    chat_svc = ChatService(
        ddl_cmds=config.DDL_COMMANDS,
        dml_cmds=config.DML_COMMANDS
    )

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
        user_input = request.json.get("message", "").strip()
        if not user_input:
            return jsonify({"response": "🤖 Por favor, ingresa un comando."})

        # Lógica unificada SQL vs LLM
        result = chat_svc.handle_message(user_input, g.user_id)

        # Si es SELECT, guardamos DataFrame y columnas
        if "dataframe" in result:
            df   = result["dataframe"]
            cols = result["columns"]
            app.last_query_df      = df
            app.last_query_columns = cols

            return jsonify({
                "response": result["response"],
                "columns": cols
            })

        # DDL/DML o LLM → solo devolvemos texto
        return jsonify({"response": result.get("response", "")})