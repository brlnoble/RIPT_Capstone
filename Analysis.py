import json
import datetime

#~~~~~~~~~~ Read in the data ~~~~~~~~~~
data = []

with open('results.json') as f:
    data = json.load(f)

#Grab the duration and remove it from the array
duration = data[0]["duration"]
data = data[1:]

#~~~~~~~~~~ Format of results #~~~~~~~~~~
metrics = {
    "hook": {
        "force": {
            "avg": 0.0,
            "quads": [0.0,0.0,0.0,0.0],
            "numPunch": [0,0,0,0]
        },
        "reaction": {
            "avg": 0.0,
            "quads": [0.0,0.0,0.0,0.0],
            "numPunch": [0,0,0,0]
        },
        "accuracy": {
            "avg": 0.0,
            "quads": [0.0,0.0,0.0,0.0],
            "numPunch": [0,0,0,0]
        },
        "form": {
            "avg": 0.0,
            "quads": [0.0,0.0,0.0,0.0],
            "numPunch": [0,0,0,0]
        },
        "numPunch": 0
    },

    "uppercut": {
        "force": {
            "avg": 0.0,
            "quads": [0.0,0.0,0.0,0.0],
            "numPunch": [0,0,0,0]
        },
        "reaction": {
            "avg": 0.0,
            "quads": [0.0,0.0,0.0,0.0],
            "numPunch": [0,0,0,0]
        },
        "accuracy": {
            "avg": 0.0,
            "quads": [0.0,0.0,0.0,0.0],
            "numPunch": [0,0,0,0]
        },
        "form": {
            "avg": 0.0,
            "quads": [0.0,0.0,0.0,0.0],
            "numPunch": [0,0,0,0]
        },
        "numPunch": 0
    },
    
    "straight": {
        "force": {
            "avg": 0.0,
            "quads": [0.0,0.0,0.0,0.0],
            "numPunch": [0,0,0,0]
        },
        "reaction": {
            "avg": 0.0,
            "quads": [0.0,0.0,0.0,0.0],
            "numPunch": [0,0,0,0]
        },
        "accuracy": {
            "avg": 0.0,
            "quads": [0.0,0.0,0.0,0.0],
            "numPunch": [0,0,0,0]
        },
        "form": {
            "avg": 0.0,
            "quads": [0.0,0.0,0.0,0.0],
            "numPunch": [0,0,0,0]
        },
        "numPunch": 0
    },
    "performance": {
        "avg": 0.0,
        "data": []
    },    
}

best_metrics = {
    "force": 0.0,
    "reaction": 0.0,
    "accuracy": 0.0,
    "form": 0.0
}
#~~~~~~~~~~ Copy data over to metrics ~~~~~~~~~~

for p in data: #for hook, straight, uppercut

    #Averages
    metrics[p["type"]]["force"]["avg"] += p["force"]
    metrics[p["type"]]["reaction"]["avg"] += p["reaction"]
    metrics[p["type"]]["accuracy"]["avg"] += p["accuracy"]*100

    #Quadrant specific
    metrics[p["type"]]["force"]["quads"][int(p["quad"][1])-1] += p["force"]
    metrics[p["type"]]["reaction"]["quads"][int(p["quad"][1])-1] += p["reaction"]
    metrics[p["type"]]["accuracy"]["quads"][int(p["quad"][1])-1] += p["accuracy"]*100

    #Count number number of punches so average can be calculated
    metrics[p["type"]]["numPunch"] += 1
    metrics[p["type"]]["force"]["numPunch"][int(p["quad"][1])-1] += 1
    metrics[p["type"]]["reaction"]["numPunch"][int(p["quad"][1])-1] += 1
    metrics[p["type"]]["accuracy"]["numPunch"][int(p["quad"][1])-1] += 1

    #Grab the best values for each metrix (used later by performance)
    best_metrics["force"] = p["force"] if p["force"] > best_metrics["force"] else best_metrics["force"]
    best_metrics["reaction"] = p["reaction"] if p["reaction"] < best_metrics["reaction"] else best_metrics["reaction"]
    best_metrics["accuracy"] = p["accuracy"] if p["accuracy"] > best_metrics["accuracy"] else best_metrics["accuracy"]

#~~~~~~~~~~ Calculate the average of each ~~~~~~~~~~
for pType in ["hook","uppercut","straight"]:
    for avg in ["force","reaction","accuracy","form"]:

        #Overall average
        if metrics[pType]["numPunch"] > 0:
            metrics[pType][avg]["avg"] = round(metrics[pType][avg]["avg"] / metrics[pType]["numPunch"],2)

        #Average per quadrant
        for quad in range(0,4):
            if metrics[pType][avg]["numPunch"][quad] > 0:
                metrics[pType][avg]["quads"][quad] = round(metrics[pType][avg]["quads"][quad] / metrics[pType][avg]["numPunch"][quad],0)

        #Remove the number of punches from the metrics dictionary
        del metrics[pType][avg]["numPunch"]
    
    #Remove the number of punches from the metrics dictionary
    del metrics[pType]["numPunch"]

#~~~~~~~~~~ Calculate the performance score of each punch ~~~~~~~~~~
for p in data:

    performance = 0
    consider = ["force","reaction","accuracy"] #need to incorporate form

    for val in consider:
        if best_metrics[val] > 0:
            performance += p[val] / best_metrics[val]

    #Add to the JSON
    metrics["performance"]["data"].append( 100*round(performance / len(consider),4) )

#Normalize so the data is between 0-100%, otherwise it reads as very low
p_data = metrics["performance"]["data"].copy() #make a copy so it doesn't affect the original
p_data[:] = (val for val in p_data if val != 0) #remove zeros so the min function doesn't pick them up
p_max = max(p_data)
p_min = min(p_data)

for i in range(len(metrics["performance"]["data"])):
    if metrics["performance"]["data"][i] > 0.0:
        metrics["performance"]["data"][i] = round(100* ( (metrics["performance"]["data"][i] - p_min)/(p_max - p_min) ),2)

#Average performance
metrics["performance"]["avg"] = round(sum(metrics["performance"]["data"]) / len(metrics["performance"]["data"]),2)

#~~~~~~~~~~ Create the final JSON object ~~~~~~~~~~
session = {
    "id": "", #to be generated by server
    "username": "", #to be assigned by server
    "category": "Personalized", #hard coding for now as we haven't enabled other categories
    "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), #time the metrics were calculated, close enough to when the session took place
    "duration": "0 0:"+duration,
    "metrics": metrics
}

#~~~~~~~~~~ Write results to file ~~~~~~~~~~
with open("metrics.json","w") as f:
    json.dump(session, f, indent=4)