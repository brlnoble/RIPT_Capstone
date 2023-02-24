import React from "react"
import Collapsible from 'react-collapsible';

import "../../CSS/Box.css"
import "../../CSS/Session/Session.css"

import SessionsBoxHeader from "./SessionBoxHeader";
import PunchMetrics from "./PunchMetrics";

const force = {avg: "250 N", quads: {q1: 100, q2: 200, q3: 300, q4: 400}};
const accuracy = {avg: "92%", quads: {q1: 90, q2: 90, q3: 88, q4: 100}}
const reaction = {avg: "315 ms", quads: {q1: 335, q2: 295, q3: 310, q4: 320}}
const form = {avg: "60%", quads: {q1: 65, q2: 62, q3: 50, q4: 63}}

class SessionBox extends React.Component {
    render() {
        return (

            <div className="container">
                <div className="makeMeBig">
                    <Collapsible trigger={SessionsBoxHeader("Personalized","Feb. 23, 2023","3:09 PM", "3m 30s")}>
                        <div className="container_collapse">
                            <PunchMetrics
                                punch="Uppercut" 
                                force={force} 
                                accuracy={accuracy} 
                                reaction={reaction}
                                form={form}>
                            </PunchMetrics>

                            <hr className="line_separator"></hr>

                            <PunchMetrics
                                punch="Cross" 
                                force={force} 
                                accuracy={accuracy} 
                                reaction={reaction}
                                form={form}>
                            </PunchMetrics>

                            <hr className="line_separator"></hr>

                            <PunchMetrics
                                punch="Straight" 
                                force={force} 
                                accuracy={accuracy} 
                                reaction={reaction}
                                form={form}>
                            </PunchMetrics>
                        </div>
                    </Collapsible>
                </div>
            </div>
            
        )
    }
}

export default SessionBox