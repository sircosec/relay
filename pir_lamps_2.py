import RPi.GPIO as GPIO
import time

# this version logs actions taken to /var/log/pir_lamps
logfile = "/var/log/pir_lamps/pir_lamps.log"
# variable which controls the time interval between the lamps turning on and off
sleeptime = .25
# variable for tracking the condition of the lamps (True/False)
lamps_on = False
# variable for tracking the condition of the pir sensor (motion True/False)
motion = False
# variable which controls how long (in 5 second intervals) the lamps should stay on for when motion is detected.
# default: 60 * 5 = 300 seconds (5 minutes)
intervals = 60
# variable to control the time interval between checks of the pir motion sensor
# default: 5 seconds
# note: this gets multiplied by intervals in the state_on_loop() function
wait = 5
# use BCM mode for addressing the pins
GPIO.setmode(GPIO.BCM)
# assigning the pins variable names to make coding them simpler
lamp1 = 26
lamp2 = 19
lamp3 = 13
lamp4 = 6
lamps = [lamp1,lamp2,lamp3,lamp4]
# assign the pir sensor input pin a variable to make coding it simpler
pirPin = 5
# example code for turning lamps on and off
# lampx ON
# GPIO.output(i, GPIO.LOW)
# lampx OFF
# GPIO.output(i, GPIO.HIGH)

def log_action(message):
    timestamp = time.asctime()
    file = open(logfile, "a")
    file.write("@ " + timestamp + " " + message + "\n")
    file.close()

def lamp_on(lamp_number):
    #print("setting", lamp_number, "to ON")
    log_action("setting " + str(lamp_number) + " to ON")
    GPIO.output(lamp_number, GPIO.LOW)
    return

def lamp_off(lamp_number):
    #print("setting", lamp_number, "to OFF")
    log_action("setting " + str(lamp_number) + " to OFF")
    GPIO.output(lamp_number, GPIO.HIGH)
    return

def all_lamps_on_forward():
    #print("setting all lamps ON FORWARD")
    log_action("setting all lamps ON FORWARD")
    for lamp in lamps:
        lamp_on(lamp)
        time.sleep(sleeptime)
    lamps_on = True
    #print("lamps are ON")
    log_action("lamps are ON")
    return lamps_on

def all_lamps_off_reverse():
    #print("setting all lamps OFF REVERSE")
    log_action("setting all lamps OFF REVERSE")
    for lamp in lamps[::-1]:
        lamp_off(lamp)
        time.sleep(sleeptime)
    lamps_on = False
    #print("lamps are OFF")
    log_action("lamps are OFF")
    return lamps_on

def gpio_setup():
    # configure the GPIO pins
    #print("setting pir pin", pirPin,"as INPUT")
    log_action("setting pir pin " + str(pirPin) + " as INPUT")
    GPIO.setup(pirPin, GPIO.IN)
    GPIO.setwarnings(False)
    #print("setting all lamps as OUTPUT")
    log_action("setting all lamps as OUTPUT")
    for lamp in lamps:
        #print("setting", lamp,"to OUTPUT")
        log_action("setting " + str(lamp) + " to OUTPUT")
        GPIO.setup(lamp, GPIO.OUT)

def pir_check_for_motion():
    # check the pir sensor for motion
    if GPIO.input(pirPin) == 1:
        #print("motion detected TRUE")
        log_action("motion detected TRUE")
        return True
    else:
        #print("motion detected FALSE")
        #log_action("motion detected FALSE")
        return False

def check_lamps_condition():
    if lamps_on == True:
        return True
    else:
        return False

def state_off_loop():
    """ run this loop when the lamps are off, which decides 
    whether to keep the lamps off, or turn them on"""
    while True:
        motion = pir_check_for_motion()
        if motion == False:
            # check every 1 second for motion
            #print("motion detected is FALSE and lamps are OFF, taking no action")
            #log_action("motion detected is FALSE and lamps are OFF, taking no action")
            time.sleep(1)
        else:
            #print("motion detected is TRUE and lamps are OFF, turning lamps ON")
            log_action("motion detected is TRUE and lamps are OFF, turning lamps ON")
            all_lamps_on_forward()
            state_on_loop()

def state_on_loop():
    """ run this loop when the lamps are on, which decides 
    whether to keep the lamps on, or turn them off"""
    iterations = 0
    #print("iterations is now", iterations)
    log_action("iterations is now " + str(iterations))
    while True:
        motion = pir_check_for_motion()
        if motion == True:
            #print("motion detected is TRUE and lamps are ON")
            log_action("motion detected is TRUE and lamps are ON")
            #print("resetting iterations to 0 and sleeping", wait,"seconds")
            log_action("resetting iterations to 0 and sleeping " + str(wait) + " seconds")
            iterations = 0
            time.sleep(wait)
        else:
            #print("motion detected is FALSE and lamps are ON")
            log_action("motion detected is FALSE and lamps are ON")
            if iterations == intervals:
                #print("iterations is now", intervals)
                log_action("iterations is now " + str(intervals))
                #print("iterations has reached", intervals)
                log_action("iterations has reached " + str(intervals))
                #print("turning lamps OFF")
                log_action("turning lamps OFF")
                all_lamps_off_reverse()
                state_off_loop()
            else:
                #print("iterations has not yet reached", intervals)
                log_action("iterations has not yet reached " + str(intervals))
                iterations = iterations + 1
                #print("iterations is now", iterations)
                log_action("iterations is now " + str(iterations))
                time.sleep(wait)
           
def main():
    try:
        # initial GPIO setup
        gpio_setup()
        # start by turning the lamps on and off again just because
        lamps_on = all_lamps_on_forward()
        lamps_on = all_lamps_off_reverse()
        state_off_loop()

    except KeyboardInterrupt:
        #print("/n")
        #print("keyboard interrupt detected!")
        GPIO.cleanup()

if __name__ == "__main__":
    main()
