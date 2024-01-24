import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import neurokit2 as nk
 
class ScrollingGraph(QMainWindow):
    def __init__(self):
        super(ScrollingGraph, self).__init__()
 
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle('Scrolling Graphs')
        self.setGeometry(100, 100, 800, 600)
 
        # Create a central widget and set the layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
 
        layout = QVBoxLayout(central_widget)
 
        # Create the first Matplotlib figure and canvas
        self.figure1, self.ax1 = plt.subplots()
        self.canvas1 = FigureCanvas(self.figure1)
        layout.addWidget(self.canvas1)
 
        # Initialize data for the first graph
        self.x_data1 = np.arange(0, 100, 0.1)
        self.y_data1 = np.sin(self.x_data1)
 
        # Plot the initial data for the first graph
        self.line1, = self.ax1.plot(self.x_data1, self.y_data1)
 
        # Create the second Matplotlib figure and canvas
        self.figure2, self.ax2 = plt.subplots()
        self.canvas2 = FigureCanvas(self.figure2)
        layout.addWidget(self.canvas2)
 
        # Initialize data for the second graph
        self.x_data2 = np.arange(0, 100, 0.1)
        self.y_data2 = np.cos(self.x_data2)
 
        # Plot the initial data for the second graph
        self.line2, = self.ax2.plot(self.x_data2, self.y_data2)
 
        # Create a QTimer to update both graphs at regular intervals
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateGraphs)
        self.timer.start(100)  # Update every 100 milliseconds
 
    def updateGraphs(self):
        # Update the first graph
        self.x_data1 = np.roll(self.x_data1, -1)
        self.y_data1 = np.roll(self.y_data1, -1)
        self.x_data1[-1] += 0.1
        self.y_data1[-1] = np.sin(self.x_data1[-1])
        self.line1.set_xdata(self.x_data1)
        self.line1.set_ydata(self.y_data1)
        self.ax1.set_xlim(self.x_data1[0], self.x_data1[-1] + 10)
 
        # Update the second graph
        self.x_data2 = np.roll(self.x_data2, -1)
        self.y_data2 = np.roll(self.y_data2, -1)
        self.x_data2[-1] += 0.1
        self.y_data2[-1] = np.cos(self.x_data2[-1])
        self.line2.set_xdata(self.x_data2)
        self.line2.set_ydata(self.y_data2)
        self.ax2.set_xlim(self.x_data2[0], self.x_data2[-1] + 10)
 
        # Redraw both canvases
        self.canvas1.draw()
        self.canvas2.draw()
 
class SignalSimulator():
    def generateSynthSignals ():
        ecg = nk.ecg_simulate(duration=10, heart_rate=70)
        ppg = nk.ppg_simulate(duration=10, heart_rate=70)
        rsp = nk.rsp_simulate(duration=10, respiratory_rate=15)
        eda = nk.eda_simulate(duration=10, scr_number=3)
        emg = nk.emg_simulate(duration=10, burst_number=2)

        data = pd.DataFrame({"ECG": ecg,
                             "PPG": ppg,
                             "RSP": rsp,
                             "EDA": eda,
                             "EMG": emg})
        return data
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    signals = SignalSimulator()
    window = ScrollingGraph()
    window.show()
    sys.exit(app.exec_())