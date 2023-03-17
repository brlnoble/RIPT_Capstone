import random
from time import time

class punch:
    def __init__(self, quadrant, typ):
        self.quadrant = quadrant
        self.postion = []
        self.typ = typ
        self.delay = None
        self.form = None
        self.force = None
    
    def punchToArray(self):
        return [self.quadrant, self.typ]

prob = {
    'q1' : 0.5,
    'q2' : 0.5,
    'q3' : 0.5,
    'q4' : 0.5,
    'straight': 0.33,
    'hook' : 0.33,
    'uppercut': 0.33
}

<<<<<<< Updated upstream
def punchSeq(prob, numPunch):
    sequence = []
    printable = []
    for i in range(numPunch):
        temp = random.random()
        if temp < 0.25:
            quadrant = 'q1'
        elif temp >= 0.25 and temp < 0.5:
            quadrant = 'q2'
        elif temp >= 0.5 and temp < 0.75:
            quadrant = 'q3'
=======
def Punch_Sequence(numPunch, quads, prob):
    sequence = []

    for i in range(numPunch):
        temp = random.random()

        if temp < prob[quads[0]]:
            y_pos = random.randint(0,20)
        else:
            y_pos = random.randint(21,40)
        
        #Generate the positions
        x_pos = random.randint(0,12)

        #Assign quadrants based on positions
        if y_pos <= 20:
            quadrant = quads[0]
>>>>>>> Stashed changes
        else:
            quadrant = 'q4'
        temp1 = random.random()
        if temp1 < prob['straight']:
            typ = 'straight'
        elif temp1 >= prob['straight'] + prob['uppercut']:
            typ = 'hook'
        else:
            typ = 'uppercut'
        
        newPunch = punch(quadrant, typ)
        punchArray = punch.punchToArray(newPunch)
        sequence.append(newPunch)
        printable.append(punchArray)
    print(printable)

random.seed(time())
punchSeq(None, 200)
