import json

##~~~~~~~~~~ Read in the data #~~~~~~~~~~
data = []
with open('results.json') as f:
    data = json.load(f)

#~~~~~~~~~~ Format of results #~~~~~~~~~~
metrics = {
    "hook": {
        "force": {
            "avg": 0,
            "quads": [0,0,0,0],
            "numPunch": [0,0,0,0]
        },
        "reaction": {
            "avg": 0,
            "quads": [0,0,0,0],
            "numPunch": [0,0,0,0]
        },
        "accuracy": {
            "avg": 0,
            "quads": [0,0,0,0],
            "numPunch": [0,0,0,0]
        },
        "numPunch": 0
    },

    "uppercut": {
        "force": {
            "avg": 0,
            "quads": [0,0,0,0],
            "numPunch": [0,0,0,0]
        },
        "reaction": {
            "avg": 0,
            "quads": [0,0,0,0],
            "numPunch": [0,0,0,0]
        },
        "accuracy": {
            "avg": 0,
            "quads": [0,0,0,0],
            "numPunch": [0,0,0,0]
        },
        "numPunch": 0
    },
    
    "straight": {
        "force": {
            "avg": 0,
            "quads": [0,0,0,0],
            "numPunch": [0,0,0,0]
        },
        "reaction": {
            "avg": 0,
            "quads": [0,0,0,0],
            "numPunch": [0,0,0,0]
        },
        "accuracy": {
            "avg": 0,
            "quads": [0,0,0,0],
            "numPunch": [0,0,0,0]
        },
        "numPunch": 0
    },    
}

#~~~~~~~~~~ Copy data over to metrics ~~~~~~~~~~

for p in data: #for hook, straight, uppercut

    #Averages
    metrics[p["type"]]["force"]["avg"] += p["force"]
    metrics[p["type"]]["reaction"]["avg"] += p["reaction"]
    metrics[p["type"]]["accuracy"]["avg"] += p["accuracy"]

    #Quadrant specific
    metrics[p["type"]]["force"]["quads"][int(p["quad"][1])-1] += p["force"]

    metrics[p["type"]]["reaction"]["quads"][int(p["quad"][1])-1] += p["reaction"]

    metrics[p["type"]]["accuracy"]["quads"][int(p["quad"][1])-1] += p["accuracy"]

    #Count number number of punches so average can be calculated
    metrics[p["type"]]["numPunch"] += 1
    metrics[p["type"]]["force"]["numPunch"][int(p["quad"][1])-1] += 1
    metrics[p["type"]]["reaction"]["numPunch"][int(p["quad"][1])-1] += 1
    metrics[p["type"]]["accuracy"]["numPunch"][int(p["quad"][1])-1] += 1

#~~~~~~~~~~ Calculate the average of each ~~~~~~~~~~
for pType in ["hook","uppercut","straight"]:
    for avg in ["force","reaction","accuracy"]:

        #Overall average
        if metrics[pType]["numPunch"] > 0:
            metrics[pType][avg]["avg"] = round(metrics[pType][avg]["avg"] / metrics[pType]["numPunch"],2)

        #Average per quadrant
        for quad in range(0,4):
            if metrics[pType][avg]["numPunch"][quad] > 0:
                metrics[pType][avg]["quads"][quad] = round(metrics[pType][avg]["quads"][quad] / metrics[pType][avg]["numPunch"][quad],2)

        #Remove the number of punches from the metrics dictionary
        del metrics[pType][avg]["numPunch"]
    
    #Remove the number of punches from the metrics dictionary
    del metrics[pType]["numPunch"]


#~~~~~~~~~~ Write results to file ~~~~~~~~~~
with open("metrics.json","w") as f:
    json.dump(metrics, f, indent=4)