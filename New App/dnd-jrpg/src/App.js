import React, {useState, useEffect} from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import HeroComp from './Components/HeroComp.js';
import MonsterComp from './Components/MonsterComp.js';
import { Arena } from './scripts/combat.js';
import Herc from './images/Herccolored.png';
import Gobo from './images/250px-Chuffy_Lickwound.jpg';

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Card from 'react-bootstrap/Card';


const arena = new Arena()    
arena.createHero("Hercules", 30, 20, Herc)
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
    <Container fluid style={{ height: "100vh" }}>
      <Row style={{height: "10%"}}>
        <Col className="text-center" style={{fontSize: "6vh", fontWeight: "bold" }}>Monster Dungeon</Col>
      </Row>
      <Row className="battle-field justify-content-center" style={{height: "60%"}}>
        <Col md={5} className="player-side">
          < HeroComp 
          heroInfo = {arena.combatants[0]}
          heroSprite = {arena.combatants[0].sprite}
          />
        </Col>
        <Col md={5} className="monster-side">
          <Row>
            {monsters}
          </Row>
        </Col>
      </Row>
      <Row className="interface text-center justify-content-center" style={{height: "28%"}}>
        <Col lg={3} className="commands">
          <Container style={{height: "98%"}}>
            <button onClick= {attack}>Attack</button>
          </Container>
        </Col>
        <Col lg={8} className="combat-log">
          Combat Log
        </Col>
      </Row>
    </Container>




  );
}

export default App;


// render() {
//   const cityList = this.context.cities.cities.map((city, i) => {
//       return <CityCard
//           key={i}
//           city={city}
//           index={i}
//           handleDelete={this.props.handleDelete}
//           handleWarning={this.props.handleWarning}
//           cityChecker={this.props.cityChecker}
//           cityInfoSelector={this.props.cityInfoSelector}
//       />
//   })

//   <input
//   type="button"
//   value="Moved In"
//   className="city-button city-card-elements"
//   onClick={() => this.handleMovedIn(this.props.index)} />