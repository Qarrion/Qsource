import pyqtgraph as pg
import numpy as np
# ---------------------------------------------------------------------------- #
x = np.arange(1000, dtype=float)
y = np.random.normal(size=1000)
y += 5 * np.sin(x/100) 

# ---------------------------------------------------------------------------- #
# plt = pg.plot(x, y, title='Sine Wave')
# plt.setXRange(300, 450)
# plt.setMouseEnabled(x=True, y=False)
# # plt.enableAutoRange(x=False, y=True)
# # plt.enableAutoRange('y')
# plt.setAutoVisible(x=False, y=True)

app = pg.mkQApp()

vb = pg.ViewBox()
vb.setXRange(300, 450)
vb.setMouseEnabled(x=True, y=False)
# vb.enableAutoRange(x=False, y=True)
vb.setAutoVisible(x=False, y=True)


pw = pg.PlotWidget(title='Sine Wave', viewBox =vb)
pw.plot(x,y)

pw.show()
# ---------------------------------------------------------------------------- #


# PlotDataItem 객체 생성과 설정
# plot_item = pg.PlotDataItem(x, y, symbol='o', pen='r', name='Sine Wave')
# plot = pg.PlotWidget()
# plot.addItem(plot_item)


# ---------------------------------------------------------------------------- #
pg.exec()