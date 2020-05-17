import React from 'react';
import { AppContext } from '../AppContext';

const MonsterComp = (props) => {
    const appContext = React.useContext(AppContext)

    const name = props.monsterInfo.name;
    const healthbar = 200;
    const currentHp = (props.monsterInfo.maxHp / props.monsterInfo.hp) * healthbar;

    const handleClick = () => {
        appContext.setSelectedMonster(props.monsterInfo);
    }

    return (
        <div className="monster container col-sm-6 col-md-4 text-center justify-content-center m-0 p-2" onClick={handleClick}>
            <div className={`container p-2 border border-secondary ` + (props.monsterInfo === appContext.selectedMonster ? "selected" : null)}>
                <p className="font-weight-bold">{name}</p>
                <img alt="boblin the goblin" className="img-responsive" src={props.monsterInfo.sprite} height={150} style={{ transform: "scaleX(-1)" }} />
                <div className="container" style={{ width: `${healthbar}px` }}>
                    <div style={{ width: `${currentHp}px` }}></div>
                </div>
            </div>
        </div>
    )
}

export default MonsterComp;