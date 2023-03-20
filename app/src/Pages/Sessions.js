import React from "react"

import "../CSS/General.css"
import "../CSS/Box.css"
import "../CSS/Session/SessionAlt.css" //Changed the CSS for vertical layout, still holding onto old one
import "../CSS/Session/SessionFilter.css"

import SessionBox from "../Components/Sessions/SessionBox.js"
import FilterForm from "../Components/Sessions/FilterForm.js"

class Sessions extends React.Component {
    render() {
        return(
            <div className="main_container">
                <h1 className="page_title">Sessions and Metrics</h1>
                
                <hr className="line_separator"></hr>
                <FilterForm></FilterForm>

                {this.props.user.sessions.map( (session) => (
                    <SessionBox
                        key={session.id}
                        data={session}
                    />
                ))}
            </div>
        )
    }
}

export default Sessions