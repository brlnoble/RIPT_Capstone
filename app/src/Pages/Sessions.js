import React from "react"

import "../CSS/General.css"

import SessionBox from "../Components/Sessions/SessionBox"

class Sessions extends React.Component {
    render() {
        return(
            <div className="main_container">
                <h1>Sessions and stuff</h1>

                {this.props.user.sessions.map( (session) => (
                    <SessionBox
                        key={session.key}
                        info={session.sessionInfo}
                        punchData={session.punchData}
                    />
                ))}
            </div>
        )
    }
}

export default Sessions