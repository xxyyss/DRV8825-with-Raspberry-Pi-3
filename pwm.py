# Import
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import _thread as thread
# Variable KILL um sicheres Beenden durchführen zu können
KILL = 0

# Konfiguration
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

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
        print("PWM-Kanal (Standart: 12):")
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
        print("Input-Pin (Standart: 11):")
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
        print("Das Programm wurde Beendet")
        print("---------------------------------")
        print("---------------------------------")
        break

    # Abbrechen bei 2 Gleichen Werten
    if(i == k):
        print("---------------------------------")
        print("Input und PWM-Kanal können NICHT")
        print("auf den gleichen Pins sein!")
        print("---------------------------------")
        time.sleep(1.5)
        continue
    
    # Abbrechen bei falschen Pin-Werten
    if(i != 12 and i != 32 and i != 33 and i != 35 and i != 0 \
       and i != 23 and i != 24 and i != 1 and i!= 26):
        print("---------------------------------")
        print("Im PWM-Kanal gehen nur die Pins")
        print("12, 32, 33 & 35. Im Input gehen ")
        print("nur die Pins mit der der Nummer 8,")
        print("10, 16, 18, 22, 36, 37, 3, 29, 15,")
        print("13, 11 & 7. Die Pins 23, 24,")
        print("26 & 1 sind für In oder PWM-Kanal")
        print("möglich")
        print("---------------------------------")
        time.sleep(1.5)
        continue
    
    if(k != 8 and k != 10 and k != 16 and k != 18 and k != 22 \
       and k != 36 and k != 37 and k != 31 and k != 29 \
       and k != 15 and k != 13 and k != 11 and k != 7 and k != 23 \
       and k != 24 and k != 26 and k != 1 and k != 0):
        print("---------------------------------")
        print("Im PWM-Kanal gehen nur die Pins")
        print("12, 32, 33 & 35. Im Input gehen ")
        print("nur die Pins mit der der Nummer 8,")
        print("10, 16, 18, 22, 36, 37, 3, 29, 15,")
        print("13, 11 & 7. Die Pins 23, 24,")
        print("26 & 1 sind für In oder PWM-Kanal")
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
        print("Das Prgramm wurde abgebrochen")
        print("Starte das Program neu!")
        print("---------------------------------")
        break

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
        print("Bitte Eingabe prüfen!")
        print("---------------------------------")
        time.sleep(1.5)
        print("Setup wird neu gestartet")
        continue
    


    # Noch in Testphase    
    def show():
        while(1):
            time.sleep(1.5)
            print("Test")
            
    #Setup Ende

    #Start des eigentlichen Programmes
    while 1:
        # Setup durchführen
        GPIO.setup(i, GPIO.OUT)
        GPIO.setup(k, GPIO.IN)

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
        # thread.start_new_thread(show,())

        #Eingabe
        x = input()

        # Auswertung
        if x == 'Start':
            try:
                p = GPIO.PWM(i, y)
                p.start(z)
                time.sleep(1.5)
                print("---------------------------------")
                print("Das Programm wurde gestartet")
                print("---------------------------------")
                time.sleep(1)
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
            print("Das Programm wurde Beendet")
            print("---------------------------------")
            print("---------------------------------")
            KILL = 1
            break

        #Pause
        if x == 'Pause':
            try:
                p.stop()
                print("---------------------------------")
                print("Das Programm wurde Pausiert")
                print("---------------------------------")
                time.sleep(1.5)
                continue
            except:
                print("---------------------------------")
                print("Du kannst nichts Pausieren,")
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

        # Prüfen auf Eingabe von Null
        if z == 0 or y == 0:
            
            # Beenden durch eingabe von zwei Nullen
            if z == 0 and y == 0:
                GPIO.cleanup()
                print("    Das Programm wurde Beendet   ")
                print("---------------------------------")
                print("-----Code by Maurice Seifert-----")
                print("---------------------------------")
                KILL = 1
                break

            # Fehlermeldung bei Wert Null
            print("---------------------------------")
            print("Die Werte 0 im Duty Cycle und/oder")
            print("in der Frequenz sind NICHT möglich!")
            print("---------------------------------")
            time.sleep(1.5)
            continue

        # Prüfen auf Eingabe höher als 100
        if z > 101:
            print("---------------------------------")
            print("Der Wert beim Duty Cycle darf")
            print("nicht höher als 100 sein")
            print("---------------------------------")
            time.sleep(1.5)
            continue

        # Ausgabe
        print("---------------------------------")
        print("Frequenz auf", x,"&")
        print("Duty Cycle auf", z,"gestellt")
        print("---------------------------------")
        time.sleep(1.5)
