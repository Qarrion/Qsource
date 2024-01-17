import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui

class Qcandle(pg.GraphicsObject):
    def __init__(self, data):
        pg.GraphicsObject.__init__(self)

        self.cmap={"inc":"g", "des":"r"}
        self.w_body = 0.8
        self.w_tail = 0.02

        self.data = data
        self.d_picture()

    def d_picture(self):
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)

        w_body = (self.data[1][0] - self.data[0][0]) * self.w_body/2
        w_tail = (self.data[1][0] - self.data[0][0]) * self.w_tail/2
        
        for (I,O,C,H,L) in self.data:
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
    
data = [  ## fields are (time, open, close, min, max).
    (1., 10, 13, 5, 15),
    (2., 13, 17, 9, 20),
    (3., 17, 14, 11, 23),
    (4., 14, 15, 5, 19),
    (5., 15, 9, 8, 22),
    (6., 9, 15, 8, 16),
]
item = Qcandle(data)
plt = pg.plot()
plt.addItem(item)
plt.setWindowTitle('pyqtgraph example: customGraphicsItem')

if __name__ == '__main__':
    pg.exec()
