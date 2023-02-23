import React from "react"

import "../../CSS/Box.css"
import styles from "../../CSS/Profile/ProfileBox.module.css"
import user_pic from "../../Images/user_pic.png"

class ProfileBox extends React.Component {
    render() {
        return(
            <div className="container">
                <div className={styles.profile_box}>

                    {/*Profile picture and first name*/}
                    <img src={user_pic} alt="profile_picture" className={styles.profile_pic}></img>
                    <h1 className={styles.user_fullname}>Brandon</h1>
                    
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
                            <h2>GingaNinja</h2>
                            <h2>brandon@email.com</h2>
                            <h2>March 28, 1999</h2>
                            <br></br>
                            <h2>September 8, 2022</h2>
                            <h2>88</h2>
                            <h2>Orthodox</h2>
                        </div>

                    </div>
                </div>

                {/*Buttons we might not actually need*/}
                <button>Update my info</button>
                <button>Change my password</button>
                
            </div>               
        )
    }
}

export default ProfileBox