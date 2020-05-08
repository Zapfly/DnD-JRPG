import React from 'react';
// import Herc from '../images/Herccolored.png';

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Card from 'react-bootstrap/Card';
import Image from 'react-bootstrap/Image';

const MonsterComp = (props) => {

    // const handleClick = () => {
    //     console.log(props.selectedMonster)
    //     props.setSelectedMonster(props.monsters[props.index])
    //     console.log(props.selectedMonster)

    // }
    const name = props.monsterInfo.name
    const healthbar = 200
    const currentHp = (props.monsterInfo.maxHp / props.monsterInfo.hp) * healthbar
    return (
        <Col md={5} className="text-center" onClick={() => {
            props.setSelectedMonster(props.monsterInfo)
            console.log(props.monsterInfo)
        }}>
            <div>{name}</div>
            <Row className="justify-content-center">
                <Image className="img-responsive" src={props.monsterInfo.sprite} height={150} style = {{transform: "scaleX(-1)"}} ></Image>
            </Row>
            <Row className="healthbar justify-content-center">
                <div style={{ width: `${healthbar}px` }}>
                    <div style={{ width: `${currentHp}px` }}></div>
                </div>
            </Row>
        </Col>
    )
}

export default MonsterComp;



// () => props.setSelectedMonster(props.selectedMonster = props.monsters[props.index])