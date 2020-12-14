import React, { useState } from 'react';
// import './homepagecomp.module.css';

import UserLoginComp from '../UserAuth/UserLoginComp.js';
import UserRegisterComp from '../UserAuth/UserRegisterComp.js';
import AuthOptionsComp from '../UserAuth/AuthOptionsComp.js';


const HomePageComp = (props) => {
  const [userAuthDisplay, setUserAuthDisplay] = useState(null);
  
  const displayStateHandler = (displayName) => {
    setUserAuthDisplay(displayName);
  }

  const authDisplay = () => {
    if (userAuthDisplay === "login") {
      return <UserLoginComp
      displayStateHandler={displayStateHandler}
      pageStateHandler={props.pageStateHandler}/>;
    } if (userAuthDisplay === "register") {
      return <UserRegisterComp
      displayStateHandler={displayStateHandler}
      pageStateHandler={props.pageStateHandler}/>;
    } else return <AuthOptionsComp
      displayStateHandler={displayStateHandler}/>;
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