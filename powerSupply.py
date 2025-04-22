from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import QIODevice
from dataclasses import dataclass, field


@dataclass
class Channel_:
    """
    Représente un canal de contrôle.

    Attributs :
        number (int) : Numéro du canal (1 à 120).
        duty (int) : Valeur du duty cycle à appliquer (0 à 65535).
        status (bool) : Statut activé/désactivé du canal.
        serialPort (QSerialPort) : Port série utilisé pour communiquer.
    """
    number: int
    duty: int = 0
    status: bool = False
    serialPort: QSerialPort = field(repr=False, default=None)

    def open(self):
        """
        Active le canal.

        Retour :
            int : 0 si succès, 1 si erreur.
        """
        if self.serialPort and self.serialPort.isOpen():
            if self.serialPort.bytesToWrite() == 0:
                self.serialPort.write(b'$')
                self.serialPort.write(self.number.to_bytes())
                self.serialPort.write(b'S')
                self.serialPort.write(b'\x01')
                return 0
        return 1

    def close(self):
        """
        Désactive le canal.

        Retour :
            int : 0 si succès, 1 si erreur.
        """
        if self.serialPort and self.serialPort.isOpen():
            if self.serialPort.bytesToWrite() == 0:
                self.serialPort.write(b'$')
                self.serialPort.write(self.number.to_bytes())
                self.serialPort.write(b'S')
                self.serialPort.write(b'\x00')
                return 0
        return 1

    def setDuty(self):
        """
        Applique la valeur de duty cycle au canal.

        Retour :
            int : 0 si succès, 1 si erreur.
        """
        if self.serialPort and self.serialPort.isOpen():
            if self.serialPort.bytesToWrite() == 0:
                self.serialPort.write(b'$')
                self.serialPort.write(self.number.to_bytes())
                self.serialPort.write(b'D')
                self.serialPort.write(self.duty.to_bytes(2, 'big'))
                return 0
        return 1


@dataclass
class powerSupply_:
    """
    Gestionnaire global d'alimentation, permettant le contrôle de jusqu'à 120 canaux via un port série.

    Attributs :
        portName (str) : Nom du port série (ex: "COM3").
        serialPort (QSerialPort) : Objet PySide6 pour la communication série.
        CH1 à CH120 (Channel_) : Canaux instanciés automatiquement.
    """
    portName = ""
    serialPort: QSerialPort = field(default_factory=QSerialPort)

    def __post_init__(self):
        """
        Initialise les 120 canaux et configure le port série.
        """
        self.serialPort.setPortName(self.portName)
        self.serialPort.setBaudRate(QSerialPort.Baud115200)
        for i in range(1, 121):
            setattr(self, f"CH{i}", Channel_(i, serialPort=self.serialPort))

    def openSerial(self):
        """
        Ouvre le port série configuré.

        Retour :
            int : 0 si succès, 1 si erreur.
        """
        self.serialPort.setPortName(self.portName)
        if not self.serialPort.isOpen():
            if self.serialPort.open(QIODevice.ReadWrite):
                return 0
        return 1

    def closeSerial(self):
        """
        Ferme le port série s’il est ouvert.

        Retour :
            int : 0 si succès, 1 si erreur.
        """
        if self.serialPort.isOpen():
            self.serialPort.close()
            return 0
        return 1
