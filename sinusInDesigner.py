from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np

# Assuming you have the `SignalSimulator` class for data generation
class SignalSimulator:
    @staticmethod
    def generateSynthSignals():
        # Your data generation logic here
        pass

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 361, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.ECG_widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.ECG_widget.setObjectName("ECG_widget")
        
        self.figure, self.ax1 = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        
        layout = QtWidgets.QVBoxLayout(self.ECG_widget)
        layout.addWidget(self.canvas)
        
        self.verticalLayout.addWidget(self.ECG_widget)

        # Create an instance of ScrollingGraph and pass the canvas
        self.scrolling_graph = ScrollingGraph(self.canvas)

        self.verticalLayout.addWidget(self.ECG_widget)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(360, 0, 91, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        self.ECG_lcd = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.ECG_lcd.setObjectName("ECG_lcd")
        self.gridLayout.addWidget(self.ECG_lcd, 0, 0, 1, 1)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

class ScrollingGraph(QMainWindow):
    def __init__(self, parent_canvas):
        super(ScrollingGraph, self).__init__()

        self.initUI(parent_canvas)

    def initUI(self, parent_canvas):
        # Use the provided canvas as the parent for the new canvas
        self.canvas = FigureCanvas(plt.Figure())

        # Add the canvas to the existing layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.canvas)

        # Create a central widget and set the layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Initialize data for the graph
        self.x_data = np.arange(0, 100, 0.1)
        self.y_data = SignalSimulator.generateSynthSignals()["ECG"]

        # Plot the initial data for the graph
        self.line, = plt.plot(self.x_data, self.y_data)
        self.ax = self.canvas.figure.add_subplot(111)
        self.ax.plot(self.x_data, self.y_data)

        # Create a QTimer to update the graph at regular intervals
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateGraph)
        self.timer.start(100)  # Update every 100 milliseconds

    def updateGraph(self):
        # Update the graph
        self.x_data = np.roll(self.x_data, -1)
        self.y_data = np.roll(self.y_data, -1)
        self.x_data[-1] += 0.1
        self.y_data[-1] = np.sin(self.x_data[-1])
        self.line.set_xdata(self.x_data)
        self.line.set_ydata(self.y_data)
        self.ax.set_xlim(self.x_data[0], self.x_data[-1] + 10)

        # Redraw the canvas
        self.canvas.draw()