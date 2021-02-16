# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)

LED=[22,27,17,10]

for i in LED:
    GPIO.setup(i, GPIO.OUT, initial=0)

z=len(LED)
w=5
t=0.2

print("Lichteffekte zur Auswahl")
print("1 - Lauflicht zyklisch")
print("2 - Lauflicht hin und zurück")
print("3 - Auf und asteigend")
print("4 - Alle blinken gleichzeitig")
print("5 - Alle blinken zufällig")
print("Strg+C beendet das Program")

try:
    while True:
        e=raw_input("Bitte Muster auswählen: ")
        if e == "1":
            for i in range(w):
                for j in range(z):
                    GPIO.output(LED[j], True)
                    time.sleep(t)
                    GPIO.output(LED[j], False)
        elif e == "2":
            for i in range(w):
                for j in range(z):
                    GPIO.output(LED[j], True)
                    time.sleep(t)
                    GPIO.output(LED[j], False)
                for j in range(z-1, -1, -1):
                    GPIO.output(LED[j], True)
                    time.sleep(t)
                    GPIO.output(LED[j], False)
        elif e == "3":
            for i in range(w):
                for j in range(z):
                    GPIO.output(LED[j], True)
                    time.sleep(t)
                time.sleep(2*t)
                for j in range(z-1, -1, -1):
                    GPIO.output(LED[j], False)
                    time.sleep(t)
                time.sleep(2*t)
        elif e == "4":
            for i in range(w):
                for j in range(z):
                    GPIO.output(LED[j], True)
                time.sleep(2*t)
                for j in range(z):
                    GPIO.output(LED[j], False)
                time.sleep(t)
        elif e == "5":
            for i in range(w*z):
                j = random.randint(0, z-1)
                GPIO.output(LED[j], True)
                time.sleep(t)
                GPIO.output(LED[j], False)
        else:
            print("Ungültige Eingabe. Wählen Sie bitte eine Nummer 1 bis 5")

except KeyboardInterrupt:
    GPIO.cleanup()