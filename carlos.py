import RPi.GPIO as GPIO


ON=GPIO.HIGH
OFF=GPIO.LOW


digit_pins=[17,27,22,10]
dot=7
segment_pins=[9,11,5,6,13,19,26]

i = 35.7

def setup():
    GPIO.setmode(GPIO.BCM)
    for i in digit_pins+segment_pins+[dot]:
         GPIO.setup(i,GPIO.OUT)

        ## initilize
    for i in digit_pins:
        GPIO.output(i,OFF)
            
    for i in segment_pins:
        GPIO.output(i,OFF)

setup()
try:
    while True:
        GPIO.output(digit_pins[1],ON)
        for p in segment_pins:
            GPIO.output(p,ON)
except:
      GPIO.cleanup()  