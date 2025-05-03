# routes/dash_app.py
import dash
import pandas as pd
from flask import jsonify
from routes.dash_layout import get_layout

# Variables globales para exponer la instancia
# dash_app será asignada en init
dash_app = None
flask_app = None

def init_dash_app(app):
    global dash_app, flask_app
    flask_app = app

    # 1) Creamos la instancia de Dash ligada al Flask app
    dash_app = dash.Dash(
        __name__,
        server=app,
        url_base_pathname='/dash/'
    )

    # 2) Asignamos el layout como función sin argumentos
    dash_app.layout = get_layout

    # 3) Endpoint REST para servir JSON del último DataFrame
    @app.route("/api/last_query_df")
    def serve_last_query_df():
        df = getattr(app, 'last_query_df', None)
        cols = getattr(app, 'last_query_columns', [])
        if df is None:
            return jsonify({"columns": [], "index": [], "data": []})
        if not hasattr(df, 'to_json'):
            df = pd.DataFrame(df, columns=cols)
        return df.to_json(orient='split')

    # 4) Registramos los callbacks en la instancia de Dash
    from routes.dash_callbacks import register_dash_callbacks
    register_dash_callbacks(dash_app)

    return dash_app