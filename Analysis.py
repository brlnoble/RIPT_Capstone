import json

#Read in the data
data = []
with open('results.json') as f:
    data = json.load(f)

#Punch type arrays
metrics = [
    #Hook [0]
    [
        [],[],[],[]
    ],

    #Straight [1]
    [
        [],[],[],[]
    ],

    #Uppercut [2]
    [
        [],[],[],[]
    ]
]


#Copy the data into the quadrant arrays
for p in data:

    #Check punch type
    if p["type"] == "hook":
        typeIndex = 0
    elif p["type"] == "straight":
        typeIndex = 1
    else:
        typeIndex = 2

    if p["quad"] == "q1":
        metrics[typeIndex][0].append(p)
    elif p["quad"] == "q2":
        metrics[typeIndex][1].append(p)
    elif p["quad"] == "q3":
        metrics[typeIndex][2].append(p)
    else:
        metrics[typeIndex][3].append(p)

#~~~~~~~~~~ Calculate average forces ~~~~~~~~~~

for pType in metrics: #for hook, straight, uppercut
    print("#"*50)
    #Average per quadrant
    reaction = [0,0,0,0]
    force = [0,0,0,0]
    accuracy = [0,0,0,0]

    #Average for all quadrants
    reactionAll = 0
    forceAll = 0
    accuracyAll = 0

    for quad in range(0,4): #for q1, q2, q3, q4
        for p in pType[quad]:
            reaction[quad] += p["reaction"]
            reactionAll += p["reaction"]

            force[quad] += p["force"]
            forceAll += p["force"]

            accuracy[quad] += p["accuracy"] * 1
            accuracyAll += p["accuracy"] * 1

        if len(pType[quad]) > 0:
            force[quad] /= len(pType[quad])
            reaction[quad] /= len(pType[quad])
            accuracy[quad] /= len(pType[quad])


        print(f"Q: {quad+1}\nF: {force[quad]}\nR: {reaction[quad]}\nA: {accuracy[quad]}\nNum Punches: {len(pType[quad])}")
        print("~"*20)

    if len(pType[0]) > 0:
        forceAll /= (len(pType[0]) + len(pType[1]) + len(pType[2]) + len(pType[3]))
        reactionAll /= (len(pType[0]) + len(pType[1]) + len(pType[2]) + len(pType[3]))
        accuracyAll /= (len(pType[0]) + len(pType[1]) + len(pType[2]) + len(pType[3]))
        
    print(f"FORCE: {forceAll}, REAC: {reactionAll}, ACC: {accuracyAll}")