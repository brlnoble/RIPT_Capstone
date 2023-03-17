import random
from time import time

class punch:
    def __init__(self, quadrant, typ, position):
        self.quadrant = quadrant #q1, q2, q3, or q4
        self.position = position #[x,y]
        self.typ = typ #hook, straight, uppercut
        self.reaction = None #time until impact or 1s max
        self.force = None #load cell or null
        self.accuracy = None #did they hit (True/False)

    def __str__(self):
        return f"Punch Object: \nQuad: {self.quadrant} \nPos: {self.position} \nType: {self.typ} \nReac: {self.reaction} \nForce: {self.force} \nAcc: {self.accuracy}"
    
    def Punch_To_Array(self):
        return [self.quadrant, self.typ]
    
    def Set_Reaction(self,reaction):
        self.reaction = reaction

    def Set_Force(self,force):
        self.force = force

    def Set_Accuracry(self,accuracy):
        self.accuracy = accuracy

prob = {
    'q1' : 0.25,
    'q2' : 0.25,
    'q3' : 0.25,
    'q4' : 0.25,
    'straight': 0.33,
    'hook' : 0.33,
    'uppercut': 0.33
}

def Punch_Sequence(numPunch,quads):
    sequence = []

    for i in range(numPunch):    
        #Generate the positions
        x_pos = random.randint(0,12)
        y_pos = random.randint(0,40)

        #Assign quadrants based on positions
        if y_pos <= 20:
            quadrant = quads[0]
        else:
            quadrant = quads[1]

        #Assign punch type based on random variable
        temp1 = random.random()
        if temp1 < 0.33:
            typ = 'straight'
        elif temp1 >= 0.67:
            typ = 'hook'
        else:
            typ = 'uppercut'
        
        newPunch = punch(quadrant, typ, [x_pos,y_pos])
        sequence.append(newPunch)

    return sequence

random.seed(time())
