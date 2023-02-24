import React from "react"

import "../CSS/General.css"

import SessionBox from "../Components/Sessions/SessionBox"


//This sets up the data for a single entry in the session
const force = {avg: "250 N", quads: {q1: 100, q2: 200, q3: 300, q4: 400}};
const accuracy = {avg: "92%", quads: {q1: 90, q2: 90, q3: 88, q4: 100}}
const reaction = {avg: "315 ms", quads: {q1: 335, q2: 295, q3: 310, q4: 320}}
const form = {avg: "60%", quads: {q1: 65, q2: 62, q3: 50, q4: 63}}
const stability = {avg: 70,chartData: [75,84,80,92,77,65,74,53,45,58,61,65,63,72]};

//Uppercut punch data for this session
const uppercut = {
    type: "Uppercut", 
    metrics: {
        force: force, accuracy: accuracy, reaction: reaction, form: form, stability: stability
    }
}

//Straight punch data for this session
const straight = {
    type: "Straight", 
    metrics: {
        force: force, accuracy: accuracy, reaction: reaction, form: form, stability: stability
    }
}

//Cross punch data for this session
const cross = {
    type: "Cross", 
    metrics: {
        force: force, accuracy: accuracy, reaction: reaction, form: form, stability: stability
    }
}

//Array of punches for this session
const punches = [uppercut, straight, cross];

//Session data object that needs to be passed from backend
const sessionData = {
    key: 12345, //needs to be generated
    sessionInfo: {
        category: "Personalized",
        date: "Feb. 23, 2023",
        time: "3:09 PM",
        duration: "3m 30s",
    },
    punchData: punches
}


class Sessions extends React.Component {
    render() {
        return(
            <div className="main_container">
                <h1>Sessions and stuff</h1>
                <SessionBox
                    key={sessionData.key}
                    info={sessionData.sessionInfo}
                    punchData={sessionData.punchData}
                />
            </div>
        )
    }
}

export default Sessions