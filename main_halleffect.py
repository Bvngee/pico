# DRV5053VAQLPGM

from machine import Pin, ADC
import time

adc = ADC(Pin(26))

# Function to convert ADC reading to Gauss value
def adc_to_gauss(adc_value):
    # Calibration factor (mV/Gauss) for DRV5053VAQLPGM
    sensitivity = 1.65
    # Vref (reference voltage) of ADC (3.3V for ESP32)
    vref = 3.3
    # Convert ADC reading to voltage
    voltage = adc_value / 4095 * vref

    # Convert voltage to Gauss using sensitivity
    gauss = voltage / sensitivity
    return gauss

while True:
    gauss = adc_to_gauss(adc.read_u16())
    print("Magnetic Field Strength (Gauss):", gauss)
    time.sleep(0.2)
