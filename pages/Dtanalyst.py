import dash
from dash import dcc, html
import plotly.graph_objs as go
from utils import Header, make_dash_table
import pandas as pd
import pathlib
from dash.dependencies import Input, Output, State
from plotly.subplots import make_subplots

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
df_votatility = pd.read_csv(DATA_PATH.joinpath("volatility.csv"))
df_nflx = pd.read_csv(DATA_PATH.joinpath("NFLX_data.csv"))
df_stocks = pd.read_csv(DATA_PATH.joinpath("Stock_data.csv"))
df_describe = pd.read_csv(DATA_PATH.joinpath("descibe.csv"))
df_compara = pd.read_csv(DATA_PATH.joinpath("sma_ema_comparison.csv"))
df_rsi = pd.read_csv(DATA_PATH.joinpath("RSI_description.csv"))

def create_layout(app):
    #Fig2
    # kết hợp MACD với biểu đồ giá cổ phiếu
    colors = ['green' if val >= 0 else 'red' for val in df_nflx['Histogram']]

    fig2 = make_subplots(
        rows=2, cols=1, shared_xaxes=True,
        vertical_spacing=0.1, subplot_titles=('NFLX Price', 'MACD Indicator'),
        row_width=[0.3, 0.7]
    )
    # vẽ biểu đồ cổ phiếu giá
    fig2.add_trace(go.Scatter(x=df_nflx['Date'], y=df_nflx[('Close')], name='Close Price',  line=dict(color='blue')), row=1, col=1)
    fig2.add_trace(go.Scatter(x=df_nflx['Date'], y=df_nflx['Signal'], name='Signal',line=dict(color='red')), row=2, col=1)
    fig2.add_trace(go.Scatter(x=df_nflx['Date'], y=df_nflx['MACD'], name='MACD',line=dict(color='green')), row=2, col=1)
    fig2.add_trace(go.Bar(x=df_nflx['Date'], y=df_nflx['Histogram'],marker_color=colors,name='Histogram'), row=2, col=1)
    fig2.update_layout(
        title='Stock Price and MACD Indicator',
        height=700,
        template='plotly_white',
        font=dict(family='Times New Roman',color='darkblue', size=14),
        hovermode='x unified'
        
    )
    fig2.update_xaxes(
        tickformat='%Y', 
        hoverformat='%d-%m-%Y'
    )
    #Fig1
    # Tạo cột 'YearWeek' nhóm theo tuần
    df_nflx['Date'] = pd.to_datetime(df_nflx['Date'], errors='coerce')

    df_nflx['YearWeek'] = df_nflx['Date'].dt.to_period('W').apply(lambda x: x.start_time)


    # Gộp dữ liệu theo tuần với các phép tính
    weekly = df_nflx.groupby('YearWeek').agg({
        ('Open'): 'first',      # Giá mở đầu tuần
        ('High'): 'max',        # Giá cao nhất tuần
        ('Low'): 'min',         # Giá thấp nhất tuần
        ('Close'): 'last',      # Giá đóng cửa cuối tuần
        ('Volume'): 'sum'       # Tổng volume tuần
    }).reset_index()

    weekly.rename(columns={'YearWeek': 'Date'}, inplace=True)
    fig1 = make_subplots(
    rows=2, cols=1, shared_xaxes=True,
    vertical_spacing=0.10, subplot_titles=('NFLX', 'Volume'),
    row_width=[0.3, 1]
)

    fig1.add_trace(
        go.Candlestick(x=weekly['Date'], open=weekly[('Open')],
            high=weekly[('High')], low=weekly[('Low')],
            close=weekly[('Close')], name='OHLC'
        ),
        row=1, col=1
    )
    # Volume bar theo tuần
    fig1.add_trace(
        go.Bar(
            x=weekly['Date'],
            y=weekly[('Volume')],
            marker=dict(color='#FF0000', opacity=1),
            showlegend=False,
            name="NFLX Volume"
        ),
        row=2, col=1
    )

    # Cập nhật layout
    fig1.update_layout(
        title='NFLX Price Chart',

        xaxis=dict(
            tickfont=dict(size=12)
        ),

        yaxis=dict(
            title=dict(
                text='Price ($/share)',
                font=dict(size=14)
            ),
            tickfont=dict(size=12)
        ),

        autosize=True,
        margin=dict(l=50, r=50, b=100, t=100, pad=4),
        paper_bgcolor='white',

        template='plotly_white',
        font=dict(family='Times New Roman',color='darkblue', size=14),
        hovermode='x unified'
    )

    fig1.update_xaxes(
        tickformat='%d-%m-%Y', 
        hoverformat='%d-%m-%Y'
    )

    fig1.update_xaxes(visible=False, row=2, col=1)
    fig1.update(layout_xaxis_rangeslider_visible=False)
    #fig0
    df_nflx["Date"] = pd.to_datetime(df_nflx["Date"], errors='coerce')
    fig = make_subplots(
        rows=2, cols=1, shared_xaxes=True,
        row_heights=[0.7, 0.3],
        vertical_spacing=0.05,
        subplot_titles=("Stock Price with Envelope", "RSI (14-day)")
    )

    # Thêm các trace, shapes, annotation
    fig.add_trace(go.Scatter(x=df_nflx[("Date")], y=df_nflx[('Close')], name='Close Price'), row=1, col=1)
    fig.add_trace(go.Scatter(x=df_nflx["Date"], y=df_nflx['SMA_20'], name='SMA 20'), row=1, col=1)
    fig.add_trace(go.Scatter(x=df_nflx["Date"], y=df_nflx['Lower_Envelope'], line=dict(width=0), showlegend=False), row=1, col=1)
    fig.add_trace(go.Scatter(
        x=df_nflx["Date"], y=df_nflx['Upper_Envelope'], fill='tonexty',
        fillcolor='rgba(0, 100, 80, 0.2)', name='Envelope Range',
        line=dict(dash='dot', color='rgba(0,100,80,0.5)')
    ), row=1, col=1)

    fig.add_trace(go.Scatter(x=df_nflx["Date"], y=df_nflx['RSI'], name='RSI', line=dict(color='orange')), row=2, col=1)

    fig.add_shape(type='line', x0=df_nflx["Date"].min(), x1=df_nflx["Date"].max(), y0=70, y1=70,
                  line=dict(color='red', dash='dash'), row=2, col=1)
    fig.add_shape(type='line', x0=df_nflx["Date"].min(), x1=df_nflx["Date"].max(), y0=30, y1=30,
                  line=dict(color='green', dash='dash'), row=2, col=1)

    fig.update_layout(
        title='Stock Price and RSI (Interactive)',
        height=700,
        template='plotly_white',
        font=dict(family='Times New Roman', color='darkblue', size=14),
        hovermode='x unified'
    )

    fig.add_annotation(
        x=df_nflx["Date"].max(), y=70,
        xref='x2', yref='y2',
        text='70 (Overbought)',
        showarrow=False,
        font=dict(color='red', size=12),
        xanchor='left',
        yanchor='bottom'
    )

    fig.add_annotation(
        x=df_nflx["Date"].max(), y=30,
        xref='x2', yref='y2',
        text='30 (Oversold)',
        showarrow=False,
        font=dict(color='green', size=12),
        xanchor='left',
        yanchor='top'
    )
    fig.update_yaxes(title_text="Price", row=1, col=1)
    fig.update_yaxes(title_text="RSI", range=[0, 100], row=2, col=1)
    fig.update_xaxes(
        tickformat='%Y', 
        hoverformat='%d-%m-%Y'
    )

    return html.Div(
        [
            Header(app),
            #page 3
            html.Div(
                [
                    # row 1
                    html.Div(
                        [
                            html.Div(
                                [html.H6(["Describe of Netflix"], className="subtitle padded")],
                                className="twelve columns",
                            )
                        ],
                        className="row"
                    ),
                    # row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Strong(),
                                    html.Table(make_dash_table(df_describe)),
                                ]
                            )
                        ],
                        className="row"
                    ),
                    #row3
                    html.Div(
                        [
                            html.P(
                                "• Strong price volatility: The standard deviation of the price columns (Close, High, Low, Open) is quite high (around 170), indicating that this stock experienced significant price fluctuations during the observed period."

                            ),
                            html.P(
                                "• Wide price range: The difference between the minimum and maximum values is very large, showing that the stock has undergone both strong growth phases and deep corrections."

                            ),
                            html.P(
                                "• Good liquidity: The average trading volume is fairly high and the maximum value is very large, indicating that the stock has good liquidity and is easy to buy and sell."

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
                            html.Div(
                                [
                                    html.H6(["Stock Closing Price"], className="subtitle padded")
                                ],
                                className="twelve columns",
                            ),
                        ],
                        className="row"
                    ),
                    #row5
                    html.Div(
                        html.Div(
                            [
                                dcc.Graph(
                                    id='stock-price-line-chart',
                                    figure={
                                        'data': [
                                            go.Scatter(
                                                x=df_nflx["Date"],  # Trục x: ngày tháng
                                                y=df_nflx[('Close')],  # Trục y: giá cổ phiếu
                                                mode='lines',          # Vẽ đường liên tục
                                                name='Price'
                                            )
                                        ],
                                        'layout': go.Layout(
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
                                    }
                                ),
                            ],
                            className="twelve columns"
                        )
                    ),
                    #row6
                    html.Div(
                        [
                            html.P(
                                "• The stock experienced significant volatility from late 2021 to early 2023. The stock price underwent a sharp decline, followed by signs of gradual recovery."
                            ),
                        ],
                        className="row",
                        style={"color": "#696969",
                               "font-size": "14px"
                               },
                    ),
                    #row 7ver 2
                    html.Div(
                        [
                            html.Div(
                                [html.H6(["Histogram of Simple Return"], className="subtitle padded")],
                                className="twelve columns",
                            )
                        ],
                        className="row"
                    ),
                    # row 7ver 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Img(
                                        src=app.get_asset_url("dailydistribution.png"),
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
                                "• Based on the chart, we can observe that the daily return index has a left-skewed distribution, with most values falling within the range of -0.05 to 0.05. This suggests that the majority of trading days experience small increases or decreases, with only a few days showing larger fluctuations. Additionally, there are still some outliers with significant negative returns."

                            ),
                        ],
                        className="row",
                        style={"color": "#696969",
                            "font-size": "14px"
                               },
                    ),
                    html.Div(
                        [
                            html.Div(
                                [html.H6(["Volatility"], className="subtitle padded")],
                                className="twelve columns",
                            )
                        ],
                        className="row"
                    ),
                    html.Div(
                        html.Div(
                            [
                                dcc.Graph(
                                    id='price-chart',
                                    figure={
                                        'data': [
                                            go.Scatter(
                                                x=df_votatility['Date'],
                                                y=df_votatility[('Volatility')],
                                                name='Close Price',
                                                mode='lines'
                                            ),
                                        ],
                                        'layout': go.Layout(
                                            title='Volatility',
                                            xaxis={
                                                'title': 'Year',        
                                                'tickformat': '%Y',     
                                                'hoverformat': '%d-%m-%Y',  
                                                'dtick': 'M12'           
                                            },
                                            yaxis={'title': 'Volatility'},
                                            hovermode='x',
                                            height=500,
                                            margin=dict(l=40, r=40, t=60, b=40),
                                            font=dict(family='Times New Roman', color='darkblue', size=14),
                                        ),
                                    },
                                ),
                            ],
                            className="row"
                        )
                    ),
                    html.Div(
                        [
                            html.P(
                                "• Based on the chart, we can observe that the stock price volatility in 2022 was high, with the volatility index exceeding 30%. This indicates significant instability in the stock price during this period."

                            ),
                            html.P(
                                "• Additionally, starting from 2024, the stock price volatility ranged from 10% to 20%, which suggests a more stable period with less sharp fluctuations in the stock price during this time."

                            ),
                        ],
                        className="row",
                        style={"color": "#696969",
                            "font-size": "14px"
                               },
                    ),
                    #row7
                    html.Div(
                        [
                            html.Div(
                                [html.H6(["Moving SMA"], className="subtitle padded")],
                                className="twelve columns",
                            )
                        ],
                        className="row"
                    ),
                    #row8
                    html.Div(
                        html.Div(
                            [
                                dcc.Graph(
                                    id='price-chart',
                                    figure={
                                        'data': [
                                            go.Scatter(
                                                x=df_nflx['Date'],
                                                y=df_nflx[('Close')],
                                                name='Close Price',
                                                mode='lines'
                                            ),
                                            go.Scatter(
                                                x=df_nflx['Date'],
                                                y=df_nflx['SMA_20'],
                                                name='SMA 20',
                                                mode='lines'
                                            ),
                                            go.Scatter(
                                                x=df_nflx['Date'],
                                                y=df_nflx['Lower_Envelope'],
                                                line=dict(width=0),
                                                showlegend=False,
                                                mode='lines',
                                                name="Envelope Lower"
                                            ),
                                            go.Scatter(
                                                x=df_nflx['Date'],
                                                y=df_nflx['Upper_Envelope'],
                                                fill='tonexty',
                                                fillcolor='rgba(0, 100, 80, 0.2)',
                                                name='Envelope Upper',
                                                line=dict(dash='dot', color='rgba(0,100,80,0.5)'),
                                                mode='lines',
                                            ),
                                        ],
                                        'layout': go.Layout(
                                            title='Moving Average',
                                            xaxis={
                                                'title': 'Year',        
                                                'tickformat': '%Y',     
                                                'hoverformat': '%d-%m-%Y',  
                                                'dtick': 'M12'           
                                            },
                                            yaxis={'title': 'Price'},
                                            hovermode='x',
                                            height=500,
                                            margin=dict(l=40, r=40, t=60, b=40),
                                            font=dict(family='Times New Roman', color='darkblue', size=14),
                                        ),
                                    },
                                ),
                            ],
                            className="row"
                        )
                    ),
                    #row9
                    html.Div(
                        [
                            html.P(
                                "• Main function: Helps eliminate short-term noise and clarify the overall trend."
                            ),
                            html.P(
                                "• Meaning: Prices in the market often fluctuate erratically. The SMA calculates the average price over a specific period, helping traders see the trend (upward, downward, or sideways) more clearly."
                            ),
                            html.P(
                                "• Based on the SMA_20 line, we observe that stock prices below the SMA_20 tend to show a downward trend. Conversely, stock prices above the SMA_50 often tend to rise further."
                            ),
                            html.P(
                                "• Envelope lines help investors easily identify overbought and oversold levels of a stock. Additionally, they indicate the market’s volatility. When the two envelope lines are close together, it reflects market stability, whereas when the lines widen, it indicates strong market volatility."
                            )
                        ],
                        className="row",
                        style={"color": "#696969",
                            "font-size": "14px"
                               },
                    ),
                    #row 10
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(["Compare SMA and EMA"], className="subtitle padded")
                                ],
                                className="twelve columns",
                            ),
                        ],
                        className="row"
                    ),
                    #row 12
                    html.Div(
                        html.Div(
                            [
                                dcc.Graph(
                                    id='price-chart',
                                    figure={
                                        'data': [
                                            go.Scatter(
                                                x=df_nflx['Date'],
                                                y=df_nflx[('Close')],
                                                name='Close Price',
                                                mode='lines'
                                            ),
                                            go.Scatter(
                                                x=df_nflx['Date'],
                                                y=df_nflx['SMA_50'],
                                                name='SMA 50',
                                                mode='lines'
                                            ),
                                            go.Scatter(
                                                x=df_nflx['Date'],
                                                y=df_nflx['EMA_50'],
                                                name='EMA 50',
                                                mode='lines'
                                            )
                                        ],
                                        'layout': go.Layout(
                                            title='Moving Average SMA And EMA',
                                            xaxis={
                                                'title': 'Year',        
                                                'tickformat': '%Y',     
                                                'hoverformat': '%d-%m-%Y',  
                                                'dtick': 'M12'           
                                            },
                                            yaxis={'title': 'Price'},
                                            hovermode='x',
                                            height=500,
                                            margin=dict(l=40, r=40, t=60, b=40),
                                            font=dict(family='Times New Roman', color='darkblue', size=14),
                                        ),
                                    },
                                ),
                            ],
                            className="row"
                        )
                    ),
                    #row 13
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Strong(),
                                    html.Table(make_dash_table(df_compara)),
                                ]
                            )
                        ],
                        className="row"
                    ),
                    #row 14
                    html.Div(
                        [
                            html.H6(["Stock Price and RSI (Interactive)"], className="subtitle padded"),
                            dcc.Graph(
                                id='price-rsi-chart',
                                figure=fig,
                                style={'height': '700px'}
                            )
                        ],
                        className="row"
                    ),
                    #row15
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Strong(),
                                    html.Table(make_dash_table(df_rsi)),
                                ]
                            )
                        ],
                        className="row"
                    ),
                    #row 16
                    html.Div(
                        [
                            html.H6(["Candlestick chart"], className="subtitle padded"),
                            dcc.Graph(
                                id='price-rsi-chart',
                                figure=fig1,
                                style={'height': '700px'}
                            )
                        ],
                        className="row"
                    ),
                    #row17
                    html.Div(
                        [
                            html.P(
                                "• Based on the chart, we can observe a sharp decline in the stock price at the beginning of 2022, indicated by the long red candles. This downtrend continued until mid-2022, after which the appearance of green candles began to emerge. However, the length of the green candles remained short, and there was resistance from the red candles. Nonetheless, the overall trend showed a steady upward movement in the stock price."
                            ),
                        ],
                        className="row",
                        style={"color": "#696969",
                            "font-size": "14px"
                               },
                    ),
                    #row 18
                    html.Div(
                        [
                            html.H6(["Stock Price and MACD"], className="subtitle padded"),
                            dcc.Graph(
                                id='price-rsi-chart',
                                figure=fig2,
                                style={'height': '700px'}
                            )
                        ],
                        className="row"
                    ),
                    #row19
                    html.Div(
                        [
                            html.P(
                                "The MACD indicator provides signals for market trends:"
                            ),
                            html.P(
                                "• When the MACD line > Signal line (green histogram), the market is in an uptrend."
                            ),
                            html.P(
                                "• When the MACD line < Signal line (red histogram), the market is in a downtrend."
                            ),
                            html.P(
                                "It helps investors make decisions to buy stocks."
                            ),
                        ],
                        className="row",
                        style={"color": "#696969",
                            "font-size": "14px"
                               },
                    ),      
                            
                ],
                className="sub_page",
            ),
        ],
        className="page"
    )