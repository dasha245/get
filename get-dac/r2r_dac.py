import RPi.GPIO as GPIO


class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def voltage_to_number(self, voltage):
            if not (0.0 <= voltage <= self.dynamic_range):
                print(f"напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
                print("устанавливаем 0.0 В")
                return 0
            return int(voltage/self.dynamic_range*255)

    def number_to_dac(self, number):
            return [int(element) for element in bin(number)[2:].zfill(8)]

    def set_number(self, number):
        a = self.number_to_dac(number)
        GPIO.output(self.gpio_bits, a)

    def set_voltage(self, voltage):
        number = self.voltage_to_number(voltage)
        a = self.number_to_dac(number)
        print("число на вход ЦАП:", number, "биты:", a)
        GPIO.output(self.gpio_bits, a)

if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.19, True)

        while True:
            try:
                voltage = float(input("введите напряжение в вольтах: "))
                dac.set_voltage(voltage)
                number = int(input("введите целое число: "))
                dac.set_number(number)

            except ValueError:
                print("вы ввели не число. попробуйте ещё раз\n")

    finally:
        dac.deinit()