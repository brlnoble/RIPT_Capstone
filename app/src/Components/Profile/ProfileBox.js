import React from "react"
import {Link} from "react-router-dom"

import "../../CSS/Box.css"
import styles from "../../CSS/Profile/ProfileBox.module.css"

function getStance(stance) {
    if(stance == true) {
        return "Orthodox"
    }
    else {
        return "Southpaw"
    }
}

class ProfileBox extends React.Component {
    render() {
        return(
            <div className="container">
                <div className={styles.profile_box}>

                    {/*Profile picture and first name*/}
                    <img src={this.props.user.picture} alt="profile_picture" className={styles.profile_pic}></img>
                    <h1 className={styles.user_fullname}>{this.props.user.first_name}</h1>
                    
                    <div className={styles.user_info}>
                        
                        {/*Labels for the user information*/}
                        <div className={styles.info_titles}>
                            <h2>Username: </h2>
                            <h2>Email: </h2>
                            <h2>Birthday: </h2>
                            <br className={styles.divide_line}></br>
                            <h2>Member Since: </h2>
                            <h2>Sessions: </h2>
                            <h2>Stance: </h2>
                        </div>

                        {/*The user's actual information*/}
                        <div className={styles.info_text}>
                            <h2>{this.props.user.username}</h2>
                            <h2>{this.props.user.email}</h2>
                            <h2>{this.props.user.birthday.slice(0,10)}</h2>
                            <br></br>
                            <h2>{this.props.user.membership.slice(0,10)}</h2>
                            <h2>{this.props.user.session_num}</h2>
                            <h2>{getStance(this.props.user.isorthodox)}</h2>
                        </div>

                    </div>

                    <div>
                        {/*Buttons we might not actually need*/}
                        <Link className="react_link_button"><button className="react_link_button">Update my info</button></Link>
                        <Link className="react_link_button"><button className="react_link_button">Change my password</button></Link>
                    </div>

                </div>                
            </div>               
        )
    }
}

export default ProfileBox