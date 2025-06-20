from dash import dcc, html
import plotly.graph_objs as go
from utils import Header, make_dash_table
import pandas as pd
import pathlib
# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
def create_layout(app):
    return html.Div(
        [
            Header(app),
            #page
            html.Div(
                [
                    #row 1
                    html.Div(
                        [
                            html.Div(
                                [html.H6(["Date Clean"], className="subtitle padded")],
                                className="twelve columns",
                            )
                        ],
                        className="row"
                    ),
                    #row2
                    html.Div(
                        [
                            html.P(
                                "• Handling missing values. In the process of calculating the indicators, if there are any NaN values, replace them with 0."

                            ),
                            html.P(
                                "• Convert date column to datetime format."

                            ),
                            html.P(
                                "• Convert Date column to index."

                            ),
                        ],
                        className="row",
                        style={"color": "#696969",
                            "font-size": "14px"
                               },
                    ),
                    #row 3
                    html.Div(
                        [
                            html.Div(
                                [html.H6(["Calculate basic technical indicators."], className="subtitle padded")],
                                className="twelve columns",
                            )
                        ],
                        className="row"
                    ),
                    #row4
                    html.Div(
                        [
                            html.P(
                                "• Calculate the 20-day and 50-day Simple Moving Averages (SMA)"

                            ),
                            html.P(
                                "• Calculate the 20-day Exponential Moving Average(EMA)"

                            ),
                            html.P(
                                "• Calculate Relative Strength Index(RSI)"
                            ),
                            html.P(
                                "• Calculate MACD Indicator"
                            ),
                            html.P(
                                "• Calculate Daily Return."
                            ),
                            html.P(
                                "• Calculate the quarterly Volatility."
                            ),

                        ],
                        className="row",
                        style={"color": "#696969",
                            "font-size": "14px"
                               },
                    ),

                ],
                className='sub_page'
            ),
        ],
        className='page'
    )