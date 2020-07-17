import React, { useState } from 'react';
import App from './App.js';

import { Arena } from './scripts/combat.js';

import Herc from './images/Herccolored.png';
import Gobo from './images/250px-Chuffy_Lickwound.jpg';
import CombatComp from './Components/CombatComp/CombatComp.js';

export const AppContext = React.createContext();

const arena = new Arena();
// let combatLog = [];
const levels = 
    { 
        level1: [
            {
                name:'Boblin 0',
                atk: 2,
                hp: 40,
                sprite: Gobo
            },{
                name:'Boblin 1',
                atk: 2,
                hp: 40,
                sprite: Gobo
            },{
                name:'Boblin 2',
                atk: 2,
                hp: 40,
                sprite: Gobo
            },{
                name:'Boblin 3',
                atk: 2,
                hp: 40,
                sprite: Gobo
            },
            {
                name:'Boblin 4',
                atk: 2,
                hp: 40,
                sprite: Gobo
            },
            {
                name:'Boblin 5',
                atk: 2,
                hp: 40,
                sprite: Gobo
            },
        ],
        level2: [

        ]
    }


export const ContextProvider = (props) => {
    const [selectedMonster, setSelectedMonster] = useState(null);
    const [attackMessage, setAttackMessage] = useState("");

    const [initFetch, setInitFetch] = useState(false);
    const [currentLevel, setCurrentLevel] = useState(levels.level1);
    const [combatLog, setCombatLog] = useState([]);

    if (initFetch === false) {
        arena.monsters = [];
        arena.heroes = [];        
        // combatLog = [];
        arena.createHero("Hercules", 30, 40, Herc);        
        currentLevel.forEach(i => {
            arena.createMonster(i.name, i.atk, i.hp, i.sprite)
        })
        setInitFetch(true);       
    }

    const addToLog = (msg) => {
        // combatLog.push(msg);
        setCombatLog([...combatLog, ...msg])
    }

    const deleteCombatants = () => {
        arena.combatants = [];
    }

    const specifyLevel = (lvl) => {
        // arena.monsters = [...lvl];
        setCurrentLevel(lvl);
        setInitFetch(false);
    }

    return (
        <AppContext.Provider
            value={{
                arena,
                combatLog,
                selectedMonster,
                setSelectedMonster,
                attackMessage,
                setAttackMessage,
                currentLevel,
                setCurrentLevel,
                addToLog,
                deleteCombatants,
            }}>
                {props.children}
        </AppContext.Provider>
    )
}