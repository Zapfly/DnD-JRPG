export const mon1 = JSON.parse({
    "monster": {
        "name": "goblin",
        "class": "monster",
        "attack":5,
        "HP":30
    }
})

export const hero1 = JSON.parse({
    "monster": {
        "name": "blarg",
        "class": "fighter",
        "attack":5,
        "HP":30
    }
})

export const actions = {
    attack: (atk, vicHp) => {
        vicHp - atk;
    }
}