import json
import datetime

#~~~~~~~~~~ Read in the data ~~~~~~~~~~
data = []
#Read in most of the data
with open('results.json') as f:
    data = json.load(f)

#Read in the form data
form_data = []
with open('form_results.json') as f:
    form_data = json.load(f)

#Grab the duration and remove it from the array
duration = data[0]["duration"]
data = data[1:]

#~~~~~~~~~~ Calculate IOU Scores ~~~~~~~~~~
#Total IOU score
total_iou = sum(form_data["iou_data"]) / form_data["frames"]

prev_frames = [0,0]
iou_vals = []

#Values for the left side
for curr_frames in form_data["iou_left"]:
    iou_vals.append( round(100*sum(form_data["iou_data"][prev_frames[1]:curr_frames[1]]) / (curr_frames[1] - prev_frames[1]),2))

    prev_frames = curr_frames

prev_frames = [0,0]

#Values for the right side
for curr_frames in form_data["iou_right"]:
    iou_vals.append( round(100*sum(form_data["iou_data"][prev_frames[1]:curr_frames[1]]) / (curr_frames[1] - prev_frames[1]),2))

    prev_frames = curr_frames

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

avg_metrics = {
    "force": 0.0,
    "reaction": 0.0,
    "accuracy": 0.0,
    "form": 0.0
}
#~~~~~~~~~~ Copy data over to metrics ~~~~~~~~~~

iou_index = 0

for p in data: #for hook, straight, uppercut

    #Add the IOU
    if iou_index < len(iou_vals):
        metrics[p["type"]]["form"]["avg"] += iou_vals[iou_index]
        metrics[p["type"]]["form"]["quads"][int(p["quad"][1])-1] += iou_vals[iou_index]
    else:
        metrics[p["type"]]["form"]["avg"] += total_iou
        metrics[p["type"]]["accuracy"]["quads"][int(p["quad"][1])-1] += total_iou

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

    #Used for calculating the overall average of the session
    avg_metrics["force"] += p["force"]
    avg_metrics["reaction"] += p["reaction"]
    avg_metrics["accuracy"] += p["accuracy"]

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
consider = ["force","reaction","accuracy","form"]

#Find metric averages across the session
for val in consider:
    avg_metrics[val] /= len(data)

#Calculate performance
for p in data:
    performance = 0

    for val in consider:
        if avg_metrics[val] > 0:
            performance += p[val] / avg_metrics[val]

    #Add to the JSON
    metrics["performance"]["data"].append( round(100*performance / len(consider),2) )

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