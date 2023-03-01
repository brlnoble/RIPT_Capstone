import React from "react"
import { Link } from "react-router-dom";

const pageStyle = {
    height: "45vh",
    margin: "10%",
    marginTop: "100px",
    textAlign: "center"
};

class NoPage extends React.Component {
    render() {
        return(
            <div style={pageStyle}>
                <h2>Whoops! It appears this page didn't make it to the ring.</h2>
                <Link to="/" style={{textDecoration: "None",color: "#777"}}><h3>Click here to return home.</h3></Link>
            </div>
        )
    }
}

export default NoPage