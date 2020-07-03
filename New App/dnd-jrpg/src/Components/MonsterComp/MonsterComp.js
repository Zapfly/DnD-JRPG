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
        <div role="monster" className="monster" onClick={handleClick}>
            <div className={ (props.monsterInfo === appContext.selectedMonster ? "selected" : null)}>
                <p>{name}</p>
                <img alt="boblin the goblin" className={styles.monsterImg} src={props.monsterInfo.sprite}  />
                <div className={styles.maxHealthbar} >
                    <div className={styles.currentHp} style={{ width: `${currentHp}%`}}></div>
                </div>
            </div>
        </div>
    )
}

export default MonsterComp;