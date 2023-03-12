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
punchSeqRight = punch.punchSeq(50)
punchSeqLeft = punch.punchSeq(50)

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
end_time = perf_counter() + 30.0 #maximum runtime of the program (30s)

#Timers for the two sides
time_right = perf_counter()
time_left = perf_counter()

#Index in the punch sequences
punch_right = 0
punch_left = 0

while end_time - perf_counter() > 0.0 or (punch_left > 50 and punch_right > 50):

    #If the pad has been hit or the timer expires
    if punch_right < 50 and ((perf_counter() - time_right > 1.0) or (boardRight.ReadLoad() > 0.0)):
        thread1 = Thread(target=boardRight.Move_To(punchSeqRight[punch_right].position))
        thread1.start()

        punch_right += 1
        time_right = perf_counter()
    
    #If the pad has been hit or the timer expires
    if punch_left < 50 and ((perf_counter() - time_left > 1.0) or (boardLeft.ReadLoad() > 0.0)):
        thread2 = Thread(target=boardLeft.Move_To(punchSeqLeft[punch_left].position))
        thread2.start()
        
        punch_left += 1
        time_left = perf_counter()
        