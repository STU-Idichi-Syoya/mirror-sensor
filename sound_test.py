import RPi.GPIO as GPIO

import time


GPIO.setmode(GPIO.BCM)
pin=12
GPIO.setup(pin,GPIO.OUT)

GPIO.PWM(pin,500)
time.sleep(10)