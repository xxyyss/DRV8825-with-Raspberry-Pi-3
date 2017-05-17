# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import pigpio
import time
import _thread as thread
import os

# Variables
#a
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
j = 0
k = 0
l = 0
o = 0
#p
w = 0
#x
y = 1
#z

# configuration
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
clear()

def stroke():
    print("---------------------------------")
    
def exitsetps():
    stroke()
    print("Closing program")
    stroke()
    stroke()
    if b == 1:
        pi.hardware_PWM(18, 0, 0)
    time.sleep(1)
    if c == 1:
        clear()
    raise SystemExit
    
pi = pigpio.pi()
if not pi.connected:
    clear()
    stroke()
    stroke()
    print("You have to start pigpio first with 'sudo pigpoi'")
    exitsetps()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
pigpio.exceptions = False
pi = pigpio.pi() 

# Information 1
def info1():
    stroke()
    print("Commands:")
    print(" ")
    print("'start' to start the PWM")
    print("'pause' stops the PWM")
    print("'exit' closes the program")
    print("'value' shows settings")
    if (e!= 0):
        print("'dir' changes the direction")
    print("'setup' go back to Setup")
    print("'?' shows help")
    print(" ")
    print("To input a new frequency enter a number. After that you can set the duty cicle")

# Information 2
def info2():
    stroke()
    print("|       |      HELP      |      |")
    stroke()
    print("https://github.com/mauricesifrt/DRV8825-with-Raspberry-Pi-3/")
    print("For help see Github")
    print(" ")
    print("Commands:")
    print("'start' to start the PWM")
    print("'pause' stops the PWM")
    print("'exit' closes the program")
    print("'value' shows settings")
    print("'setup' go back to Setup")
    if (e!= 0):
        print("'dir' changes the direction")
    
# Check Input Message
def checkInpMessage():
    stroke()
    print("Check input")
    stroke()
    
# invalid pin values Message
def PinInfoMessage():
    stroke()
    print("PWM-Pins possible     : only 12")
    print("Input-Pins possible   : 7, 8, 10, 11, 13, 15, 16, 18, 22, 23, 24, 26, 29, 36, 37")
    print("Direction-Pin possible: 7, 8, 10, 11, 13, 15, 16, 18, 22, 23, 24, 26, 29, 36, 37")
    stroke()

def exitnow():
    if k == 'exit':
        exitsetps()
    if w == 'exit':
        exitsetps()
    if l == 'exit':
        exitsetps()
    if j == 'exit':
        exitsetps()
    if d == 'exit':
        exitsetps()

def InValCheck():
    if (k != 0):
        print("Input Pin    :", k)
    else:
        print("Input Pin    :")
    if (e != 0):
        ("Direction-Pin:", e)
    else:
        print("Direction-Pin:")
    
# Start thread for checking fault-output of driver
def overheated():
    while(1):
        if g == 1:
            break
        time.sleep(1)
        try:
            if GPIO.input(k) == 1:
                o = 0
            if GPIO.input(k) == 0 and o == 0:
                stroke()
                print("!!! WARNING: DRIVER MALFUNCTION !!!")
                stroke()
                o = 1
        except:
            time.sleep(0)

def dosetup():
    stroke()
    print("Do setup first")
    stroke()            
            
        
# Here starts the program
c = 1
stroke()
print("https://github.com/mauricesifrt/DRV8825-with-Raspberry-Pi-3")
time.sleep(0.5)
stroke()
print("|       |    SETUP      |       |")
stroke()

