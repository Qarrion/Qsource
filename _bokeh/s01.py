from bokeh.plotting import figure
from bokeh.layouts import column
from bokeh.models import Button
from bokeh.application import Application
from bokeh.application.handlers.function import FunctionHandler
from bokeh.server.server import Server
from random import randint

def modify_doc(doc):
    # 새로운 플롯 생성
    p = figure(title="Random Data Scatter", x_axis_label='X-Axis', y_axis_label='Y-Axis')
    r = p.circle([], [], size=10, color="navy", alpha=0.5)

    # 버튼 위젯 생성
    button = Button(label="Generate Random Data")

    # 버튼 클릭 시 실행될 콜백 함수 정의
    def update():
        # 새로운 데이터 생성
        new_data = {'x': [randint(0, 10)], 'y': [randint(0, 10)]}

        # 기존 데이터에 새 데이터 추가
        r.data_source.stream(new_data)

    # 버튼에 콜백 함수 연결
    button.on_click(update)

    # 문서에 버튼과 플롯을 포함한 레이아웃 추가
    doc.add_root(column(button, p))

# 애플리케이션 인스턴스 생성
bokeh_app = Application(FunctionHandler(modify_doc))

# 서버 시작
server = Server({'/': bokeh_app}, port=5000)  # 포트 5000에서 시작
server.start()
# 서버가 바로 종료되지 않도록 무한 루프 실행
server.io_loop.start()

