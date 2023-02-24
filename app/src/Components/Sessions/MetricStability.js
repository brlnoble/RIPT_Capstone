import React from "react"

import LineChart from "../LineChart"

const data = [75,84,80,92,77,65,74,53,45,58,61,65,63,72];

class MetricStability extends React.Component {
    render() {
        return(
            <div>
                <h3>Stability</h3>
                <div className="metrics_stability">
                    <p className="punch_average">Session average:<br/> <strong>{this.props.avg}</strong></p>
                    <LineChart chartData={data}></LineChart>
                </div>

                
            </div>
        )
    }
}

export default MetricStability