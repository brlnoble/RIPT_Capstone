import React from "react"
import styles from "../CSS/Navbar.module.css" //Style sheet for the navigation bar

//Import images
import logo from "../Images/Logov2-01.svg"
import user_icon from "../Images/Icons/account_icon.svg"
import menu_icon from "../Images/Icons/menu_icon.svg"

class Navbar extends React.Component {
    render() {
        return (
            <div className={styles.container}>

                {/*The logo and title sit here*/}
                <div className={styles.logo_and_title}>
                    <img src={logo} alt="logo" className={styles.logo}></img>
                    <h1 className={styles.title}>R.I.P.T.</h1>
                </div>
            
                {/*Links to other pages*/}
                <ul className={styles.link}>
                    <li>About Us</li>
                    <li>How it Works</li>
                    <li>Sessions</li>
                    <li>Trends</li>
                </ul>

                {/*User icon and burger menu*/}
                <img src={user_icon} alt="user_icon" className={styles.icon}></img>
                <img src={menu_icon} alt="menu_icon" className={styles.icon}></img>
            </div>
        )
    }
}

export default Navbar