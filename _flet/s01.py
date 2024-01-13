import flet

def main(page):
    # Bokeh 서버의 URL 설정
    bokeh_server_url = "http://localhost:5000/"

    # Flet의 WebView 위젯 생성 및 설정
    webview = flet.WebView(url=bokeh_server_url, width=800, height=600)

    # 페이지에 WebView 추가
    page.add(webview)

# Flet 앱 실행
flet.app(target=main)