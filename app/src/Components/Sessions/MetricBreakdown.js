import React from "react"

import QuadBox from "./QuadBox"

class MetricBreakdown extends React.Component {
    render() {
        return(
            <div>
                <h3>{this.props.metricType}</h3>
                <div className="metrics">
                    <p className="punch_average">Session average:<br/> <strong>{this.props.metrics.avg} {this.props.units}</strong></p>
            
                    {/*This is to make the quadrants of the numerics*/}
                    <QuadBox quads={this.props.metrics.quads}></QuadBox>
                </div>
            </div>
        )
    }
}

export default MetricBreakdown