import React, { useState } from 'react';
import App from './App.js';

import { Arena } from './scripts/combat.js';

import Herc from './images/Herccolored.png';
import Gobo from './images/250px-Chuffy_Lickwound.jpg';

export const AppContext = React.createContext();

const arena = new Arena();
const combatLog = [];

export const ContextProvider = () => {
    const [selectedMonster, setSelectedMonster] = useState(null);
    const [attackMessage, setAttackMessage] = useState("");

    const [initFetch, setInitFetch] = useState(false);

    if (initFetch === false) {
        arena.createHero("Hercules", 30, 40, Herc);
        for (let i = 0; i < 6; i++) {
            arena.createMonster(`Boblin ${i}`, 2, 40, Gobo);
        }
        setInitFetch(true);
    }

    const addToLog = (msg) => {
        combatLog.push(msg);
    }

    return (
        <AppContext.Provider
            value={{
                arena: arena,
                combatLog: combatLog,
                selectedMonster: selectedMonster,
                setSelectedMonster: setSelectedMonster,
                attackMessage: attackMessage,
                setAttackMessage: setAttackMessage,
                addToLog: addToLog
            }}>
            <App />
        </AppContext.Provider>
    )
}