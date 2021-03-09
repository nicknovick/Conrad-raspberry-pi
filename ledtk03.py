import RPi.GPIO as GPIO
import time
from Tkinter import Label, Button, Tk, LEFT, IntVar, Radiobutton, Scale, HORIZONTAL
GPIO.setmode(GPIO.BCM)

LED=[10,22,27,17]

for i in LED:
    GPIO.setup(i, GPIO.OUT, initial=0)
w = 5

muster = [("Lauflicht nach links", 1), ("Blinken", 2), ("Lauflicht nach rechts", 3)]
root = Tk()
root.title("LED")
v = IntVar()
v.set(1)
g = IntVar()
g.set(5)

def LedEin():
    e = v.get()
    t = 1.0/g.get()
    if e == 1:
        for i in range(w):
            for j in LED:
                GPIO.output(j, True)
                time.sleep(t)
                GPIO.output(j, False)
    elif e == 2:
        for i in range(w):
            for j in LED:
                GPIO.output(j, True)
            time.sleep(t)
            for j in LED:
                GPIO.output(j, False)
            time.sleep(t)
    else:
        for i in range(w):
            for j in range(4):
                GPIO.output(LED[3-j], True)
                time.sleep(t)
                GPIO.output(LED[3-j], False)
Label(root, text="Bitte Button klicken, um das Lauflicht zu starten").pack()
for txt, m in muster:
    Radiobutton(root, text = txt, variable = v, value = m).pack()

Label(root, text="Geschwindigkeit").pack()

Scale(root, orient=HORIZONTAL, from_ = 1, to = 10, variable = g).pack()

Button(root, text="Start", command=LedEin).pack(side=LEFT)

root.mainloop()
GPIO.cleanup()