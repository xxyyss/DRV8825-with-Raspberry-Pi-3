# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
    


while 1:
    print ("Frequenz eingeben (dannach Duty Cycle), 'Ende' zum Beenden oder 'Stop' zum Pausieren")
    x = input()
	
    if x == 'Ende':
        GPIO.cleanup()
        print("Das Programm wurde Beendet")
        print("---------------------------------")
        print("---------------------------------")
        break
    if x == 'Stop':
        p.stop()
        print("---------------------------------")
        continue
    
    try:
        y = int(x)
        print("---------------------------------")
        print("Duty Cycle:")
        x = input()
        z = int(x)
        
    except:
        print("Bitte Eingabe prüfen!")
        print("---------------------------------")
        continue
        
    print("Frequenz auf",x, "& Duty Cycle auf", z,"gestellt")
    print("---------------------------------")
    p = GPIO.PWM(12, y)
    p.start(z)
