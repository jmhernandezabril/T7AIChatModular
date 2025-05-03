# routes/chat_routes.py

from flask import (
    render_template, request, jsonify,
    send_file, g, session
)
import pandas as pd
from io import BytesIO
import yaml

from services.chat_service import ChatService  # asegúrate de que este path es correcto
import config
from orchestrator.schema import PipelineConfig  # NUEVO: import Orquestador
from orchestrator.runner import load_pipeline     # NUEVO: import runner

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

        # NUEVO: detectar comando !run para pipelines declarativos
        if user_input.startswith("!run "):
            parts = user_input.split()
            # !run <pipeline> key1=val1 key2=val2
            pipeline_name = parts[1]
            args = {}
            for token in parts[2:]:
                if "=" in token:
                    k, v = token.split("=", 1)
                    # intentar parsear JSON para valores complejos
                    try:
                        args[k] = yaml.safe_load(v)
                    except Exception:
                        args[k] = v.strip('"').strip("'")
            # Carga y valida el YAML del pipeline
            try:
                with open(f"orchestrator/example_pipelines/{pipeline_name}.yaml") as f:
                    cfg = PipelineConfig.model_validate(yaml.safe_load(f))
            except FileNotFoundError:
                return jsonify({"response": f"❌ Pipeline '{pipeline_name}' no encontrado."})
            # Ejecuta el pipeline
            runner = load_pipeline(cfg)
            result = runner(**args)
            return jsonify({
                "response": f"✅ Pipeline `{pipeline_name}` ejecutado.",
                "data": result
            })

        # Lógica unificada SQL vs LLM
        result = chat_svc.handle_message(user_input, g.user_id)

        # Si es SELECT, guardamos DataFrame y columnas
        if "dataframe" in result:
            df   = result["dataframe"]
            cols = result["columns"]
            app.last_query_df      = df
            app.last_query_columns = cols

            return jsonify({
                "response": result.get("response", ""),
                "columns": cols
            })

        # DDL/DML o LLM → solo devolvemos texto
        return jsonify({"response": result.get("response", "")})