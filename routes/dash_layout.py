# routes/dash_layout.py

from dash import html, dcc, dash_table
import plotly.express as px

def get_layout(df_data):
    # gráficos
    if df_data.empty:
        fig = px.scatter(df_data, title="No hay datos disponibles")
    else:
        fig = px.scatter(df_data,
                         x=df_data.columns[0],
                         y=df_data.columns[1],
                         title="Gráfico dinámico")

    return html.Div([
        html.H1('Panel Avanzado', style={'textAlign': 'center', 'fontFamily': 'Arial'}),

        # **AQUÍ** ponemos el Pre con id
        html.Div([
            html.H3("Datos cargados en df_data:"),
            html.Pre(id='df-data-display',   # <- importante
                     children="",           # <- inicialmente vacío
                     style={
                        'whiteSpace': 'pre-wrap',
                        'wordBreak': 'break-word',
                        'fontFamily': 'Arial'
                     })
        ], style={'paddingBottom': '20px'}),

        html.Div([
            dcc.Dropdown(id='x-axis', placeholder='Seleccionar eje X'),
            dcc.Dropdown(id='y-axis', placeholder='Seleccionar eje Y'),
            dcc.Dropdown(
                id='chart-type',
                options=[
                    {'label': 'Bar', 'value': 'bar'},
                    {'label': 'Line', 'value': 'line'},
                    {'label': 'Scatter', 'value': 'scatter'},
                    {'label': 'Pie', 'value': 'pie'}
                ],
                value='bar'
            )
        ], style={
            'display': 'flex',
            'gap': '10px',
            'justifyContent': 'center',
            'paddingBottom': '20px'
        }),

        dcc.Graph(id='graph', figure=fig),

        dash_table.DataTable(
            id='table',
            style_table={'overflowX': 'auto'},
            style_cell={'fontFamily': 'Arial'}
        ),

        html.Br(),

        html.A(
            html.Button('📂 Exportar a Excel', style={
                'backgroundColor': '#007bff',
                'color': 'white'
            }),
            href='/download_excel',
            style={
                'textDecoration': 'none',
                'display': 'block',
                'textAlign': 'center'
            }
        ),

        html.Button('Ver datos en el chat', id='show-data-button', style={
            'backgroundColor': '#28a745',
            'color': 'white'
        }),

        html.Div(id='output-data')
    ])