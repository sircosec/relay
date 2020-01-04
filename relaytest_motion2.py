"""This script combines a PIR motion sensor with four individual lamps driven by opto-isolated relays.
If the PIR sensor senses motion, the script will turn on the four lamps waiting a brief time in between. 
A timer is then set for five minutes, during which if motion is not sensed, the lamps will be turned off
again in sequence, waiting a brief time in between. If motion is not detected by the PIR sensor the lamps 
will remain off.
"""
#relaytest_motion2.py
#Import GPIO and time libraries.
import RPi.GPIO as GPIO
import time

#Set variables for the GPIO pins driving the lamp relay channels, and receiving for
# the PIR sensor.
lamp1 = 5
lamp2 = 6
lamp3 = 13
lamp4 = 19
pirPin = 17

#Configure the GPIO pins driving the lamps as output pins, and the pin for the PIR 
#sensor as an input.
GPIO.setmode(GPIO.BCM)
GPIO.setup(lamp1,GPIO.OUT)
GPIO.setup(lamp2,GPIO.OUT)
GPIO.setup(lamp3,GPIO.OUT)
GPIO.setup(lamp4,GPIO.OUT)
GPIO.setup(pirPin,GPIO.IN)

#Turn all lamps on in sequence, waiting a short time in between.
def all_lamps_on():
	GPIO.output(lamp1, GPIO.LOW)
	time.sleep(lamp_on_delay)
	GPIO.output(lamp2, GPIO.LOW)
	time.sleep(lamp_on_delay)
	GPIO.output(lamp3, GPIO.LOW)
	time.sleep(lamp_on_delay)
	GPIO.output(lamp4, GPIO.LOW)
	lamps_on = True

#Turn all lamps off in reverse sequence, waiting a short time in between.
def all_lamps_off():
	GPIO.output(lamp1, GPIO.HIGH)
	time.sleep(lamp_on_delay)
	GPIO.output(lamp2, GPIO.HIGH)
	time.sleep(lamp_on_delay)
	GPIO.output(lamp3, GPIO.HIGH)
	time.sleep(lamp_on_delay)
	GPIO.output(lamp4, GPIO.HIGH)
	lamps_on = False

#Reset the count_to_timer variable back to the desired time before turning them off.
def reset_counter(counter):
	counter = 0
#Increment the counter variable by one.
def increment_counter(counter):
	counter = counter + 1
	
#Set the motion_detected variable to True based on the PIR sensor input.	
def set_motion_to_true():
	motion_detected = True
	return motion_detected
	
#Set the motion_detected variable to False based on the PIR sensor input.
def set_motion_to_false():
	motion_detected = False
	return motion_detected

#Check for the condition of the motion sensor and set the variable motion_detected to True or False.
def check_for_motion(motion_detected):
	if GPIO.input(pirPin) == 1:
		print "setting set_motion_to_true to True."
		set_motion_to_true()
		return motion_detected
	else:
		print "setting set_motion_to_true to False."
		set_motion_to_false()
		return motion_detected

#Check for the condition of the lamps and set the lamps_on variable accordingly.
def check_lamps():
	if lamps_on == True:
		return True
	else:
		return False

#The counter variable is used to determine how long the script should wait between 
#iterations of checking the PIR sensor for motion.
counter = 0
reset_counter(counter)
#The motion_detected variable is used to capture the condition of the PIR sensor, 
#either True or False
motion_detected = False
#The lamps_on variable is used to capture the condition of the lamps, either on 
#(True) or off (False)
lamps_on = False
#The count_to_timer variable is effectively the number of seconds the script should 
#wait before turning the lamps off, 
#provided no motion is detected.
count_to_timer = 300
#This is the delay between turning on individual lamps.
lamp_on_delay = .25	
		
try:
	print "=> testing lamps"
	time.sleep(.25)
	print "==> lamp 1"
	GPIO.output(lamp1, GPIO.LOW)
	time.sleep(.25)
	print "===> lamp 2"
	GPIO.output(lamp2, GPIO.LOW)
	time.sleep(.25)
	print "====> lamp 3"
	GPIO.output(lamp3, GPIO.LOW)
	time.sleep(.25)
	print "=====> lamp 4"
	GPIO.output(lamp4, GPIO.LOW)
	print "=> reverting lamps"
	time.sleep(.25)
	print "==> lamp 1"
	GPIO.output(lamp1, GPIO.HIGH)
	time.sleep(.25)
	print "===> lamp 2"
	GPIO.output(lamp2, GPIO.HIGH)
	time.sleep(.25)
	print "====> lamp 3"
	GPIO.output(lamp3, GPIO.HIGH)
	time.sleep(.25)
	print "=====> lamp 4"
	GPIO.output(lamp4, GPIO.HIGH)
	print "setting motion to false"
	set_motion_to_false()
	print "turning OFF all lamps"
	all_lamps_off()
	while True:
		print "=======> beginning loop <======="
		print "checking for motion"
		#This function will set the motion_detected variable to True if it is equal to 1, or False if it is equal to 0.
		time.sleep(1)		
		if GPIO.input(pirPin) == 1:
			print "motion detected"
			print "checking lamps"
			check_lamps()
			if lamps_on == False:
				print "lamps are OFF"
				print "turning lamps ON"
				reset_counter(counter)
				all_lamps_on()
			else:
				print "lamps are already ON"
				print "resetting counter"
				reset_counter(counter)
		else:
			print "no motion detected"
			print "checking lamps"
			if lamps_on == True:
				print "lamps are on"
				print "checking counter"
				if counter >= count_to_timer:
					print "timer hit"
					print "turning off all lamps"
					all_lamps_off()
				else:
					print "lamps are off"
					time.sleep(1)
			else:
				print "timer not hit"
				print "the timer is at %d" % (counter)
				print "waiting"
				time.sleep(1)
				increment_counter(counter)

except KeyboardInterrupt:
	print "  Quit"
	# Reset GPIO settings
	GPIO.cleanup()
