# routes/dash_callbacks.py
import pandas as pd
import plotly.express as px
from dash import dcc
from dash.dependencies import Input, Output
from routes.dash_app import dash_app, flask_app


def register_dash_callbacks(app):
    """
    Registra los callbacks de Dash sobre la instancia 'app'.
    """
    # 1) Mostrar JSON al pulsar el botón
    @app.callback(
        Output('output-data', 'children'),
        Input('show-data-button', 'n_clicks'),
    )
    def show_json(n_clicks):
        df = getattr(flask_app, 'last_query_df', pd.DataFrame())
        if n_clicks and not df.empty:
            return str(df.to_dict('records'))
        return ''

    # 2) Actualizar dropdowns, gráfico y tabla
    @app.callback(
        Output('x-axis', 'options'),
        Output('y-axis', 'options'),
        Output('graph', 'figure'),
        Output('table', 'columns'),
        Output('table', 'data'),
        Input('show-data-button', 'n_clicks'),
        Input('chart-type', 'value'),
        Input('x-axis', 'value'),
        Input('y-axis', 'value'),
    )
    def update_all(n_clicks, chart_type, x_sel, y_sel):
        df = getattr(flask_app, 'last_query_df', pd.DataFrame()).copy()
        if df.empty:
            empty_fig = px.scatter(pd.DataFrame(), title="No hay datos disponibles")
            return [], [], empty_fig, [], []

        cols = list(df.columns)
        opts = [{'label': c, 'value': c} for c in cols]
        x_col = x_sel or cols[0]
        y_col = y_sel or (cols[1] if len(cols)>1 else cols[0])

        try:
            if chart_type == 'bar':
                fig = px.bar(df, x=x_col, y=y_col, title="Gráfico dinámico")
            elif chart_type == 'line':
                fig = px.line(df, x=x_col, y=y_col, title="Gráfico dinámico")
            elif chart_type == 'scatter':
                fig = px.scatter(df, x=x_col, y=y_col, title="Gráfico dinámico")
            else:
                fig = px.pie(df, names=y_col, values=x_col, title="Gráfico dinámico")
        except Exception:
            df_aux = df.copy()
            df_aux['conteo'] = 1
            fig = px.bar(df_aux, x='conteo', y=y_col,
                         title="Gráfico alternativo (datos incompatibles)")

        table_columns = [{'name': c, 'id': c} for c in df.columns]
        table_data    = df.to_dict('records')

        return opts, opts, fig, table_columns, table_data

    # 3) Exportar a Excel al pulsar el botón
    @app.callback(
        Output('download-excel', 'data'),
        Input('btn-export-excel', 'n_clicks'),
        prevent_initial_call=True
    )
    def export_to_excel(n_clicks):
        df = getattr(flask_app, 'last_query_df', pd.DataFrame())
        if df.empty:
            return dash.no_update
        return dcc.send_data_frame(df.to_excel, 'datos.xlsx', index=False)