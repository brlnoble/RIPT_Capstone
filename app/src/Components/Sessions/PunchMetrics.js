import React from "react"

import MetricBreakdown from "./MetricBreakdown"

class PunchMetrics extends React.Component {
    render() {
        return(
            <div className="punch_container">
                <h2 className="punch_title">{this.props.punch}</h2>

                <div className="metric_grid">
                    <MetricBreakdown metricType="Force" metrics={this.props.force} units="N"></MetricBreakdown>
                    <MetricBreakdown metricType="Accuracy" metrics={this.props.accuracy} units="%"></MetricBreakdown>
                    <MetricBreakdown metricType="Reaction Time" metrics={this.props.reaction} units="ms"></MetricBreakdown>
                    <MetricBreakdown metricType="Form" metrics={this.props.form} units="%"></MetricBreakdown>
                </div>
            </div>
        )
    }
}

export default PunchMetrics