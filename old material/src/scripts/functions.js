import aatxe from './JSON/example2.json'

let monster = `{"name": "goblin",
        "class": "monster",
        "attack": 5,
        "HP": 30}`

let hero = `{"name": "blarg",
"class": "fighter",
"attack": 5,
"HP": 30}`

export const mon2 = JSON.parse(aatxe)

export const mon1 = JSON.parse(monster);
//     "monster": {
//         "name": "goblin",
//         "class": "monster",
//         "attack": 5,
//         "HP": 30
//     }
// });

export const hero1 = JSON.parse(hero);

const actions = {
    attack: (atk, vicHp) => {
        return vicHp - atk;
    }
};

export default actions;