import React, { useState } from 'react';
import App from './App.js';

import { Arena } from './scripts/combat.js';

export const AppContext = React.createContext();

export const ContextProvider = () => {
    const arena = new Arena()
    const [selectedMonster, setSelectedMonster] = useState(null)

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