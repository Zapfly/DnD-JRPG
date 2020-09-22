import React, { useState, useEffect } from 'react';
import App from './App.js';

import { Arena } from './scripts/combat.js';
import { useFetch, useFetchWithAuth } from './Components/FetchComp/FetchComp.js';

import Herc from './images/Herccolored.png';
import Gobo from './images/250px-Chuffy_Lickwound.jpg';
import CombatComp from './Components/CombatComp/CombatComp.js';

export const AppContext = React.createContext();

const arena = new Arena();


export const ContextProvider = (props) => {
    const [selectedMonster, setSelectedMonster] = useState(null);
    const [attackMessage, setAttackMessage] = useState("");

    const [initFetch, setInitFetch] = useState(false);
    const [levelList, setLevelList] = useState(null);
    const [currentLevel, setCurrentLevel] = useState(null);
    const [combatLog, setCombatLog] = useState([]);
    const [url, setUrl] = useState("http://localhost:5000");

    // useFetchWithAuth()

    // useEffect(async() => {
    //     const response = await fetch("http://localhost:5000/levels", {
    //         method: 'GET',
    //         headers: {
    //             Authorization: `JWT ${token}`
    //         }
    //     });
    //     const data = await response.json();
    //     const [levels] = data.levels;
    //     setLevelList(levels);
    //     setCurrentLevel(levels[0]); //this code will have to change when current user's current level is stored in database
    // }, []);

    // if (initFetch === false) {
    //     arena.monsters = [];
    //     arena.heroes = [];        
    //     arena.createHero("Hercules", 30, 40, Herc);        
    //     currentLevel.forEach(i => {
    //         arena.createMonster(i.name, i.atk, i.hp, i.sprite)
    //     })
    //     setInitFetch(true);       
    // }

    const addToLog = (msg) => {
        setCombatLog([...combatLog, ...msg])
    }

    const deleteCombatants = () => {
        arena.combatants = [];
    }

    // const specifyLevel = (lvl) => {
    //     // arena.monsters = [...lvl];
    //     setCurrentLevel(lvl);
    //     setInitFetch(false);
    // }

    return (
        <AppContext.Provider
            value={{
                arena,
                combatLog,
                selectedMonster,
                setSelectedMonster,
                attackMessage,
                setAttackMessage,
                levelList,
                setLevelList,
                currentLevel,
                setCurrentLevel,
                url,
                setUrl,
                addToLog,
                deleteCombatants,
            }}>
                {props.children}
        </AppContext.Provider>
    )
}