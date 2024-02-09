import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui

class Qcandle(pg.GraphicsObject):
    def __init__(self, data):
        pg.GraphicsObject.__init__(self)

        self.cmap = {"inc": "g", "des": "r"}
        self.w_body = 0.8
        self.w_tail = 0.05

        self.data = data
        self.draw()

    def draw(self):
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)

        w_body = 1 * self.w_body / 2
        w_tail = 1 * self.w_tail / 2

        for I, (T, O, H, L, C, V) in enumerate(self.data):
            if O > C:
                col = self.cmap['des']
                p.setPen(pg.mkPen(col))
                p.setBrush(pg.mkBrush(col))
            else:
                col = self.cmap['inc']
                p.setPen(pg.mkPen(col))
                p.setBrush(pg.mkBrush(col))

            p.drawRect(QtCore.QRectF(I - w_body, O, w_body * 2, C - O))
            # p.drawRect(QtCore.QRectF(I - w_tail, L, w_tail * 2, H - L))
            p.drawLine(QtCore.QPointF(I, H), QtCore.QPointF(I, L))
        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())


if __name__ == '__main__':
    import pandas as pd

    data = pd.read_excel('AAPL.xlsx', index_col=0)
    data.index.name = 'DT'
    data = data.drop(columns=['Adj Close'])
    data.columns = ['O', 'H', 'L', 'C', 'V']

    item = Qcandle(data.to_records())
    plt = pg.plot()
    plt.resize(800, 400)
    plt.setWindowTitle('pyqtgraph example: customGraphicsItem')


    vbx = plt.getViewBox()
    vbx.setXRange(300, 450) # 보여지는 위치
    vbx.setMouseEnabled(x=True, y=False)  # 마우스로 조작 가능 여부

    # plt.setXRange(100, 120)  # 보여지는 위
    vbx.enableAutoRange(axis=pg.ViewBox.YAxis)
    vbx.setAutoVisible(x=False, y=True)

    # plt.enableAutoRange('y',1)
    # plt.hideAxis('left')  # Y 축 숨기기
    plt.addItem(item)
    pg.exec()

    # app = pg.mkQApp()
    # vb = pg.ViewBox()
    # vb.setXRange(300, 450)
    # vb.setMouseEnabled(x=True, y=False)
    # # vb.enableAutoRange(x=False, y=True)
    # vb.setAutoVisible(x=False, y=True)
    # pw = pg.PlotWidget(title='Sine Wave', viewBox =vb)
    # pw.addItem(item)
    # pw.show()

    # pg.exec()