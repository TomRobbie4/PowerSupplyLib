from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from dataclasses import dataclass, field

@dataclass
class Channel_:
    """
    Represents a control channel.

    Attributes:
        number (int): Channel number (1 to 120).
        duty (int): Duty cycle value to apply (0 to 4095).
        status (bool): Channel enabled/disabled status.
        serialPort (QSerialPort): Serial port used for communication.
    """

    number: int
    duty: int = 0
    status: bool = False
    serialPort: QSerialPort = field(repr=False, default=None)

    def open(self):
        """
        Activates the channel.

        Returns:
            int: 0 if success, 1 if error.
        """
        if self.serialPort and self.serialPort.isOpen():
            if self.serialPort.bytesToWrite() == 0:
                self.serialPort.write(b'$')
                self.serialPort.write(self.number.to_bytes(1, 'big'))
                self.serialPort.write(b'S')
                self.serialPort.write(b'\x01')
                return 0
        return 1

    def close(self):
        """
        Deactivates the channel.

        Returns:
            int: 0 if success, 1 if error.
        """
        if self.serialPort and self.serialPort.isOpen():
            if self.serialPort.bytesToWrite() == 0:
                self.serialPort.write(b'$')
                self.serialPort.write(self.number.to_bytes(1, 'big'))
                self.serialPort.write(b'S')
                self.serialPort.write(b'\x00')
                return 0
        return 1

    def setDuty(self):
        """
        Applies the duty cycle value to the channel.

        Returns:
            int: 0 if success, 1 if error.
        """
        if self.serialPort and self.serialPort.isOpen():
            if self.serialPort.bytesToWrite() == 0:
                self.serialPort.write(b'$')
                self.serialPort.write(self.number.to_bytes(1, 'big'))
                self.serialPort.write(b'D')
                self.serialPort.write(self.duty.to_bytes(2, 'big'))
                return 0
        return 1

@dataclass
class powerSupply_:
    """
    Global power supply manager, allowing control of up to 120 channels via a serial port.

    Attributes:
        portName (str): The serial port name (e.g., "COM3").
        serialPort (QSerialPort): PySide6 object for serial communication.
        CH1 to CH120 (Channel_): Channels instantiated automatically.
    """

    portName = ""
    serialPort: QSerialPort = field(default_factory=QSerialPort)

    def __post_init__(self):
        """
        Initializes the 120 channels and configures the serial port.
        """
        self.serialPort.setPortName(self.portName)
        self.serialPort.setBaudRate(QSerialPort.Baud115200)
        for i in range(1, 121):
            setattr(self, f"CH{i}", Channel_(i, serialPort=self.serialPort))

    def openSerial(self):
        """
        Opens the configured serial port.

        Returns:
            int: 0 if success, 1 if error.
        """
        self.serialPort.setPortName(self.portName)
        if not self.serialPort.isOpen():
            if self.serialPort.open(QSerialPort.ReadWrite):
                return 0
        return 1

    def closeSerial(self):
        """
        Closes the serial port if it is open.

        Returns:
            int: 0 if success, 1 if error.
        """
        if self.serialPort.isOpen():
            self.serialPort.close()
            return 0
        return 1
