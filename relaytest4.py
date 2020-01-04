import RPi.GPIO as GPIO
import time

sleeptime = 1

GPIO.setmode(GPIO.BCM)

pinList = [21, 22, 23, 24, 25, 27, 28, 29]

for i in pinList:
	GPIO.setup(i, GPIO.OUT)

for i in pinList:
	print "pin", i, "HIGH"
	GPIO.output(i, GPIO.HIGH)
	time.sleep(sleeptime)
	print "pin", i, "LOW"
	GPIO.output(i, GPIO.LOW)
	time.sleep(sleeptime)

print "Done"
GPIO.cleanup()
