import { Arena } from "./combat.js"
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
    colosseum.createMonster("Boblin2", 30, 20, hero)

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
    colosseum.createMonster("Boblin", 30, 20, hero)
    colosseum.createMonster("Boblin", 30, 20, hero)


    expect(colosseum.currentTurn).toEqual(0)
    colosseum.cycleTurn()
    expect(colosseum.currentTurn).toEqual(1)
    colosseum.combatants[2].hp = 0
    colosseum.cycleTurn()
    expect(colosseum.currentTurn).toEqual(3)  
    colosseum.cycleTurn()
    expect(colosseum.currentTurn).toEqual(0)  
})

test("Who won?", () => {
    const arena1 = new Arena();
    arena1.createHero("Hercules", 30, 20, hero)
    arena1.createMonster("Boblin", 1, 20, hero)
    arena1.createMonster("Boblin", 1, 20, hero)
    expect(arena1.combatants.length).toEqual(3)    
    expect(arena1.monsters.length).toEqual(2)    
    expect(arena1.heroes.length).toEqual(1)    

    arena1.attack(arena1.combatants[1])
    expect(arena1.victoryCheck()).toEqual("contested")
    expect(arena1.victoryCheck()).toEqual("contested")
    expect(arena1.currentTurn).toEqual(2)

    const arena2 = new Arena();
    arena2.createHero("Hercules", 30, 20, hero)
    arena2.createMonster("Boblin", 1, 20, hero)
    arena2.createMonster("Boblin", 1, 20, hero)

    arena2.attack(arena2.combatants[1])
    expect(arena2.victoryCheck()).toEqual("contested")
    arena2.attack(arena2.combatants[0])
    expect(arena2.victoryCheck()).toEqual("contested")
    arena2.attack(arena2.combatants[2])
    expect(arena2.victoryCheck()).toEqual("victory")

    const arena3 = new Arena();
    arena3.createHero("Hercules", 30, 20, hero)
    arena3.createMonster("Super Boblin", 500, 500, hero)
    
    arena3.attack(arena3.combatants[0], arena3.combatants[1])
    expect(arena3.victoryCheck()).toEqual("defeat")    
})