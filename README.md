## RPiPico Voltmeter

---

RPi Pico powered battery level monitoring system

---

### Wiring

| Pico PIN | External PIN                                  |
|----------|-----------------------------------------------|
| 38       | Source GND                                    |
| 34       | Vin (through 10k and 1k ohms voltage divider) |
| 21       | Red LED (through 330 ohms resistor)           |
| 22       | Green LED (through 330 ohms resistor)         |

---

### Usage
Voltage range can be specified by changing values of resistors in voltage divider,
currently it's 0V - 36V (since we can't exceed 3.3V on ADC pin), so we maintain 1 to 11 ratio
(1V on ADC pin = 11V of source voltage).  For LEDs and battery levels thresholds see `consts.py`
