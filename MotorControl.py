'''
This will be the main file for which the R-Pi runs all the motor control code from

The two boards will be operated in parallel with both the gantry and pad control
'''

import RPi.GPIO as GPIO
from time import sleep, perf_counter
from multiprocessing import Process, Queue

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
punchSeqLeft = punch.Punch_Sequence(numPunches,["q1","q4"])
punchSeqRight = punch.Punch_Sequence(numPunches,["q2","q4"])

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

#Print the results now that the threads have finished running

print("\n\n################## LEFT SIDE ##################")
for i in range(resultsL.qsize()):
    p = resultsL.get()

    print(p)
    print("~~~~~~~~~~~~~~~~")

print("\n\n################## RIGHT SIDE ##################")
for i in range(resultsR.qsize()):
    p = resultsR.get()

    print(p)
    print("~~~~~~~~~~~~~~~~")

del boardLeft
del boardRight
GPIO.cleanup()