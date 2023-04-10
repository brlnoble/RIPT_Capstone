import React from "react"

import "../CSS/General.css"
import "../CSS/About.css"

import ript_text from "../Images/RIPT_Text.svg"

class About extends React.Component {
    render() {
        return(
            <div className="main_container">
                <h1 className="page_title">About This Project</h1>

                <h2>Overview</h2>
                <p>The Robot Integrated Pad Trainer (<img src={ript_text} alt="ript" className="ript_text"></img>) is a device for helping boxers develop their offensive skills. The project uses a YOLOv7 computer vision model to observe and track the user with webcams, and identifies deficiencies in their skills. Once a training regime has been developed by a custom algorithm, pad training sessions can be conducted with the new regime. A gantry like system moves pads around for the user to interact with, sensing when they are hit before moving to a new location. This robotic emulation of a human pad trainer allows for more direct customization in the training, and is expandable and repeatable for any number of users and skill levels.</p>
                <p>The Github for the project can be found <a href="https://www.github.com/brlnoble/RIPT_Capstone" target="_blank" rel="noreferrer" style={{fontStyle: "italic",color: "#777"}}>here</a>.</p>

                <h2>Prototype</h2>
                <p>Below are images and GIFs of the prototype developed by the team.</p>
                <div className="prototype_images">
                    <img className="sample_img" src="https://github.com/brlnoble/RIPT_Capstone/blob/main/Pictures%20and%20Documents/Movement_Final_Face_On.gif?raw=true" alt="Movement Face On"></img>
                    <img className="sample_img" src="https://github.com/brlnoble/RIPT_Capstone/blob/main/Pictures%20and%20Documents/Movement_Final_Side.gif?raw=true" alt="Movement Side"></img>
                    <img className="sample_img" src="https://github.com/brlnoble/RIPT_Capstone/blob/main/Pictures%20and%20Documents/YOLO_Final.gif?raw=true" alt="YOLO Model"></img>
                </div>

                <div className="video_frame">
                    <iframe width="560" height="315" src="https://www.youtube.com/embed/QMfrOVIuLZo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
                </div>

                <h2>Meet the Team</h2>
                <div className="team">
                    <div className="team_member">
                        <img className="person_pic" src="https://media.licdn.com/dms/image/C4E03AQGG_IctTxaLUQ/profile-displayphoto-shrink_800_800/0/1651869250195?e=1682553600&v=beta&t=qmdkKuuHH5l8q7UoS7TbQdMsSNBywSbTkERCuexUAaI" alt="Brandon"></img>
                        <h3>Brandon Noble</h3>
                        <p>Electrical Engineering & Society</p>
                        <hr/>
                        <a href="https://www.linkedin.com/in/brlnoble" target="_blank" rel="noreferrer">LinkedIn</a>
                        <br/>
                        <a href="https://www.github.com/brlnoble" target="_blank" rel="noreferrer">Github</a>
                    </div>

                    <div className="team_member">
                        <img className="person_pic" src="https://media.licdn.com/dms/image/C5603AQHKFP9oDdw3Qw/profile-displayphoto-shrink_800_800/0/1517802772288?e=1682553600&v=beta&t=7KDN2YSPAxKd2MExycBdR_8EVp2_73O1b3Salfzwwjw" alt="Labib"></img>
                        <h3>Labib Kazi</h3>
                        <p>Electrical Engineering</p>
                        <hr/>
                        <a href="https://www.linkedin.com/in/alkazi/" target="_blank" rel="noreferrer">LinkedIn</a>
                        <br/>
                        <a href="https://www.github.com/kazia3" target="_blank" rel="noreferrer">Github</a>
                    </div>

                    <div className="team_member">
                        <img className="person_pic" src="https://media.licdn.com/dms/image/D5603AQE8ENTNaOqtSw/profile-displayphoto-shrink_800_800/0/1676244356117?e=1682553600&v=beta&t=0hX6vDOxhJ0nYgi3sN5ibLk__ZUwEiQuPVHtQnFSVQo" alt="Labib"></img>
                        <h3>Jame Tran</h3>
                        <p>Software Engineering</p>
                        <hr/>
                        <a href="https://www.linkedin.com/in/jame-tran/" target="_blank" rel="noreferrer">LinkedIn</a>
                        <br/>
                        <a href="https://www.github.com/JameTran" target="_blank" rel="noreferrer">Github</a>
                    </div>

                    <div className="team_member">
                        <img className="person_pic" src="https://media.licdn.com/dms/image/D5603AQEJ8s8phxbMMg/profile-displayphoto-shrink_800_800/0/1669326109089?e=1684972800&v=beta&t=VSoq6Mk-ZeQG4Hq1UqjEfUW5ZwmnSxGnkEH-xAQXPCQ" alt="Labib"></img>
                        <h3>Hunter Ceranic</h3>
                        <p>Mechatronics Engineering & Society</p>
                        <hr/>
                        <a href="https://www.linkedin.com/in/hunterceranic/" target="_blank" rel="noreferrer">LinkedIn</a>
                        <br/>
                        <a href="https://www.github.com/cer-hunter" target="_blank" rel="noreferrer">Github</a>
                    </div>


                </div>
            </div>
        )
    }
}

export default About