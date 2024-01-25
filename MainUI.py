import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from Hackathon_v3 import Ui_MainWindow
# from ecg import Ui_MainWindow
from uart_handler import UARTHandler 
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, uart_handler):
        super().__init__()
#######################################
        self.uart_handler = uart_handler
        
        self.setupUi(self, uart_handler)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.uart_handler.read_uart_data)
        self.timer.start(200) #Interval in milliseconds 

    def closeEvent(self, event):
        # Close the serial port when the application is closed
        self.uart_handler.close_serial_port()
        event.accept()    
####################################### 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Create an instance of the UARTHandler class
    uart_handler = UARTHandler('COM7')
    
    mainWindow = MainWindow(uart_handler)
    mainWindow.show()
    sys.exit(app.exec_())

