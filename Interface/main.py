from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QPushButton, QLabel, QSpinBox
from Interface_ui import Ui_MainWindow

from powerSupply import *

@dataclass # When adding channel, link button etc to class and add each channel frame 
           # to enableWhenSerialConnected & disableWhenSerialConnected
class Channel_UI:
    number: bytes
    duty: int
    memory_duty: int
    voltage: float
    memory_voltage: float
    output_status: bool
    live_status: bool

    frame_Channel: QFrame
    spinBox_Duty: QSpinBox
    label_Current_Duty: QLabel
    label_Current_Voltage: QLabel
    label_Voltage: QLabel
    pushButton_State: QPushButton
    pushButton_LiveState: QPushButton
    pushButton_Set: QPushButton

duty_value = 0
powerSupply = powerSupply_()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.serialPort = QSerialPort(self)

        # Channel 1 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        self.CH1 = Channel_UI(number ='1', duty = 0, memory_duty = 0, voltage = 0, memory_voltage = 0, output_status = False, live_status = 0,
                frame_Channel=self.frame_Channel_CH_1,
                spinBox_Duty=self.spinBox_Duty_CH_1,
                label_Current_Duty= self.label_Current_Duty_CH_1,
                label_Current_Voltage= self.label_Current_Voltage_CH_1,
                label_Voltage= self.label_Voltage_CH_1,
                pushButton_State = self.pushButton_State_CH_1,
                pushButton_LiveState = self.pushButton_LiveState_CH_1,
                pushButton_Set = self.pushButton_Set_CH_1)
        
        self.CH1.spinBox_Duty.valueChanged.connect(lambda:self.sendOutputValue(self.CH1, powerSupply.CH1))
        self.CH1.pushButton_State.clicked.connect(lambda: self.setOutputStatus(self.CH1, powerSupply.CH1))
        self.CH1.pushButton_LiveState.clicked.connect(lambda:self.setLiveState(self.CH1, powerSupply.CH1))
        self.CH1.pushButton_Set.clicked.connect(lambda:self.setOutputValue(self.CH1, powerSupply.CH1))
        
        # Channel 2 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        self.CH2 = Channel_UI(number = '2', duty = 0, memory_duty = 0, voltage = 0, memory_voltage = 0, output_status = False, live_status = 0,
                frame_Channel=self.frame_Channel_CH_2,
                spinBox_Duty=self.spinBox_Duty_CH_2,
                label_Current_Duty= self.label_Current_Duty_CH_2,
                label_Current_Voltage= self.label_Current_Voltage_CH_2,
                label_Voltage= self.label_Voltage_CH_2,
                pushButton_State = self.pushButton_State_CH_2,
                pushButton_LiveState = self.pushButton_LiveState_CH_2,
                pushButton_Set = self.pushButton_Set_CH_2)
        
        self.CH2.spinBox_Duty.valueChanged.connect(lambda:self.sendOutputValue(self.CH2, powerSupply.CH2))
        self.CH2.pushButton_State.clicked.connect(lambda: self.setOutputStatus(self.CH2, powerSupply.CH2))
        self.CH2.pushButton_LiveState.clicked.connect(lambda:self.setLiveState(self.CH2, powerSupply.CH2))
        self.CH2.pushButton_Set.clicked.connect(lambda:self.setOutputValue(self.CH2, powerSupply.CH2))

        # Channel 3 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        self.CH3 = Channel_UI(number = '3', duty = 0, memory_duty = 0, voltage = 0, memory_voltage = 0, output_status = False, live_status = 0,
                frame_Channel=self.frame_Channel_CH_3,
                spinBox_Duty=self.spinBox_Duty_CH_3,
                label_Current_Duty= self.label_Current_Duty_CH_3,
                label_Current_Voltage= self.label_Current_Voltage_CH_3,
                label_Voltage= self.label_Voltage_CH_3,
                pushButton_State = self.pushButton_State_CH_3,
                pushButton_LiveState = self.pushButton_LiveState_CH_3,
                pushButton_Set = self.pushButton_Set_CH_3)
        
        self.CH3.spinBox_Duty.valueChanged.connect(lambda:self.sendOutputValue(self.CH3, powerSupply.CH3))
        self.CH3.pushButton_State.clicked.connect(lambda: self.setOutputStatus(self.CH3, powerSupply.CH3))
        self.CH3.pushButton_LiveState.clicked.connect(lambda:self.setLiveState(self.CH3, powerSupply.CH3))
        self.CH3.pushButton_Set.clicked.connect(lambda:self.setOutputValue(self.CH3, powerSupply.CH3))

        # Channel 4 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        self.CH4 = Channel_UI(number = '4', duty = 0, memory_duty = 0, voltage = 0, memory_voltage = 0, output_status = False, live_status = 0,
                frame_Channel=self.frame_Channel_CH_4,
                spinBox_Duty=self.spinBox_Duty_CH_4,
                label_Current_Duty= self.label_Current_Duty_CH_4,
                label_Current_Voltage= self.label_Current_Voltage_CH_4,
                label_Voltage= self.label_Voltage_CH_4,
                pushButton_State = self.pushButton_State_CH_4,
                pushButton_LiveState = self.pushButton_LiveState_CH_4,
                pushButton_Set = self.pushButton_Set_CH_4)
        
        self.CH4.spinBox_Duty.valueChanged.connect(lambda:self.sendOutputValue(self.CH4, powerSupply.CH4))
        self.CH4.pushButton_State.clicked.connect(lambda: self.setOutputStatus(self.CH4, powerSupply.CH4))
        self.CH4.pushButton_LiveState.clicked.connect(lambda:self.setLiveState(self.CH4, powerSupply.CH4))
        self.CH4.pushButton_Set.clicked.connect(lambda:self.setOutputValue(self.CH4, powerSupply.CH4))

        # Channel 5 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        self.CH5 = Channel_UI(number = '5', duty = 0, memory_duty = 0, voltage = 0, memory_voltage = 0, output_status = False, live_status = 0,
                frame_Channel=self.frame_Channel_CH_5,
                spinBox_Duty=self.spinBox_Duty_CH_5,
                label_Current_Duty= self.label_Current_Duty_CH_5,
                label_Current_Voltage= self.label_Current_Voltage_CH_5,
                label_Voltage= self.label_Voltage_CH_5,
                pushButton_State = self.pushButton_State_CH_5,
                pushButton_LiveState = self.pushButton_LiveState_CH_5,
                pushButton_Set = self.pushButton_Set_CH_5)
        
        self.CH5.spinBox_Duty.valueChanged.connect(lambda:self.sendOutputValue(self.CH5))
        self.CH5.pushButton_State.clicked.connect(lambda: self.setOutputStatus(self.CH5))
        self.CH5.pushButton_LiveState.clicked.connect(lambda:self.setLiveState(self.CH5))
        self.CH5.pushButton_Set.clicked.connect(lambda:self.setOutputValue(self.CH5))

        # Channel 6 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        self.CH6 = Channel_UI(number = '6', duty = 0, memory_duty = 0, voltage = 0, memory_voltage = 0, output_status = False, live_status = 0,
                frame_Channel=self.frame_Channel_CH_6,
                spinBox_Duty=self.spinBox_Duty_CH_6,
                label_Current_Duty= self.label_Current_Duty_CH_6,
                label_Current_Voltage= self.label_Current_Voltage_CH_6,
                label_Voltage= self.label_Voltage_CH_6,
                pushButton_State = self.pushButton_State_CH_6,
                pushButton_LiveState = self.pushButton_LiveState_CH_6,
                pushButton_Set = self.pushButton_Set_CH_6)
        
        self.CH6.spinBox_Duty.valueChanged.connect(lambda:self.sendOutputValue(self.CH6))
        self.CH6.pushButton_State.clicked.connect(lambda: self.setOutputStatus(self.CH6))
        self.CH6.pushButton_LiveState.clicked.connect(lambda:self.setLiveState(self.CH6))
        self.CH6.pushButton_Set.clicked.connect(lambda:self.setOutputValue(self.CH6))

        # Channel 7 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        self.CH7 = Channel_UI(number = '7', duty = 0, memory_duty = 0, voltage = 0, memory_voltage = 0, output_status = False, live_status = 0,
                frame_Channel=self.frame_Channel_CH_7,
                spinBox_Duty=self.spinBox_Duty_CH_7,
                label_Current_Duty= self.label_Current_Duty_CH_7,
                label_Current_Voltage= self.label_Current_Voltage_CH_7,
                label_Voltage= self.label_Voltage_CH_7,
                pushButton_State = self.pushButton_State_CH_7,
                pushButton_LiveState = self.pushButton_LiveState_CH_7,
                pushButton_Set = self.pushButton_Set_CH_7)
        
        self.CH7.spinBox_Duty.valueChanged.connect(lambda:self.sendOutputValue(self.CH7))
        self.CH7.pushButton_State.clicked.connect(lambda: self.setOutputStatus(self.CH7))
        self.CH7.pushButton_LiveState.clicked.connect(lambda:self.setLiveState(self.CH7))
        self.CH7.pushButton_Set.clicked.connect(lambda:self.setOutputValue(self.CH7))

        # Channel 8 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        self.CH8 = Channel_UI(number = '8', duty = 0, memory_duty = 0, voltage = 0, memory_voltage = 0, output_status = False, live_status = 0,
                frame_Channel=self.frame_Channel_CH_8,
                spinBox_Duty=self.spinBox_Duty_CH_8,
                label_Current_Duty= self.label_Current_Duty_CH_8,
                label_Current_Voltage= self.label_Current_Voltage_CH_8,
                label_Voltage= self.label_Voltage_CH_8,
                pushButton_State = self.pushButton_State_CH_8,
                pushButton_LiveState = self.pushButton_LiveState_CH_8,
                pushButton_Set = self.pushButton_Set_CH_8)
        
        self.CH8.spinBox_Duty.valueChanged.connect(lambda:self.sendOutputValue(self.CH8))
        self.CH8.pushButton_State.clicked.connect(lambda: self.setOutputStatus(self.CH8))
        self.CH8.pushButton_LiveState.clicked.connect(lambda:self.setLiveState(self.CH8))
        self.CH8.pushButton_Set.clicked.connect(lambda:self.setOutputValue(self.CH8))

        # Connexion des boutons et des actions
        self.pushButton_Serial_Connect.clicked.connect(self.connect_to_serialPort)


        # Initialisation du port série
        for port in QSerialPortInfo.availablePorts():
            self.comboBox_Port.addItem(port.portName())

        self.connectionStatus = False
        
        # Connecter la fonction pour lire les données quand elles arrivent
        powerSupply.serialPort.readyRead.connect(self.read_serial_data)

