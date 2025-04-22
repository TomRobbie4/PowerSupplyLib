# PowerSupplyLib ⚡

A Python library based on **PySide6** for controlling a multi-channel module via a serial port (up to 120 channels).  
Allows individual channel opening/closing and setting the **power (duty cycle)** for each.

---

## 🚀 Features

- 🔌 Automatic opening/closing of the serial port
- 🎚️ Control of up to 120 independent channels
- 📤 Send simple commands over the serial port (open, close, duty)
- 📦 Easy integration into a PySide6/Qt GUI

---

## 🧱 Dependencies

```bash
pip install PySide6
```
---

## 📚 Classes and Methods

```bash
@dataclass
class Channel_:
    """
    Represents a control channel.

    Attributes:
        number (int): Channel number (1 to 120).
        duty (int): Duty cycle value to apply (0 to 65535).
        status (bool): Channel status (True for active, False for inactive).
        serialPort (QSerialPort): Serial port used for communication.
    """

    def open(self):
        """
        Activates the channel.

        Returns:
            int: 0 if success, 1 if error.
        """

    def close(self):
        """
        Deactivates the channel.

        Returns:
            int: 0 if success, 1 if error.
        """

    def setDuty(self):
        """
        Applies the duty cycle value to the channel.

        Returns:
            int: 0 if success, 1 if error.
        """

@dataclass
class powerSupply_:
    """
    Global power supply manager, allowing control of up to 120 channels via a serial port.

    Attributes:
        portName (str): Name of the serial port (e.g., "COM3").
        serialPort (QSerialPort): PySide6 object for serial communication.
        CH1 to CH120 (Channel_): Channels automatically instantiated.
    """

    def __post_init__(self):
        """
        Initializes the 120 channels and configures the serial port.
        """

    def openSerial(self):
        """
        Opens the configured serial port.

        Returns:
            int: 0 if success, 1 if error.
        """

    def closeSerial(self):
        """
        Closes the serial port if it is open.

        Returns:
            int: 0 if success, 1 if error.
        """

```

📄 Usage Example

```bash
from PowerSupplyLib import powerSupply_

# Initialize the power supply with the serial port
psu = powerSupply_()
psu.portName = "COM3"
psu.openSerial()

# Open and configure channel 1
psu.CH1.open()
psu.CH1.setDuty(32768)  # Example of setting the duty cycle to 50%

# Close channel 1
psu.CH1.close()

# Close the serial port
psu.closeSerial()

```
