import RPi.GPIO as GPIO
import time

channel1 = 16
channel2 = 15
sleeptime = 1

GPIO.setmode(GPIO.BCM)

pinList = [channel1,channel2]

GPIO.setup(channel1, GPIO.OUT)
GPIO.setup(channel2, GPIO.OUT)

print "channel 1 HIGH"
GPIO.output(channel1, GPIO.HIGH)
time.sleep(sleeptime)

print "channel 2 HIGH"
GPIO.output(channel2, GPIO.HIGH)
time.sleep(sleeptime)

print "channel 1 LOW"
GPIO.output(channel1, GPIO.LOW)
time.sleep(sleeptime)


print "channel 2 LOW"
GPIO.output(channel2, GPIO.LOW)

GPIO.cleanup()
