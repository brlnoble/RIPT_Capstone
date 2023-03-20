import React from "react"

import LineChart from "../LineChart"

class MetricStability extends React.Component {
    render() {
        return(
            <div>
                <h3>Stability</h3>
                <div className="metrics_stability">
                    <p className="punch_average">Session average:<br/> <strong>{this.props.avg} %</strong></p>
                    <LineChart avg={this.props.avg} chartData={this.props.chartData}></LineChart>
                </div>
            </div>
        )
    }
}

export default MetricStability