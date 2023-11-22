import machine
import time
from consts import Consts


def get_voltage_samples(samples_count=600, delay=0.5):
    adc = machine.ADC(Consts.ADC_PIN)
    samples = []

    current_sample_id = 0

    while current_sample_id < samples_count:
        adc_value = adc.read_u16()

        adc_voltage = adc_value * Consts.ADC_CONVERSION_FACTOR
        voltage = adc_voltage * Consts.VOLTAGE_DIVIDER_FACTOR

        print(f"processing sample no. {current_sample_id} - ADC: {adc_voltage}V - Input: {voltage}V")

        samples.append(voltage)

        current_sample_id += 1
        time.sleep(delay)

    return samples


def main():
    samples = get_voltage_samples()

    print(samples)


if __name__ == '__main__':
    main()
