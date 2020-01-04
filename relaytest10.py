import RPi.GPIO as GPIO
import time

sleeptime = .25
motionsleeptime = 5
waittime = 1

lamp1 = 5
lamp2 = 6
lamp3 = 13
lamp4 = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(lamp1, GPIO.OUT)
GPIO.setup(lamp2, GPIO.OUT)
GPIO.setup(lamp3, GPIO.OUT)
GPIO.setup(lamp4, GPIO.OUT)
GPIO.setup(4, GPIO.IN)

def motion_sensed():
	print "lamp1 ON"
        GPIO.output(lamp1, GPIO.LOW)
        time.sleep(sleeptime)
        print "lamp2 ON"
	GPIO.output(lamp2, GPIO.LOW)
	time.sleep(sleeptime)
	print "lamp3 ON"
	GPIO.output(lamp3, GPIO.LOW)
	time.sleep(sleeptime)
	print "lamp4 ON"
	GPIO.output(lamp4, GPIO.LOW)
	time.sleep(motionsleeptime)
	if GPIO.input(4) == 1:
		time.sleep(motionsleeptime)
	else:
		print "lamp1 OFF"
	       	GPIO.output(lamp1, GPIO.HIGH)
		time.sleep(sleeptime)
		print "lamp2 OFF"
		GPIO.output(lamp2, GPIO.HIGH)
		time.sleep(sleeptime)
                print "lamp3 OFF"
		GPIO.output(lamp3, GPIO.HIGH)
		time.sleep(sleeptime)
                print "lamp4 OFF"
		GPIO.output(lamp4, GPIO.HIGH)
        	time.sleep(sleeptime)
try:
	while True:
		if GPIO.input(4) == 1:
			print "motion were sensed!"
			motion_sensed()
		else:
			print "all is well"
			time.sleep(waittime)

except KeyboardInterrupt:
        print "/n"
	print "keyboard interrupt detected!"	

finally:
	print "Done"
	GPIO.cleanup()
