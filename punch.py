class punch(dict):
    def new(self):
        self.
punch = {
    'quadrant' : None,
    'position' : None,
    'type' : None,
    'delay' : None,
    'form' : None
}

prob = {
    'q1' : 0.25,
    'q2' : 0.25,
    'q3' : 0.25,
    'q4' : 0.25,
    'straight': 0.33,
    'hook' : 0.33,
    'uppercut': 0.33
}

def setQuadrant(punch, quadrant):
    punch['quadrant'] = quadrant

def setType(punch, typ):
    punch['type'] = typ

def training():
