# Import
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import _thread as thread
# Variable KILL um sicheres Beenden durchführen zu können
KILL = 0
o = 0
k = 0

# Konfiguration
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Noch in Testphase    
def overheated():
    GPIO.setup(k, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    while(1):
        # Sicheres Beenden durch veränderung der KILL-Variablen
        if KILL == 1:
            return
        try:
            if GPIO.input(k) == 0:
                o = 0
            if GPIO.input(k) == 1 and o == 0:
                print("---------------------------------")
                print("ACHTUNG. MOTORTREIBER ÜBERHITZT")
                print("---------------------------------")
                o = 1
        except:            
            time.sleep(0)

#Willkommensnachricht
print("Starte pwm.py ...")
time.sleep(2)
print("---------------------------------")
print("|          Willkommen           |")
print("---------------------------------")
time.sleep(0.5)
print("Du musst zuerst das Setup")
print("(bei jedem Start des Programms)")
print("durchführen. Beim Setup musst du")
print("den Pin für den PWM-Kanal")
print("und den Input-Pin angeben.")
print("Danach startet das eigentliche")
print("Programm, das ein PWM-Signal,")
print("bei dem Raspberry, ausgeben kann.")
print("Dieses Programm ist dafür")
print("konzipiert einen Schrittmotor mit")
print("dem DRV8825-Motortreiber")
print("ansteuern.")
print("Die Inputfunktion ist noch")
print("in Arbeit, soll aber")
print("voraussichtlich durch ein GPIO-")
print("Inputsignal auf die Überhitzung")
print("des Motortreibes hinweisen.")
time.sleep(1.5)
print("---------------------------------")
print("Info: Du kannst bei jeder Eingabe,")
print("eine Null eingeben. Nach Eingabe")
print("der Nullen nach zwei Eingaben,")
print("beendet sich das Progamm")
print("---------------------------------")
time.sleep(0.5)
print("Starte SETUP ...")
time.sleep(1.5)
# Erster Start vom Setup
print("---------------------------------")
print("|       |    SETUP      |       |")
print("---------------------------------")

# Schleife wegen beenden des Programmes
while(1):
    # Hier könnte sich das Setup wiederholen
    # Sicheres Beenden durch veränderung der KILL-Variablen
    if KILL == 1:
        break
    
    # Outout-Pin umstellen
    try:
        print("PWM-Kanal (Standard: 12):")
        h = input()
        i = int(h)
    except:
        print("---------------------------------")
        print("Bitte Eingabe prüfen!")
        print("---------------------------------")
        time.sleep(1.5)
        continue
    print("---------------------------------")

    # Input-Pin umstellen
    try:
        print("Input-Pin (Standard: 11):")
        j = input()
        k = int(j)
    except:
        print("---------------------------------")
        print("Bitte Eingabe prüfen!")
        print("---------------------------------")
        time.sleep(1.5)
        continue

    # Sicheres Beenden durch eingeben von zwei Nullen
    if(i == 0 and k == 0):
        print("---------------------------------")
        print("Das Programm wurde beendet")
        print("---------------------------------")
        print("---------------------------------")
        break

    # Abbrechen bei 2 Gleichen Werten
    if(i == k):
        print("---------------------------------")
        print("Input und PWM-Pin können NICHT")
        print("auf den gleichen Pins sein!")
        print("---------------------------------")
        time.sleep(1.5)
        continue
    
    # Abbrechen bei falschen Pin-Werten
    if(i != 12 and i != 32 and i != 33 and i != 35 and i != 0 \
       and i != 23 and i != 24 and i != 1 and i!= 26):
        print("---------------------------------")
        print("Im PWM-Pin gehen nur die Pins")
        print("12, 32, 33 & 35. Im Input gehen ")
        print("nur die Pins mit der Nummer 8,")
        print("10, 16, 18, 22, 36, 37, 3, 29, 15,")
        print("13, 11 & 7. Die Pins 23, 24,")
        print("26 & 1 sind für In oder PWM-Pin")
        print("möglich")
        print("---------------------------------")
        time.sleep(1.5)
        continue
    
    if(k != 8 and k != 10 and k != 16 and k != 18 and k != 22 \
       and k != 36 and k != 37 and k != 31 and k != 29 \
       and k != 15 and k != 13 and k != 11 and k != 7 and k != 23 \
       and k != 24 and k != 26 and k != 1 and k != 0):
        print("---------------------------------")
        print("Im PWM-Pin gehen nur die Pins")
        print("12, 32, 33 & 35. Im Input gehen ")
        print("nur die Pins mit der Nummer 8,")
        print("10, 16, 18, 22, 36, 37, 3, 29, 15,")
        print("13, 11 & 7. Die Pins 23, 24,")
        print("26 & 1 sind für In oder PWM-Pin")
        print("möglich")
        print("---------------------------------")
        time.sleep(1.5)
        continue
    
    # Abfragen der Setupeinstellung
    print("---------------------------------")
    print("Output Pin:", i)
    print("Input Pin:", k)
    print("---------------------------------")              
    print("Möchtest du fortführen? [N/J]")
    l = input()

    #NEIN
    if l == "N":
        print("---------------------------------")
        print("Setup wird neu gestartet")
        print("---------------------------------")
        continue

    #JA
    if l == "J":
        print("Die Einstellung wurde übernommen")
        print("---------------------------------")
        print("Programm wird gestartet")
        time.sleep(3)
        print("---------------------------------")
        
    #Andere Eingaben
    if l != ("J" or "N"):
        print("---------------------------------")
        print("Die Eingabe '",l,"' ungültig")
        print("Bitte Eingabe prüfen!")
        print("---------------------------------")
        time.sleep(1.5)
        print("Setup wird neu gestartet")
        print("---------------------------------")
        continue
            
    #Setup Ende

    #Start des eigentlichen Programmes
    while 1:

        #Sicheres Beenden durch veränderung der KILL-Variablen
        if KILL == 1:
            break
    
        #Setup durchführen
        GPIO.setup(i, GPIO.OUT)
        GPIO.setup(k, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

        #Abfrage
        print("Diese Befehle kannst du")
        print("hier anwenden:")
        print(" ")
        print("'Start' startet die Anwendung")
        print("'Pause' pausiert die Anwendung")
        print("'Ende' beendet die Anwendung")
        print(" ")
        print("Um die Frequenz einzugeben, gebe")
        print("einfach eine beliebeige Zahl ein")
        print("Dannach erscheint auch die")
        print("Möglichkeit den Duty Cycle")
        print("einzugeben. Probiere es aus:")
        
        #Noch im Test:
        thread.start_new_thread(overheated,())
        

        #Eingabe
        x = input()

        #Auswertung
        if x == 'Start':
            try:
                p = GPIO.PWM(i, y)
                p.start(z)
                time.sleep(1.5)
                print("---------------------------------")
                print("Das Programm wurde gestartet")
                print("---------------------------------")
                continue
            except:
                print("---------------------------------")
                print("Gib zuerst die Variablen ein!")
                print("---------------------------------")
                time.sleep(1.5)
                continue

        #Ende
        if x == 'Ende':
            GPIO.cleanup()
            print("---------------------------------")
            print("Das Programm wurde beendet")
            print("---------------------------------")
            print("---------------------------------")
            KILL = 1
            break

        #Pause
        if x == 'Pause':
            try:
                p.stop()
                print("---------------------------------")
                print("Das Programm wurde pausiert")
                print("---------------------------------")
                time.sleep(1.5)
                continue
            except:
                print("---------------------------------")
                print("Du kannst nichts pausieren,")
                print("wenn nichts läuft :o")
                print("---------------------------------")
                time.sleep(1.5)
                continue

        #Eingabe DC
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
            time.sleep(1.5)
            continue

        #Prüfen auf Eingabe von Null
        if z == 0 or y == 0:
            
            # Beenden durch eingabe von zwei Nullen
            if z == 0 and y == 0:
                GPIO.cleanup()
                print("    Das Programm wurde beendet   ")
                print("---------------------------------")
                print("-----Code by Maurice Seifert-----")
                print("---------------------------------")
                KILL = 1
                time.sleep(0.2)
                break

            #Fehlermeldung bei Wert Null
            print("---------------------------------")
            print("Die Werte 0 im Duty Cycle und/oder")
            print("in der Frequenz sind NICHT möglich!")
            print("---------------------------------")
            time.sleep(1.5)
            continue

        #Prüfen auf Eingabe höher als 100
        if z > 100:
            print("---------------------------------")
            print("Der Wert beim Duty Cycle darf")
            print("nicht höher als 100 sein")
            print("---------------------------------")
            time.sleep(1.5)
            continue

        #Ausgabe
        print("---------------------------------")
        print("Frequenz auf", x,"&")
        print("Duty Cycle auf", z,"gestellt")
        print("---------------------------------")
        time.sleep(1.5)
