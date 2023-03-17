import React from "react"
import { Link } from "react-router-dom";

import "../../CSS/Box.css"
import styles from "../../CSS/Profile/AverageBox.module.css"

class AverageBox extends React.Component {
    render() {
        return(
            <div className="container">
                <div className={styles.average_box}>
                    <h1 className={styles.average_title}>My Average Metrics</h1>

                    <div className={styles.metric_box}>
                        <h2>Force</h2>
                        <h3>{this.props.user.force}</h3>
                        <p>+10% this week</p>

                        <h2>Accuracy</h2>
                        <h3>{this.props.user.accuracy}</h3>
                        <p>-8% this week</p>

                        <h2>Reation Time</h2>
                        <h3>{this.props.user.reaction}</h3>
                        <p>+3% this week</p>

                        <h2>Form Score</h2>
                        <h3>{this.props.user.form}</h3>
                        <p>+1% this week</p>

                        <h2>Stability</h2>
                        <h3>{this.props.user.stability}</h3>
                        <p>-11% this week</p>
                    </div>

                    <p className={styles.context}>Your average metrics are based off your last 10 sessions</p>

                    <Link to="/sessions" className="react_link_button"><button>View Sessions</button></Link>
                    <Link to="/trends" className="react_link_button"><button>See My Trends</button></Link>

                </div>
            </div>
        )
    }
}

export default AverageBox