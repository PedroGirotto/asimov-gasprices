import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from dash_bootstrap_templates import ThemeSwitchAIO


FONT_AWESOME = ["https://use.fontawesome.com/releases/v5.10.2/css/all.css"]
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY, dbc_css])
app.scripts.config.serve_locally = True


template_theme1 = "flatly"
template_theme2 = "vapor"
url_theme1 = dbc.themes.FLATLY
url_theme2 = dbc.themes.VAPOR

tab_card = {"height":"100%"}


df = pd.read_csv("datasets/tratado_data_gas.csv")


app.layout = dbc.Container(children=[
    dbc.Row([ # linha 01
        dbc.Col([ # coluna 01
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.Legend("Gas Prices Analysis")
                        ], sm=8),

                        dbc.Col([
                            html.I(className="fa fa-filter", style={"font-size":"300%"})
                        ], sm=4, align="center")
                    ]),

                    dbc.Row([
                        dbc.Col([
                            ThemeSwitchAIO(aio_id="theme", themes=[url_theme1, url_theme2]),
                            html.Legend("Asimov Academy")
                        ])

                    ], style={"margin-top":"10px"}),

                    dbc.Row([
                        dbc.Col([
                            dbc.Button("Visite o Site", href="https://asimov.academy/", target="_blank")
                        ])
                    ], style={"margin-top":"10px"})
                ])
            ], style=tab_card)
        ], sm=4, lg=2),

        dbc.Col([ # coluna 02
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H3("Máximos e Mínimos"),
                            dcc.Graph(id="static-maxmin", config={"displayModeBar":False, "showTips": False})
                        ])
                    ])
                ])
            ], style=tab_card)
        ], sm=8, lg=3),

        dbc.Col([ # coluna 03
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.H6("Ano de análise"),
                            dcc.Dropdown(
                                id="select_ano",
                                value=df.at[df.index[1], "ANO"],
                                clearable=False,
                                className="dbc",
                                options=[
                                    {"label":x, "value":x} for x in df["ANO"].unique()
                            ])
                        ], sm = 6),

                        dbc.Col([
                            html.H6("Região de análise"),
                            dcc.Dropdown(
                                id="select_regiao",
                                value=df.at[df.index[1], "REGIÃO"],
                                clearable=False,
                                className="dbc",
                                options=[
                                    {"label":x, "value":x} for x in df["REGIÃO"].unique()
                            ])
                        ], sm=6)
                    ]),

                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id="regiao_graph", config={"displayModeBar":False, "showTips":False})
                        ], sm=12, md=6),

                        dbc.Col([
                            dcc.Graph(id="estado_graph", config={"displayModeBar":False, "showTips":False})
                        ], sm=12, md=6)
                    ], style={"column-gap":"8px"})
                ])
            ], style=tab_card)
        ], sm=12, lg=7)
    ]) 
], fluid=True, style={"height":"100%"})


if __name__ == "__main__":
    app.run(debug=True)