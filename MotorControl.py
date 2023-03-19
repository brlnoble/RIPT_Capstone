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

#~~~~~ Setup the left stepper motors ~~~~~
leftPins = [
    19, #dir1
    6, #dir2
    13, #step1
    5 #step2
]

leftZero = [
    27, #X zero
    22 #Y zero
]

boardLeft = StepperMovement.Stepper(leftPins,leftZero,[0,0]) #can use the same clock for both load cells

#~~~~~ Setup the right stepper motors ~~~~~
rightPins = [
    12, #dir1
    20, #dir2
    16, #step1
    21 #step2
]

rightZero = [
    24, #X zero
    23 #Y zero
]

boardRight = StepperMovement.Stepper(rightPins,rightZero,[0,0]) #can use the same clock for both load cells


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
results = Queue()

#Create the movement threads
thread1 = Process(target=boardLeft.Movements, args=(punchSeqLeft,endTime,results))
thread2 = Process(target=boardRight.Movements, args=(punchSeqRight,endTime,results))
threads = [thread1, thread2]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

#~~~~~ Save the results ~~~~~

#Format the duration string
minutes = str(endTime//60)
minutes = "0" + minutes if len(minutes) < 2 else minutes #zero pad minutes
seconds = str(endTime-endTime//60)
seconds = "0" + seconds if len(seconds) < 2 else seconds #zero pad seconds
duration = minutes + ":" + seconds

#Compile dictionary
writeData = [{"duration": duration}]
for i in range(results.qsize()):
    p = results.get()
    writeData.append(p.Return_Data())

writeData = json.dumps(writeData) #Convert to json

#Write to JSON
with open("results.json","w") as f:
    f.write(writeData)

del boardLeft
del boardRight
GPIO.cleanup()