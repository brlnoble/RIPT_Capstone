import React from "react"
import { NavLink } from "react-router-dom";

import styles from "../CSS/Navbar.module.css" //Style sheet for the navigation bar

//Import images
import logo from "../Images/Logov2-01.svg"
import user_icon_unactive from "../Images/Icons/account_icon_unselect.svg"
import user_icon_active from "../Images/Icons/account_icon_select.svg"
import menu_icon from "../Images/Icons/menu_icon.svg"

//Setup active style for navlinks
const active_link = {
    textDecoration: "none",
    color: "#f15a24",
    fontWeight: "bold"
}

const unactive_link = {
    textDecoration: "none",
    color: "inherit",
}


class Navbar extends React.Component {
    render() {
        return (
            <div className={styles.container}>

                {/*The logo and title sit here*/}
                <div>
                    <NavLink to="/" className={styles.logo_and_title}>
                        <img src={logo} alt="logo" className={styles.logo}></img>
                        <h1 className={styles.title}>R.I.P.T.</h1>
                    </NavLink>
                </div>
            
                {/*Links to other pages. The styling is all weird cause of the new API*/}
                <ul className={styles.link}>
                    <li><NavLink to="/about" style={({ isActive }) => isActive ? active_link : unactive_link}>About</NavLink></li>
                    <li><NavLink to="/technical" style={({ isActive }) => isActive ? active_link : unactive_link}>How it Works</NavLink></li>
                    <li><NavLink to="/sessions" style={({ isActive }) => isActive ? active_link : unactive_link}>Sessions</NavLink></li>
                    <li><NavLink to="/trends" style={({ isActive }) => isActive ? active_link : unactive_link}>Trends</NavLink></li>
                </ul>

                {/*User icon and burger menu*/}
                <NavLink to="/profile"><img src={user_icon_unactive} alt="user_icon" className={styles.icon}></img></NavLink> {/*TODO: Update icon on click*/}
                <img src={menu_icon} alt="menu_icon" className={styles.icon}></img>
            </div>
        )
    }
}

export default Navbar