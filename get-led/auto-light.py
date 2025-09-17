import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
a = 6
GPIO.setup(a, GPIO.IN)

while True:
    state = GPIO.input(a)
    GPIO.output(led, 1 - state)