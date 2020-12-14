import React, {useState} from 'react';
import './App.css';
import { ContextProvider } from './AppContext';

import CombatComp from './Components/CombatComp/CombatComp.js';
import HomePageComp from './Components/HomePageComp/HomePageComp.js';
import MainMenuComp from './Components/MainMenuComp/MainMenuComp.js';

const App = () => {
  const [currentPage, setCurrentPage] = useState(null)

  const pageStateHandler = (page) => {
    setCurrentPage(page);
  }

  const pageDisplay = () => {
    if (currentPage === "combat") {
      return <CombatComp
      pageStateHandler={pageStateHandler}/>;
    } if (currentPage === "menu") {
      return <MainMenuComp
      pageStateHandler={pageStateHandler}/>;
    } else return <HomePageComp
      pageStateHandler={pageStateHandler}/>;
  }


  // const pages = {
  //   homePage: <HomePageComp />,
  //   // mainMenu: <MainMenuComp />,
  //   combat: <CombatComp />
  // }
  return (
    <ContextProvider>  
      {pageDisplay()}
    </ContextProvider>
  );
}

export default App;