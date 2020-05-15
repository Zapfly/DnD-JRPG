import React, { useState } from 'react';
import App from './App.js';

import { Arena } from './scripts/combat.js';

import Herc from './images/Herccolored.png';
import Gobo from './images/250px-Chuffy_Lickwound.jpg';

export const AppContext = React.createContext();

const arena = new Arena();

export const ContextProvider = () => {
    const [selectedMonster, setSelectedMonster] = useState(null);
    const [initFetch, setInitFetch] = useState(false);

    if (initFetch === false) {
        arena.createHero("Hercules", 30, 20, Herc);
        for (let i = 0; i < 6; i++) {
            arena.createMonster("Boblin", 2, 40, Gobo);
        }
        setInitFetch(true);
    }

    return (
        <AppContext.Provider
            value={{
                arena: arena,
                selectedMonster: selectedMonster,
                setSelectedMonster: setSelectedMonster
            }}>
            <App />
        </AppContext.Provider>
    )
}