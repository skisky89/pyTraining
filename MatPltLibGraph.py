# -*- coding: utf-8 -*-
"""
MatPlotLib Tutorial and tinkering
"""

import sys
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavToolbar
from matplotlib.figure import Figure

# Create figure, add axes
class figureCanvas(FigureCanvasQTAgg):
    
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(figureCanvas, self).__init__(fig)
   # super gives you access to a parent/sibling class, figureCanvas
   # The super() function returns an object that represents the parent class.
   
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create the maptlotlib FigureCanvas object, 
        # which defines a single set of axes as self.axes.
        FigObj = figureCanvas(self, width=5, height=4, dpi=100)
        FigObj.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        
        #create a toolbar object for interacting with the figure
        toolbar = NavigationToolbar(sc, self)
        
        
        
        self.setCentralWidget(FigObj)

        self.show()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()