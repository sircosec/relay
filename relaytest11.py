import RPi.GPIO as GPIO
import time

sleeptime = .25
motionsleeptime = 300
waittime = 1

lamp1 = 5
lamp2 = 6
lamp3 = 13
lamp4 = 19
pirPin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(lamp1, GPIO.OUT)
GPIO.setup(lamp2, GPIO.OUT)
GPIO.setup(lamp3, GPIO.OUT)
GPIO.setup(lamp4, GPIO.OUT)
GPIO.setup(pirPin, GPIO.IN)

def all_lamps_on():
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
	
def all_lamps_off():	
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

def motion_sensed():
	if GPIO.input(pirPin) == 1:
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
		if GPIO.input(pirPin) == 1:
			print "Motion detected"
			motion_sensed()
			time.sleep(motionsleeptime)
		else:
			print "No motion detected"
			time.sleep(waittime)

except KeyboardInterrupt:
    print "/n"
	print "keyboard interrupt detected!"	

finally:
	print "Done"
	GPIO.cleanup()
