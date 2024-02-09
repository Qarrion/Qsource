import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui

class Qcandle(pg.GraphicsObject):
    def __init__(self, data):
        pg.GraphicsObject.__init__(self)

        self.cmap={"inc":"g", "des":"r"}
        self.w_body = 0.8
        self.w_tail = 0.05

        self.data = data
        self.draw()

    def draw(self):
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)

        w_body = 1 * self.w_body/2
        w_tail = 1 * self.w_tail/2
        
        for I, (T,O,H,L,C,V) in enumerate(self.data):
            if  O > C:
                col =  self.cmap['des']
                p.setPen(pg.mkPen(col))
                p.setBrush(pg.mkBrush(col))
            else :
                col =  self.cmap['inc']
                p.setPen(pg.mkPen(col))
                p.setBrush(pg.mkBrush(col))

            p.drawRect(QtCore.QRectF(I-w_body, O, w_body*2, C-O))
            p.drawRect(QtCore.QRectF(I-w_tail, L, w_tail*2, H-L))

        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)
    
    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())
    


if __name__ == '__main__':
    import pandas as pd
    data = pd.read_excel('AAPL.xlsx',index_col=0)
    data.index.name = 'DT'
    data = data.drop(columns=['Adj Close'])
    data.columns = ['O','H','L','C','V']
    print(data)
    
    item = Qcandle(data.to_records())
    plt = pg.plot()
    plt.addItem(item)
    # plt.resize(800,400)
    plt.setWindowTitle('pyqtgraph example: customGraphicsItem')

    plt.setXRange(100,120) #! 보여지는 위치
    plt.setMouseEnabled(x=True, y=False) #! 마우스로 조작 가능 여부
    plt.enableAutoRange(x=False, y=True)
    plt.setAutoVisible(x=False, y=True)

    pg.exec()

    # ------------------------------------------------------------------------ #





# data[data.isna().any(axis=1)]

# idx = data.index
# data = data.loc[(idx >= '2024-01-02')&(idx <= '2024-01-05')]
# data[data.isna()]
# data.to_records()
# data.values