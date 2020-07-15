import React from 'react';
import { AppContext } from '../../AppContext';
import styles from './monstercomp.module.css';

const MonsterComp = (props) => {
    const appContext = React.useContext(AppContext)

    const name = props.monsterInfo.name;
    const currentHp = (props.monsterInfo.hp / props.monsterInfo.maxHp) * 100;

    const handleClick = () => {
        appContext.setSelectedMonster(props.monsterInfo);
    }

    return (
        <div id={`monster ${props.index}`}  role="monster" className={ (props.monsterInfo === appContext.selectedMonster ? "monster selected" : "monster")} onClick={handleClick}>
                <p>{name}</p>
                <img alt="boblin the goblin" className={styles.monsterImg} src={props.monsterInfo.sprite}  />
                <div className={styles.maxHealthbar} >
                    <div id={`HPBar ${props.index}`} className={styles.currentHp} style={{ width: `${currentHp}%`}}></div>
                </div>
        </div>
    )
}

export default MonsterComp;