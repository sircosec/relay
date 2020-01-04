import RPi.GPIO as GPIO
import time

channel1 = 21
channel2 = 22
channel3 = 23
channel4 = 24
channel5 = 25
channel6 = 27 
channel7 = 28
channel8 = 29
sleeptime = 1

GPIO.setmode(GPIO.BCM)

pinList = [21,22,23,24,25,27,28,29]

GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(28, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)

for i in pinList:
	print "pin", i, "HIGH"
	GPIO.output(i, GPIO.HIGH)
	time.sleep(sleeptime)
	GPIO.output(i, GPIO.LOW)
	time.sleep(sleeptime)

print "Done"
GPIO.cleanup()
