import React from 'react';
import './App.css';
import { AppContext } from './AppContext';

import HeroComp from './Components/HeroComp/HeroComp.js';
import MonsterComp from './Components/MonsterComp/MonsterComp.js';


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
    if (appContext.selectedMonster) {
      if (appContext.selectedMonster.hp > 0) {
        let currentAttacker = arena.combatants[0]
        let currentVictim = appContext.selectedMonster
        arena.attack(currentVictim)
        appContext.addToLog(`${currentAttacker.name} attacked ${currentVictim.name} for ${currentAttacker.atk} damage!`)
        appContext.setSelectedMonster(null)
        arena.cycleTurn()
        while (arena.victoryCheck() === "contested" && arena.currentTurn > 0) {
          let currentAttacker = arena.combatants[arena.currentTurn];
          let currentVictim = arena.combatants[0];
          // I think setTimeout would go here?
          arena.attack(currentVictim);
          appContext.addToLog(`${currentAttacker.name} attacked ${currentVictim.name} for ${currentAttacker.atk} damage!`)
          arena.cycleTurn()
        }
        if (arena.victoryCheck() === "contested" && arena.currentTurn === 0) {
          return appContext.setAttackMessage(`It is your turn, ${heroName}!`);
        } return appContext.setAttackMessage(arena.victoryCheck());
      } return appContext.setAttackMessage("The selected monster is dead and cannot be attacked");
    }
    else return
  }

  return (
    <div className="main-app">
      <div className="app-header-container">
        <h1 className="app-header">Monster Dungeon</h1>
      </div>
      <div className="battle-field">
        <div className="hero-container">
          < HeroComp
            heroInfo={appContext.arena.combatants[0]}
          />
        </div>
        <div className="monster-container">
            {monsters}
        </div>
      </div>
      <div id="userDisplay" >
        <div id="commands">
              <button className="my-auto" onClick={attack}>Attack</button>
              <div className="attack-message">
                {appContext.attackMessage}
              </div>
        </div>
            <div id="combatLogContainer">
              <span id="combatLogHeader" >Combat Log</span>
              <div id="combatLog" >
                {combatLog}
              </div>
            </div>
      </div>
    </div>
  );
}

export default App;