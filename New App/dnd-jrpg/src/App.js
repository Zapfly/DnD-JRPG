import React, { useState, useEffect } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import HeroComp from './Components/HeroComp.js';
import MonsterComp from './Components/MonsterComp.js';
import { Arena } from './scripts/combat.js';
import Herc from './images/Herccolored.png';
import Gobo from './images/250px-Chuffy_Lickwound.jpg';


const arena = new Arena()
arena.createHero("Hercules", 30, 20, Herc)
arena.createMonster("Boblin", 2, 20, Gobo)
arena.createMonster("Boblin", 2, 20, Gobo)
arena.createMonster("Boblin", 2, 20, Gobo)
arena.createMonster("Boblin", 2, 20, Gobo)
arena.createMonster("Boblin", 2, 20, Gobo)
arena.createMonster("Boblin", 2, 20, Gobo)

const App = () => {
  const [selectedMonster, setSelectedMonster] = useState(null)

  const monsters = arena.monsters.map((monster, i) => {
    return <MonsterComp
      monsterInfo={monster}
      key={monster.key}
      index={i}
      selectedMonster={selectedMonster}
      setSelectedMonster={setSelectedMonster}
      monsters={arena.monsters}
    />
  })

  const attack = () => {
    console.log(selectedMonster)
    arena.attack(selectedMonster)
    console.log(selectedMonster.hp)
    // Combat Log

  }

  useEffect(() => {

  }, [])

  return (
    <div className="container-fluid text-center" fluid style={{ height: "100vh" }}>
      <div className="row header border border-secondary justify-content-center" style={{ height: "10vh" }}>
        <h1 className="font-weight-bold my-auto">Monster Dungeon</h1>
      </div>
      <div className="row battle-field" style={{ height: "60vh" }}>
        <div className="container-fluid col-md-6 col-sm-12 player-side p-0 m-0 my-auto">
          <div className="row m-0 p-0 justify-content-center text-center">
            < HeroComp
              heroInfo={arena.combatants[0]}
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