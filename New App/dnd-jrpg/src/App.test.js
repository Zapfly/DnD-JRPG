import React from 'react';
import { render, fireEvent, waitFor, screen } from '@testing-library/react';
import App from './App';
import { ContextProvider, AppContext } from './AppContext.js';
import '@testing-library/jest-dom/extend-expect'
import HeroComp from './Components/HeroComp/HeroComp';
import Herc from './images/Herccolored.png';
import { Arena } from './scripts/combat.js';
import Gobo from './images/250px-Chuffy_Lickwound.jpg';
import MonsterComp from './Components/MonsterComp/MonsterComp';


// beforeAll(()=> {

// })

test('renders learn react link', () => {
  const { getByText } = render(
        <App />
  );
  const linkElement = getByText(/Monster Dungeon/i);
  expect(linkElement).toBeInTheDocument();
});

test('renders HeroComp', () => {
  const arena = new Arena();
  arena.createHero("Hercules", 30, 40, Herc)

  const Hero = render(<HeroComp
    heroInfo = {arena.combatants[0]}
    />)
  expect(screen.getByRole('playerCharacter')).toHaveTextContent('Hercules')
})

test('render MonsterComp', () => {
  const arena = new Arena();
  arena.createMonster("Boblin", 1, 1, Gobo)

  const Monster = render(
    <ContextProvider >
        <MonsterComp
          monsterInfo = {arena.combatants[0]}
          key={0}
          index={0}
          monsters={arena.monsters}
        />
    </ContextProvider>
    )


  expect(screen.getByRole('monster')).toHaveTextContent('Boblin')

})

test('renders Monster array', () => {
  const arena = new Arena();
  arena.createMonster("Boblin", 1, 1, Gobo)

  const testLevel = 
  [
    {
      name:'Boblin 0',
      atk: 2,
      hp: 40,
      sprite: Gobo
    },
    {
      name:'Boblin 1',
      atk: 2,
      hp: 40,
      sprite: Gobo
    },
    {
      name:'Boblin 2',
      atk: 2,
      hp: 40,
      sprite: Gobo
    },
  ]


})
