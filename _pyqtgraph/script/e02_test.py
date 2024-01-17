"""
This example demonstrates many of the 2D plotting capabilities
in pyqtgraph. All of the plots may be panned/scaled by dragging with 
the left/right mouse buttons. Right click on any plot to show a context menu.
"""

import numpy as np

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore

from PySide6 import QtWidgets
app = pg.mkQApp("Plotting Example")

# mw = QtWidgets.QMainWindow()
# mw.resize(800,800)

win = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
win.resize(1000,600)
win.setWindowTitle('pyqtgraph example: Plotting')

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

# Create data
x = np.linspace(0, 100, 100)
y = np.random.normal(size=100)

# Create the plot
p1 = win.addPlot(title="Basic array plotting")
p1.plot(x,y)

# Set the x-axis range to show only from 20 to 30
p1.setRange(xRange=[20, 30])


if __name__ == '__main__':
    pg.exec()
