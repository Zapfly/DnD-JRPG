import React from 'react';
import './App.css';
import { ContextProvider } from './AppContext';

import HomePageComp from './Components/HomePageComp/HomePageComp.js';

const App = () => {
  return (
    <ContextProvider>  
      <HomePageComp />
    </ContextProvider>
  );
}

export default App;