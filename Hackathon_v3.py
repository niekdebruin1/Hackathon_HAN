# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hackathon_v2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import neurokit2 as nk

def generateSynthSignals ():
    ecg = nk.ecg_simulate(duration=60, heart_rate=70, sampling_rate=100)
    ppg = nk.ppg_simulate(duration=60, heart_rate=70, sampling_rate=100)
    rsp = nk.rsp_simulate(duration=60, respiratory_rate=15, sampling_rate=100)
    # eda = nk.eda_simulate(duration=10, scr_number=3)
    # emg = nk.emg_simulate(duration=10, burst_number=2)
    # ecg = nk.ecg_clean(ecg, sampling_rate=100)
    data = pd.DataFrame({"ECG": ecg,
                        "PPG": ppg,
                        "RSP": rsp})

    return data

class Ui_MainWindow(object):
    ECG_status : bool
    PPG_status : bool
    Resp_status : bool
    def setupUi(self, MainWindow, uart_handler):

         ######################################################################################
        # Create an instance of the UARTHandler class
        self.uart_handler = uart_handler

        # Connect the UARTHandler signal to the updateGraphs slot
        self.uart_handler.dataReceived.connect(self.updateConnectionStatus)
        
        ######################################################################################
        self.ECG_status = False
        self.PPG_status = False
        self.Resp_status = False
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1336, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 50, 1051, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        ##########################################################
        ######################ECG#################################
        self.ECG_widget_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.ECG_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.ECG_widget_layout.setObjectName("ECG_widget_layout")
        self.ECG_widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.ECG_widget.setObjectName("ECG_widget")
        
        self.ECG_widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.ECG_widget.setObjectName("ECG_widget")
       ###############start here
        self.ECGfigure, self.ECG_ax = plt.subplots()
        self.ECGcanvas = FigureCanvas(self.ECGfigure)
        ECGlayout = QtWidgets.QVBoxLayout(self.ECG_widget)
        ECGlayout.addWidget(self.ECGcanvas)
       
        self.ECG_x = np.arange(-10, 0, 0.01)
        df = generateSynthSignals()
        self.full_yECG = df['ECG'].to_numpy(dtype=float)
        self.ECG_y = self.full_yECG[0:1000]
        # Plot the initial data for the first graph
        self.ECGline, = self.ECG_ax.plot(self.ECG_x, self.ECG_y, color='green')

        # Plot the initial data for the second graph
        self.ECG_widget_layout.addWidget(self.ECG_widget)
        #############################################################
        #############################################################
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 259, 1051, 161))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.PPG_widget_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.PPG_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.PPG_widget_layout.setObjectName("PPG_widget_layout")
        self.PPG_Widget = QtWidgets.QWidget(self.verticalLayoutWidget_2)
        self.PPG_Widget.setObjectName("PPG_Widget")
        self.PPG_widget_layout.addWidget(self.PPG_Widget)
        ##########################################################
        ######################PPG#################################
        self.PPG_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.PPG_widget_layout.setObjectName("PPG_widget_layout")

        self.PPGfigure, self.PPG_ax = plt.subplots()
        self.PPGcanvas = FigureCanvas(self.PPGfigure)
        PPGlayout = QtWidgets.QVBoxLayout(self.PPG_Widget)
        PPGlayout.addWidget(self.PPGcanvas)
       
        self.PPG_x = np.arange(-10, 0, 0.01)
        self.full_yPPG = df['PPG'].to_numpy(dtype=float)
        self.PPG_y = self.full_yPPG[0:1000]
        # Plot the initial data for the first graph
        self.PPGline, = self.PPG_ax.plot(self.PPG_x, self.PPG_y, color='orange')

        #############################################################
        #############################################################
        
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(1050, 50, 261, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.ECG_lcd_text_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.ECG_lcd_text_layout.setContentsMargins(0, 0, 0, 0)
        self.ECG_lcd_text_layout.setObjectName("ECG_lcd_text_layout")
        self.ECG_lcd_text_layout_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ECG_lcd_text_layout_2.setObjectName("ECG_lcd_text_layout_2")
        self.ECG_lcd_text_layout.addWidget(self.ECG_lcd_text_layout_2, 0, 0, 1, 1)
        self.gridLayoutWidget_11 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_11.setGeometry(QtCore.QRect(1050, 260, 261, 81))
        self.gridLayoutWidget_11.setObjectName("gridLayoutWidget_11")
        self.PPG_lcd_text_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_11)
        self.PPG_lcd_text_layout.setContentsMargins(0, 0, 0, 0)
        self.PPG_lcd_text_layout.setObjectName("PPG_lcd_text_layout")
        self.PPG_text_2 = QtWidgets.QLabel(self.gridLayoutWidget_11)
        self.PPG_text_2.setObjectName("PPG_text_2")
        self.PPG_lcd_text_layout.addWidget(self.PPG_text_2, 0, 0, 1, 1)
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(1050, 130, 261, 81))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.Pulse_lcd_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.Pulse_lcd_layout.setContentsMargins(0, 0, 0, 0)
        self.Pulse_lcd_layout.setObjectName("Pulse_lcd_layout")
        self.ECG_lcd = QtWidgets.QLCDNumber(self.gridLayoutWidget_6)
        self.ECG_lcd.setObjectName("ECG_lcd")
        self.Pulse_lcd_layout.addWidget(self.ECG_lcd, 0, 0, 1, 1)
        self.gridLayoutWidget_15 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_15.setGeometry(QtCore.QRect(1050, 340, 261, 81))
        self.gridLayoutWidget_15.setObjectName("gridLayoutWidget_15")
        self.PPG_lcd_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_15)
        self.PPG_lcd_layout.setContentsMargins(0, 0, 0, 0)
        self.PPG_lcd_layout.setObjectName("PPG_lcd_layout")
        self.PPG_lcd = QtWidgets.QLCDNumber(self.gridLayoutWidget_15)
        self.PPG_lcd.setObjectName("PPG_lcd")
        self.PPG_lcd_layout.addWidget(self.PPG_lcd, 0, 0, 1, 1)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 1051, 51))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.ECG_text_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.ECG_text_layout.setContentsMargins(0, 0, 0, 0)
        self.ECG_text_layout.setObjectName("ECG_text_layout")
        self.ECG_text = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.ECG_text.setObjectName("ECG_text")
        self.ECG_text_layout.addWidget(self.ECG_text)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(-1, 210, 1051, 51))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.PPG_text_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.PPG_text_layout.setContentsMargins(0, 0, 0, 0)
        self.PPG_text_layout.setObjectName("PPG_text_layout")
        self.PPG_text = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.PPG_text.setObjectName("PPG_text")
        self.PPG_text_layout.addWidget(self.PPG_text)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(-1, 419, 1051, 51))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.Resp_text_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.Resp_text_layout.setContentsMargins(0, 0, 0, 0)
        self.Resp_text_layout.setObjectName("Resp_text_layout")
        self.Resp_text = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.Resp_text.setObjectName("Resp_text")
        self.Resp_text_layout.addWidget(self.Resp_text)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(-1, 469, 1051, 161))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.Resp_widget_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.Resp_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.Resp_widget_layout.setObjectName("Resp_widget_layout")
        self.Resp_widget = QtWidgets.QWidget(self.verticalLayoutWidget_6)
        self.Resp_widget.setObjectName("Resp_widget")
        self.Resp_widget_layout.addWidget(self.Resp_widget)

        ##########################################################
        ######################Resp#################################
        self.Resp_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.Resp_widget_layout.setObjectName("Resp_widget_layout")

        self.Respfigure, self.Resp_ax = plt.subplots()
        self.Respcanvas = FigureCanvas(self.Respfigure)
        Resplayout = QtWidgets.QVBoxLayout(self.Resp_widget)
        Resplayout.addWidget(self.Respcanvas)
       
        self.Resp_x = np.arange(-10, 0, 0.01)
        self.full_yResp = df['RSP'].to_numpy(dtype=float)
        self.Resp_y = self.full_yResp[0:1000]
        # Plot the initial data for the first graph
        self.Resp_ax.set_xlim(self.Resp_x[0], self.Resp_x[-1])
        self.Resp_ax.set_ylim(-0.8, 1)
        self.Respline, = self.Resp_ax.plot(self.Resp_x, self.Resp_y, color='white')

        #############################################################
        #############################################################

        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(1049, 470, 261, 81))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.Resp_text_layout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.Resp_text_layout_2.setContentsMargins(0, 0, 0, 0)
        self.Resp_text_layout_2.setObjectName("Resp_text_layout_2")
        self.Resp_text_2 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.Resp_text_2.setObjectName("Resp_text_2")
        self.Resp_text_layout_2.addWidget(self.Resp_text_2)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(1050, 550, 261, 81))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.Resp_lcd_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.Resp_lcd_layout.setContentsMargins(0, 0, 0, 0)
        self.Resp_lcd_layout.setObjectName("Resp_lcd_layout")
        self.Resp_lcd = QtWidgets.QLCDNumber(self.verticalLayoutWidget_8)
        self.Resp_lcd.setObjectName("Resp_lcd")
        self.Resp_lcd_layout.addWidget(self.Resp_lcd)
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(0, 630, 151, 51))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.Pulse_text_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.Pulse_text_layout.setContentsMargins(0, 0, 0, 0)
        self.Pulse_text_layout.setObjectName("Pulse_text_layout")
        self.Pulse_text = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.Pulse_text.setObjectName("Pulse_text")
        self.Pulse_text_layout.addWidget(self.Pulse_text)
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(150, 630, 151, 51))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.Pulse_lcd_layout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.Pulse_lcd_layout_2.setContentsMargins(0, 0, 0, 0)
        self.Pulse_lcd_layout_2.setObjectName("Pulse_lcd_layout_2")
        self.Pulse_lcd = QtWidgets.QLCDNumber(self.verticalLayoutWidget_10)
        self.Pulse_lcd.setObjectName("Pulse_lcd")
        self.Pulse_lcd_layout_2.addWidget(self.Pulse_lcd)
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(300, 630, 151, 51))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.NIBP_text_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.NIBP_text_layout.setContentsMargins(0, 0, 0, 0)
        self.NIBP_text_layout.setObjectName("NIBP_text_layout")
        self.NIBP_text = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        self.NIBP_text.setObjectName("NIBP_text")
        self.NIBP_text_layout.addWidget(self.NIBP_text)
        self.verticalLayoutWidget_12 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(450, 630, 151, 51))
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.NIBP_lcd_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_12)
        self.NIBP_lcd_layout.setContentsMargins(0, 0, 0, 0)
        self.NIBP_lcd_layout.setObjectName("NIBP_lcd_layout")
        self.NIBP_lcd = QtWidgets.QLCDNumber(self.verticalLayoutWidget_12)
        self.NIBP_lcd.setObjectName("NIBP_lcd")
        self.NIBP_lcd_layout.addWidget(self.NIBP_lcd)
        self.verticalLayoutWidget_13 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_13.setGeometry(QtCore.QRect(600, 630, 151, 51))
        self.verticalLayoutWidget_13.setObjectName("verticalLayoutWidget_13")
        self.Temp_text_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_13)
        self.Temp_text_layout.setContentsMargins(0, 0, 0, 0)
        self.Temp_text_layout.setObjectName("Temp_text_layout")
        self.Temp_text = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.Temp_text.setObjectName("Temp_text")
        self.Temp_text_layout.addWidget(self.Temp_text)
        self.verticalLayoutWidget_14 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_14.setGeometry(QtCore.QRect(750, 630, 151, 51))
        self.verticalLayoutWidget_14.setObjectName("verticalLayoutWidget_14")
        self.Temp_lcd_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_14)
        self.Temp_lcd_layout.setContentsMargins(0, 0, 0, 0)
        self.Temp_lcd_layout.setObjectName("Temp_lcd_layout")
        self.Temp_lcd = QtWidgets.QLCDNumber(self.verticalLayoutWidget_14)
        self.Temp_lcd.setObjectName("Temp_lcd")
        self.Temp_lcd_layout.addWidget(self.Temp_lcd)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1210, 630, 101, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(1050, 630, 101, 51))
        self.pushButton_1.setObjectName("pushButton_1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1336, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateGraphs)
        self.timer.start(50)  # Update every 100 milliseconds

        self.lcd_timer = QTimer(self)
        self.lcd_timer.timeout.connect(self.updateLCDs)
        self.lcd_timer.start(1500)

        cleaned_ppg = nk.ppg_clean(self.PPG_y, sampling_rate=100, heart_rate=70)
        peaks = nk.ppg_findpeaks(cleaned_ppg,sampling_rate=100)
        ppg_rate = nk.ppg_rate(peaks,100)

        self.PPG_lcd.display(ppg_rate[0])

        ############################Colors########################
        self.setStyleSheet("background-color: #000000;")
        self.ECG_ax.set_facecolor('black')
        self.ECGfigure.set_facecolor('black')
        self.ECG_lcd.setStyleSheet("QLCDNumber { color: green; border: green;}")
        self.ECG_text.setStyleSheet("QLabel { color: green; }")
        self.Pulse_text.setStyleSheet("QLabel { color: green; }")
        self.ECG_lcd_text_layout_2.setStyleSheet("QLabel { color: green; }")

        self.PPG_ax.set_facecolor('black')
        self.PPGfigure.set_facecolor('black')
        self.PPG_lcd.setStyleSheet("QLCDNumber { color: orange; border: orange;}")
        self.PPG_text.setStyleSheet("QLabel { color: orange; }")
        self.PPG_text_2.setStyleSheet("QLabel { color: orange; }")

        self.Resp_ax.set_facecolor('black')
        self.Respfigure.set_facecolor('black')
        self.Resp_lcd.setStyleSheet("QLCDNumber { color: white; border: white;}")
        self.Resp_text.setStyleSheet("QLabel { color: white; }")
        self.Resp_text_2.setStyleSheet("QLabel { color: white; }")

        self.Temp_text.setStyleSheet("QLabel { color: green; }")
        self.Temp_lcd.setStyleSheet("QLCDNumber { color: green; border: green;}")

        self.NIBP_text.setStyleSheet("QLabel { color: red; }")
        self.NIBP_lcd.setStyleSheet("QLCDNumber { color: red; border: red;}")
        
        self.Pulse_lcd.setStyleSheet("QLCDNumber { color: green; border: green;}")

        self.pushButton_1.setStyleSheet("QPushButton  { background-color: green}")
        self.pushButton_1.clicked.connect(self.Button1_clicked)
        self.pushButton_2.setStyleSheet("QPushButton  { background-color: green}")
        ##########################################################

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def Button1_clicked(self):
        if(self.ECG_status == False):
            self.ECG_status = True
        else:
            self.ECG_status = False

        if(self.PPG_status == False):
            self.PPG_status = True
        else:
            self.PPG_status = False

        if(self.Resp_status == False):
            self.Resp_status = True
        else:
            self.Resp_status = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ECG_lcd_text_layout_2.setText(_translate("MainWindow", "Pulse"))
        self.PPG_text_2.setText(_translate("MainWindow", "PPG"))
        self.ECG_text.setText(_translate("MainWindow", "ECG"))
        self.PPG_text.setText(_translate("MainWindow", "PPG"))
        self.Resp_text.setText(_translate("MainWindow", "Resp"))
        self.Resp_text_2.setText(_translate("MainWindow", "Resp"))
        self.Pulse_text.setText(_translate("MainWindow", "Pulse"))
        self.NIBP_text.setText(_translate("MainWindow", "NIBP"))
        self.Temp_text.setText(_translate("MainWindow", "Temp"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_1.setText(_translate("MainWindow", "PushButton"))
    
    def updateConnectionStatus(self, data):
        device, number = data.split(":")
        if(device == "ECG"):
            print(number)
            if(number == '0'):
                self.ECG_status = False
                self.Resp_status = False
            else:
                self.ECG_status = True
                self.Resp_status = True
            

    def updateLCDs(self):
        if(self.ECG_status == True):
            cleaned_ecg = nk.ecg_clean(self.ECG_y, sampling_rate=100)
            ecg_peaks = nk.ecg_findpeaks(cleaned_ecg, sampling_rate=100)
            ecg_rate = nk.ecg_rate(ecg_peaks, sampling_rate=100)
            self.ECG_lcd.display(ecg_rate[0])
            self.Pulse_lcd.display(ecg_rate[0])
        else:
            self.ECG_lcd.display(0)
            self.Pulse_lcd.display(0)
        if(self.PPG_status == True):
            cleaned_ppg = nk.ppg_clean(self.PPG_y, sampling_rate=100, heart_rate=70)
            peaks = nk.ppg_findpeaks(cleaned_ppg,sampling_rate=100)
            ppg_rate = nk.ppg_rate(peaks,100)
            self.PPG_lcd.display(ppg_rate[0])
        else:
            self.PPG_lcd.display(0)
        if(self.Resp_status == True):
            self.Resp_lcd.display(15)
        else:
            self.Resp_lcd.display(0)

    def updateGraphs(self):
        self.updateECGGraphs()
        self.updateRSPGraphs()
        self.updatePPGGraphs()

    def updateRSPGraphs(self):

        for i in range(5):
            self.full_yResp = np.roll(self.full_yResp, -1)
        if(self.Resp_status == True):
            self.Resp_y = self.full_yResp[0:1000]
        else:
            self.Resp_y = None
        self.Respline.set_xdata(self.Resp_x)
        self.Respline.set_ydata(self.Resp_y)
        self.Resp_ax.set_xlim(self.Resp_x[0], self.Resp_x[-1]+1)
        # Redraw both canvases
        self.Respcanvas.draw()

    def updatePPGGraphs(self):
        for i in range(5):
            self.full_yPPG = np.roll(self.full_yPPG, -1)
        if(self.PPG_status == True):
            self.PPG_y = self.full_yPPG[0:1000]
        else:
            self.PPG_y = None
        self.PPGline.set_xdata(self.PPG_x)
        self.PPGline.set_ydata(self.PPG_y)
        self.PPG_ax.set_xlim(self.PPG_x[0], self.PPG_x[-1]+1)
        
        # Redraw both canvases
        self.PPGcanvas.draw()

    def updateECGGraphs(self):
        # Update the first graph
        for i in range(5):
            self.full_yECG = np.roll(self.full_yECG, -1)
        if(self.ECG_status == True):
            self.ECG_y = self.full_yECG[0:1000]
        else:
            self.ECG_y = None
        self.ECGline.set_xdata(self.ECG_x)
        self.ECGline.set_ydata(self.ECG_y)
        self.ECG_ax.set_xlim(self.ECG_x[0], self.ECG_x[-1]+1)
        # Redraw both canvases
        self.ECGcanvas.draw()
