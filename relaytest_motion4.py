#relaytest_motion4.py
#Import GPIO and time libraries.
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#Set variables for the GPIO pins driving the lamp relay channels, and receiving for
# the PIR sensor.
lamp1 = 5
lamp2 = 6
lamp3 = 13
lamp4 = 19
pirPin = 17

GPIO.setup(lamp1,GPIO.OUT)
GPIO.setup(lamp2,GPIO.OUT)
GPIO.setup(lamp3,GPIO.OUT)
GPIO.setup(lamp4,GPIO.OUT)
GPIO.setup(pirPin,GPIO.IN)

lamps_on = False
motion_detected = 0

def check_for_motion():
		motion_detected = GPIO.input(pirPin)
		if motion_detected == 1:
			print "motion_detected is True"
			return True
		else:
			print "motion_detected is False"
			return False

def turn_lamps_on():
	#turn all lamps on in sequence
	GPIO.output(lamp1, GPIO.LOW)
	time.sleep(.25)
	GPIO.output(lamp2, GPIO.LOW)
	time.sleep(.25)
	GPIO.output(lamp3, GPIO.LOW)
	time.sleep(.25)
	GPIO.output(lamp4, GPIO.LOW)
	lamps_on = True

def turn_lamps_off():
	#turn all lamps off in sequence
	GPIO.output(lamp1, GPIO.HIGH)
	time.sleep(.25)
	GPIO.output(lamp2, GPIO.HIGH)
	time.sleep(.25)
	GPIO.output(lamp3, GPIO.HIGH)
	time.sleep(.25)
	GPIO.output(lamp4, GPIO.HIGH)
	lamps_on = False

def lamps_are_on():
	time.sleep(60)
	if check_for_motion() == True:
		lamps_are_on()
	else:
		turn_lamps_off()

def lamps_are_off():
	time.sleep(1)
	if check_for_motion() == False:
		lamps_are_off()
	else:
		turn_lamps_on()

def main():
	try:
		while True:
			if lamps_on == True:
				lamps_are_on()
			else:
				lamps_are_off()

	except KeyboardInterrupt:
		print "  Quit"
		# Reset GPIO settings
		turn_lamps_off()
		GPIO.cleanup()