# Loop for terminating the program
while(1):
       
    # set PWM-Pin
    print('PWM-Pin: 12')
    stroke()

    # set Input-Pin
    j = input('Choose Input-Pin or enter 0: ')
    exitnow()
    time.sleep(0.1)
    if (j == '?' or j == 'help'):
        dosetup()
        continue
    try:
        k = int(j)
    except:
        checkInpMessage()
        time.sleep(0.2)
        continue
    stroke()
    
    # set Direction-Pin
    d = input('Choose Direction-Pin or enter 0: ')
    exitnow()
    if (d == '?' or d == 'help'):
        dosetup()
        continue
    time.sleep(0.1)
    try:
        e = int(d)
    except:
        checkInpMessage()
        time.sleep(0.2)
        continue
    
    # Cancel with invalid pin values
    if(k != 8 and k != 10 and k != 16 and k != 18 and k != 22 \
       and k != 36 and k != 37 and k != 31 and k != 29 \
       and k != 15 and k != 13 and k != 11 and k != 7 and k != 23 \
       and k != 24 and k != 26 and k != 0):
        PinInfoMessage()
        time.sleep(0.2)
        continue
    
    if(e != 8 and e != 10 and e != 16 and e != 18 and e != 22 \
       and e != 36 and e != 37 and e != 31 and e != 29 \
       and e != 15 and e != 13 and e != 11 and e != 7 and e != 23 \
       and e != 24 and e != 26 and e != 0):
        PinInfoMessage()
        time.sleep(0.2)
        continue
    
    #  Cancel when input and output on same pin
    if (e != 0 and k != 0):
        if(e == k):
            stroke()
            print("Input and output on same pin")
            print("Going to setup again...")
            stroke()
            time.sleep(0.1)
            continue
    
    # Continue Setup
    stroke()
    l = input('Continue? [y/n]: ').lower()
    exitnow()

    # No
    if l == "n":
        stroke()
        print("Going to setup...")
        stroke()
        continue

    # Yes
    if l == "y":
        print("Setup complete")
        # Setup
        if (e != 0):
            GPIO.setup(e, GPIO.OUT)
            GPIO.output(e, 0)
        g = 0
        # start thread:
        time.sleep(1)
        if (k != 0):
            GPIO.setup(k, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
            time.sleep(1)
            thread.start_new_thread(overheated,())
        time.sleep(0.5)
        info1()
        
    # Invalid input
    if l != ("y" or "n"):
        checkInpMessage()
        time.sleep(0.2)
        print("Going to setup")
        stroke()
        continue       
    # End of setup
      
    # Start PWM
    while 1:

        # Input informations
        x = input('>> ').lower()

        # Start
        if x == 'start':
            try:
                pi.hardware_PWM(18, y, z) 
                stroke()
                print("Program started")
                stroke()
                b = 1
                continue
            except:
                dosetup()
                continue

        # Exit
        if x == 'exit':
            exitsetps()

        # Pause
        if x == 'pause':
            if b == 1:
                pi.hardware_PWM(18, 0, 0)
                stroke()
                print("Program paused")
                stroke()
                b = 0
                continue
            if b == 0:
                stroke()
                print("Nothing to pause")
                stroke()
                continue
        # Help
        if (x == '?'or x == 'help'):
            info2()
            continue

        # Direction
        if e != 0:
            if x == 'dir':
                if f == 0:
                    GPIO.output(e, 1)
                if f == 1:
                    GPIO.output(e, 0)
                stroke()
                print("Direction changed")
                stroke()    
                continue
            
        # Value
        if x == 'value':
            try:
                stroke()
                print("Frequency    :", wert)
                print("Duty cycle   :", a)
                print("PWM-Pin      :", 12)
                InValCheck()
                stroke()
                continue
            except:
                print("Frequency    :")
                print("Duty cycle   :" )
                print("PWM-Pin      :", 12)
                InValCheck()
                stroke()
                continue

        # Go to Setup
        if x == 'setup':
            stroke()
            print("Going to setup")
            pi.hardware_PWM(18, 0, 0)
            g = 1
            stroke()
            break

        try:
            y = int(x)
        except:
            checkInpMessage()
            continue

        # Freq 0
        if y == 0:
            stroke()
            print("Frequency can not be 0")
            stroke()
            continue
        
        # Input DC
        stroke()
        print("Duty Cycle:")
        w = input('> ')
        exitnow()
        if (w == '?' or w == 'help'):
            stroke()
            print("This is the Duty cycle.")
            print("Here you enter a value from 1 to 100.")
            print("Attention, frequency was reset, now give your frequency again and then your duty cycle")
            stroke()
            continue
        time.sleep(0.5)
        try:
            time.sleep(0.1)
            a = int(w)
            z = a * 10000
            wert = x
        except:
            checkInpMessage()
            continue

        # DC 0
        if z == 0:
            stroke()
            print("Duty cycle can not be 0")
            stroke()
            continue

        # if Duty Cycle higher than 100 print warning
        if z > 1000000:
            stroke()
            print("Duty cycle can not be over 100%")
            stroke()
            continue

        # print for command 'value'
        stroke()
        print("Frequency :", wert)
        print("Duty cycle:", a)
        stroke()
