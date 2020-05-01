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
    }

    hpGained(life) {
        this.hp = this.hp + life;
    }
}

export class Arena {

    constructor() {
        this.combatants = [];
        this.counter = 0;
        this.currentTurn = 0;
    }

    createCombatant(name, atk, hp, sprite) {
        this.counter++
        const newCombatant = new Combatant(this.counter, name, atk, hp, sprite);
        this.combatants.push(newCombatant);
        return newCombatant;
    }

    attack(attacker, victim) {
        //validation for not attacking self.
        victim.hpLoss(attacker.atk)
    }

}