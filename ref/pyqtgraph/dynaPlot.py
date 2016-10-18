import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
import numpy as np
import time


win = pg.GraphicsWindow()
win.setWindowTitle('Plot Tool')
graph = win.addPlot()
graph.showGrid(x=True, y=True)
# This needs to be called to process QT events (render the window)
QtGui.QApplication.instance().processEvents()
# Main run loop while ROS is still going
while 1:
    data = np.random.normal(size=1000)
    graph.plot(data, title="Simplest possible plotting example", clear = True)
    QtGui.QApplication.instance().processEvents()
    time.sleep(0.03)
