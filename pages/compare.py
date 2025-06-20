from dash import dcc, html
import plotly.graph_objs as go
from utils import Header, make_dash_table
import pandas as pd
import numpy as npa
import pathlib
from scipy.stats import gaussian_kde
# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df_stocks = pd.read_csv(DATA_PATH.joinpath("Stock_data.csv"))
def create_layout(app):  
    list_stock = ['NFLX', 'DIS', 'LYV', 'TKO', 'FOX']
    # price close
    symbols = df_stocks.columns[1:5]
    stock_traces = []

    for symbol, ticker in zip(symbols, list_stock):
        stock_traces.append(
            go.Scatter(
                x=df_stocks['Date'],        
                y=df_stocks[symbol],              
                mode='lines',                     
                name= ticker                    
            )
        )

    layout = go.Layout(
        title='Stock Price Over Time', 
        xaxis={
            'title': 'Year',          
            'tickformat': '%Y',      
            'hoverformat': '%d-%m-%Y', 
            'dtick': 'M12'              
        },
        yaxis={'title': 'Price (USD)'},  
        hovermode='closest',             
        font=dict(family='Times New Roman', color='darkblue', size=14),  
    )
    return html.Div(
        [
            Header(app),
            #page3
            html.Div(
                [
                    # row 1
                    html.Div(
                        [
                            html.Div(
                                [html.H6(["Compare with companies in the entertainment industry."], className="subtitle padded")],
                                className="twelve columns",
                            )
                        ],
                        className="row"
                    ),
                    # row2
                    html.Div(
                        [
                            dcc.Graph(
                                id='stock-price-line-chart',
                                figure={
                                    'data': stock_traces,  
                                    'layout': layout      
                                }
                            ),
                        ],
                        className="twelve columns"
                    ),
                    #row3
                    html.Div(
                        [
                            html.P(
                                "• The stock of Netflix can experience significant volatility. Stocks of other companies in the same industry tend to be less volatile. This is because Netflix was established earlier than its competitors and thus managed to dominate a large portion of the market. However, other companies are now intensifying their competition with Netflix."

                            ),
                        ],
                        className="row",
                        style={"color": "#696969",
                            "font-size": "14px"
                               },
                    ),
                    # row4
                    html.Div(
                        [
                            html.Div(
                                [html.H6(["KDE Daily Return of entertainment industry"], className="subtitle padded")],
                                className="twelve columns",
                            )
                        ],
                        className="row"
                    ),
                    # row5
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Img(
                                        src=app.get_asset_url("KDE_daily_return.png"),
                                        className='twenty columns',
                                    ),
                                ],
                            ),
                        ],
                        className='row'
                    ),
                    # row 6
                    html.Div(
                        [
                            html.P(
                                "• Based on the KDE plot of daily returns, we can observe that Netflix's profit variability is high. In contrast, the profit volatility of Disney and Fox is relatively stable, with minimal fluctuations and differences."

                            ),
                        ],
                        className="row",
                        style={"color": "#696969",
                            "font-size": "14px"
                               },
                    ),
                    # row 7
                    html.Div(
                        [
                            html.Div(
                                [html.H6(["Correlation of Stock Price Volatility"], className="subtitle padded")],
                                className="twelve columns",
                            )
                        ],
                        className="row"
                    ),
                    # row 8
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Img(
                                        src=app.get_asset_url("warm.png"),
                                        className='twenty columns',
                                    ),
                                ],
                            ),
                        ],
                        className='row'
                    ),
                    html.Div(
                        [
                            html.P(
                                "The chart shows the correlation between the stocks:"

                            ),
                            html.P(
                                "• The highest correlation is between DIS and FOX, with a value of 0.45."

                            ),
                            html.P(
                                "• The lowest correlation is between NFLX and TKO, with a value of 0.18."

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
        className="page"
    )