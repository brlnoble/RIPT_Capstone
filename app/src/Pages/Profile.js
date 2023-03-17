import React from "react";

import "../CSS/General.css"
import "../CSS/Profile/Profile.css"

import ProfileBox from "../Components/Profile/ProfileBox";
import AverageBox from "../Components/Profile/AverageBox";

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
            </div>
        )
    }
}

export default Profile