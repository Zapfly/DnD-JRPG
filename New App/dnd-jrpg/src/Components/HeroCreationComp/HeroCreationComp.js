import React, { useState } from 'react';
import { fetchPostWithAuth } from '../FetchComp/FetchComp.js';
import { AppContext } from '../../AppContext.js';

const HeroCreationComp = (props) => {
    const[name, setName] = useState(""); 
    
    const appContext = React.useContext(AppContext);

    const createHero = async() => {
        const res = await fetchPostWithAuth(
            `${appContext.url}/hero/${name}`, 
            'POST', 
            appContext.token, 
            {"atk": 30, "hp": 200, "max_hp": 200, "sprite": "string"}
        )
        props.setCreator(null)
        console.log(res['message'])
        return res['message']
    }

    return (
        <div className="hero-creation-container">
            <div>Hero Creation Area</div>
                <label>Name Your Hero:</label>
                <input className="name-input" value={name} onChange={e => setName(e.target.value)}></input>
            <button onClick={() => createHero()}>Create Hero</button>
        </div>
    )
}

export default HeroCreationComp;