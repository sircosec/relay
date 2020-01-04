import RPi.GPIO as GPIO
import time

sleeptime = .25
motionsleeptime = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(4, GPIO.IN)

def motion_sensed():
	count = 0
	while count <=3:
		print "pin", 5, "LOW"
        	GPIO.output(5, GPIO.LOW)
        	time.sleep(sleeptime)
        	GPIO.output(6, GPIO.LOW)
		time.sleep(sleeptime)
		GPIO.output(13, GPIO.LOW)
		time.sleep(sleeptime)
		GPIO.output(19, GPIO.LOW)
		time.sleep(motionsleeptime)
		if GPIO.input(4) == 1:
			time.sleep(motionsleeptime)
		else:
			print "pin", 5, "HIGH"
	        	GPIO.output(5, GPIO.HIGH)
			GPIO.output(6, GPIO.HIGH)
			GPIO.output(13, GPIO.HIGH)
			GPIO.output(19, GPIO.HIGH)
        		time.sleep(sleeptime)
		count = count + 1
try:
	while True:
		if GPIO.input(4) == 1:
			print "motion were sensed!"
			motion_sensed()
			time.sleep(sleeptime)
		else:
			print "all is well"
			time.sleep(sleeptime)

except KeyboardInterrupt:
        print "/n"
	print "keyboard interrupt detected!"	

finally:
	print "Done"
	GPIO.cleanup()
