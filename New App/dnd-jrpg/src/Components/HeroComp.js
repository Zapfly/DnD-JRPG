import React from 'react';
// import Herc from '../images/Herccolored.png';

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Card from 'react-bootstrap/Card';
import Image from 'react-bootstrap/Image';

const HeroComp = (props) => {
    const name = props.heroInfo.name
    const healthbar = 200
    const currentHp = (props.heroInfo.maxHp / props.heroInfo.hp) * healthbar
    return (
        <div className="hero container col-sm-6 text-center justify-content-center m-0 p-2">
            <div className="container p-2 border border-secondary">
                <p className="font-weight-bold">{name}</p>
                <img className="img-responsive" src={props.heroInfo.sprite} height={300} ></img>
                <div className="container" style={{ width: `${healthbar}px` }}>
                    <div style={{ width: `${currentHp}px` }}></div>
                </div>
            </div>
        </div>
    )
}

export default HeroComp;