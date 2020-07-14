import React from 'react';
import { render, fireEvent, waitFor, screen, getByText, waitForElement } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
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
    container = document.createElement("div");
    document.body.appendChild(container);
  });

  afterEach(() => {
    unmountComponentAtNode(container);
    container.remove();
    container = null;

  });



  test('renders learn react link', () => {
    act(()=> {  
      const { getByText } = render(
          <App />, container
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
    expect(screen.getByRole('playerCharacter')).toBeInTheDocument(true)
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


    expect(screen.getByRole('monster')).toBeInTheDocument(true)

  });

  test('renders Monster array', () => {

    act(()=> {     
      render(
        <ContextProvider>
          <CombatComp/>
        </ContextProvider>,
        container
        );
    })

    
    expect(screen.getAllByRole("monster")).not.toHaveLength(0);
    expect(screen.getByRole('monsterContainer')).toBeInTheDocument(true);
    expect(screen.getAllByRole('monsterContainer')).toHaveLength(1);
    
  });

  test('clicking monster sets class to "selected"', () => {

    act(()=> {     
      render(
        <ContextProvider>
          <CombatComp/>
        </ContextProvider>,
        container
        );
    })

    expect(screen.getAllByRole("monster")[0].firstChild).not.toHaveClass("selected")
    fireEvent.click(
      screen.getAllByRole("monster")[0]
    )
    expect(screen.getAllByRole("monster")[0].firstChild).toHaveClass("selected")

    fireEvent.click(
      screen.getAllByRole("monster")[1]
    )
    expect(screen.getAllByRole("monster")[0].firstChild).not.toHaveClass("selected")
    expect(screen.getAllByRole("monster")[1].firstChild).toHaveClass("selected")
  })

  // test('attack button calls a function', async () => {
  //   act(() => {
  //     render(
  //       <ContextProvider>
  //         <CombatComp />
  //       </ContextProvider>,
  //       container
  //     );
  //   })
    
    
  //   userEvent.click(
  //     screen.getAllByRole("monster")[0]
  //     );
      
  //   await waitFor(() => {
  //     expect(screen.getAllByRole("monster")[0].firstChild).toHaveClass("selected")
  //   })
  
  //   await waitFor(() => {

  //     userEvent.click(
  //       screen.getByRole("AttackButton")
  //       )          
        
  //   })
      
  //     // expect(screen.getById('HPBar 1').width).toEqual(1000000000)
      
  //     // expect(mockFn).toHaveBeenCalled()

  // })

    

})