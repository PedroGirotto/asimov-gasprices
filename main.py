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
                        html.H3("Máximos e Mínimos"),
                        dbc.Col([
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

                    #! gráficos não ficam na mesma linha
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id="regiao_graph", config={"displayModeBar":False, "showTips":False})
                        ], sm=6),

                        dbc.Col([
                            dcc.Graph(id="estado_graph", config={"displayModeBar":False, "showTips":False})
                        ], sm=6)
                    ], style={"column-gap":"4px"})
                ])
            ], style=tab_card)
        ], sm=12, lg=7)
    ], class_name="g-2 my-auto"),


    dbc.Row([ # linha 02
        dbc.Col([ # coluna 01
            dbc.Card([
                dbc.CardBody([
                    html.H3("Preço x Estado"),
                    html.H6("Comparação temporal entre estados"),
                    dbc.Row([
                        dbc.Col([
                            dcc.Dropdown(
                                id="select_estados0",
                                value=[df.at[df.index[3], "ESTADO"], df.at[df.index[6], "ESTADO"], df.at[df.index[13], "ESTADO"]],
                                clearable=False,
                                className="dbc",
                                multi=True,
                                options=[
                                    {"label":x, "value":x} for x in df["ESTADO"].unique()
                            ])
                        ], sm=10)
                    ]),

                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id="animation_graph", config={"displayModeBar":False, "showTips":False})
                        ])
                    ])
                ])
            ], style=tab_card)
        ], sm=12, md=6, lg=5),

        dbc.Col([ # coluna 02
            dbc.Card([
                dbc.CardBody([
                    html.H3("Comparação Direta"),
                    html.H6("Qual preço é menor em um dado período de tempo?"),
                    dbc.Row([
                        dbc.Col([
                            dcc.Dropdown(
                                id="select_estado1",
                                value=df.at[df.index[3], "ESTADO"],
                                clearable=False,
                                className="dbc",
                                options=[
                                    {"label":x, "value":x} for x in df["ESTADO"].unique()
                            ])
                        ], sm=10, md=5),

                        dbc.Col([
                            dcc.Dropdown(
                                id="select_estado2",
                                value=df.at[df.index[1], "ESTADO"],
                                clearable=False,
                                className="dbc",
                                options=[
                                    {"label":x, "value":x} for x in df["ESTADO"].unique()
                            ])
                        ], sm=10, md=5),
                    ], style={"margin-top":"20px"}, justify="center"),

                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id="direct_comparison_graph", config={"displayModeBar":False, "showTips":False}),
                        ])
                    ]),
                    html.P(id="desc_comparison", style={"color":"gray", "font-size":"80%"}),
                ])
            ], style=tab_card)
        ], sm=12, md=6, lg=4),

        dbc.Col([ # coluna 03
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(id="card1_indicators", config={"displayModeBar":False, "showTips": False}, style={"margin-top": "30px"})
                        ])
                    ], style=tab_card)
                ])
            ], justify="center", style={"padding-bottom":"7px", "height":"50%"}),

            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Graph(id="card2_indicators", config={"displayModeBar":False, "showTips": False}, style={"margin-top": "30px"})
                        ])
                    ], style=tab_card)
                ])
            ], justify="center", style={"height":"50%"})
        ], sm=12, lg=3, style={"height":"100%"})
    ], className="g-2 my-auto"),


    dbc.Row([ # linha 03
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            dbc.Button([html.I(className="fa fa-play")], id="play-button", style={"margin-right":"15px"}),
                            dbc.Button([html.I(className="fa fa-stop")], id="stop-button")
                        ], sm=12, md=1, style={"justify-content":"center", "margin-top":"10px"}),

                        dbc.Col([
                            dcc.RangeSlider(
                                id="ranger_slider",
                                marks={int(x): f"{x}" for x in df["ANO"].unique()},
                                step=3,
                                min=df["ANO"].min(),
                                max=df["ANO"].max(),
                                className="dbc",
                                value=[df["ANO"].min(),df["ANO"].max()],
                                dots=True,
                                pushable=3,
                                tooltip={"always_visible":False, "placement":"bottom"},
                            )
                        ], sm=12, md=10, style={"margin-top":"15px"}),

                        dcc.Interval(id="interval", interval=2000),
                    ], className="g-1", style={"height":"20%", "justify-content":"center"})
                ])
            ], style=tab_card)
        ])
    ], className="g-2 my-auto")
], fluid=True, style={"height":"100%"})


if __name__ == "__main__":
    app.run(debug=True)