import RPi.GPIO as GPIO
from Tkinter import Label, Button, Tk, LEFT
LED = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
def LedEin():
    GPIO.output(LED, True)

def LedAus():
    GPIO.output(LED, False)

root = Tk()
root.title("LED-Schalter")
Label(root, text="Bitte Button klicken, um die LED ein- und auszuschalten").pack()
Button(root, text="Ein", command=LedEin).pack(side=LEFT)
Button(root, text="Aus", command=LedAus).pack(side=LEFT)
root.mainloop()
GPIO.cleanup()