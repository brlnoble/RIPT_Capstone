import React from "react"
import { Link } from "react-router-dom";

import "../CSS/Box.css"

class ListBox extends React.Component {
    render() {
        return(
            <div className="container">
                <h1>{this.props.title_text}</h1>

                {/*Makes a list of the array passed in*/}
                <ul>
                    {this.props.show_text.map( (item) => (
                        <li id={item.text}>{item.text}</li>
                    ))}
                </ul>

                {/*Button to redirect pages*/}
                <Link to={this.props.redirect} className="react_link_button"><button>{this.props.button_text}</button></Link>
            </div>
        )
    }
}

export default ListBox