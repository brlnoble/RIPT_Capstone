import React from "react"
import styles from "../CSS/Footer.module.css"

import github_icon from "../Images/Icons/github_icon.svg"

class Footer extends React.Component {
    render() {
        return(
            <div className={styles.container}>
                <ul>
                    <li>This is an engineering capstone project by students. <br></br><strong>Copyright © 2023</strong></li>
                    <li>brlnoble@hotmail.com</li>
                    <li><a href="https://github.com/brlnoble/RIPT_Capstone" target="_blank" rel="noreferrer" className={styles.link}><img src={github_icon} alt="github" className={styles.icon}></img>Github</a></li>
                </ul>
            </div>
        )
    }
}

export default Footer