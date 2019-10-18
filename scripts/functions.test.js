import { actions, hero1, mon1} from "./functions.js"

test('test', () => {
    expect(hero1.attack, mon1.HP).toEqual(100);
})