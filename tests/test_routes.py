# routes/chat_routes.py

from flask import (
    render_template, request, jsonify,
    send_file, g, session
)
from services.chat_service import ChatService
import config

def register_chat_routes(app):
    # Inicializamos para futuras descargas
    app.last_query_df = None
    app.last_query_columns = []

    # Creamos el servicio de chat (SQL + LLM)
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

        # Delegamos todo el flujo (SQL vs. LLM) al ChatService
        result = chat_svc.handle_message(user_input, g.user_id)

        # Si vino con DataFrame (SELECT), lo guardamos para descarga
        if "dataframe" in result:
            app.last_query_df = result.pop("dataframe")
            app.last_query_columns = result.get("columns", [])
            return jsonify({
                "response": result["response"],
                "columns": app.last_query_columns
            })

        # Devolvemos la respuesta normal (DDL, DML o LLM)
        return jsonify({"response": result["response"]})

    @app.route("/download_excel")
    def download_excel():
        # Importación perezosa para no romper tests sin pandas/numpy
        import pandas as pd
        from io import BytesIO

        df = getattr(app, "last_query_df", None)
        cols = getattr(app, "last_query_columns", [])
        if df is None:
            return "No hay datos para exportar", 400

        # Si el 'dataframe' no es un DataFrame, lo convertimos
        if not hasattr(df, "to_excel"):
            df = pd.DataFrame(df, columns=cols)

        output = BytesIO()
        df.to_excel(output, index=False)
        output.seek(0)

        return send_file(
            output,
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            as_attachment=True,
            download_name="datos.xlsx"
        )
