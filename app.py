import dash
from dash import dcc, html
from dash.dependencies import Input, Output

from pages import (
    compare,
    Dataclean,
    Dtanalyst,
    Interpretation,
    Introduction,
    model,
)

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}],
)
app.title = "Financial Report"
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
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

# Xuất ra file HTML
if __name__ == "__main__":
    # Lấy mã HTML của trang đầu tiên
    html_output = app.index()

    # Lưu vào file HTML
    with open("dashboard_output.html", "w") as f:
        f.write(html_output)

    # Chạy ứng dụng
    app.run(debug=True)
