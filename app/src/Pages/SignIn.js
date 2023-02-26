import React from "react"

import "../CSS/General.css"
import "../CSS/Box.css"
import "../CSS/SignIn.css"

class SignIn extends React.Component {
    render() {
        return (
            <div className="main_container">
                <div className="sign_in_container">
                    <div className="container">
                        <h1>Sign In</h1>
                        <form className="sign_in_form">
                            <label for="userName" className="sign_in_label">User Name:</label>
                            <input type="text" id="userName" className="sign_in_input"></input>
                            <br></br>
                            <label for="passWord" className="sign_in_label">Password:</label>
                            <input type="password" id="password"className="sign_in_input"></input>
                            <br></br>
                            <button type="submit">Sign In</button>
                        </form>
                    </div>
                </div>
            </div>
        )
    }
}

export default SignIn