from PySide6.QtWidgets import QApplication
from src.powerSupply import powerSupply_
import sys
import time



def main():
    psu = powerSupply_()
    psu.portName = "COM9"

    # Open the serial port
    if psu.openSerial():
        print("Error opening the serial port.")
        return
    print("Serial port opened successfully.")

    # put "psu.serialPort.waitForBytesWritten(10)" between each command
    # refer to "example.py" if needed
    
    # ------------ Your code here ------------
    stay = True
    i = 0

    if psu.CH2.open():
        print("Error opening channel 2.")
        return
    print("Channel 2 opened successfully.")
    psu.serialPort.waitForBytesWritten(10)

    for i in range(4096):  # 0 to 500 included
        time.sleep(0.005)
        psu.CH2.duty = i
        print(psu.CH2.duty)
        if psu.CH2.setDuty():
            print("Error applying the duty cycle.")
            break
        psu.serialPort.waitForBytesWritten(10)

    time.sleep(1)

    if psu.CH2.close():
        print("Error closing channel 2.")
    print("Channel 2 closed successfully.")
    psu.serialPort.waitForBytesWritten(10)
    # ----------------------------------------
    

    # Close the serial port
    if psu.closeSerial():
        print("Error closing the serial port.")
    print("Serial port closed successfully.")

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Necessary for Qt objects
    main()
    sys.exit(0)  # No need for app.exec() since there's no GUI
