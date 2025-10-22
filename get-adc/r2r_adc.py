import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):

        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        self.gpio_bits = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def number_to_dac(self, number):
            a = [int(element) for element in bin(number)[2:].zfill(8)]
            for i, pin in enumerate(self.gpio_bits):
                GPIO.output(pin, a[i])

    def sequential_counting_adc(self):
        for number in range (256):
            self.number_to_dac(number)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio) == 1:
                return number

        return 255

    def get_sc_voltage(self):
        return (self.sequential_counting_adc()/255)*self.dynamic_range

if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.22)

        while True:
            voltage = adc.get_sc_voltage()
            print(f"Напряжение: {voltage:.3f} В")

    finally:
        adc.deinit()