# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import _thread as thread
KILL = 0
while(1):
    if KILL == 1:
        break
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    print("---------------------------------")
    print("SETUP:")
    print("---------------------------------")
    print("Output-Pin (Standart: 12):")
    h = input()
    i = int(h)
    print("---------------------------------")
    print("Input-Pin (Standart: 11):")
    j = input()
    k = int(j)
    GPIO.setup(i, GPIO.OUT)
    GPIO.setup(k, GPIO.IN)
    print("---------------------------------")
    print("Output Pin:", i)
    print("Input Pin:", k)
    print("---------------------------------")
    print("Möchtest du fortführen? [N/J]")
    l = input()

    if l == "N":
        print("---------------------------------")
        print("Das Prgramm wurde abgebrochen")
        print("Starte das Program neu!")
        print("---------------------------------")
        break
    if l == "J":
        print("Deine Einstellung wurde übernommen")
        print("---------------------------------")
        print("Programm wird gestartet")
        time.sleep(3)
        print("---------------------------------")

    def show():
        while(1):
            time.sleep(1.5)
            print("Test")

    while 1:
        print("Frequenz eingeben (danach Duty Cycle),")
        print("'Ende' zum Beenden oder 'Pause' zum Pausieren")
        # thread.start_new_thread(show,())
        x = input()
            
        if x == 'Ende':
            GPIO.cleanup()
            print("---------------------------------")
            print("Das Programm wurde Beendet")
            print("---------------------------------")
            print("---------------------------------")
            KILL = 1
            break
        if x == 'Pause':
            try:
                p.stop()
                print("---------------------------------")
                print("Das Programm wurde Pausiert")
                print("---------------------------------")
                continue
            except:
                print("---------------------------------")
                print("Du kannst nichts Pausieren wenn nichts läuft :o")
                print("---------------------------------")
                continue
        
        try:
            y = int(x)
            print("---------------------------------")
            print("Duty Cycle:")
            w = input()
            z = int(w)
            
        except:
            print("---------------------------------")
            print("Bitte Eingabe prüfen!")
            print("---------------------------------")
            
            continue
            
        if z == 0 or y == 0:
            if z == 0 and y == 0:
                GPIO.cleanup()
                
                print("    Das Programm wurde Beendet   ")
                print("---------------------------------")
                print("-----Code by Maurice Seifert-----")
                print("---------------------------------")
                KILL = 1
                break
            print("---------------------------------")
            print("Die Werte 0 im Duty Cycle und/oder in der Frequenz sind NICHT möglich!")
            print("---------------------------------")
            continue
        if z > 101:
            print("---------------------------------")
            print("Der Wert beim Duty Cycle darf nicht höher als 100 sein")
            print("---------------------------------")
            continue

        print("---------------------------------")
        print("Frequenz auf", x,"& Duty Cycle auf", z,"gestellt")
        print("---------------------------------")
        p = GPIO.PWM(12, y)
        p.start(z)

