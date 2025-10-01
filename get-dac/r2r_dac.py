import RPi.GPIO as GPIO
dac_bits = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setup(dac_bits, GPIO.OUT)
dynamic_range = 3.19