#  Fonction qui permette de générer des tensions avec différent channel  

    def setOutputStatus(self, CH: Channel_UI, PwrSupCH: Channel_):
        if CH.output_status == False:
            CH.pushButton_State.setText("Off")
            CH.pushButton_Set.setEnabled(True)
            CH.pushButton_LiveState.setEnabled(True)
            CH.spinBox_Duty.setEnabled(True)
            CH.output_status = True

            PwrSupCH.number = int(CH.number)
            PwrSupCH.status = CH.output_status
            PwrSupCH.duty = CH.duty
            if PwrSupCH.open() == 0:
                print("Canal 2 ouvert avec succès.")
            else:
                print("Erreur lors de l'ouverture du canal 2.")
            #self.openChannel(self.serialPort, CH) ######################################
        else:
            CH.pushButton_State.setText("On")
            CH.pushButton_Set.setEnabled(False)
            CH.pushButton_LiveState.setEnabled(False)
            CH.spinBox_Duty.setEnabled(False)
            CH.output_status = False

            PwrSupCH.number = int(CH.number)
            PwrSupCH.status = CH.output_status
            PwrSupCH.duty = CH.duty
            PwrSupCH.close()
            #self.closeChannel(self.serialPort, CH)####################################################
        #self.sendData(CH)

    def setLiveState(self, CH: Channel_UI, PwrSupCH: Channel_):
        if CH.live_status == False:
            CH.pushButton_LiveState.setText("Live Off")
            CH.live_status = True
            PwrSupCH.number = int(CH.number)
            PwrSupCH.status = CH.output_status
            PwrSupCH.duty = CH.duty
            PwrSupCH.setDuty()
            #self.sendOutputValue()              #####################################################
        else:
            CH.pushButton_LiveState.setText("Live On")
            CH.live_status = False

    def setOutputValue(self, CH: Channel_UI, PwrSupCH: Channel_):
        if CH.live_status == True:
            return
        CH.duty = CH.memory_duty
        CH.label_Current_Duty.setText(f"{CH.duty}")
        CH.voltage = CH.memory_voltage
        CH.label_Current_Voltage.setText(f"{CH.voltage:.4f}")

        PwrSupCH.number = int(CH.number)
        PwrSupCH.status = CH.output_status
        PwrSupCH.duty = CH.duty
        PwrSupCH.setDuty()
        #self.sendData(CH)################################################################################
        #Send data
    
    def sendOutputValue(self, CH: Channel_UI, PwrSupCH: Channel_):
        CH.memory_duty = CH.spinBox_Duty.value()
        # Calculer le voltage
        CH.memory_voltage = (12 / 4096) * CH.memory_duty
        CH.label_Voltage.setText(f"{CH.memory_voltage:.4f}")

        if CH.live_status == True:
            CH.duty = CH.memory_duty
            CH.label_Current_Duty.setText(f"{CH.duty}")
            CH.voltage = CH.memory_voltage
            CH.label_Current_Voltage.setText(f"{CH.voltage:.4f}")
            PwrSupCH.number = int(CH.number)

            PwrSupCH.status = CH.output_status
            PwrSupCH.duty = CH.duty

            PwrSupCH.setDuty()
            #self.setDutyChannel(self.serialPort, CH) ######################################################
            #self.sendData(CH)

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    def connect_to_serialPort(self):
        
        powerSupply.portName = self.comboBox_Port.currentText()

        if powerSupply.openSerial() == 0:
            self.connectionStatus = True
            self.pushButton_Serial_Connect.setText("Déconnecter")
            self.enableWhenSerialConnected()
            self.comboBox_Port.setDisabled(True)
        else:
            if self.connectionStatus == True:
                self.connectionStatus = False
                self.pushButton_Serial_Connect.setText("Connecter")
                self.comboBox_Port.setEnabled(True)
                powerSupply.closeSerial()
                self.disableWhenSerialConnected()

    def enableWhenSerialConnected(self):
        self.CH1.frame_Channel.setEnabled(True)
        self.CH2.frame_Channel.setEnabled(True)
        self.CH3.frame_Channel.setEnabled(True)
        self.CH4.frame_Channel.setEnabled(True)
        self.CH5.frame_Channel.setEnabled(True)
        self.CH6.frame_Channel.setEnabled(True)
        self.CH7.frame_Channel.setEnabled(True)
        self.CH8.frame_Channel.setEnabled(True)
    
    def disableWhenSerialConnected(self):
        self.CH1.frame_Channel.setEnabled(False)
        self.CH2.frame_Channel.setEnabled(False)
        self.CH3.frame_Channel.setEnabled(False)
        self.CH4.frame_Channel.setEnabled(False)
        self.CH5.frame_Channel.setEnabled(False)
        self.CH6.frame_Channel.setEnabled(False)
        self.CH7.frame_Channel.setEnabled(False)
        self.CH8.frame_Channel.setEnabled(False)

    def read_serial_data(self):
        # Lire les données du port série quand elles arrivent
        data = powerSupply.serialPort.readAll()
        print(data)  # Affiche les données reçues

    def closeEvent(self, event):
        # Fermer proprement la connexion série lors de la fermeture de la fenêtre
        if self.connectionStatus:
            self.serialPort.close()
            powerSupply.closeSerial()
        event.accept()


app = QApplication([])
window = MainWindow()
window.show()
app.exec_() 
