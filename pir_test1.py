#Import GPIO and time libraries.
import RPi.GPIO as GPIO
import time

#Set variables for the GPIO pins driving the lamp relay channels, and receiving for
# the PIR sensor.
pirPin = 3

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pirPin, GPIO.IN)

try:
	while True:
		if GPIO.input(pirPin) == 1:
			print "motion detected!"
			time.sleep(1)
		else:
			print "nothing is happening."
			time.sleep(1)
			
except KeyboardInterrupt:
	print "Quit"
	# Reset GPIO settings
	GPIO.cleanup()		