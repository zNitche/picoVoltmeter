import machine
import time
from consts import Consts


class Voltmeter:
    def __init__(self):
        self.onboard_led = machine.Pin(Consts.ONBOARD_LED_PIN, machine.Pin.OUT)
        self.red_led = machine.Pin(Consts.RED_LED_PIN, machine.Pin.OUT)
        self.green_led = machine.Pin(Consts.GREEN_LED_PIN, machine.Pin.OUT)

        self.adc = machine.ADC(Consts.ADC_PIN)

        self.voltage = 0

    def init_leds(self):
        self.onboard_led.on()
        self.red_led.off()
        self.green_led.off()

    def update_leds(self):
        if self.voltage >= Consts.HIGH_BATTERY_THRESHOLD:
            self.red_led.off()
            self.green_led.on()

        elif Consts.LOW_BATTERY_VOLTAGE_THRESHOLD <= self.voltage <= Consts.HIGH_BATTERY_THRESHOLD:
            self.green_led.off()
            self.red_led.on()

        elif self.voltage <= Consts.EXTREME_LOW_VOLTAGE_THRESHOLD:
            self.green_led.off()
            self.red_led.toggle()

    def mainloop(self):
        while True:
            adc_value = self.adc.read_u16()
            adc_voltage = adc_value * Consts.CONVERSION_FACTOR

            self.voltage = adc_voltage * Consts.VOLTAGE_DIVIDER_FACTOR - Consts.VOLTAGE_ACCURACY

            self.update_leds()

            if Consts.PRINT_READING:
                print(f"ADC: {adc_value}, Voltage: {adc_voltage}, Source Voltage: {self.voltage}")

            time.sleep(Consts.UPDATE_TIME)

    def start(self):
        self.init_leds()
        self.mainloop()
