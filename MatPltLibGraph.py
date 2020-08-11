import sys
import matplotlib
matplotlib.use('Qt5Agg')

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
        FigObj = figureCanvas(self, width=5, height=4, dpi=100)
        FigObj.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        
        #create a toolbar object for interacting with the figure
        toolbar = NavToolbar(FigObj, self)
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(FigObj)
        
        #Place-holder for toolbar
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()

        # Use a timer to trigger redraw
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        # discard first y element, append a new one.
        self.yData = self.yData[1:] + [random.randint(0, 10)]
        self.canvas.axes.cla()  # Clear the canvas.
        self.canvas.axes.plot(self.xData, self.yData, 'r')
        # Trigger the canvas to update and redraw.
        self.canvas.draw()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()