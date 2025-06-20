import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

from pages import (
    compare,
    Dataclean,
    Dtanalyst,
    Interpretation,
    Introduction,
    model,
)

app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])
app.title = "Financial Report"
server = app.server

app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/dash-financial-report/Overview":
        return Introduction.create_layout(app)
    elif pathname == "/dash-financial-report/DataCleaning":
        return Dataclean.create_layout(app)
    elif pathname == "/dash-financial-report/DataAnalysis":
        return Dtanalyst.create_layout(app)
    elif pathname == "/dash-financial-report/Compare":
        return compare.create_layout(app)
    elif pathname == "/dash-financial-report/Modeling":
        return model.create_layout(app)
    elif pathname == "/dash-financial-report/Conclusion":
        return Interpretation.create_layout(app)
    elif pathname == "/dash-financial-report/full-view":
        return (
            Introduction.create_layout(app),
            Dataclean.create_layout(app),
            Dtanalyst.create_layout(app),
            compare.create_layout(app),
            model.create_layout(app),
            Interpretation.create_layout(app),
        )
    else:
        return Introduction.create_layout(app)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8050))
    # Mở server Dash
    app.run(debug=True)

