# routes/chat_routes.py

from flask import render_template, request, jsonify, send_file, g, session
import config
from modules.db_manager import execute_sql, query_sql
import pandas as pd
from io import BytesIO

def register_chat_routes(app):
    # Inicializamos el atributo en el app para la última consulta
    app.last_query_df = pd.DataFrame()

    @app.before_request
    def load_user():
        # Si no hay usuario en sesión, por defecto 't7AI'
        g.user_id = session.get('user_id', 't7AI')

    @app.route("/")
    def index():
        return render_template(
            "base.html",
            app_name        = config.APP_NAME,
            ai_model        = config.AI_MODEL,
            ai_provider     = config.AI_PROVIDER,
            font_family     = config.FONT_FAMILY,
            saludo_inicial  = config.SALUDO_INICIAL
        )

    @app.route("/chat", methods=["POST"])
    def chat():
        user_id = g.user_id
        user_input = request.json.get("message", "").strip()
        if not user_input:
            return jsonify({"response": "🤖 Por favor, ingresa un comando."})

        first = user_input.split()[0].upper()
        ddl_cmds = ("CREATE", "ALTER", "DROP")
        dml_cmds = ("INSERT", "UPDATE", "DELETE")
        query_cmds = ("SELECT",)

        # Comandos DDL: CREATE, ALTER, DROP
        if first in ddl_cmds:
            res = execute_sql(user_input, usuario=user_id)
            return jsonify({"response": f"⚡ {res['message']}"})

        # Consultas SELECT
        if first in query_cmds:
            try:
                result = query_sql(user_input)
                # Guardamos el DataFrame en el app
                df_result = pd.DataFrame(result["rows"], columns=result["columns"])
                app.last_query_df = df_result
                print(f"[{user_id}] Datos obtenidos y guardados en app.last_query_df:", df_result)
                return jsonify({
                    "response": result["rows"],
                    "columns":  result["columns"]
                })
            except Exception as e:
                return jsonify({"response": f"❌ Error en consulta: {e}"})

        # Comandos DML: INSERT, UPDATE, DELETE
        if first in dml_cmds:
            res = execute_sql(user_input, usuario=user_id)
            return jsonify({"response": f"⚡ {res['message']}"})

        # Respuesta por defecto (eco del mensaje)
        return jsonify({"response": f"🤖 {user_input}"})

    @app.route("/download_excel")
    def download_excel():
        # 1) Recupera el DataFrame de la última consulta
        df = getattr(app, 'last_query_df', pd.DataFrame())

        # Si no hay datos, devolvemos un error
        if df.empty:
            return "No hay datos para exportar", 400

        # 2) Volcar a Excel en memoria (Pandas elige el engine por defecto)
        output = BytesIO()
        df.to_excel(output, index=False)
        output.seek(0)

        # 3) Enviar el buffer como fichero adjunto
        return send_file(
            output,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            download_name='datos.xlsx'
        )