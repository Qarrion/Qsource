import sys
import pyqtgraph as pg
from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # pyqtgraph 그래프 위젯 생성
        graphWidget = pg.PlotWidget()
        self.setCentralWidget(graphWidget)

        # 그래프 데이터 설정
        hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

        # 그래프에 데이터 추가
        graphWidget.plot(hours, temperature)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())