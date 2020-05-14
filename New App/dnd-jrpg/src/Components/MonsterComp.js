import React, { useState } from 'react';
import { AppContext } from '../AppContext.js';


const MonsterComp = (props) => {
    const [stateToggle, setStateToggle] = useState(true)
    const appContext = React.useContext(AppContext)
    let monsterClassName = () => {
        if (props.monsterInfo === appContext.arena.currentMonster) {
            return "container p-2 border border-secondary selected"
        } else {
            return "container p-2 border border-secondary not-selected"
        }
    }
    const handleClick = (e) => {
        // props.appHandleClick(e)
        // console.log(props.selectedMonster)
        // props.setSelectedMonster(props.monsters[props.index])
        // console.log(props.selectedMonster)

        // console.log(props.monsterInfo)

        appContext.arena.selectMonster(props.monsterInfo)
        // appContext.setSelectedMonster(arena.currentMonster)
        // appContext.selectedMonster(props.monsterInfo)
        // if (props.monsterInfo === appContext.arena.currentMonster) {
        //     monsterClassName = "selected"
        // } else {
        //     monsterClassName = "not-selected"
        // }
        // console.log(monsterClassName)
        setStateToggle(!stateToggle)
        props.toggle()
        console.log(appContext.arena.currentMonster.key)

    }





    const name = props.monsterInfo.name;
    const healthbar = 200;
    const currentHp = (props.monsterInfo.maxHp / props.monsterInfo.hp) * healthbar;

    return (
        <div className="monster container col-sm-6 col-md-4 text-center justify-content-center m-0 p-2" onClick={handleClick}>
            {/* <div className="monster container col-sm-6 col-md-4 text-center justify-content-center m-0 p-2" onClick={() => { appContext.arena.selectMonster(props.monsterInfo) }}> */}
            {/* <div className={monsterClassName}> */}
            <div className={`container p-2 border border-secondary ` + monsterClassName()}>
                <p className="font-weight-bold">{name}</p>
                <img className="img-responsive" src={props.monsterInfo.sprite} height={150} style={{ transform: "scaleX(-1)" }} />
                <div className="container" style={{ width: `${healthbar}px` }}>
                    <div style={{ width: `${currentHp}px` }}></div>
                </div>
            </div>
        </div>
    )
}

export default MonsterComp;

// const ListCard = (props) => (
//     <div className={`list-card ` + ((props.node === context.linkedList.current) ? "active-list-card" : null)}>
//         <span className="list-card-text">Subject: {props.node.subject}</span>
//         <span className="list-card-text">Amount: {props.node.amount}</span>
//     </div>
// );