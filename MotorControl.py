'''
This will be the main file for which the R-Pi runs all the motor control code from

The two boards will be operated in parallel with both the gantry and pad control
'''

import RPi.GPIO as GPIO
from time import sleep, perf_counter
from threading import Thread

import punch
import StepperMovement

#~~~~~ Setup the two stepper motors ~~~~~
boardRight = StepperMovement.Stepper([0,1,2,3],[4,5],[6,7])
boardLeft = StepperMovement.Stepper([8,9,10,11],[12,13],[14,7]) #can use the same clock for both load cells

#~~~~~ Get the punch sequences ~~~~~
numPunches = 5
punchSeqRight = punch.punchSeq(numPunches)
punchSeqLeft = punch.punchSeq(numPunches)

#~~~~~ Zero the motors ~~~~~
thread1 = Thread(target=boardRight.Zero_Motors())
thread2 = Thread(target=boardLeft.Zero_Motors())

#Start threads
thread1.start()
thread2.start()

#Join so the threads so we ensure both finish before continuing
thread1.join()
thread2.join()

#~~~~~ Loop through the punches ~~~~~
endTime = perf_counter() + 30.0 #maximum runtime of the program (30s)
punchTimer = 3.0 #maximum time the user has to punch

#Timers for the two sides
timerRight = perf_counter()
timerLeft = perf_counter()

#Index in the punch sequences
punchRight = 0
punchLeft = 0

#Load cell readings
forceRight = 0.0
forceLeft = 0.0

while endTime - perf_counter() > 0.0 and (punchLeft <= numPunches and punchRight <= numPunches):

    #Read the load cells
    force_right = boardRight.ReadLoad()
    force_left = boardLeft.ReadLoad()

    #~~~~~~~~~~ Right Side ~~~~~~~~~~
    #If the pad has been hit or the timer expires
    if punchRight < numPunches and ((perf_counter() - timerRight > punchTimer) or (forceRight > 0.0)):
        #Add the metrics
        punchSeqRight[punchRight].reaction = perf_counter() - timerRight #Reaction time in miliseconds
        punchSeqRight[punchRight].force = forceRight #Force of the punch in Newtons
        punchSeqRight[punchRight].accuracy = True if forceRight > 0.0 else False #Was it hit? True/False

        #Move the pad
        boardRight.Move_To(punchSeqRight[punchRight].position)

        punchRight += 1
        time_right = perf_counter()
    
    #~~~~~~~~~~ Left Side ~~~~~~~~~~
    #If the pad has been hit or the timer expires
    if punchLeft < numPunches and ((perf_counter() - timerLeft > punchTimer) or (forceLeft > 0.0)):
        #Add the metrics
        punchSeqLeft[punchLeft].reaction = perf_counter() - timerLeft #Reaction time in miliseconds
        punchSeqLeft[punchLeft].force = forceLeft #Force of the punch in Newtons
        punchSeqLeft[punchLeft].accuracy = True if forceLeft > 0.0 else False #Was it hit? True/False

        #Move the pad
        boardLeft.Move_To(punchSeqLeft[punchLeft].position)
        
        punchLeft += 1
        time_left = perf_counter()