#This is test code in Python to try and move the motors
#Once the Jetson Nano is setup, this will be tested

import RPi.GPIO as GPIO
import time

########################################################################
################################ Setup #################################
########################################################################
#Define the stepper motor pins
dirPin1 = 1
stepPin1 = 1

dirPin2 = 2
stepPin2 = 2

#Define the zeroing pins
zeroPinX = 3
zeroPinY = 3

#Setup the GPIO pins
GPIO.setmode(GPIO.BCM)

GPIO.setup(dirPin1,GPIO.OUT)
GPIO.setup(stepPin1,GPIO.OUT)
GPIO.setup(dirPin2,GPIO.OUT)
GPIO.setup(stepPin2,GPIO.OUT)

GPIO.setup(zeroPinX,GPIO.IN)
GPIO.setup(zeroPinY,GPIO.IN)

########################################################################
############################## Variables ###############################
########################################################################
pulseDelay = 0.5 #delay between pulses in seconds
waitDelay = 2 #delay between movements

numStepsX = 250 #number of steps in X direction (left/right)
numStepsY = 500 #number of steps in the Y direction (up/down)

print("~~Setup complete~~")
print("Pulse at " + str(pulseDelay))
print("Wait at " + str(waitDelay))

########################################################################
############################## Move Motors #############################
########################################################################

#Move the motors up?
GPIO.output(dirPin1,GPIO.LOW)
GPIO.output(dirPin2,GPIO.HIGH)
print("Moving up (1: LOW, 2: HIGH)")

for Y in range(0,numStepsY):
    GPIO.output(stepPin1,GPIO.HIGH)
    GPIO.output(stepPin2,GPIO.HIGH)
    time.sleep(pulseDelay)
    GPIO.output(stepPin1,GPIO.LOW)
    GPIO.output(stepPin2,GPIO.LOW)
    time.sleep(pulseDelay)
time.sleep(waitDelay)

#Move the motor left?
GPIO.output(dirPin1,GPIO.LOW)
GPIO.output(dirPin2,GPIO.LOW)
print("Moving up (1: LOW, 2: LOW)")

for X in range(0,numStepsX):
    GPIO.output(stepPin1,GPIO.HIGH)
    GPIO.output(stepPin2,GPIO.HIGH)
    time.sleep(pulseDelay)
    GPIO.output(stepPin1,GPIO.LOW)
    GPIO.output(stepPin2,GPIO.LOW)
    time.sleep(pulseDelay)
time.sleep(waitDelay)

#Move the motors down?
GPIO.output(dirPin1,GPIO.HIGH)
GPIO.output(dirPin2,GPIO.LOW)
print("Moving down (1: HIGH, 2: LOW)")

for Y in range(0,numStepsY):
    GPIO.output(stepPin1,GPIO.HIGH)
    GPIO.output(stepPin2,GPIO.HIGH)
    time.sleep(pulseDelay)
    GPIO.output(stepPin1,GPIO.LOW)
    GPIO.output(stepPin2,GPIO.LOW)
    time.sleep(pulseDelay)
time.sleep(waitDelay)

#Move the motor right?
GPIO.output(dirPin1,GPIO.HIGH)
GPIO.output(dirPin2,GPIO.HIGH)
print("Moving right (1: HIGH, 2: HIGH)")

for X in range(0,numStepsX):
    GPIO.output(stepPin1,GPIO.HIGH)
    GPIO.output(stepPin2,GPIO.HIGH)
    time.sleep(pulseDelay)
    GPIO.output(stepPin1,GPIO.LOW)
    GPIO.output(stepPin2,GPIO.LOW)
    time.sleep(pulseDelay)
time.sleep(waitDelay)

print("Finished")
