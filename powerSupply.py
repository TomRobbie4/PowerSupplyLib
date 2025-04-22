from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import QIODevice
from dataclasses import dataclass, field

@dataclass
class Channel_:
    number: int
    duty: int = 0
    status: bool = False
    serialPort: QSerialPort = field(repr=False, default=None)

    def open(self):
        if self.serialPort and self.serialPort.isOpen():
            if self.serialPort.bytesToWrite() == 0:
                self.serialPort.write(b'$')
                self.serialPort.write(self.number.to_bytes())
                self.serialPort.write(b'S')
                self.serialPort.write(b'\x01')
                #print(f"[CH{self.number}] Open command sent")
                return 1
        return 0

    def close(self):
        if self.serialPort and self.serialPort.isOpen():
            if self.serialPort.bytesToWrite() == 0:
                self.serialPort.write(b'$')
                self.serialPort.write(self.number.to_bytes())
                self.serialPort.write(b'S')
                self.serialPort.write(b'\x00')  # 0 en byte
                #print(f"[CH{self.number}] Close command sent")
                return 1
        return 0

    def setDuty(self):
        if self.serialPort and self.serialPort.isOpen():
            if self.serialPort.bytesToWrite() == 0:
                self.serialPort.write(b'$')
                self.serialPort.write(self.number.to_bytes())
                self.serialPort.write(b'D')
                self.serialPort.write(self.duty.to_bytes(2, 'big'))
                #print(f"[CH{self.number}] Duty set to {self.duty}")
                return 1
        return 0


@dataclass
class powerSupply_:
    portName = ""
    serialPort: QSerialPort = field(default_factory=QSerialPort)
    CH1: Channel_ = field(init=False)
    CH2: Channel_ = field(init=False)
    CH3: Channel_ = field(init=False)
    CH4: Channel_ = field(init=False)
    CH5: Channel_ = field(init=False)
    CH6: Channel_ = field(init=False)
    CH7: Channel_ = field(init=False)
    CH8: Channel_ = field(init=False)

    def __post_init__(self):
        # Setup du port série
        self.serialPort.setPortName(self.portName)
        self.serialPort.setBaudRate(QSerialPort.Baud115200)

        # Initialiser les channels dynamiquement avec le port de 0 a 120.
        for i in range(1, 121):
            setattr(self, f"CH{i}", Channel_(i, serialPort=self.serialPort))
        #ex: self.CH120 = Channel_(120, serialPort=self.serialPort)


    def openSerial(self):
        self.serialPort.setPortName(self.portName)
        if not self.serialPort.isOpen():
            if self.serialPort.open(QIODevice.ReadWrite):
                #print("[SERIAL] Port série ouvert.")
                return 1
            else:
                #print("[ERREUR] Impossible d'ouvrir le port série.")
                return 0

    def closeSerial(self):
        if self.serialPort.isOpen():
            self.serialPort.close()
            #print("[SERIAL] Port série fermé.")
            return 1
