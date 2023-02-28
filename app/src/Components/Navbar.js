import React from "react"
import { NavLink } from "react-router-dom";

import "../CSS/Navbar.css" //Style sheet for the navigation bar

//Import images
import logo from "../Images/Logov2-01.svg"
import user_icon_unactive from "../Images/Icons/account_icon_unselect.svg"
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
            <div className="nav_container">

                {/*The logo and title sit here*/}
                <div>
                    <NavLink to="/" className="nav_logo_and_title">
                        <img src={logo} alt="logo" className="nav_logo"></img>
                        <h1 className="nav_title">R.I.P.T.</h1>
                    </NavLink>
                </div>
            
                {/*Links to other pages. The styling is all weird cause of the new API*/}
                <ul className="nav_link">
                    <li><NavLink to="/about" style={({ isActive }) => isActive ? active_link : unactive_link}>About</NavLink></li>
                    <li><NavLink to="/technical" style={({ isActive }) => isActive ? active_link : unactive_link}>How it Works</NavLink></li>
                    <li><NavLink to="/sessions" style={({ isActive }) => isActive ? active_link : unactive_link}>Sessions</NavLink></li>
                    <li><NavLink to="/trends" style={({ isActive }) => isActive ? active_link : unactive_link}>Trends</NavLink></li>
                </ul>

                {/*User icon and burger menu*/}
                <NavLink to="/profile" className={({ isActive }) => isActive ? "nav_active_icon" : "nav_inactive_icon"}>
                    <img src={user_icon_unactive} alt="user_icon" className="nav_icon"></img>
                </NavLink> {/*The best I can do is make the icon orange*/}
                <NavLink to="/sign-in" className="menu_icon"><img src={menu_icon} alt="menu_icon" className="nav_icon"></img></NavLink>
            </div>
        )
    }
}

export default Navbar