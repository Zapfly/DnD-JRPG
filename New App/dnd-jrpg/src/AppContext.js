import React, { useState} from 'react';
// import App from './App.js';

import { Arena } from './scripts/combat.js';
import { fetchFuncAuth, fetchPostWithAuth } from './Components/FetchComp/FetchComp.js';

import Herc from './images/Herccolored.png';
import Gobo from './images/250px-Chuffy_Lickwound.jpg';
// import CombatComp from './Components/CombatComp/CombatComp.js';

export const AppContext = React.createContext();

const arena = new Arena();

export const ContextProvider = (props) => {
    const [selectedMonster, setSelectedMonster] = useState(null);
    const [attackMessage, setAttackMessage] = useState("");

    // const [initFetch, setInitFetch] = useState(false);
    const [currentLevelName, setCurrentLevelName] = useState("");
    const [currentLevelMonsters, setCurrentLevelMonsters] = useState(null);
    const [currentHeroData, setCurrentHeroData] = useState(null);
    const [combatLog, setCombatLog] = useState([]);
    const [url, setUrl] = useState("http://localhost:5000");
    const [token, setToken] = useState(null);
    const [refreshToken, setRefreshToken] = useState(null);

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
    const arenaSetupFunc = () => {
        arena.monsters = [];
        arena.heroes = [];
        arena.createHero(currentHeroData.heroname, currentHeroData.atk, currentHeroData.hp, Herc)
        currentLevelMonsters.forEach(i => {
            arena.createMonster(i.monstername, i.atk, i.hp, Gobo)
        })
        return "Setup Complete";
    }

    const setupFunc = async () => {
        await fetchPostWithAuth(`${url}/level`, 'POST', token, {"levelname": "First Level"})
        await fetchPostWithAuth(`${url}/monster`, 'POST', token, {"monstername": "Boblin1", "atk": 50, "hp": 60, "max_hp": 60, "sprite": "string", "levelname": "First Level"})
        await fetchPostWithAuth(`${url}/monster`, 'POST', token, {"monstername": "Boblin2", "atk": 50, "hp": 60, "max_hp": 60, "sprite": "string", "levelname": "First Level"})
    }

    const getCurrentLevel = async (tok) => {
        const response = await fetchFuncAuth(`${url}/level`, 'GET', tok, {"levelname": "First Level"})
        setCurrentLevelName(response.levelname)
        setCurrentLevelMonsters(response.monsters)
    }

    const getHeroes = async (tok) => {
        const response = await fetch(`${url}/heroes`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${tok}`
            },
        });
        let heroData = response.json()
        heroData.then((result) => {
            if (result.heroes[0]) {
                setCurrentHeroData(result.heroes[0])
            }
        })
    }

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
                currentLevelName,
                setCurrentLevelName,
                currentLevelMonsters,
                setCurrentLevelMonsters,
                currentHeroData,
                setCurrentHeroData,
                url,
                setUrl,
                arenaSetupFunc,
                setupFunc,
                token,
                setToken,
                refreshToken,
                setRefreshToken,
                getCurrentLevel,
                getHeroes,
                addToLog,
                deleteCombatants,
            }}>
                {props.children}
        </AppContext.Provider>
    )
}