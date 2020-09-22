import React, {useState} from 'react';
import './App.css';
import { ContextProvider } from './AppContext';

import CombatComp from './Components/CombatComp/CombatComp.js'
import HomePageComp from './Components/HomePageComp/HomePageComp.js';

const App = () => {
  const [currentPage, setCurrentPage] = useState(<HomePageComp />)

  // const stateHandler = (data) => {
  //   setUserAuthDisplay(data);
  // }

  // const pageDisplay = () => {
  //   if (userAuthDisplay === "combat") {
  //     return <CombatComp
  //     stateHandler={stateHandler}/>;
  //   } if (userAuthDisplay === "menu") {
  //     return <MainMenuComp
  //     stateHandler={stateHandler}/>;
  //   } else return <HomePageComp
  //     stateHandler={stateHandler}/>;
  // }


  const pages = {
    homePage: <HomePageComp />,
    // mainMenu: <MainMenuComp />,
    combat: <CombatComp />
  }
  return (
    <ContextProvider>  
      {currentPage}
    </ContextProvider>
  );
}

export default App;