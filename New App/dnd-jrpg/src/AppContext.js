import React, { useState } from 'react';
import App from './App.js';
import { Arena } from './scripts/combat.js';
import Herc from './images/Herccolored.png';
import Gobo from './images/250px-Chuffy_Lickwound.jpg';


export const AppContext = React.createContext();

export const ContextProvider = () => {
    const arena = new Arena()
    // App.js State
    const [selectedMonster, setSelectedMonster] = useState(null)

    arena.createHero("Hercules", 30, 20, Herc)
    arena.createMonster("Boblin", 2, 20, Gobo)
    arena.createMonster("Boblin", 2, 20, Gobo)
    arena.createMonster("Boblin", 2, 20, Gobo)
    arena.createMonster("Boblin", 2, 20, Gobo)
    arena.createMonster("Boblin", 2, 20, Gobo)
    arena.createMonster("Boblin", 2, 20, Gobo)
  

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