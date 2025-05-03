from dash import html, dcc, dash_table

def get_layout():
    return html.Div([

        html.H1('Panel Avanzado',
                style={'textAlign': 'center', 'fontFamily': 'Arial'}),

        # ─── Controles ──────────────────────────────────────────────
        html.Div([
            dcc.Dropdown(id='x-axis', placeholder='Seleccionar eje X'),
            dcc.Dropdown(id='y-axis', placeholder='Seleccionar eje Y'),
            dcc.Dropdown(
                id='chart-type',
                options=[
                    {'label': 'Bar',     'value': 'bar'},
                    {'label': 'Line',    'value': 'line'},
                    {'label': 'Scatter', 'value': 'scatter'},
                    {'label': 'Pie',     'value': 'pie'}
                ],
                value='bar'
            )
        ], style={
            'display': 'flex',
            'gap': '10px',
            'justifyContent': 'center',
            'paddingBottom': '20px'
        }),

        # ─── Gráfico ───────────────────────────────────────────────
        dcc.Graph(id='graph', figure={}),

        # ─── Tabla ─────────────────────────────────────────────────
        dash_table.DataTable(
            id='table',
            columns=[],
            data=[],
            style_table={'overflowX': 'auto'},
            style_cell={'fontFamily': 'Arial'}
        ),

        html.Br(),

        # ─── Botón “Ver datos en JSON” ─────────────────────────────
        html.Button('Ver datos en JSON', id='show-data-button',
                    n_clicks=0,
                    style={'backgroundColor': '#28a745', 'color': 'white'}),
        html.Div(id='output-data',
                 style={'whiteSpace': 'pre-wrap', 'fontFamily': 'Arial',
                        'marginBottom':'20px'}),

        # ─── Botón “Exportar a Excel” ─────────────────────────────
        html.Button('Exportar a Excel', id='btn-export-excel', n_clicks=0,
                    style={'backgroundColor': '#007bff', 'color': 'white'}),
        dcc.Download(id='download-excel'),
    ])