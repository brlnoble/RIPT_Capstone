import MotorMovementTest as move
import punch
import random
import time

random.seed(time())

sequence = punch.punchSeq(200)

for i in sequence:
    if i.quadrant == 'q1':
        i.position = [random.randint(0,12), random.randint(22.5,45)]
    elif i.quadrant == 'q4':
        i.position = [random.randint(0,12), random.randint(0,22.5)]

for i in sequence:
    move.Move_To(i.position[0], i.position[1])
    


