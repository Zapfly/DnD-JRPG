import React from 'react';
import './combatcomp.css';
import { AppContext } from '../../AppContext';

import HeroComp from '../HeroComp/HeroComp.js';
import MonsterComp from '../MonsterComp/MonsterComp.js';


const CombatComp = () => {
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
    const [logEntry, givenAttr] = message
    return <div key={i} className={givenAttr} >{`Log ${i}: ${logEntry}`}</div>
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
        appContext.addToLog([`${currentAttacker.name} attacked ${currentVictim.name} for ${currentAttacker.atk} damage!`, 'hero-attack'])
        appContext.setSelectedMonster(null)
        arena.cycleTurn()
        while (arena.victoryCheck() === "contested" && arena.currentTurn > 0) {
          let currentAttacker = arena.combatants[arena.currentTurn];
          let currentVictim = arena.combatants[0];
          // I think setTimeout would go here?
          arena.attack(currentVictim);
          appContext.addToLog([`${currentAttacker.name} attacked ${currentVictim.name} for ${currentAttacker.atk} damage!`, 'monster-attack'])
          arena.cycleTurn()
        }
        if (arena.victoryCheck() === "contested" && arena.currentTurn === 0) {
          return appContext.addToLog([`It is your turn, ${heroName}!`, 'turn-message']);
        } return appContext.addToLog([arena.victoryCheck(), 'victory-check-message']);
      } return appContext.addToLog(["The selected monster is dead and cannot be attacked", "bad-selection"]);
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
        <div id="monsterContainer" className="monster-container" role='monsterContainer'>
            {monsters}
        </div>
      </div>
      <div id="userDisplay" >
        <div id="commands">
              <button className="my-auto" onClick={attack}>Attack</button>
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

export default CombatComp;