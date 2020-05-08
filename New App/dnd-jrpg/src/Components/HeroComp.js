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
        <Container className="text-center">
            <div>{name}</div>
            <Row className="justify-content-center">
                <Image className="img-responsive" src={props.heroInfo.sprite} height={300} ></Image>
            </Row>
            <Row className="healthbar justify-content-center">
                <div style={{ width: `${healthbar}px` }}>
                    <div style={{ width: `${currentHp}px` }}></div>
                </div>
            </Row>
        </Container>
    )
}

export default HeroComp;