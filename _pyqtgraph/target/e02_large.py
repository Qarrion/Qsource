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
        # w_body = (self.data[1][0] - self.data[0][0]) * self.w_body/2
        # w_tail = (self.data[1][0] - self.data[0][0]) * self.w_tail/2
        
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
        ## boundingRect _must_ indicate the entire area that will be drawn on
        ## or else we will get artifacts and possibly crashing.
        ## (in this case, QPicture does all the work of computing the bouning rect for us)
        return QtCore.QRectF(self.picture.boundingRect())
    


if __name__ == '__main__':
    import pandas as pd
    data = pd.read_excel('AAPL.xlsx',index_col=0)
    data.index.name = 'DT'
    data = data.drop(columns=['Adj Close'])
    data.columns = ['O','H','L','C','V']
    print(data)
    
    # data = [  ## fields are (time, open, close, min, max).
    #     (1., 10, 13, 5, 15),
    #     (2., 13, 17, 9, 20),
    #     (3., 17, 14, 11, 23),
    #     (4., 14, 15, 5, 19),
    #     (5., 15, 9, 8, 22),
    #     (6., 9, 15, 8, 16),
    # ]
    item = Qcandle(data.to_records())
    plt = pg.plot()
    plt.resize(800,400)
    plt.addItem(item)
    plt.setWindowTitle('pyqtgraph example: customGraphicsItem')

    pg.exec()









# data[data.isna().any(axis=1)]

# idx = data.index
# data = data.loc[(idx >= '2024-01-02')&(idx <= '2024-01-05')]
# data[data.isna()]
# data.to_records()
# data.values