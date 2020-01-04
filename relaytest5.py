import RPi.GPIO as GPIO
import time

sleeptime = .25

GPIO.setmode(GPIO.BCM)

pinList = [5,6,13,19,26,16,20,21]

for i in pinList:
	GPIO.setup(i, GPIO.OUT)
	
for i in pinList:
 	print "pin", i, "LOW"
        GPIO.output(i, GPIO.LOW)
        time.sleep(sleeptime)
	print "pin", i, "HIGH"
	GPIO.output(i, GPIO.HIGH)
	time.sleep(sleeptime)

print "Done"
GPIO.cleanup()
