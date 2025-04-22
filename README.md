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

## Methods

```bash
/**
 * @fn setMode
 * @brief set power mode 
 * @param powerMode Set power mode,three are normal mode and power down mode.
 * @n               The following are three modes of power down.
 * @n               MCP4725_POWER_DOWN_1KRES      1 kΩ resistor to ground
 * @n               MCP4725_POWER_DOWN_100KRES    100 kΩ resistor to ground
 * @n               MCP4725_POWER_DOWN_500KRES    500 kΩ resistor to ground
 * @return None
 */
```

