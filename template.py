from PySide6.QtWidgets import QApplication
from powerSupply import powerSupply_
import sys
import time

stay = True

def main():
    psu = powerSupply_()
    psu.portName = "YOUR_PORT_NUMBER"

    # Open the serial port
    if psu.openSerial():
        print("Error opening the serial port.")
        return
    print("Serial port opened successfully.")

    # put "psu.serialPort.waitForBytesWritten(10)" between each command
    # refer to "example.py" if needed
    while(stay):
    # ------------ Your code here ------------
        print("your script")
    # ----------------------------------------
    

    # Close the serial port
    if psu.closeSerial():
        print("Error closing the serial port.")
    print("Serial port closed successfully.")

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Necessary for Qt objects
    main()
    sys.exit(0)  # No need for app.exec() since there's no GUI
