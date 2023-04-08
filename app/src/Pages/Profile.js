import React from "react";


import "../CSS/General.css"
import "../CSS/Profile/Profile.css"

import ProfileBox from "../Components/Profile/ProfileBox";
import AverageBox from "../Components/Profile/AverageBox";

//Selects the user to view
async function BrandonClick() {
    console.log("Brandon");
}

function JameClick() {
    console.log("Jame")
}

function LabibClick() {
    console.log("Labib")
}

function HunterClick() {
    console.log("Hunter")
}

//Main class
class Profile extends React.Component {
    render() {
        return(
            <div className="main_container">
                <div className="profile_container">
                    {/*User's profile on left side*/}
                    <ProfileBox user={this.props.user.profile}></ProfileBox>                    

                    {/*Average statistics on right side*/}
                    <AverageBox user={this.props.user.averageMetrics}></AverageBox>
                </div>

                <h2 className="user_select_title">Select User to Display</h2>
                <div className="user_select">
                    <button onClick={BrandonClick}>Brandon</button>
                    <button onClick={JameClick}>Jame</button>
                    <button onClick={LabibClick}>Labib</button>
                    <button onClick={HunterClick}>Hunter</button>
                </div>
            </div>
        )
    }
}

export default Profile