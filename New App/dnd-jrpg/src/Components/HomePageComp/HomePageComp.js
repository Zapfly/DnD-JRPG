import React, { useState } from 'react';
// import './homepagecomp.module.css';
// import { AppContext } from '../../AppContext';

import UserLoginComp from '../UserAuth/UserLoginComp.js';
import UserRegisterComp from '../UserAuth/UserRegisterComp.js';
import AuthOptionsComp from '../UserAuth/AuthOptionsComp.js';


const HomePageComp = () => {
  const [userAuthDisplay, setUserAuthDisplay] = useState(null);

  // const appContext = React.useContext(AppContext);
  
  const stateHandler = (data) => {
    setUserAuthDisplay(data);
  }

  const authDisplay = () => {
    if (userAuthDisplay === "login") {
      return <UserLoginComp
      stateHandler={stateHandler}/>;
    } if (userAuthDisplay === "register") {
      return <UserRegisterComp
      stateHandler={stateHandler}/>;
    } else return <AuthOptionsComp
      stateHandler={stateHandler}/>;
  }
  

  return (
    <div className="main-container">
      <div className="app-header-container">
        <h1 className="app-header">Monster Dungeon</h1>
      </div>
      {authDisplay()}
      <div className="monster-dungeon-sales-pitch">
        Play Monster Dungeon It's Fun
      </div>
    </div>
  );
}

export default HomePageComp;