import React from "react"

import LineChart from "../LineChart"

class MetricPerformance extends React.Component {
    render() {
        return(
            <div>
                <h3>Performance</h3>
                <p className="punch_average">Session average:<br/> <strong>{this.props.avg} %</strong></p>
                <LineChart avg={this.props.avg} chartData={this.props.chartData}></LineChart>
            </div>
        )
    }
}

export default MetricPerformance