# routes/dash_app.py

import dash
import pandas as pd
from routes.dash_layout import get_layout

dash_app = None
flask_app = None

def init_dash_app(app):
    global dash_app, flask_app
    flask_app = app

    dash_app = dash.Dash(
        __name__,
        server=app,
        url_base_pathname='/dash/',
    )

    # Layout dinámico: se recalcula cada vez que visitas /dash/
    def serve_layout():
        # Tomamos la última consulta; si no existe o es None, creamos un DataFrame vacío
        df = getattr(flask_app, 'last_query_df', None)
        if df is None:
            df = pd.DataFrame()
        return get_layout(df)

    dash_app.layout = serve_layout

    # Tras inicializar dash_app, registramos los callbacks
    import routes.dash_callbacks  # noqa: registers callbacks
