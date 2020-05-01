import { Combatant, Arena } from "./combat.js"
import hero from "../images/Herccolored.png"

test("Making a hero", () => {
    const Colosseum = new Arena();
    Colosseum.createCombatant("Hercules", 30, 20, hero)
    
    expect(Colosseum.combatants[0].key).toEqual(1)
    expect(Colosseum.combatants[0].name).toEqual("Hercules")
    expect(Colosseum.combatants[0].atk).toEqual(30)
    expect(Colosseum.combatants[0].hp).toEqual(20)
    expect(Colosseum.combatants[0].sprite).toEqual("Herccolored.png")
})

test("attacking enemies", () => {
    const Colosseum = new Arena();

    Colosseum.createCombatant("Hercules", 30, 20, hero)
    Colosseum.createCombatant("Boblin", 30, 20, hero)

    expect(Colosseum.combatants[0].name).toEqual("Hercules")
    expect(Colosseum.combatants[1].name).toEqual("Boblin")
    expect(Colosseum.combatants[1].hp).toEqual(20)

    Colosseum.attack(Colosseum.combatants[0], Colosseum.combatants[1])
    expect(Colosseum.combatants[1].hp).toEqual(-10)

})