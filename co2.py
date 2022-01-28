"""
Blah
"""
import subprocess
import time
import json
import mh_z19
import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BCM)
RED = 18
YELLOW = 1
GREEN = 24
CO2_CRITICAL = 1000
CO2_WARNING = 700
CO2_LOW = 430
GPIO.setup(RED, GPIO.OUT, initial=False)
GPIO.setup(YELLOW, GPIO.OUT, initial=False)
GPIO.setup(GREEN, GPIO.OUT, initial=False)

subprocess.run("echo none > /sys/class/leds/led0/trigger", shell=True)
subprocess.run("echo none > /sys/class/leds/led1/trigger", shell=True)
os.system("sudo sh -c 'echo 0 > /sys/class/leds/led0/brightness'") # red

def set_green():
    subprocess.run("sudo sh -c 'echo 1 > /sys/class/leds/led0/brightness'", shell=True) #green on
    subprocess.run("sudo sh -c 'echo 0 > /sys/class/leds/led1/brightness'", shell=True) #red off
    GPIO.output(GREEN, True)
    GPIO.output(YELLOW, False)
    GPIO.output(RED, False)

def set_yellow():
    subprocess.run("sudo sh -c 'echo 1 > /sys/class/leds/led0/brightness'", shell=True) #green on
    subprocess.run("sudo sh -c 'echo 1 > /sys/class/leds/led1/brightness'", shell=True) #red on
    GPIO.output(GREEN, False)
    GPIO.output(YELLOW, True)
    GPIO.output(RED, False)

def set_red():
    subprocess.run("sudo sh -c 'echo 0 > /sys/class/leds/led0/brightness'", shell=True) #green off
    subprocess.run("sudo sh -c 'echo 1 > /sys/class/leds/led1/brightness'", shell=True) #red on
    GPIO.output(GREEN, False)
    GPIO.output(YELLOW, False)
    GPIO.output(RED, True)

def set_none():
    subprocess.run("sudo sh -c 'echo 0 > /sys/class/leds/led0/brightness'", shell=True) #green off
    subprocess.run("sudo sh -c 'echo 0 > /sys/class/leds/led1/brightness'", shell=True) #red off
    GPIO.output(GREEN, False)
    GPIO.output(YELLOW, False)
    GPIO.output(RED, False)

try:
    while True:
        X = mh_z19.read()
        VALUE = X["co2"]
        print(VALUE)
        if VALUE > CO2_CRITICAL:
            set_red()
        elif VALUE > CO2_WARNING:
            set_yellow()
        elif VALUE < CO2_LOW:
            set_green()
            time.sleep(1)
            set_none()
        else:
            set_green()
        time.sleep(1)
except Exception as error:
    print("Error '{0}' occured. Arguments {1}.".format(error.message, error.args))
    subprocess.run("echo mmc0 > /sys/class/leds/led0/trigger", shell=True)
    subprocess.run("echo input > /sys/class/leds/led1/trigger", shell=True)
    GPIO.cleanup()
except KeyboardInterrupt:
    GPIO.cleanup()
    subprocess.run("echo mmc0 > /sys/class/leds/led0/trigger", shell=True)
    subprocess.run("echo input > /sys/class/leds/led1/trigger", shell=True)
