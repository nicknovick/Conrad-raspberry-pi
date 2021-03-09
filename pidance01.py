# -*- coding: utf-8 -*-
import time
import random
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
rzahl = 10
farbe = []
for i in range(rzahl):
    farbe.append(random.randrange(4))

LED = [17, 22, 9, 5]
for i in LED:
    GPIO.setup(i, GPIO.OUT, initial=False)

TAST = [27, 10, 11, 6]
for i in TAST:
    GPIO.setup(i, GPIO.IN)

def LedEin(n, z):
    GPIO.output(LED[n], True)
    time.sleep(z)
    GPIO.output(LED[n], False)
    time.sleep(0.15)

def Druecken():
    while True:
        for i in range(len(TAST)):
            if (GPIO.input(TAST[i])):
                return i

ok = True

for runde in range(1, rzahl+1):
    print "Runde ", runde
    for i in range(runde):
        LedEin(farbe[i], 1)
    for i in range(runde):
        taste = Druecken()
        LedEin(taste, 0.2)
        if (taste != farbe[i]):
            print "Verloren!"
            print "Du hast es bis Runde ", runde-1, " geschafft"
            for j in LED:
                GPIO.output(j, True)
            for j in LED:
                time.sleep(0.5)
                GPIO.output(j, False)
            ok = False
            break
    if (ok == False):
        break
    time.sleep(0.5)
if (ok == True):
    print "Super gemacht!"
    for i in range(5):
        for j in LED:
            GPIO.output(j, True)
        time.sleep(0.05)
        for j in LED:
            GPIO.output(j, False)
        time.sleep(0.05)
GPIO.cleanup()