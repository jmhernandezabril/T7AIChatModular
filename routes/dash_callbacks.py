# routes/dash_callbacks.py

import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
from routes.dash_app import dash_app, flask_app


@dash_app.callback([
    Output('df-data-display', 'children'),
    Output('x-axis', 'options'),
    Output('y-axis', 'options'),
    Output('graph', 'figure'),
    Output('table', 'columns'),
    Output('table', 'data'),
], [
    Input('chart-type', 'value'),
    Input('show-data-button', 'n_clicks'),
    Input('x-axis', 'value'),
    Input('y-axis', 'value')
])
def update_all(chart_type, n_clicks, x_selected, y_selected):
    df = getattr(flask_app, 'last_query_df', pd.DataFrame())
    df = df.copy()
    df["indice_auto"] = range(len(df))  # columna numérica para respaldo

    # 1) texto con el DataFrame
    display_text = (
        str(df[[c for c in df.columns if c != "indice_auto"]])
        if not df.empty and len(df.columns) > 1
        else "No hay datos cargados."
    )

    cols = list(df.columns)
    opts = [{'label': c, 'value': c} for c in cols]

    # 2) si no hay datos devolvemos todo vacío / gráfico vacío
    if df.empty:
        empty_fig = px.scatter(pd.DataFrame(), title="No hay datos disponibles")
        return display_text, opts, opts, empty_fig, [], []

    # 3) determinar ejes
    real_cols = [c for c in cols if c != "indice_auto"]

    x_axis = x_selected or (real_cols[0] if real_cols else "indice_auto")
    y_axis = y_selected or (real_cols[1] if len(real_cols) > 1 else x_axis)

    if y_axis == x_axis and x_axis == "indice_auto" and len(real_cols) == 1:
        df[real_cols[0]] = df[real_cols[0]].astype(str)
        y_axis = real_cols[0]

    # 4) construimos la figura
    try:
        if chart_type == 'bar':
            fig = px.bar(df, x=x_axis, y=y_axis, title='Gráfico dinámico')
        elif chart_type == 'line':
            fig = px.line(df, x=x_axis, y=y_axis, title='Gráfico dinámico')
        elif chart_type == 'scatter':
            fig = px.scatter(df, x=x_axis, y=y_axis, title='Gráfico dinámico')
        else:
            fig = px.pie(df, names=y_axis, values=x_axis, title='Gráfico dinámico')
    except Exception:
        df_aux = df.copy()
        df_aux["conteo"] = 1
        fig = px.bar(df_aux, y=y_axis, x="conteo", title="Gráfico alternativo (datos incompatibles)")

    # 5) tabla: columnas y datos
    columns = [{"name": c, "id": c} for c in df.columns]
    data = df.to_dict('records')

    return display_text, opts, opts, fig, columns, data


@dash_app.callback(
    Output('output-data', 'children'),
    [Input('show-data-button', 'n_clicks')]
)
def show_data_in_chat(n_clicks):
    if n_clicks and hasattr(flask_app, 'last_query_df'):
        return str(flask_app.last_query_df.to_dict('records'))
    return ''