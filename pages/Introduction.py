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
                                [
                                    html.H6(
                                        ["Topic: Analysis of stock price fluctuations"],
                                        # className="subtitle padded",
                                        style={'fontSize': '20px', 'textAlign': 'center'} 
                                    )
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row",
                    ),
                    #row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Target"],
                                        className="subtitle padded",
                                        style={'fontSize': '20px'} 
                                    )
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row",
                    ),
                    #row 3
                    html.Div(
                        [
                            html.P(
                                "1. Develop skills in interpreting results and drawing conclusions based on data."

                            ),
                            html.P(
                                "2. Analyze and evaluate the fundamental information about stocks."

                            ),
                            html.P(
                                "3. Forecast and make investment recommendations for the future."

                            ),
                        ],
                        className="row",
                        style={"color": "#696969",
                            "font-size": "14px"
                               },
                    ),
                    #row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Netflix: The Streaming Giant."],
                                        className="subtitle padded",
                                        style={'fontSize': '20px'} 
                                    )
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row",
                    ),
                    #row 5
                    html.Div(
                        [
                            html.P(
                                "Netflix is a popular online streaming service that offers a vast library of content, including movies, TV series, documentaries, reality shows, and original programming. The service allows users to watch video on demand (VOD) across various platforms such as computers, smartphones, smart TVs, gaming consoles, and many other devices."

                            ),
                            html.P(
                                "This report will analyze Netflix's stock price and its business performance over the recent years( the period from January 1, 2021 to January 2, 2025).",
                                style={
                                    'font-size': '16px',   
                                    'font-weight': 'bold',
                                }
                            )
                        ],
                        className="row",
                        style={"color": "#696969",
                            "font-size": "14px"
                               },
                    ),
                    # row 6
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Summary of Main Contents"],
                                        className="subtitle padded",
                                        style={'fontSize': '20px'} 
                                    )
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row",
                    ),
                    #row7
                    html.Div(
                        [
                            html.P(
                                "• Data Cleaning & Processing"

                            ),
                            html.P(
                                "• Data Analysis"

                            ),
                            html.P(
                                "• Compare"
                            ),
                            html.P(
                                "• Modeling"
                            ),
                            html.P(
                                "• Conclusion"
                            ),
                        ],
                        className="row",
                        style={"color": "#696969",
                            "font-size": "14px"
                               },
                    ),
                ],
                className="sub_page"
            ),
        ],
        className="page"
    )