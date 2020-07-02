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
    <ContextProvider>
      <AppContext.Consumer>
        <App />
      </AppContext.Consumer>
    </ContextProvider>
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

// test('render MonsterComp', () => {
//   // const arena = new Arena();
//   // arena.createMonster("Boblin", 1, 1, Gobo)
//   // const appContext = React.useContext(AppContext);
//   const testLevel = 
//     [
//       {
//         name:'Boblin 0',
//         atk: 2,
//         hp: 40,
//         sprite: Gobo
//       },
//     ]
//   // appContext.currentLevelHandler(testLevel)



//   const Monster = render(
//     <ContextProvider value={setCurrentLevel(testLevel)}>
//       <AppContext.Consumer>
//         {/* <MonsterComp
//           monsterInfo = {arena.combatants[0]}
//           key={0}
//           index={0}
//           monsters={arena.monsters}
//         /> */}
//       </AppContext.Consumer>
//     </ContextProvider>
//     )


//   expect(screen.getByText('Boblin 0')).toHaveTextContent('Boblin 0')

// })

test('renders Monster array', () => {
  const arena = new Arena();
  arena.createMonster("Boblin", 1, 1, Gobo)

})
