import React from "react"

import "../../CSS/Box.css"
import styles from "../../CSS/Session/SessionBoxHeader.module.css"

import expand_icon from "../../Images/Icons/expand_icon.svg"

//For converting month numeric to the long name
function getMonthName(monthNumber) {
    const date = new Date();
    date.setMonth(parseInt(monthNumber)-1);
  
    return date.toLocaleString('en-US', { month: 'long' });
}

function SessionsBoxHeader(datetime, duration) {
    console.log(datetime)

    return (
        <div>
            <div className={styles.header}>

                <div className={styles.header_box}>
                    <h2>Personalized</h2>

                    {/*Vertical line for styling*/}
                    <span></span>

                    {/*Keeps the date and time on top of each other*/}
                    <div className={styles.time_box}>
                        {/*Converts the datetime into something readable like "March 19, 2023" and "00:30"*/}
                        <h3>{getMonthName(datetime.slice(5,7))} {datetime.slice(8,10)}, {datetime.slice(0,4)}</h3>
                        <h3>{datetime.slice(11,16)}</h3>
                    </div>

                    {/*Vertical line for styling*/}
                    <span></span>

                    <h3>{duration.slice(4,9)}</h3>
                </div>

                <img src={expand_icon} alt="expand_icon" className={styles.expand_icon}></img>
            </div>
        </div>
    )
}

export default SessionsBoxHeader