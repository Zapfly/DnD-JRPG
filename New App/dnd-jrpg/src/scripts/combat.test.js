import { Combatant, Arena } from "./combat.js"
import hero from "../images/Herccolored.png"

test("Making a hero", () => {
    const colosseum = new Arena();
    colosseum.createHero("Hercules", 30, 20, hero)

    expect(colosseum.combatants[0].key).toEqual(1)
    expect(colosseum.combatants[0].name).toEqual("Hercules")
    expect(colosseum.combatants[0].atk).toEqual(30)
    expect(colosseum.combatants[0].hp).toEqual(20)
    expect(colosseum.combatants[0].sprite).toEqual("Herccolored.png")

    colosseum.createMonster("Boblin", 30, 20, hero)

})

test("attacking enemies", () => {
    const colosseum = new Arena();

    colosseum.createHero("Hercules", 30, 20, hero)
    colosseum.createMonster("Boblin", 30, 20, hero)

    expect(colosseum.combatants[0].name).toEqual("Hercules")
    expect(colosseum.combatants[1].name).toEqual("Boblin")
    expect(colosseum.combatants[1].hp).toEqual(20)

    colosseum.attack(colosseum.combatants[1], colosseum.combatants[0])
    expect(colosseum.combatants[1].hp).toEqual(0)

    expect(colosseum.combatants[0].hp).toEqual(20)
    colosseum.attack(colosseum.combatants[0], colosseum.combatants[0])
    expect(colosseum.combatants[0].hp).toEqual(20)

    colosseum.attack(colosseum.combatants[1])
    expect(colosseum.combatants[1].hp).toEqual(0)
})

test("Who's turn is it anyway?", () => {
    const colosseum = new Arena();
    colosseum.createHero("Hercules", 30, 20, hero)
    colosseum.createMonster("Boblin", 30, 20, hero)


    expect(colosseum.currentTurn).toEqual(0)
    colosseum.cycleTurn()
    expect(colosseum.currentTurn).toEqual(1)
    colosseum.cycleTurn()
    expect(colosseum.currentTurn).toEqual(0)  
})
