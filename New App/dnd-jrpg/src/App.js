import React from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Card from 'react-bootstrap/Card';



const App = () => {

  
  return (
    <Container fluid style={{ height: "100vh" }}>
      <Row style={{height: "10%"}}>
        <Col className="text-center" style={{fontSize: "6vh", fontWeight: "bold" }}>Monster Dungeon</Col>
      </Row>
      <Row className="battle-field" style={{height: "60%"}}>
        <Col className="player-side">
          
        </Col>
        <Col className="monster-side"></Col>
      </Row>
      <Row className="interface text-center justify-content-center" style={{height: "28%"}}>
        <Col lg={3} className="commands">
          <Container style={{height: "98%"}}>
            <button>Attack</button>
          </Container>
        </Col>
        <Col lg={8} className="combat-log">
          Combat Log
        </Col>
      </Row>
    </Container>


    // <div className="container-fluid h-100">
    //   <div className="container-fluid col-xs-12 text-center border border-primary h-25">
    //     <div className="row text-center">
    //       Monster Dungeon
    //     </div>
    //   </div>

    //   <div className="battle-field">
    //     <div>left</div>
    //     <div>right</div>
    //   </div>


    //   <div className="row">
    //     <div className="col-md-6 col-xs-12 border border-primary text-left h-50">
    //       <div className="container col-md-6 border border-primary" >
    //       </div>
    //     </div>
    //     <div className="col-md-6 col-sm-12 border border-primary text-left">Test!</div>
    //   </div>
    // </div>


  );
}

export default App;
