from PyQt5.QtCore import QObject, pyqtSignal
import serial

class UARTHandler(QObject):
    dataReceived = pyqtSignal(str)  # Signal to notify the reception of new data

    def __init__(self, port, baudrate=9600, timeout=1):
        super().__init__()
        try:
            self.ser = serial.Serial(port, baudrate, timeout=timeout)
        except:
            self.ser = None
            print("Error, UART not connected")
            
    def read_uart_data(self):
        try:
            # Read data from the serial port
            data = self.ser.readline().decode('utf-8').strip()

            # Emit the signal with the received data
            self.dataReceived.emit(data)

        except Exception as e:
            # Handle exceptions (e.g., serial port errors)
            print("Error:", str(e))

    def close_serial_port(self):
        # Close the serial port
        self.ser.close()