
export class Combatant {

    constructor(key, name, atk, hp, sprite) {
        this.key = key;
        this.name = name;
        this.atk = atk;
        this.hp = hp;
        this.maxHp = hp
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
};

export class Arena {// different for each encounter

    constructor() {
        this.combatants = []; //...this.heroes, ...this.monsters
        this.monsters = [];
        this.heroes = [];

        this.counter = 0;
        this.currentTurn = 0;
    }

    createHero(name, atk, hp, sprite) {
        this.counter++
        const newHero = new Hero(this.counter, name, atk, hp, sprite);
        this.heroes.push(newHero);
        this.combatants = [...this.heroes, ...this.monsters]
        return newHero;
    }

    createMonster(name, atk, hp, sprite) {
        this.counter++
        const newMonster = new Monster(this.counter, name, atk, hp, sprite);
        this.monsters.push(newMonster);
        this.combatants = [...this.heroes, ...this.monsters]
        return newMonster;
    }

    victoryCheck() {
        const heroVictory = this.monsters.every(monster => monster.hp <= 0)
        const monsterVictory = this.heroes.every(hero => hero.hp <= 0)
        // eslint-disable-next-line
        if (heroVictory == true) {
            this.monsters = []
            this.combatants = [...this.heroes, ...this.monsters]
            return "victory"
            // eslint-disable-next-line
        } else if (monsterVictory == true) {
            return "defeat"
        } else {
            return "contested"
        }
    }

    turnIncrement() {
        if (this.combatants[this.currentTurn].hp <= 0) {
            this.currentTurn = this.currentTurn + 1
            this.turnIncrement()
        }
    }

    cycleTurn() {
        if (this.currentTurn < this.combatants.length - 1) {
            this.currentTurn = this.currentTurn + 1
        }
        else this.currentTurn = 0
        this.turnIncrement()
    }

    attack(victim, attacker = this.combatants[this.currentTurn]) {
        if (victim) {
            // eslint-disable-next-line
            if (attacker != victim && victim.hp > 0) {
                victim.hpLoss(attacker.atk)
            }
        }
        else return
    }
};

export class Hero extends Combatant { // instantiate combatant and change to hero or monster?
    constructor(...args) {
        super(...args)
        this.hero = true;
    }
};

export class Monster extends Combatant { // instantiate combatant and change to hero or monster?
    constructor(...args) {
        super(...args)
        this.hero = false;
    }
};