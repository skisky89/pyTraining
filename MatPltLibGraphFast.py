import sys
import matplotlib
matplotlib.use('Qt5Agg')
import random
from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.FigObj = figureCanvas(self, width=5, height=4, dpi=100)
        self.setCentralWidget(self.FigObj)        
        
        n_data = 50
        self.xData = list(range(n_data))
        self.yData = [random.randint(0, 10) for i in range(n_data)]
        
        self.PlotRef = None
        self.update_plot()
        
        self.show()
 
        # Use a timer to trigger redraw
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        # discard first y element, append a new one.
        self.yData = self.yData[1:] + [random.randint(0, 10)]
        
        if self.PlotRef is None:
            PlotRefs = self.FigObj.axes.plot(self.xData, self.yData, 'r')
            self.PlotRef = PlotRefs[0]
        
        else:
            self.PlotRef.set_ydata(self.yData)
  
        # Trigger the canvas to update and redraw.
        self.FigObj.draw()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()