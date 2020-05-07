import React from 'react';
// import Herc from '../images/Herccolored.png';

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Card from 'react-bootstrap/Card';
import Image from 'react-bootstrap/Image';

const HeroComp = (props) => {
    console.log(props.heroSprite)
    const name = props.heroInfo.name
    const healthbar = props.heroInfo.hp 
    return( 
        <Container className="text-center h-100">
            <div>{name}</div>
            <Image className="img-responsive" src={props.heroInfo.sprite} height={300} ></Image> 
            <div className= "healthbar" style={{width: `${healthbar}px`}}>
            <div></div>
            </div>      
        </Container>
    )

}

export default HeroComp;