
def re(sen):
	import RPi.GPIO as GPIO
	import time
	GPIO.setmode(GPIO.BOARD)

	TRIG=11
	ECHO=13


	if sen==0:
		GPIO.setwarnings(False)
		GPIO.setup(TRIG,GPIO.OUT)
		GPIO.setup(ECHO,GPIO.IN)
	
		GPIO.output(TRIG,GPIO.LOW)
		time.sleep(0.3)
		GPIO.output(TRIG,True)
		time.sleep(0.00001)
		
		while GPIO.input(ECHO)==0:
			signaloff=time.time()
			
		while GPIO.input(ECHO)==1:
			signalon=time.time()
		
		timepass=signalon-signaloff
		
		distance=timepass*17000
		return distance
		GPIO.cleanup()

if __name__=="__main__":
	print(re(0))

