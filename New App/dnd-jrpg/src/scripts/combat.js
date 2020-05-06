export class Combatant {

    constructor(key, name, atk, hp, sprite) {
        this.key = key;
        this.name = name;
        this.atk = atk;
        this.hp = hp;
        this.sprite = sprite;

    }

    hpLoss(dmg) {
        this.hp = this.hp - dmg;
        if (this.hp < 0) {
            this.hp = 0;
        }
    }

    hpGained(life) {
        this.hp = this.hp + life;
    }
}

export class Arena {// different for each encounter

    constructor() {
        this.combatants = []; //...this.heroes, ...this.monsters
        this.monsters = [];
        this.heroes = [];

        this.counter = 0;
        this.currentTurn = 0;
    }

    // createCombatant(name, atk, hp, sprite) {
    //     this.counter++
    //     const newCombatant = new Combatant (this.counter, name, atk, hp, sprite);
    //     this.combatants.push(newCombatant);
    //     return newCombatant;
    // }

    createHero(name, atk, hp, sprite) {
        this.counter++
        const newHero = new Hero (this.counter, name, atk, hp, sprite);
        this.heroes.push(newHero);
        this.combatants = [...this.heroes, ...this.monsters]
        return newHero;
    }

    createMonster(name, atk, hp, sprite) {
        this.counter++
        const newMonster = new Monster (this.counter, name, atk, hp, sprite);
        this.monsters.push(newMonster);
        this.combatants = [...this.heroes, ...this.monsters]

        return newMonster;
    }


    cycleTurn() {
        if (this.currentTurn < this.combatants.length - 1) {
            this.currentTurn = this.currentTurn + 1
        }
        else this.currentTurn = 0;
        // if(this.combatants[this.currentTurn].hp <= 0) {
        //     this.cycleTurn()
        // }
    }

    turnLog(victim, attacker) {
        return `${attacker.name} attacks ${victim.name} for ${attacker.atk}.`
    }

    attack(victim, attacker = this.combatants[this.currentTurn]) {
        if (attacker != victim && victim.hp > 0) {
            victim.hpLoss(attacker.atk)
        }
    }
}

export class Hero extends Combatant { // instantiate combatant and change to hero or monster?
    constructor(...args) {
        super(...args)
        this.hero = true;
    }
}

export class Monster extends Combatant { // instantiate combatant and change to hero or monster?
    constructor(...args) {
        super(...args)
        this.hero = false;
    }
}