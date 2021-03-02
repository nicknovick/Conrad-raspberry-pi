# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import os

# Freie Speicherplatz in Gb
g1 = 5      # rot
g2 = 10     # rot-gelb
g3 = 15     # gelb
g4 = 20     # gelb-grün
# oberhalb = grün

GPIO.setmode(GPIO.BCM)
LED = [22, 27, 17]

for i in range(3):
    GPIO.setup(LED[i], GPIO.OUT, initial=False)

print("Strg+C beendet das Programm")

try:
    while True:
        s = os.statvfs('/')
        f = s.f_bsize * s.f_bavail / 1024/1024/1024

        if f < g1:
            x = "100"
        elif f < g2:
            x = "110"
        elif f < g3:
            x = "010"
        elif f < g4:
            x = "011"
        else:
            x = "001"

        for i in range(3):
            GPIO.output(LED[i], int(x[i]))
        time.sleep(1.0)

except KeyboardInterrupt:
    GPIO.cleanup()
