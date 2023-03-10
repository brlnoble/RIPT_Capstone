import React from "react";

import ListBox from "../Components/ListBox"

import "../CSS/General.css"
import "../CSS/Home.css"

//The information to be displayed in the boxes
const profile = [{text: 'Update personal information'}, {text: 'Change your settings'}, {text: 'View your average stats'}]
const sessions = [{text: 'View all your past training sessions'}, {text: 'Get an extensive breakdown of all your metrics'}]
const progress = [{text: 'Check out trends in your recent sessions'}, {text: 'Identify key areas to focus your efforts on'}]

//Need to link to the API
const user_fullname = 'Brandon'

class Home extends React.Component {
    render() {
        return(
            <div className='main_container'>

                {/*Little greeting, customize for user's name*/}
                <div className='greeting'>
                    <h1>Welcome {user_fullname}, let's get <span className='title'>R.I.P.T.</span></h1>
                </div>

                {/*Information boxes with links to pages*/}
                <div className='boxes'>
                    <ListBox 
                    title_text="My Profile" 
                    show_text={profile}
                    button_text="Go to profile"
                    redirect="/profile">
                    </ListBox>

                    <ListBox 
                    title_text="Training Sessions" 
                    show_text={sessions}
                    button_text="View sessions"
                    redirect="/sessions">
                    </ListBox>

                    <ListBox 
                    title_text="Track My Progress" 
                    show_text={progress}
                    button_text="Check my progress"
                    redirect="/progress">
                    </ListBox>
                </div>

            </div>
        )
    }
}

export default Home