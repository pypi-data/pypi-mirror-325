import threading
import errno
import socket
import serial
from .Transport import Transport



class SerialTransport (Transport):
    def __init__(self, port, baud = 115200, stopbits= serial.STOPBITS_ONE , databits= serial.EIGHTBITS, parity =  serial.PARITY_NONE, callback = None): 
        super().__init__(callback)
        
        self.port = port
        self.baud = baud
        self.opened = False
        
        try:
            self.serialPort = serial.Serial(
                port = port,
                baudrate=baud,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize= serial.EIGHTBITS
            )
            self.opened = True
            print( f"Opened {port} at {baud} baud")
        except serial.SerialException as e:
            print(e)
            print(f"Failed to open {port} at {baud} baud")

    def __del__(self):
        self.close()
        self.join()     #stop thread



    def close(self):
        if self.opened:
            self.serialPort.close()


    def send(self, data):
        if self.opened:
            self.serialPort.write(data)

    def run(self):
        if self.opened:
            while True:
                if self.serialPort.inWaiting() > 0:
                    data = self.serialPort.read()
                    if self.callback:
                        self.callback(data)


serialConnectionHelp = """

    Invalid serial connection string.

    serial:/dev/ttyUSB0:115200
    serial:/dev/ttyUSB0:115200-E-8-1
"""

def parseSerialConnectionString(connString):
    """
    Parse a serial connection string and return a dictionary of the parameters

    Examples: 
        SERIAL:/dev/ttyUSB0:115200  
        SERIAL:/dev/ttyUSB0:115200-E-8-1

    """
    try:

        
        parts = connString.split(":")
        if len(parts) < 3:
            return None

        port = parts[1]
        baud = 115200
        stopbits = serial.STOPBITS_ONE
        databits = serial.EIGHTBITS
        parity = serial.PARITY_NONE

        if len(parts) > 2:
            params = parts[2].split("-")
            baud = int(params[0])

            if len(params) > 1:
                if params[1] == 'E':
                    parity = serial.PARITY_EVEN
                elif params[1] == 'O':
                    parity = serial.PARITY_ODD
                elif params[1] == 'N':
                    parity = serial.PARITY_NONE

            if len(params) > 2:
                databits = int(params[2])
            
            if len(params) > 3:
                stopbits = int(params[3])


        out = {
            'port': port,
            'baud': baud,
            'stopbits': stopbits,
            'databits': databits,
            'parity': parity
        }

        return out
    except:
        return None
