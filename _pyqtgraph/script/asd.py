from PySide6 import QtWidgets, QtCore
import pyqtgraph as pg
import sys  # sys는 QApplication에 argv를 전달하기 위해 필요
import os

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

        # 백그라운드 색상을 흰색으로 설정
        self.graphWidget.setBackground('w')
        # 제목 추가
        self.graphWidget.setTitle("Your Title Here", color="b", size="30pt")
        # 축 레이블 추가
        styles = {"color": "#f00", "font-size": "20px"}
        self.graphWidget.setLabel("left", "Temperature (°C)", **styles)
        self.graphWidget.setLabel("bottom", "Hour (H)", **styles)
        # 범례 추가
        self.graphWidget.addLegend()
        # 그리드 추가
        self.graphWidget.showGrid(x=True, y=True)
        # 범위 설정
        self.graphWidget.setXRange(0, 10, padding=0)
        self.graphWidget.setYRange(20, 55, padding=0)

        pen = pg.mkPen(color=(255, 0, 0))
        self.graphWidget.plot(hour, temperature, name="Sensor 1", pen=pen, symbol='+', symbolSize=30, symbolBrush=('b'))

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()