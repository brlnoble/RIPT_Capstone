import React from "react";

import "../CSS/General.css"
import "../CSS/About.css"

class Technical extends React.Component {
    render() {
        return(
            <div className="main_container">
                <h1 className="page_title">About This Project</h1>

                <p>Below is a video explaining the prototype and showcasing future plans should the project continue.</p>
                <div className="video_frame">
                    <iframe width="800" height="400" src="https://www.youtube.com/embed/TRa0bQ9WmGY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
                </div>
            
            </div>
        )
    }
}

export default Technical