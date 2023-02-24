import React from "react"

class QuadBox extends React.Component {
    render() {
        return(
            <div className="box">
                <p className="right_line bottom_line">{this.props.quads.q1}</p>
                <p className="bottom_line">{this.props.quads.q2}</p>
                <p className="right_line">{this.props.quads.q3}</p>
                <p>{this.props.quads.q4}</p>
            </div>
        )
    }
}

export default QuadBox