import RPi.GPIO as GPIO
import time

sleeptime = .25

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(4, GPIO.IN)

def motion_sensed():
	count = 0
	while count <=1:
		print "pin", 5, "LOW"
        	GPIO.output(5, GPIO.LOW)
        	time.sleep(3)
        	print "pin", 5, "HIGH"
        	GPIO.output(5, GPIO.HIGH)
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
