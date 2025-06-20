import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

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
    # Mở server Dash
    app.run(debug=True)
  # set use_reloader=False để tránh lỗi khi dùng Selenium

    # Sử dụng Selenium để lấy mã HTML sau khi server đã chạy
    time.sleep(2)  # Đợi server khởi động

    # Tạo kết nối đến Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8050/")  # Địa chỉ của ứng dụng Dash đang chạy

    # Lấy mã HTML của trang
    html_output = driver.page_source

    # Lưu mã HTML vào file
    with open("dashboard_output.html", "w") as f:
        f.write(html_output)

    driver.quit()  # Đóng trình duyệt sau khi lấy HTML
