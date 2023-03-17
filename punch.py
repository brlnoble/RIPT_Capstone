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
        self.reaction = round(reaction*1000,2) #Convert to ms, 2 decimals

    def Set_Force(self,force):
        self.force = round(force,2) #Convert to 2 decimals

    def Set_Accuracy(self,accuracy):
        self.accuracy = accuracy

    def Return_Data(self):
        return {
            'quad': self.quadrant,
            'type': self.typ,
            'reaction': self.reaction,
            'force': self.force,
            'accuracy': self.accuracy 
        }

prob = {
    'q1' : 0.5,
    'q2' : 0.5,
    'q3' : 0.5,
    'q4' : 0.5,
    'straight': 0.33,
    'hook' : 0.33,
    'uppercut': 0.33
}

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
        else:
            quadrant = quads[1]

        #Assign punch type based on random variable
        temp1 = random.random()
        if temp1 < prob['straight']:
            typ = 'straight'
        elif temp1 >= prob['straight'] + prob['uppercut']:
            typ = 'hook'
        else:
            typ = 'uppercut'
        
        newPunch = punch(quadrant, typ, [x_pos,y_pos])
        sequence.append(newPunch)

    return sequence

random.seed(time())
