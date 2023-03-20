import React from "react"

class QuadBox extends React.Component {
    render() {
        return(
            <div className="quad_box">
                <p className="right_line bottom_line">{this.props.quads[0]}</p>
                <p className="bottom_line">{this.props.quads[1]}</p>
                <p className="right_line">{this.props.quads[2]}</p>
                <p>{this.props.quads[3]}</p>
            </div>
        )
    }
}

export default QuadBox