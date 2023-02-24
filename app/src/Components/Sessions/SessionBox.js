import React from "react"
import Collapsible from 'react-collapsible';

import "../../CSS/Box.css"
import "../../CSS/Session/Session.css"

import SessionsBoxHeader from "./SessionBoxHeader";
import PunchMetrics from "./PunchMetrics";



class SessionBox extends React.Component {
    render() {
        return (
            <div className="container">
                <div className="makeMeBig">
                    <Collapsible triggerOpenedClassName="collapsible_open" triggerClassName="collapsible_close" trigger={

                        //Box with information that can be opened or collapsed
                        SessionsBoxHeader(
                            this.props.info.category,
                            this.props.info.date,
                            this.props.info.time, 
                            this.props.info.duration)}
                        
                    >
                        <div className="container_collapse">

                            {/*Create a metric box for each punch type analyzed*/}
                            {this.props.punchData.map( (punch) => (
                                <PunchMetrics
                                    punch={punch.type} 
                                    force={punch.metrics.force} 
                                    accuracy={punch.metrics.accuracy} 
                                    reaction={punch.metrics.reaction}
                                    form={punch.metrics.form}
                                    stability={punch.metrics.stability}>
                                </PunchMetrics>
                            ))}

                            <p style={{textAlign: "center"}}>The results of this session will be analyzed and applied to your next personalized session. 
                                <br/> <strong>R.I.P.T.</strong> is commited to bettering your skills with our boxing algorithms!
                            </p>

                        </div>
                    </Collapsible>
                </div>
            </div>
        )
    }
}

export default SessionBox