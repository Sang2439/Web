import dash
from dash import dcc, html


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [

            html.Div(
                [
                    html.Div(
                        [html.H5("Report on Netflix Stock Analysis")],
                        className="seven columns main-title",
                    ),
                    
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Overview",
                href="/dash-financial-report/Overview",
                className="tab"
            ),
            dcc.Link(
                "Data Cleaning & Processing",
                href="/dash-financial-report/DataCleaning",
                className="tab",
            ),
            dcc.Link(
                "Data Analysis",
                href="/dash-financial-report/DataAnalysis",
                className="tab",
            ),
            dcc.Link(
                "Compare",
                href="/dash-financial-report/Compare",
                className="tab"
            ),
            dcc.Link(
                "Modeling",
                href="/dash-financial-report/Modeling",
                className="tab",
            ),
            dcc.Link(
                "Conclusion",
                href="/dash-financial-report/Conclusion",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu

def make_dash_table(df):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in df.columns])
        ),
        html.Tbody([
            html.Tr([html.Td(row[col]) for col in df.columns])
            for _, row in df.iterrows()
        ])
    ])