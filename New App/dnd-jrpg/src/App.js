import React from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { AppContext } from './AppContext.js';

import HeroComp from './Components/HeroComp.js';
import MonsterComp from './Components/MonsterComp.js';


const App = () => {
  const appContext = React.useContext(AppContext);

  const monsters = appContext.arena.monsters.map((monster, i) => {
    return <MonsterComp
      monsterInfo={monster}
      key={monster.key}
      index={i}
      monsters={appContext.arena.monsters}
    />
  })

  const combatLog = appContext.combatLog.map((message, i) => {
    return <div key={i}>{`Log ${i}: ${message}`}</div>
  })

  const attack = () => {
    const arena = appContext.arena;
    const heroName = arena.combatants[0].name;
    console.log(arena.combatants)
    if (appContext.selectedMonster.hp > 0) {
      let currentAttacker = arena.combatants[0]
      let currentVictim = appContext.selectedMonster
      arena.attack(currentVictim)
      appContext.addToLog(`${currentAttacker.name} attacked ${currentVictim.name} for ${currentAttacker.atk} damage!`)
      appContext.setSelectedMonster(null) 
      arena.cycleTurn()
      while (arena.victoryCheck() === "contested" && arena.currentTurn > 0) {
        let currentAttacker = arena.combatants[arena.currentTurn]
        let currentVictim = arena.combatants[0]
        arena.attack(currentVictim)
        appContext.addToLog(`${currentAttacker.name} attacked ${currentVictim.name} for ${currentAttacker.atk} damage!`)
        arena.cycleTurn()
      }
      if (arena.victoryCheck() === "contested" && arena.currentTurn === 0) {
        return appContext.setAttackMessage(`It is your turn, ${heroName}!`);
      } return appContext.setAttackMessage(arena.victoryCheck());
    } return appContext.setAttackMessage("The selected monster is dead and cannot be attacked");
  }

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
            <div className="commands container-fluid border border-secondary my-auto" style={{ height: "25vh" }}>
              <button className="my-auto" onClick={attack}>Attack</button>
              <div className="attack-message">
                {appContext.attackMessage}
              </div>
            </div>
          </div>
        </div>
        <div className="container-fluid col-md-7 text-center my-auto">
          <div className="row m-2 p-0 justify-content-center text-center">
            <div className="combat-log-container container-fluid my-auto border border-secondary" style={{ height: "25vh" }}>
              <span className="combat-log-header container-fluid my-auto" style={{ height: "5vh" }}>Combat Log</span>
              <div className="combat-log overflow-auto" style={{ height: "20vh" }}>
                {combatLog}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;