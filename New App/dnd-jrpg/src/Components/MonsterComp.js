import React from 'react';

const MonsterComp = (props) => {

    // const handleClick = () => {
    //     console.log(props.selectedMonster)
    //     props.setSelectedMonster(props.monsters[props.index])
    //     console.log(props.selectedMonster)

    // }

    const name = props.monsterInfo.name;
    const healthbar = 200;
    const currentHp = (props.monsterInfo.maxHp / props.monsterInfo.hp) * healthbar;

    return (
        <div className="monster container col-sm-6 col-md-4 text-center justify-content-center m-0 p-2" onClick={() => { props.setSelectedMonster(props.monsterInfo) }}>
            <div className={`container p-2 border border-secondary ` + (props.monsterInfo === props.selectedMonster ? "selected" : null)}>
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