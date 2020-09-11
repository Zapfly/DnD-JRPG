import React from 'react';
import { AppContext } from '../../AppContext';

const AuthOptionsComp = (props) => {
    const appContext = React.useContext(AppContext)

    return (
        <div className="user-auth-container">
          <button className="login-button" onClick={() => props.stateHandler("login")}>Login</button>
          <button className="new-user-button" onClick={() => props.stateHandler("register")}>New User</button>
        </div>
    )
}

export default AuthOptionsComp;