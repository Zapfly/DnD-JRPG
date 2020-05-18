import { Arena } from "./combat.js"
import hero from "../images/Herccolored.png"
import gobo from '../images/250px-Chuffy_Lickwound.jpg';

test("createHero method", () => {
    const colosseum = new Arena();
    colosseum.createHero("Hercules", 30, 20, hero)

    expect(colosseum.combatants[0].key).toEqual(1)
    expect(colosseum.combatants[0].name).toEqual("Hercules")
    expect(colosseum.combatants[0].atk).toEqual(30)
    expect(colosseum.combatants[0].hp).toEqual(20)
    expect(colosseum.combatants[0].sprite).toEqual("Herccolored.png")

})

test("createMonster method", () => {
    const colosseum = new Arena();

    expect(colosseum.combatants).toEqual([])

    colosseum.createMonster("Boblin", 2, 20, gobo)

    expect(colosseum.combatants[0].name).toEqual("Boblin")
})

test("attack method", () => {
    const colosseum = new Arena();

    colosseum.createHero("Hercules", 30, 20, hero)
    colosseum.createMonster("Boblin", 30, 20, gobo)
    colosseum.createMonster("Boblin2", 30, 20, gobo)

    expect(colosseum.combatants[0].name).toEqual("Hercules")
    expect(colosseum.combatants[1].name).toEqual("Boblin")
    expect(colosseum.combatants[1].hp).toEqual(20)

    colosseum.attack(colosseum.combatants[1], colosseum.combatants[0])
    expect(colosseum.combatants[1].hp).toEqual(0)

    expect(colosseum.combatants[0].hp).toEqual(20)
    colosseum.attack(colosseum.combatants[0], colosseum.combatants[0])
    expect(colosseum.combatants[0].hp).toEqual(20)

    colosseum.attack(colosseum.combatants[1], colosseum.combatants[0])
    expect(colosseum.combatants[1].hp).toEqual(0)
})

test("cycleTurn and turnIncrement methods", () => {
    const colosseum = new Arena();
    colosseum.createHero("Hercules", 30, 20, hero)
    colosseum.createMonster("Boblin", 30, 20, gobo)
    colosseum.createMonster("Boblin", 30, 20, gobo)
    colosseum.createMonster("Boblin", 30, 20, gobo)

    expect(colosseum.currentTurn).toEqual(0)
    colosseum.cycleTurn()
    expect(colosseum.currentTurn).toEqual(1)
    colosseum.combatants[2].hp = 0
    colosseum.cycleTurn()
    expect(colosseum.currentTurn).toEqual(3)  
    colosseum.cycleTurn()
    expect(colosseum.currentTurn).toEqual(0)  
})

test("victoryCheck method", () => {
    const colosseum = new Arena();
    colosseum.createHero("Hercules", 30, 20, hero)
    colosseum.createMonster("Boblin", 1, 20, gobo)
    colosseum.createMonster("Boblin", 1, 20, gobo)
    expect(colosseum.combatants.length).toEqual(3)    
    expect(colosseum.monsters.length).toEqual(2)    
    expect(colosseum.heroes.length).toEqual(1)  

    expect(colosseum.victoryCheck()).toEqual("contested")

    colosseum.combatants[1].hp = 0;
    colosseum.combatants[2].hp = 0;

    expect(colosseum.victoryCheck()).toEqual("victory")
    expect(colosseum.combatants.length).toEqual(1)

    colosseum.createMonster("Boblin", 1, 1, gobo)
    colosseum.combatants[0].hp = 0;

    expect(colosseum.victoryCheck()).toEqual("defeat")
})