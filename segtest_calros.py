import RPi.GPIO as GPIO


ON=GPIO.HIGH
OFF=GPIO.LOW

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

digit_pins=[17,27,22,10]
dot=7
segment_pins=[9,11,5,6,13,19,26]
seg_arr=list("abcdefg")


for i in digit_pins+segment_pins+[dot]:
 GPIO.setup(i,GPIO.OUT)
 

## initilize
for i in digit_pins:
    GPIO.output(i,OFF)
    
for i in segment_pins:
    GPIO.output(i,OFF)
    
import time
## show number
three=list("abcd")
Number_arr=["abcdef","bc","abged","abcd","fgbc","afgcd","fedcg","abc","abcefg","abcdfg"]

show_dot=False


number=str(38.7)

while True:
  count=0
  for i in digit_pins:
    GPIO.output(i,ON)
    if count==len(number):break
    num=number[count]
    if len(number)>count+1:
        if number[count+1]==".":
            show_dot=True
            count+=1
    num=int(num)
    count+=1
    show=Number_arr[num]
    for j in show:
        print(j)
        j=seg_arr.index(j)
        GPIO.output(segment_pins[j],ON)
        if show_dot:
            GPIO.output(dot,ON)
            
    time.sleep(0.05)
    
    GPIO.output(i,OFF)
    for j in show:
        j=seg_arr.index(j)
        GPIO.output(segment_pins[j],OFF)
        if show_dot:
            GPIO.output(dot,OFF)
    show_dot=True



    

