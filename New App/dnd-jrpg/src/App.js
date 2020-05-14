import React, { useState, useEffect } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { AppContext } from './AppContext.js';

import HeroComp from './Components/HeroComp.js';
import MonsterComp from './Components/MonsterComp.js';
// import { Arena } from './scripts/combat.js';



const App = () => {

  const [stateToggle, setStateToggle] = useState(true)
  const toggle = () =>{setStateToggle(!stateToggle)}

  const appContext = React.useContext(AppContext)






  const monsters = appContext.arena.monsters.map((monster, i) => {

    return <MonsterComp
      toggle = {toggle}
      monsterInfo={monster}
      key={monster.key}
      index={i}
      // selectedMonster={appContext.selectedMonster}
      // setSelectedMonster={appContext.setSelectedMonster}
      monsters={appContext.arena.monsters}
    />
  })


  const attack = () => {
    console.log(appContext.arena.currentMonster)
    appContext.arena.attack(appContext.arena.currentMonster)
    console.log(appContext.arena.currentMonster.hp)
    // Combat Log


  }


  useEffect(() => {
    

  }, [])
  return (
    <div className="container-fluid text-center" style={{ height: "100vh" }}>
      <div className="row header border border-secondary justify-content-center" style={{ height: "10vh" }}>
        <h1 className="font-weight-bold my-auto">Monster Dungeon</h1>
      </div>
      <div className="row battle-field" style={{ height: "60vh" }}>
        <div className="container-fluid col-md-6 col-sm-12 player-side p-0 m-0 my-auto">
          <div className="row m-0 p-0 justify-content-center text-center">
            < HeroComp
              heroInfo={appContext.arena.combatants[0]}
            />
          </div>
        </div>
        <div className="container col-md-6 col-sm-12 monster-side p-0 m-0 my-auto">
          <div className="row p-0 m-0 justify-content-center text-center">
            {monsters}
          </div>
        </div>
      </div>
      <div className="row interface border border-secondary" style={{ height: "30vh" }}>
        <div className="container-fluid col-md-5 my-auto">
          <div className="row m-2 p-0 justify-content-center text-center">
            <div className="commands container-fluid border border-secondary my-auto"  style={{ height: "25vh" }}>
              <button className="my-auto" onClick={attack}>Attack</button>
            </div>
          </div>
        </div>
        <div className="container-fluid col-md-7 text-center my-auto">
          <div className="row m-2 p-0 justify-content-center text-center">
            <div className="combat-log container-fluid my-auto border border-secondary" style={{ height: "25vh" }}>
              Combat Log
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;