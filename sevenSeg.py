import threading,queue
import conf
from conf import segment_io

import time


import RPi.GPIO as GPIO


DIGIT_ON=GPIO.LOW
DIGIT_OFF=GPIO.HIGH

SEG_ON=GPIO.HIGH
SEG_OFF=GPIO.LOW

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

digit_pins=[22,10,9,11]
dot_pin=21
segment_pins=[5,13,26,20,16,6,19]
seg_arr=list("abcdefg")


def setup():
    for i in digit_pins+segment_pins+[dot_pin]:
         GPIO.setup(i,GPIO.OUT)
 

        ## initilize
    for i in digit_pins:
        GPIO.output(i,DIGIT_OFF)
            
    for i in segment_pins:
        GPIO.output(i,SEG_OFF)
    
    GPIO.output(dot_pin,SEG_OFF)
    
def start_segment():
    
    threading.Thread(target=digit_show).start()
    

WAIT_TIME=0.0025
def one_number_show(i:int,dot=False):
    n=Number_arr[i]
    if dot:
        GPIO.output(dot_pin,SEG_ON)

    for ch in list(n):
        idx=seg_arr.index(ch)
        pin=segment_pins[idx]
        GPIO.output(pin,SEG_ON)
    time.sleep(WAIT_TIME)
    for ch in list(n):
        idx=seg_arr.index(ch)
        pin=segment_pins[idx]
        GPIO.output(pin,SEG_OFF)
        
    if dot:
        GPIO.output(dot_pin,SEG_OFF)
   
        
Char_arr={"C":"afed"," ":""
          
    }
Number_arr=["abcdef","bc","abdeg","abcdg","bcfg","acdfg","cdefg","abc","abcdefg","abcdfg"]

def one_char_show(i:str,dot=False):
    n=Char_arr[i]
    
    if dot:
        #print("char-->",i,dot)
        GPIO.output(dot_pin,SEG_ON)
    else:
        GPIO.output(dot_pin,SEG_OFF)
    
    for ch in list(n):
        if ch in seg_arr:
            idx=seg_arr.index(ch)
            pin=segment_pins[idx]
            GPIO.output(pin,SEG_ON)
        
    time.sleep(WAIT_TIME)
    
    for ch in list(n):
        idx=seg_arr.index(ch)
        pin=segment_pins[idx]
        GPIO.output(pin,SEG_OFF)
        
    if dot:
        GPIO.output(dot_pin,SEG_OFF)

class show_num:
    def __init__(self,str_i:str):
        self.str_idx=0
        self.str_i=str_i
    def isNext_dot(self):
        if self.str_i[self.str_idx]==".":
            self.str_idx+=1
            self.str_idx%=len(self.str_i)
            return True
        
        return False
    def __next__(self):
        r=self.str_i[self.str_idx]
        self.str_idx+=1
        self.str_idx=self.str_idx%len(self.str_i)
        return r


class CHR_state:
    def __init__(self,arr=["1111","2222","3333","4444","5555","6666","7777","8888","9999"]):
        self.arr=arr
        self.idx=0
        self.stime=time.time()
        self.dur=0.5
    def __next__(self):
        if time.time()-self.stime<self.dur:
           return self.arr[self.idx]
        
        self.idx=(self.idx+1)%len(self.arr)
        return self.arr[self.idx]
    
digit_que=queue.Queue()
def digit_show(FOURdigit_str:str="1111"):
    digit_idx=0
    len_show=len(FOURdigit_str)
    str_idx=0
    
    if 4>len_show or len_show>8:
        import sys
        print("digit_show::len()>=9 or <=3",file=sys.stderr)
        
    FOURdigit_str=show_num(FOURdigit_str)
    
    number_str=list(map(str,range(10)))
    
    while True:
        
        if not digit_que.empty():
            
            obj=digit_que.get()
            if FOURdigit_str.str_i== obj:
                pass
            else:
                digit_idx=0
                FOURdigit_str=show_num(obj)
        
        dot=FOURdigit_str.isNext_dot()
        
        
        show_char=next(FOURdigit_str)
        
     #   print(digit_idx,"char-->",show_char)
        GPIO.output(digit_pins[digit_idx],DIGIT_ON)
        
        if show_char in number_str:
            one_number_show(int(show_char),dot=dot)
        else:
            one_char_show(show_char,dot=dot)
            
        GPIO.output(digit_pins[digit_idx],DIGIT_OFF)
        
        digit_idx+=1
        if digit_idx==4:
            digit_idx=0
        
if __name__ == "__main__":
    #q=start_segment()
    i=0
    setup()
    num=str("4545")
    
    setup()
    start_segment()

    sevenQue=digit_que

    nexter_str=CHR_state()
    
    time.sleep(0.1)
    
    while True:
        n=next(nexter_str)
        
        #sevenQue.put(n)
        #time.sleep(0.2)
        for i in range(9999,-1,-1):
            sevenQue.put("3.75C")
            time.sleep(1)
        
    
    digit_show(num)
    """
    while True:
        i=i%len(digit_pins)
        GPIO.output(digit_pins[i],DIGIT_ON)
        j=num[i]
        j=int(j)
        one_number_show(j)
        GPIO.output(digit_pins[i],DIGIT_OFF)
        i+=1
    """