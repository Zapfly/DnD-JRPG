import React from 'react';
import styles from './herocomp.module.css';

const HeroComp = (props) => {
    const name = props.heroInfo.name
    const healthbar = 100
    const currentHp = (props.heroInfo.hp / props.heroInfo.maxHp) * healthbar;
    return (
            <div role= "playerCharacter" className="container">
                <p >{name}</p>
                <img className={styles.heroImg} alt="hero-sprite" src={props.heroInfo.sprite} ></img>
                <div className={styles.maxHealthbar}>
                    <div className={styles.currentHp} style={{ width: `${currentHp}%` }}></div>
                </div>
            </div>
    )
}

export default HeroComp;