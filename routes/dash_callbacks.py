# routes/dash_callbacks.py

import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
from routes.dash_app import dash_app, flask_app

@dash_app.callback(
    [
        Output('df-data-display', 'children'),
        Output('x-axis', 'options'),
        Output('y-axis', 'options'),
        Output('graph', 'figure'),
        Output('table', 'columns'),
        Output('table', 'data'),
    ],
    [
        Input('chart-type', 'value'),
        Input('show-data-button', 'n_clicks')
    ]
)
def update_all(chart_type, n_clicks):
    df = getattr(flask_app, 'last_query_df', pd.DataFrame())

    # 1) texto con el DataFrame
    display_text = str(df) if not df.empty else "No hay datos cargados."

    cols = list(df.columns)
    opts = [{'label': c, 'value': c} for c in cols]

    # 2) si no hay datos devolvemos todo vacío / gráfico vacio
    if df.empty:
        empty_fig = px.scatter(pd.DataFrame(), title="No hay datos disponibles")
        return display_text, opts, opts, empty_fig, [], []

    # 3) ejes por defecto
    x_axis, y_axis = cols[0], cols[1]

    # 4) construimos la figura
    if chart_type == 'bar':
        fig = px.bar(df, x=x_axis, y=y_axis, title='Gráfico dinámico')
    elif chart_type == 'line':
        fig = px.line(df, x=x_axis, y=y_axis, title='Gráfico dinámico')
    elif chart_type == 'scatter':
        fig = px.scatter(df, x=x_axis, y=y_axis, title='Gráfico dinámico')
    else:
        fig = px.pie(df, names=x_axis, values=y_axis, title='Gráfico dinámico')

    # 5) tabla: columnas y datos
    columns = [{"name": c, "id": c} for c in cols]
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