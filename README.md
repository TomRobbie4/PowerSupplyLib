# PowerSupplyLib ⚡

Une librairie Python basée sur **PySide6** pour le contrôle d'un module multi-canaux via un port série (jusqu'à 120 canaux).  
Permet l’ouverture/fermeture individuelle des canaux et le réglage de la **puissance (duty cycle)** sur chacun.

---

## 🚀 Fonctionnalités

- 🔌 Ouverture/fermeture automatique du port série
- 🎚️ Contrôle jusqu’à 120 canaux indépendants
- 📤 Envoi de commandes simples sur port série (open, close, duty)
- 📦 Intégration facile dans une GUI PySide6/Qt

---

## 🧱 Dépendances

```bash
pip install PySide6
```
---

## 📚 Classes et Méthodes

```bash
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

    def open(self):
        """
        Active le canal.

        Retour :
            int : 0 si succès, 1 si erreur.
        """

    def close(self):
        """
        Désactive le canal.

        Retour :
            int : 0 si succès, 1 si erreur.
        """

    def setDuty(self):
        """
        Applique la valeur de duty cycle au canal.

        Retour :
            int : 0 si succès, 1 si erreur.
        """

@dataclass
class powerSupply_:
    """
    Gestionnaire global d'alimentation, permettant le contrôle de jusqu'à 120 canaux via un port série.

    Attributs :
        portName (str) : Nom du port série (ex: "COM3").
        serialPort (QSerialPort) : Objet PySide6 pour la communication série.
        CH1 à CH120 (Channel_) : Canaux instanciés automatiquement.
    """

    def __post_init__(self):
        """
        Initialise les 120 canaux et configure le port série.
        """

    def openSerial(self):
        """
        Ouvre le port série configuré.

        Retour :
            int : 0 si succès, 1 si erreur.
        """

    def closeSerial(self):
        """
        Ferme le port série s’il est ouvert.

        Retour :
            int : 0 si succès, 1 si erreur.
        """

```

📄 Exemple d'utilisation

```bash
from PowerSupplyLib import powerSupply_

# Initialisation de l'alimentation avec le port série
psu = powerSupply_()
psu.portName = "COM3"
psu.openSerial()

# Ouvrir et configurer le canal 1
psu.CH1.open()
psu.CH1.setDuty(32768)  # Exemple de setting du duty cycle à 50%

# Fermer le canal 1
psu.CH1.close()

# Fermer le port série
psu.closeSerial()
```
