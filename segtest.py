import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
## a b c d e f g
a=[5,13,26,20,16,6,19]
s=[22,10,9,11]
dot_pin=21

DIGIT_ON=GPIO.LOW
DIGIT_OFF=GPIO.HIGH

SEG_ON=GPIO.HIGH
SEG_OFF=GPIO.LOW


for i in a:
  GPIO.setup(i,GPIO.OUT)
  GPIO.output(i,SEG_OFF)
  
for i in s:
  GPIO.setup(i,GPIO.OUT)
  GPIO.output(i,DIGIT_OFF)


GPIO.output(s[2],DIGIT_ON)
GPIO.output(a[0],SEG_ON)
GPIO.setup(dot_pin,GPIO.OUT)
GPIO.output(dot_pin,GPIO.HIGH)

#GPIO.output(a[1],GPIO.HIGH)
#GPIO.output(a[0],GPIO.HIGH)
#GPIO.output(a[3],GPIO.HIGH)


import time
print("wait")
time.sleep(60*60)
GPIO.cleanup()

