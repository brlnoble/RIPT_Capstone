import React from "react"
import Collapsible from 'react-collapsible';

import SessionsBoxHeader from "./SessionBoxHeader";
import PunchMetrics from "./PunchMetrics";
import MetricPerformance from "./MetricPerformance"

import ript_text from "../../Images/RIPT_Text.svg"


class SessionBox extends React.Component {
    render() {
        return (
            <div className="container">
                <div className="makeMeBig">
                    <Collapsible triggerOpenedClassName="collapsible_open" triggerClassName="collapsible_close" trigger={

                        //Box with information that can be opened or collapsed
                        SessionsBoxHeader(
                            this.props.data.category,
                            this.props.data.datetime,
                            this.props.data.duration)}
                        
                    >
                        <hr className="line_separator"></hr>
                        <div className="container_collapse">

                            {/*Create a metric box for each punch type analyzed*/}
                            <PunchMetrics
                                key={"Hook"}
                                punch={"Hook"} 
                                force={this.props.data.metrics.hook.force} 
                                accuracy={this.props.data.metrics.hook.accuracy} 
                                reaction={this.props.data.metrics.hook.reaction}
                                form={this.props.data.metrics.hook.form}>
                            </PunchMetrics>

                            <PunchMetrics
                                key={"Straight"}
                                punch={"Straight"} 
                                force={this.props.data.metrics.straight.force} 
                                accuracy={this.props.data.metrics.straight.accuracy} 
                                reaction={this.props.data.metrics.straight.reaction}
                                form={this.props.data.metrics.straight.form}>
                            </PunchMetrics>

                            <PunchMetrics
                                key={"Uppercut"}
                                punch={"Uppercut"} 
                                force={this.props.data.metrics.uppercut.force} 
                                accuracy={this.props.data.metrics.uppercut.accuracy} 
                                reaction={this.props.data.metrics.uppercut.reaction}
                                form={this.props.data.metrics.uppercut.form}>
                            </PunchMetrics>
                        </div>

                        <div className="metrics_performance">
                            <MetricPerformance avg={this.props.data.metrics.performance.avg} chartData={this.props.data.metrics.performance.data}></MetricPerformance>
                        </div>
                        
                        <hr className="line_separator"></hr>
                        <p style={{textAlign: "center"}}>The results of this session will be analyzed and applied to your next personalized session. 
                            <br/> <img src={ript_text} alt="ript" className="ript_text"></img> is commited to bettering your skills with our boxing algorithms!
                        </p>
                    </Collapsible>
                </div>
            </div>
        )
    }
}

export default SessionBox