import React, {useState} from 'react';
import { AppContext } from '../../AppContext';
// import styles from './userauth.module.css';

import { fetchFunc } from '../FetchComp/FetchComp.js';

const UserRegisterComp = (props) => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const appContext = React.useContext(AppContext);

    const handleSubmit = async() => {
        let res = await fetchFunc(`${appContext.url}/register`, 'POST', {"username": `${username}`, "password": `${password}`})
        console.log(res)
        if (res['message'] !== "Something went wrong.") {
            props.displayStateHandler('login')
            return res
        } else {
            return res
        }
    }

    return (
        <div className="register-container">
            <label>Username:</label>
            <input className="username-input" value={username} onChange={e => setUsername(e.target.value)}></input>
            <label>Password:</label>
            <input className="password-input" type="password" value={password} onChange={e => setPassword(e.target.value)}></input>
            <button onClick={handleSubmit}>Create Account</button>
            <button className="back-button" onClick={() => props.displayStateHandler(null)}>Go Back</button>
        </div>
    )
}

export default UserRegisterComp;