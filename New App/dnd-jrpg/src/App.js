import React from 'react';
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Card from 'react-bootstrap/Card';



const App = () => {
  return (
    <Col lg={12} style={{ height: "10vh", border: "solid 1px black" }}>Test</Col>

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
