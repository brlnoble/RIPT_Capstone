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
    'q1' : 0.25,
    'q2' : 0.25,
    'q3' : 0.25,
    'q4' : 0.25,
    'straight': 0.33,
    'hook' : 0.33,
    'uppercut': 0.33
}

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
        else:
            quadrant = 'q4'
        temp1 = random.random()
        if temp1 < 0.33:
            typ = 'straight'
        elif temp1 >= 0.67:
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
