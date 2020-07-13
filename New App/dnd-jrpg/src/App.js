import React from 'react';
import './App.css';
import { ContextProvider } from './AppContext';

import CombatComp from './Components/CombatComp/CombatComp.js';

const App = () => {
  return (

    /*<ContextProvider>*/
      
      <CombatComp />
      /* </ContextProvider> */
  );
}

export default App;