import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [16, 12, 25, 17, 27, 23, 22, 24]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
up = 9
down = 10
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)
num = 0
def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
while True:
    if GPIO.input(up):
        if num<256:
            num = num + 1
            print(num, dec2bin(num))
            time.sleep(0.2)
        else:
            num=0
    if GPIO.input(down):
        if num > 0:
            num = num - 1
            print(num, dec2bin(num))
            time.sleep(0.2)
        else:
            num=0
    for i in range (len(leds)):
        GPIO.output(leds[i], dec2bin(num)[i])