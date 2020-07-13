import React from 'react';
import { render, fireEvent, waitFor, screen } from '@testing-library/react';
import App from './App';
import { ContextProvider, AppContext } from './AppContext.js';
import '@testing-library/jest-dom/extend-expect';
import HeroComp from './Components/HeroComp/HeroComp';
import Herc from './images/Herccolored.png';
import { Arena } from './scripts/combat.js';
import Gobo from './images/250px-Chuffy_Lickwound.jpg';
import MonsterComp from './Components/MonsterComp/MonsterComp';
import CombatComp from './Components/CombatComp/CombatComp';
import { /*render,*/ unmountComponentAtNode } from "react-dom";
import { act } from 'react-dom/test-utils';



describe("App testing block", () => {
  let container = null;

  beforeEach(() => {
    console.log("from beforeEach");
    container = document.createElement("div");
    document.body.appendChild(container);
  });

  afterEach(() => {
    console.log("from afterEach");   
    // screen.getByRole("monsterContainer").textContent = ""; 
    unmountComponentAtNode(container);
    container.remove();
    container = null;
    // document.body.textContent = null; 
  });



  test('renders learn react link', () => {
    act(()=> {  
      const { getByText } = render(
        <ContextProvider >
          <CombatComp />
        </ContextProvider>, container
    )
      const linkElement = getByText(/Monster Dungeon/i);
      expect(linkElement).toBeInTheDocument();
    })



  });

  test('renders HeroComp', () => {
    const arena = new Arena();
    arena.createHero("Hercules", 30, 40, Herc)

    act(() => {
      render(<HeroComp
        heroInfo = {arena.combatants[0]}
        />, container)

    })

    // const Hero = render(<HeroComp
    //   heroInfo = {arena.combatants[0]}
    //   />)
    expect(screen.getByRole('playerCharacter')).toHaveTextContent('Hercules')
  });

  test('render MonsterComp', () => {
    const arena1 = new Arena();
    arena1.createMonster("Boblin", 1, 1, Gobo)

    act(()=>{
      render(
        <ContextProvider >
            <MonsterComp
              monsterInfo = {arena1.combatants[0]}
              key={0}
              index={0}
              monsters={arena1.monsters}
            />
        </ContextProvider>,
        container
        )
    }
    )


    expect(screen.getByRole('monster')).toHaveTextContent('Boblin')

  });

  test('renders Monster array', () => {
    // const arena2 = new Arena();
    // arena2.createMonster("Boblin", 1, 1, Gobo)

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
    ];

    act(()=> {     
      render(
        <ContextProvider>
          <CombatComp/>
        </ContextProvider>,
        container
        );
    })

    
    expect(screen.getByText('Boblin 0')).toHaveTextContent(['Boblin 0']);
    expect(screen.getAllByText("Boblin 1")).toHaveLength(1);
    expect(screen.getByRole('monsterContainer')).toBeInTheDocument(true);
  });

  test("new Test", () => {



  })



})
