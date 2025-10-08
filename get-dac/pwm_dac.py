import RPi.GPIO as GPIO


class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)

        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)

    def deinit(self):
        self.pwm.stop()
        GPIO.cleanup()


    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
                print(f"напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
                print("устанавливаем 0.0 В")
                return 0
        duty_cycle = (voltage/self.dynamic_range)*100
        self.pwm.start(duty_cycle)
        print("коэффициент заполнения: " , duty_cycle)

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.3, True)

        while True:
            try:
                voltage = float(input("введите напряжение в вольтах: "))
                dac.set_voltage(voltage)
                

            except ValueError:
                print("вы ввели не число. попробуйте ещё раз\n")

    finally:
        dac.deinit()