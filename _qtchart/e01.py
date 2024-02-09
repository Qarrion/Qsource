# https://toylee.net/pyqt6-qgraphicsview-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0/

import sys
from PySide6.QtCore import Qt, QPointF
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsView
from PySide6.QtCharts import QChart, QValueAxis, QChartView, QLineSeries
from PySide6.QtGui import QPainter, QWheelEvent, QMouseEvent

import numpy as np

class SimpleChart(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple Chart Example")
        self.setGeometry(100, 100, 800, 600)
        self.lastPoint = None
        # ------------------------------- Chart ------------------------------ #
        self.chart = QChart()
        self.chart.setTitle("Simple Line Chart")

        # ------------------------------ Series ------------------------------ #
        series = QLineSeries()
        series.setName("Line Chart")


        x = np.arange(1000, dtype=float)
        y = np.random.normal(size=1000)
        y += 5 * np.sin(x/100) 
        # Add data points to the series
        for i in range(len(x)):
                series.append(x[i], y[i])


        # Add the series to the chart
        self.chart.addSeries(series)

        # ------------------------------- Axis ------------------------------- #
        # Create an axis for the X-axis
        self.axis_x = QValueAxis()
        self.axis_x.setLabelFormat("%d")
        self.axis_x.setTickCount(5)
        self.axis_x.setTitleText("X-axis")
        self.chart.addAxis(self.axis_x, Qt.AlignmentFlag.AlignBottom)
        series.attachAxis(self.axis_x)

        # Create an axis for the Y-axis
        self.axis_y = QValueAxis()
        self.axis_y.setLabelFormat("%.1f")
        self.axis_y.setTickCount(6)
        self.axis_y.setTitleText("Y-axis")
        self.chart.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)
        series.attachAxis(self.axis_y)

        # ----------------------------- ChartView ---------------------------- #
        # Create a chart view and set the chart
        # self.chart_view = QChartView(self.chart)
        # self.chart_view.setRenderHint(QPainter.Antialiasing)  # Enable antialiasing for smooth lines
        self.chart_view = ChartView(self.chart)

        self.setCentralWidget(self.chart_view)

    def wheelEvent(self, event: QWheelEvent):
        print(self.axis_x.min())
        print(self.axis_x.max())

        if event.angleDelta().y() > 0:
            self.chart_view.chart().zoomIn()
        else:
            self.chart_view.chart().zoomOut()
        
class ChartView(QChartView):
    def __init__(self, chart):
        super().__init__(chart)
        self.setRenderHint(QPainter.Antialiasing)
        self.isDragging = False
        self.lastMousePosition = QPointF()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.isDragging = True
            self.lastMousePosition = event.position()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.isDragging:
            currentPosition = event.position()
            dx = currentPosition.x() - self.lastMousePosition.x()
            dy = currentPosition.y() - self.lastMousePosition.y()
            self.chart().scroll(-dx, dy)
            self.lastMousePosition = currentPosition

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.isDragging = False




if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = SimpleChart()
    window.show()
    sys.exit(app.exec())