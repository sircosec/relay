#relaytest_motion3.py
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

#Turn all lamps on in sequence, waiting a short time in between.
def all_lamps_on():
	GPIO.output(lamp1, GPIO.LOW)
	time.sleep(.25)
	GPIO.output(lamp2, GPIO.LOW)
	time.sleep(.25)
	GPIO.output(lamp3, GPIO.LOW)
	time.sleep(.25)
	GPIO.output(lamp4, GPIO.LOW)

#Turn all lamps off in reverse sequence, waiting a short time in between.
def all_lamps_off():
	GPIO.output(lamp1, GPIO.HIGH)
	time.sleep(.25)
	GPIO.output(lamp2, GPIO.HIGH)
	time.sleep(.25)
	GPIO.output(lamp3, GPIO.HIGH)
	time.sleep(.25)
	GPIO.output(lamp4, GPIO.HIGH)
	
try:
	counter = 0
	count_to_timer = 300
	print "testing all lamps"
	all_lamps_on()
	lamps_on = True
	print "sleeping..."
	time.sleep(2)
	print "turning all lamps off"
	all_lamps_off()
	lamps_on = False
		
	while True:
		motion_detected = GPIO.input(pirPin)
		if motion_detected == 1:
			print "motion_detected is True"
			print "setting counter to 0"
			counter = 0
			if lamps_on == False:
				print "lamps_on is False"
				print "turning lamps on"
				all_lamps_on()
				print "lamps are on"
				print "setting lamps_on to True"
				lamps_on = True
				print "sleeping..."
				time.sleep(1)
			else:
				print "lamps are already on"
				print "sleeping..."
				time.sleep(1)
		else:
			print "motion_detected is False"
			if lamps_on == True:
				print "lamps_on is True"
				print "incrementing counter"
				counter = counter + 1
				print "counter is at %d" % (counter)
				#check for the value of counter
				if counter == count_to_timer:
					print "count_to_timer hit"
					print "turning lamps off"
					all_lamps_off()
					print "setting lamps_on to False"
					lamps_on = False
					"sleeping..."
					time.sleep(1)
				else:
					print "count_to_timer not hit"
					print "leaving lamps on"
					print "sleeping..."
					time.sleep(1)
			else:
				print "lamps_on is False"
				print "sleeping..."
				time.sleep(1)
				
except KeyboardInterrupt:
	print "  Quit"
	# Reset GPIO settings
	GPIO.cleanup()