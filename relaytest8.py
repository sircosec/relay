import RPi.GPIO as GPIO
import time

sleeptime = .25

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.OUT)
count = 0	
while count <= 10:
 	print "pin", 6, "LOW"
        GPIO.output(6, GPIO.LOW)
        time.sleep(sleeptime)
	print "pin", 6, "HIGH"
	GPIO.output(6, GPIO.HIGH)
	time.sleep(sleeptime)
	count = count + 1
print "Done"
GPIO.cleanup()
