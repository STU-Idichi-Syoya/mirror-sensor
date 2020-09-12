import RPi.GPIO as GPIO
import time, math
from scipy.io.wavfile import read

#rate,arr=read(r"/home/pi/Downloads/Kanojo, Okarishimasu Rent-a-Girlfriend PV Music Episode 3 OST [Piano Cover] (Synthesia)ピアノ (online-audio-converter.com).wav")

f=445
tw=2**(1/12)
GPIO.setmode(GPIO.BCM)
p=12


onkai={"D":f,"R":1.122*f,"M":f*1.26,"F":1.335*f,"S":1.498*f,"L":1.682*f,"Z":1.888*f,"DD":2*f}

onki_list=list(onkai.keys())





import threading as th
def sound(ok_s=True):
  if ok_s:
    f=ok
  else:
   f=alert
#  th.Thread(target=f).start()
  f()
def ok():

  GPIO.setup(p,GPIO.OUT)
  pwm=GPIO.PWM(p,44100)
  pwm.start(50)
  pwm.ChangeFrequency(2000)
  time.sleep(0.15)
  pwm.ChangeFrequency(2500)

  pwm.stop()



def startup():
 
  GPIO.setup(p,GPIO.OUT)
  pwm=GPIO.PWM(p,44100)
  pwm.start(50) 
  for o in ["D","R","M","F","S","L","Z","DD"]:
   o=onkai[o]
   pwm.ChangeFrequency(o)
   time.sleep(0.5)
#   pwm.ChangeDutyCycle(o)
  pwm.stop()

def alart():

  GPIO.setup(p,GPIO.OUT)
  pwm=GPIO.PWM(p,44100)
  for i in range(5):
   pwm.start(50)
#  for o in ["D","R","D","R","D"]:
#   o=onkai[o]
#   pwm.ChangeFrequency(o)
#  pwm.ChangeDutyCycle(o)
   pwm.ChangeFrequency(2000)
   time.sleep(0.3)
   pwm.stop()
   time.sleep(0.3)
   pwm.start(50)
   pwm.ChangeFrequency(2000)
   time.sleep(0.5)
   pwm.stop()

startup()
#time.sleep(1)
#for i in range(5):
# alart()
