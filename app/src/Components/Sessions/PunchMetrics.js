import React from "react"

import MetricBreakdown from "./MetricBreakdown"
import MetricStability from "./MetricStability"

import styles from "../../CSS/Session/Session.css"

class PunchMetrics extends React.Component {
    render() {
        return(
            <div className={styles.container}>
                <h2 className="punch_title">{this.props.punch}</h2>

                <div className="metric_grid">
                    <MetricBreakdown metricType="Force" metrics={this.props.force}></MetricBreakdown>
                    <MetricBreakdown metricType="Accuracy" metrics={this.props.accuracy}></MetricBreakdown>
                    <MetricBreakdown metricType="Reaction Time" metrics={this.props.reaction}></MetricBreakdown>
                    <MetricBreakdown metricType="Form" metrics={this.props.form}></MetricBreakdown>
                    <div className="metric_grid_stability"><MetricStability avg="70%"></MetricStability></div>
                </div>
            </div>
        )
    }
}

export default PunchMetrics