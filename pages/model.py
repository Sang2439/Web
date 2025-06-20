from dash import dcc, html
import plotly.graph_objs as go
from utils import Header, make_dash_table
import pandas as pd
import pathlib
# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df_nflx = pd.read_csv(DATA_PATH.joinpath("NFLX_data.csv"))
df_stocks = pd.read_csv(DATA_PATH.joinpath("Stock_data.csv"))
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
                                        ["Build an LSTM model to predict the price of a stock."],
                                        className="subtitle padded",
                                        style={'fontSize': '18px'}  # Center the text and increase font size
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
                            html.P(
                                [
                                    "Step 1: Standardize data"
                                ],
                                style={'fontSize': '14px'}
                            )
                        ],
                        className='row'
                    ),
                    #row3
                    html.Div(
                        [
                            html.P(
                                "• Use MinMaxScaler to normalize the data into the range [0, 1], which helps to increase the efficiency of model training."
                            ),
                        ],
                        className="row",
                        style={"color": "#696969",
                            "font-size": "14px"
                               },
                    ),
                    #row4
                    html.Div(
                        [
                            html.P(
                                [
                                    "Step 2: Preparing data for LSTM"
                                ],
                                style={'fontSize': '14px'}
                            )
                        ],
                        className='row'
                    ),
                    #row 5
                    html.Div(
                        [
                            html.P(
                                "• We need to prepare the data to train the model."
                            ),
                        ],
                        className="row",
                        style={"color": "#696969",
                            "font-size": "14px"
                               },
                    ),
                    #row6
                    html.Div(
                        [
                            html.P(
                                [
                                    "Step 3: Build the LSTM model"
                                ],
                                style={'fontSize': '14px'}
                            )
                        ],
                        className='row'
                    ),
                    # row 7
                    html.Div(
                        [
                            html.P(
                                "• To build an LSTM model using Python, we can use the Keras library, which is part of TensorFlow. Keras provides high-level APIs for building and training models, and it includes a built-in LSTM layer."
                            ),
                        ],
                        className="row",
                        style={"color": "#696969",
                            "font-size": "14px"
                               },
                    ),
                    #row 8
                    html.Div(
                        [
                            html.P(
                                [
                                    "Step 4: Training LSTM model"
                                ],
                                style={'fontSize': '14px'}
                            )
                        ],
                        className='row'
                    ),
                    #row 9
                    html.Div(
                        [
                            html.P(
                                "• Train the model with the training data that we created in step 2."
                            ),
                        ],
                        className="row",
                        style={"color": "#696969",
                            "font-size": "14px"
                               },
                    ),
                    #row 10
                    html.Div(
                        [
                            html.P(
                                [
                                    "Step 5: Evaluate the model"
                                ],
                                style={'fontSize': '14px'}
                            )
                        ],
                        className='row'
                    ),
                    # row11
                    html.Div(
                        [
                            html.P(
                                "• Evaluate the accuracy and the errors that the model may cause. Plot a graph to verify the model we have trained."
                            ),
                        ],
                        className="row",
                        style={"color": "#696969",
                            "font-size": "14px"
                               },
                    ),
                    #row12
                    html.Div(
                        [
                            html.P(
                                [
                                    "Step 6: Future Stock Price Prediction"
                                ],
                                style={'fontSize': '14px'}
                            )
                        ],
                        className='row'
                    ),
                    # row 13
                    html.Div(
                        [
                            html.P(
                                "• Once the model is trained and optimized, we can use the model to predict future stock prices."
                            ),
                        ],
                        className="row",
                        style={"color": "#696969",
                            "font-size": "14px"
                               },
                    ),
                    #row14
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["LSTM model to predict the price of a stock."],
                                        className="subtitle padded",
                                        style={'fontSize': '18px'}  # Center the text and increase font size
                                    )
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row",
                    ),
                    #row15
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Img(
                                        src=app.get_asset_url("lsmt.png"),
                                        className='twenty columns',
                                    ),
                                ],
                            ),
                        ],
                        className='row'
                    ),
                    #row16
                    html.Div(
                        [
                            html.P(
                                "• Test set fit score: 0.9837117115271493"

                            ),
                            html.P(
                                "• Mean absolute error of the test set: 9.040425922147078"

                            ),
                            html.P(
                                "• Mean absolute percentage error of the test set: 1.3036331951561007"

                            ),
                        ],
                        className="row",
                        style={"color": "#696969",
                            "font-size": "14px"
                               },
                    ),
                    #row 17
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Limitations of the model."],
                                        className="subtitle padded",
                                        style={'fontSize': '18px'}  # Center the text and increase font size
                                    )
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row",
                    ),
                    # row 18
                    html.Div(
                        [
                            html.P(
                                "• Model AI cannot predict stock prices for distant future points. The forecast may deviate significantly from the actual price."

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