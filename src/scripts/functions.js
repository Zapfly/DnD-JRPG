let monster = `{"name": "goblin",
        "class": "monster",
        "attack": 5,
        "HP": 30}`


export const mon1 = JSON.parse(monster);
//     "monster": {
//         "name": "goblin",
//         "class": "monster",
//         "attack": 5,
//         "HP": 30
//     }
// });

// export const hero1 = JSON.parse({
//     "name": "blarg",
//     "class": "fighter",
//     "attack": 5,
//     "HP": 30
// });

const actions = {
    attack: (atk, vicHp) => {
        return vicHp - atk;
    }
};

export default actions;