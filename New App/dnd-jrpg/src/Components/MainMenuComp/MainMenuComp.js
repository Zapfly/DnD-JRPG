import React, { useState } from 'react';
import { AppContext } from '../../AppContext';

import HeroCreationComp from '../HeroCreationComp/HeroCreationComp.js';

const MainMenuComp = (props) => {
    const [creator, setCreator] = useState(null);

    const appContext = React.useContext(AppContext);
    const heroCreator = () => {
        if (creator != null) {
            return < HeroCreationComp
            setCreator={setCreator}/>
        } return null;
    }
    const currentHero = () => {
        if (appContext.currentHeroData) {
            return appContext.currentHeroData.heroname
        } else {
            return "This user has no saved heroes"
        }
    }
    const continueHandler = async() => {
        let promise = new Promise((resolve, reject) => {
            resolve(appContext.arenaSetupFunc())
        });
        await promise;
        props.setCurrentPage("combat")
    }

    return (
        <div className="main-menu-container">
            <div>Current Hero:</div>
            <div>{currentHero()}</div>
            <button onClick={() => continueHandler()}>Continue</button>
            <button onClick={() => setCreator("newHero")}>New Hero</button>
            {heroCreator()}
            {/*remove the following button for production - dev use only */}
            <button onClick={() => appContext.setupFunc()}>Create Levels in Database</button>
        </div>
    )
}

export default MainMenuComp;