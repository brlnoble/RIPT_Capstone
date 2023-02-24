import React from "react"

import "../../CSS/Box.css"
import styles from "../../CSS/Session/SessionBoxHeader.module.css"

import expand_icon from "../../Images/Icons/expand_icon.svg"

function SessionsBoxHeader(category, date, time, duration) {
    return (
        <div>
            <div className={styles.header}>

                <div className={styles.header_box}>
                    <h2>{category}</h2>

                    {/*Vertical line for styling*/}
                    <span></span>

                    {/*Keeps the date and time on top of each other*/}
                    <div className={styles.time_box}>
                        <h3>{date}</h3>
                        <h3>{time}</h3>
                    </div>

                    {/*Vertical line for styling*/}
                    <span></span>

                    <h3>{duration}</h3>
                </div>

                <img src={expand_icon} alt="expand_icon" className={styles.expand_icon}></img>
            </div>
        </div>
    )
}

export default SessionsBoxHeader