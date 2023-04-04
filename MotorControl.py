'''
This will be the main file for which the R-Pi runs all the motor control code from

The two boards will be operated in parallel with both the gantry and pad control
'''

import RPi.GPIO as GPIO
from time import sleep
from multiprocessing import Process, Queue
import json

import punch
import StepperMovement
import ServoMovement

#~~~~~ Setup the left stepper motors ~~~~~
leftPins = [
    3, #dir1
    17, #dir2
    2, #step1
    4 #step2
]

leftZero = [
    14, #X zero
    15 #Y zero
]

leftServoPins = [
    6, #top
    13 #bot
]

leftServoAngs = [
     [0,0], #jab
     [90,0], #hook
     [45,90], #uppercut
]

boardLeft = StepperMovement.Stepper(leftPins,leftZero,[0,0],leftServoPins,leftServoAngs) #can use the same clock for both load cells

#~~~~~ Setup the right stepper motors ~~~~~
rightPins = [
    16, #dir1
    21, #dir2
    12, #step1
    20 #step2
]

rightZero = [
    19, #X zero
    26 #Y zero
]

rightServoPins = [
     23, #top
     24 #bot
]

rightServoAngs = [
     [75,90], #jab
     [160,90], #uppercut
     [120,0] #hook
]

boardRight = StepperMovement.Stepper(rightPins,rightZero,[0,0],rightServoPins,rightServoAngs) #can use the same clock for both load cells


#~~~~~ Get the punch sequences ~~~~~
numPunches = 5
punchSeqLeft = punch.Punch_Sequence(numPunches,["q1","q2"])
punchSeqRight = punch.Punch_Sequence(numPunches,["q3","q4"])

#~~~~~ Zero the motors ~~~~~
print("~~~~~ Zeroing motors ~~~~~")
thread1 = Process(target=boardRight.Zero_Motors, args=())
thread2 = Process(target=boardLeft.Zero_Motors, args=())
threads = [thread1, thread2]

#Start threads
for thread in threads:
    thread.start()

#Join so the threads so we ensure both finish before continuing
for thread in threads:
    thread.join()

#~~~~~ Loop through the punches ~~~~~
endTime = 30.0 #maximum runtime of the program (30s)

sleep(3)
print("~~~~~ Starting movements ~~~~~")

#Using queues to return the punch objects to the main program
resultsL = Queue()
resultsR = Queue()

#Create the movement threads
thread1 = Process(target=boardLeft.Movements, args=(punchSeqLeft,endTime,resultsL))
thread2 = Process(target=boardRight.Movements, args=(punchSeqRight,endTime,resultsR))
threads = [thread1, thread2]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

#~~~~~ Save the results ~~~~~

#Left side
writeData = []
for i in range(resultsL.qsize()):
    p = resultsL.get()
    writeData.append(p.Return_Data())

writeData = json.dumps(writeData) #Convert to json

with open("resultsL.json","w") as f:
    f.write(writeData)

#Right side
writeData = []
for i in range(resultsR.qsize()):
    p = resultsR.get()
    writeData.append(p.Return_Data())

writeData = json.dumps(writeData) #Convert to json

with open("resultsR.json","w") as f:
    f.write(writeData)

del boardLeft
del boardRight
GPIO.cleanup()
