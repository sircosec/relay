import RPi.GPIO as GPIO
import time

channel1 = 15
channel2 = 4
sleeptime = 1

GPIO.setmode(GPIO.BCM)

pinList = [channel1,channel2]

for i in pinList:
	print "Setting up pin", i, "as output"
	GPIO.setup(i,GPIO.OUT)

try:
#	for i in pinList:
#		print "pin ",i," HIGH"
#		GPIO.output(i,GPIO.HIGH)
#		time.sleep(sleeptime)
#		print "pin ",i," LOW"
#		GPIO.output(i,GPIO.LOW)
#		time.sleep(sleeptime)
#

	print "channel 1 HIGH"
	GPIO.output(channel1,GPIO.HIGH)
	time.sleep(sleeptime)
	print "channel 1 LOW"
	GPIO.output(channel1,GPIO.LOW)
	time.sleep(sleeptime)
	print "channel 2 HIGH" 
	GPIO.output(channel2,GPIO.HIGH)
	time.sleep(sleeptime)
	print "channel 2 LOW"
	GPIO.output(channel2,GPIO.LOW)


except KeyboardInterrupt:
        print "keyboard interrupt"

finally:
	print "Cleaning up"
        GPIO.cleanup()

