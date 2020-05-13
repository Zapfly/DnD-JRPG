import React from 'react';

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