"""This script combines a PIR motion sensor with four individual lamps driven by opto-isolated relays.
If the PIR sensor senses motion, the script will turn on the four lamps waiting a brief time in between. 
A timer is then set for five minutes, during which if motion is not sensed, the lamps will be turned off
again in sequence, waiting a brief time in between. If motion is not detected by the PIR sensor the lamps 
will remain off.
"""
#Import GPIO and time libraries.
import RPi.GPIO as GPIO
import time

#Set up sleep time variables as various intervals are needed and referenced multiple times.
sleeptime = .25
motionsleeptime = 15
waittime = 1

#Set variables for the GPIO pins driving the lamp relay channels, and receiving for the PIR sensor.
lamp1 = 5
lamp2 = 6
lamp3 = 13
lamp4 = 19
pirPin = 4

#Configure the GPIO pins driving the lamps as output pins, and the pin for the PIR sensor as an input.
GPIO.setmode(GPIO.BCM)
GPIO.setup(lamp1, GPIO.OUT)
GPIO.setup(lamp2, GPIO.OUT)
GPIO.setup(lamp3, GPIO.OUT)
GPIO.setup(lamp4, GPIO.OUT)
GPIO.setup(pirPin, GPIO.IN)

#Turn all lamps on in sequence, waiting for the sleeptime in between.
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
	lamps_on = True

#Turn all lamps off in sequence, waiting for the sleeptime in between.
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
	lamps_on = False

#Set the motion sensor variable to false and return it.	
def set_motion_to_false():
	motion_sensor_tripped = False
	return motion_sensor_tripped

#Set the motion sensor variable to true and return it.
def set_motion_to_true():
	motion_sensor_tripped = True
	return motion_sensor_tripped

#Read the PIR GPIO input pin to see if motion has been detected by the sensor.	
def check_for_motion():
	#If the sensor has detected motion, call the function set_motion_to_true().
	if GPIO.input(pirPin) == 1:
		set_motion_to_true()
	else:
		#If the sensor has not detected motion, call the function set_motion_to_false().
		set_motion_to_false()

#If motion is sensed, call the all_lamps_on() function		
def motion_sensed():
	print "motion sensed"
	print "turning on all lamps"
	all_lamps_on()

#Set the default state of the motion sensor variable to False. This should mean that the lamps will always be off when the script starts.
motion_sensor_tripped = False

#Initialize a variable to capture the state of the lamps, on or off.
lamps_on = False
	
#Set a count-to timer limit for motion sensor. This represents the number of seconds the script will count to before turning the lamps off.
counterstarttime = 300
#Initialize the counter variable to 0 to start.
counter = 0

#Initialize an infinite while loop to continuously check for motion.
try:
	while True:
		#Iterate through a loop from 0 to 300 seconds (5 minutes).
		for i in range(0, counter):
			check_for_motion()
			#If motion is sensed, set the counter back to 0 seconds.
			if motion_sensor_tripped == True:
				print "motion sensor tripped = True"
				print "counter is at %d" % (counter)
				print "setting the count-to timer to 0"
				counter = 0
				print "counter is at %d" % (counter)
				print "turning on all lamps"
				all_lamps_on()
				time.sleep(waittime)
				
			#If motion is not sensed, set the motion sensor variable to False.
			else:
				print "motion sensor tripped = False"
				#If the count-to timer hits 300 seconds, turn off all lamps in sequence.
				if counter >= 300:
					print "counter is 300"
					print "turning off all lamps"
					all_lamps_off()
					time.sleep(waittime)
					
				else:
					print "counter =",counter
					counter = counter + 1
					time.sleep(waittime)

except KeyboardInterrupt:
	print "  Quit"
	# Reset GPIO settings
	GPIO.cleanup()



