"""
Blah
"""
import time
import json
import mh_z19
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
RED = 18
YELLOW = 1
GREEN = 24
CO2_CRITICAL = 1000
CO2_WARNING = 700
CO2_LOW = 450
GPIO.setup(RED, GPIO.OUT, initial=False)
GPIO.setup(YELLOW, GPIO.OUT, initial=False)
GPIO.setup(GREEN, GPIO.OUT, initial=False)
try:
    while True:
        X = mh_z19.read()
        VALUE = X["co2"]
        print(VALUE)
        if VALUE > CO2_CRITICAL:
            GPIO.output(GREEN, False)
            GPIO.output(YELLOW, False)
            GPIO.output(RED, True)
        elif VALUE > CO2_WARNING:
            GPIO.output(GREEN, False)
            GPIO.output(YELLOW, True)
            GPIO.output(RED, False)
        elif VALUE < CO2_LOW:
            GPIO.output(GREEN, True)
            GPIO.output(YELLOW, False)
            GPIO.output(RED, False)
            time.sleep(1)
            GPIO.output(GREEN, False)
        else:
            GPIO.output(GREEN, True)
            GPIO.output(YELLOW, False)
            GPIO.output(RED, False)
        time.sleep(1)
except Exception as error:
    print("Error '{0}' occured. Arguments {1}.".format(error.message, error.args))
except KeyboardInterrupt:
    GPIO.cleanup()
