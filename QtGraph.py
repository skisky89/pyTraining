# -*- coding: utf-8 -*-

# PyQt Graphing examples

#Import dependencies
from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as QtG
import sys  # We need sys so that we can pass argv to QApplication
import os, random
from PyQt5 import QtCore
#Import dependencies

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = QtG.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]
        temperature2 = [ x+2 for x in temperature ] 


        

# Graph configuration             
        # Background color supports a single character for commons colors
        # But also supports ( R , G , B ) and #hexhex expressed colors
        self.graphWidget.setBackground('w')
        
        # Graph line properties via QPen
        pen = QtG.mkPen(color=(255, 0, 0), width=2, style=QtCore.Qt.DashLine)
        
        
        # For updating graph
        self.x = list(range(100)) 
        self.y = [random.randint(0,100) for _ in range(100)]
        self.data = self.graphWidget.plot(self.x, self.y, pen=pen)
        
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.refreshingPlot)
        self.timer.start()
        
        
        # More formatting examples
        self.graphWidget.setTitle("The Best Graph Ever", color="b" , size="32pt") # Set title supports HTML tags!
        self.graphWidget.showGrid(x=True, y=True)
        
        self.graphWidget.setXRange(0, 15, padding=0)
        self.graphWidget.setYRange(20, 50, padding=0)
        
        Labelstyle = {'color':'g', 'font-size':'14px'} 
        self.graphWidget.setLabel('left','Temp (C)', **Labelstyle)
        self.graphWidget.setLabel('bottom','Time (Hr)', **Labelstyle)
        
        # Be a lengend, make a legend
        self.graphWidget.addLegend()


# Drawing the graph     
        # plot data              x, y          ,QPen   
  #      self.graphWidget.plot(hour, temperature,name="SensorA", pen=pen, symbol='s')
        # Careful here! " import QtCore * " imported all the contents of Qt core
        # BUT it didn't import the 'namspace' QtCore. So python didn't know what 
        # QtCore was ... fix : 'from PyQt5 import QtCore'
        
# Calling .plot summons a new 'line' the the graph
   #     self.plot(hour, temperature2, "SensorB", 'b')
    
# Make a plot function, so QPen can be modifed more easily
    def plot(self, x, y, plotname, color):
        pen = QtG.mkPen(color=color)
        self.graphWidget.plot(x, y, name=plotname, pen=pen, symbol='+', symbolSize=30, symbolBrush=(color))

    def clearPlots(self):
        self.graphWidget.clear()
        
    def refreshingPlot(self):
        self.x = self.x[1:]  # Remove first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first 
        self.y.append(random.randint(0,100))  # Add a new random value.

        self.data_line.setData(self.x, self.y)  # Update the data.     
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()