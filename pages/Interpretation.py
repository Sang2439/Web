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
                                [html.H6(["Interpretation & Conclusion"], className="subtitle padded")],
                                className="twelve columns",
                            )
                        ],
                        className="row"
                    ),
                    #row 2
                    html.Div(
                        [
                            html.P(
                                "Netflix's stock price experienced a sharp decline in the first half of 2022."

                            ),
                            html.P(
                                "• Increasing competition from industry rivals such as Disney (DIS), Fox, and others led to a significant loss of subscribers for Netflix."

                            ),
                            html.P(
                                "• The Russia-Ukraine war forced Netflix to abandon the large Russian market, resulting in a loss of revenue."
                            ),
                            html.P(
                                "• Additionally, Netflix's stricter policies on account sharing and price hikes led to a decline in the number of new sign-ups"
                            ),
                            html.P(
                                "As a result, the company's stock price decreased accordingly."
                            ),
                            html.P(
                                "After that period of decline, the stock price recovered and increased again, although not quickly, but rather steadily."
                            )
                        ],
                        className="row",
                        style={"color": "#696969",
                            "font-size": "14px"
                               },
                    ),
                    # row 3
                    html.Div(
                        [
                            html.Div(
                                [html.H6(["Investment recommendation."], className="subtitle padded")],
                                className="twelve columns",
                            )
                        ],
                        className="row"
                    ),
                    #row 4
                    html.Div(
                        [
                            html.P(
                                "Based on the recent recovery and increase in Netflix’s stock price, combined with the analysis using indicators such as SMA, EMA, RSI, etc., investing in Netflix appears to be a wise decision with high growth potential. However, investors should closely monitor market fluctuations to make the most informed decisions."

                            ),

                        ],
                        className="row",
                        style={"color": "#696969",
                            "font-size": "14px"
                               },
                    ),
                    # row 5
                    html.Div(
                        [
                            html.Div(
                                [html.H6(["Future Works"], className="subtitle padded")],
                                className="twelve columns",
                            )
                        ],
                        className="row"
                    ),
                    #row 6
                    html.Div(
                        [
                            html.P(
                                "1. Integrate more types of charts and indicators that provide the best support for investors."

                            ),
                            html.P(
                                "2. AI models have limitations in predicting stock prices over long periods. They perform well in short-term predictions, but predicting too far ahead results in large errors and inaccurate forecasts. The model needs improvement to predict over longer time frames."

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