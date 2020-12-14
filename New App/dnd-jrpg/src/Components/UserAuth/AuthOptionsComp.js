import React from 'react';

const AuthOptionsComp = (props) => {

    return (
        <div className="user-auth-container">
          <button className="login-button" onClick={() => props.displayStateHandler("login")}>Login</button>
          <button className="new-user-button" onClick={() => props.displayStateHandler("register")}>New User</button>
        </div>
    )
}

export default AuthOptionsComp;