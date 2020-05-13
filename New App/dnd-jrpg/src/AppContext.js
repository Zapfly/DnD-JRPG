import React, { useState } from 'react';
import App from './App.js';

export const AppContext = React.createContext();

export const ContextProvider = () => {
    // App.js State
    const [selectedMonster, setSelectedMonster] = useState(null)

    return (
        <AppContext.Provider
        value={{
            selectedMonster: selectedMonster,
            setSelectedMonster: setSelectedMonster
        }}>
            <App />
        </AppContext.Provider>
    )
}