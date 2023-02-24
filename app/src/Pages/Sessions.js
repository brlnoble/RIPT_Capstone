import React from "react"

import "../CSS/General.css"

import SessionBox from "../Components/Sessions/SessionBox"

class Sessions extends React.Component {
    render() {
        return(
            <div className="main_container">
                <h1>Sessions and stuff</h1>
                <SessionBox/>
            </div>
        )
    }
}

export default Sessions